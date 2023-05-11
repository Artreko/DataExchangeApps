unit Unit1;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, System.StrUtils, System.DateUtils,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Vcl.ExtCtrls, Vcl.ComCtrls,
  System.Win.ScktComp;

type

  // ����� ���������������� ��������� ��� �������� ������
  TDataRec = packed record
    Name: ansistring;
    WorkYears: Integer;
    BirthDate: TDate;
  end;


  TReceiverMainForm = class(TForm)
    Edit1: TEdit;
    Label1: TLabel;
    Image1: TImage;
    Label2: TLabel;
    GroupBox1: TGroupBox;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Edit2: TEdit;
    Edit3: TEdit;
    DateTimePicker1: TDateTimePicker;
    ClientSocket1: TClientSocket;
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
    procedure ClientSocket1Connect(Sender: TObject; Socket: TCustomWinSocket);
  private
    { Private declarations }
    // ��������� ��������� ��� ��������� ����������� ��������� WM_COPYDATA
    procedure WMCopyData(var Msg: TWMCopyData); message WM_COPYDATA;
    // ������ ��������� ��� ��������� ������ ��������
    procedure HandleCopyDataImage(copyDataStruct: PCopyDataStruct);
    // ������ ��������� ��� ��������� ������ ���������
    procedure HandleCopyDataRecord(copyDataStruct: PCopyDataStruct);

  public
    { Public declarations }
  end;

var
  ReceiverMainForm: TReceiverMainForm;

implementation

{$R *.dfm}
{ ���������
  ������ TWMCopyData ������� �� ��������� ���:
  Msg: Cardinal;
  From: HWND;// ���������� ����, ������� �������� ������
  CopyDataStruct: PCopyDataStruct; // ������������ ������
  Result: Longint;// ������������, ����� �������� �������� ����� (���� ��� �������� ���� "Sender")
}

procedure TReceiverMainForm.WMCopyData(var Msg: TWMCopyData);
var
  s: ansistring;
begin
  // (cdtString = 0, cdtImage = 1, cdtRecord = 2);
  if Msg.copyDataStruct.dwData = 0 then
  begin
    // ��������� ����������� ������
    s := PAnsiChar(Msg.copyDataStruct.lpData);
    // ��������� ���������� ���������� �����
    Edit1.Text := s;

    ClientSocket1.Socket.SendText('3 1 ' + FormatDateTime('yyyymmdd hh:nn', Now))
  end;
  // ��������� ���������� ��������
  if Msg.copyDataStruct.dwData = 1 then
    HandleCopyDataImage(Msg.copyDataStruct);
  // ��������� ���������������� ���������
  if Msg.copyDataStruct.dwData = 2 then
    HandleCopyDataRecord(Msg.copyDataStruct);
  // ������� ���-������ �����
  Msg.Result := 1111;
end;

procedure TReceiverMainForm.Button1Click(Sender: TObject);
begin
  ClientSocket1.Active := true;
end;

procedure TReceiverMainForm.ClientSocket1Connect(Sender: TObject;
  Socket: TCustomWinSocket);
begin
    Edit1.Text := 'Connected'
end;

procedure TReceiverMainForm.HandleCopyDataImage(copyDataStruct
  : PCopyDataStruct);
var
  // ��������� �����
  ms: TMemoryStream;
begin
  // ������� �����
  ms := TMemoryStream.Create;
  try
    // ������� �������� � ����� ������ �� ������ ��������� � ����������� �������
    ms.Write(copyDataStruct.lpData^, copyDataStruct.cbData);
    // ��������� ������� ������ � ������
    ms.Position := 0;
    // ���������  Bitmap �������� �� ������
    Image1.Picture.Bitmap.LoadFromStream(ms);

    ClientSocket1.Socket.SendText('3 2 ' + FormatDateTime('yyyymmdd hh:nn', Now))
  finally
    // ������������ �����
    ms.Free;
  end;
end;

procedure TReceiverMainForm.HandleCopyDataRecord(
  copyDataStruct: PCopyDataStruct);
var
  sampleRecord : TDataRec;
  s: ansistring;
  splited_s: TArray<string>;
begin
  s := PAnsiChar(copyDataStruct.lpData);

  splited_s := SplitString(s, ';');

//  ShowMessageFmt('%s %s %s',[splited_s[0], splited_s[1], splited_s[2]]);

  sampleRecord.Name := splited_s[0];
  sampleRecord.WorkYears := StrToInt(splited_s[1]);

  sampleRecord.BirthDate := StrToDate(splited_s[2]);



  Edit2.Text:=sampleRecord.Name;
  Edit3.Text:=inttostr(sampleRecord.WorkYears);

  DateTimePicker1.Date:= sampleRecord.BirthDate;

  ClientSocket1.Socket.SendText('3 3 ' + FormatDateTime('yyyymmdd hh:nn', Now))
end;


end.
