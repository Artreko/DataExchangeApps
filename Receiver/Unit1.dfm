object ReceiverMainForm: TReceiverMainForm
  Left = 0
  Top = 0
  Caption = 'ReceiverMainForm'
  ClientHeight = 280
  ClientWidth = 619
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  TextHeight = 13
  object Label1: TLabel
    Left = 16
    Top = 19
    Width = 120
    Height = 13
    Caption = #1055#1086#1083#1091#1095#1077#1085#1085#1086#1077' '#1089#1086#1086#1073#1097#1077#1085#1080#1077
  end
  object Image1: TImage
    Left = 142
    Top = 43
    Width = 211
    Height = 248
    Center = True
    Proportional = True
    Stretch = True
  end
  object Label2: TLabel
    Left = 16
    Top = 43
    Width = 115
    Height = 13
    Caption = #1055#1086#1083#1091#1095#1077#1085#1085#1072#1103' '#1082#1072#1088#1090#1080#1085#1082#1072' '
  end
  object Edit1: TEdit
    Left = 142
    Top = 16
    Width = 459
    Height = 21
    TabOrder = 0
    TextHint = #1054#1073#1083#1072#1089#1090#1100' '#1090#1077#1082#1089#1090#1072' '#1076#1083#1103' '#1087#1086#1083#1091#1095#1077#1085#1080#1103' '#1089#1086#1086#1073#1097#1077#1085#1080#1103
  end
  object GroupBox1: TGroupBox
    Left = 370
    Top = 43
    Width = 249
    Height = 110
    Caption = #1069#1083#1077#1084#1077#1085#1090#1099' '#1087#1086#1083#1091#1095#1077#1085#1085#1086#1081' '#1089#1090#1088#1091#1082#1090#1091#1088#1099
    TabOrder = 1
    object Label3: TLabel
      Left = 16
      Top = 27
      Width = 19
      Height = 13
      Caption = #1048#1084#1103
    end
    object Label4: TLabel
      Left = 16
      Top = 54
      Width = 68
      Height = 13
      Caption = #1057#1090#1072#1078' '#1088#1072#1073#1086#1090#1099
    end
    object Label5: TLabel
      Left = 18
      Top = 81
      Width = 80
      Height = 13
      Caption = #1044#1072#1090#1072' '#1088#1086#1078#1076#1077#1085#1080#1103
    end
    object Edit2: TEdit
      Left = 56
      Top = 24
      Width = 161
      Height = 21
      TabOrder = 0
      TextHint = #1048#1084#1103
    end
    object Edit3: TEdit
      Left = 120
      Top = 51
      Width = 97
      Height = 21
      TabOrder = 1
      TextHint = #1057#1090#1072#1078
    end
    object DateTimePicker1: TDateTimePicker
      Left = 120
      Top = 78
      Width = 97
      Height = 21
      Date = 18576.000000000000000000
      Time = 18576.000000000000000000
      TabOrder = 2
    end
  end
  object Button1: TButton
    Left = 440
    Top = 184
    Width = 75
    Height = 25
    Caption = 'Connect'
    TabOrder = 2
    OnClick = Button1Click
  end
  object ClientSocket1: TClientSocket
    Active = False
    ClientType = ctNonBlocking
    Host = '127.0.0.1'
    Port = 65433
    OnConnect = ClientSocket1Connect
    Left = 448
    Top = 232
  end
end
