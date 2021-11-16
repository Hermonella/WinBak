
from smb.SMBConnection import SMBConnection
from nmb.NetBIOS import NetBIOS

smb_user = input("SMB Username: ")
smb_pass = input("SMB Password: ")

#conn = SMBConnection(userID, password, client_machine_name, server_name, use_ntlm_v2 = True)
conn = SMBConnection('smb_user', 'smb_pass', 'test', 'bolvar', use_ntlm_v2 = True)
conn.connect('10.0.100.222', 139)
if conn:
    print ("successfull: " + str(conn))
else:
    print ("failed to connect")