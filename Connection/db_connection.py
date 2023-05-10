import mysql.connector
from mysql.connector import Error


class DBConnection:
    def __init__(self, host, user_name, password, db_name):
        self.host = host
        self.user_name = user_name
        self.password = password
        self.db_name = db_name

        self.connection = self._create_connection()

    def _create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user_name,
                passwd=self.password,
                database=self.db_name
            )
            print('Connection successful')
        except Error as err:
            print(f"Error: '{err}'")
        return connection

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
