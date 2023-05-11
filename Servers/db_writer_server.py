from Connection.db_connection import DBConnection
import socket
from dotenv import load_dotenv
import os
import threading

load_dotenv()
HOST = os.getenv('HOST')
PORT = int(os.getenv('DB_SERVER_PORT'))
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')

table_query = [
    'DROP TABLE IF EXISTS op_stats;',
    """
    CREATE TABLE op_stats (
      op_id int(11) NOT NULL AUTO_INCREMENT,
      op_type_id int(11) DEFAULT NULL,
      mes_type_id int(11) DEFAULT NULL,
      op_time datetime DEFAULT NULL,
      PRIMARY KEY (op_id)
    )
    ENGINE = INNODB,
    AVG_ROW_LENGTH = 16384,
    CHARACTER SET utf8,
    COLLATE utf8_general_ci;
    """,
    """
    ALTER TABLE dataex_stats.op_stats
    ADD CONSTRAINT FK_op_stats_mes_type_id FOREIGN KEY (mes_type_id)
    REFERENCES dataex_stats.mes_type (mes_type_id) ON DELETE NO ACTION;
    """,
    """
    ALTER TABLE dataex_stats.op_stats
    ADD CONSTRAINT FK_op_stats_op_type_id FOREIGN KEY (op_type_id)
    REFERENCES dataex_stats.op_type (op_type_id) ON DELETE NO ACTION;
    """
]


def main():
    db = DBConnection(HOST, USER_NAME, PASSWORD, 'dataex_stats')
    for query in table_query:
        db.execute_query(query)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(3)

        def listen():
            conn, addr = sock.accept()
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                command = data.decode('utf-8')
                print('Command:', command)
                command = command.split()
                query = f"""INSERT INTO op_stats(op_type_id, mes_type_id, op_time)
                                VALUES({command[0]}, {command[1]}, '{command[2]}');"""
                db.execute_query(query)
                cursor = db.connection.cursor()
                cursor.execute("SELECT * FROM op_view;")
                result = cursor.fetchall()
                print('Количество записей:', len(result))
                print(f'{"id":>3} {"type":^10} {"message":^9} {"time":^17}')
                for x in result:
                    print(f"{x[0]:>3} {x[1]:^10} {x[2]:^9} {x[3].strftime('%X %x')}")
        for _ in range(2):
            threading.Thread(target=listen(), daemon=True).start()


if __name__ == '__main__':
    main()
