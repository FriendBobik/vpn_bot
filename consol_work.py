from work_mySQL import sql_free_value,sql_free_date
from datetime import datetime, timedelta
def get_profil(name):
 import paramiko
 import time
 from config import ip_server,password_server
 global vpn_give



 client = paramiko.SSHClient()
 client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


 client.connect(ip_server, username='root', password=password_server)


 ssh = client.invoke_shell()
 #print(ssh.recv(3000))
 time.sleep(0.7)

 ssh.send("./wireguard-install.sh\n")
 #print(ssh.recv(3000))
 time.sleep(0.7)

 ssh.send("1\n")
 #print(ssh.recv(3000))
 time.sleep(0.7)

 ssh.send(name+"\n")
 #print(ssh.recv(3000))
 time.sleep(0.7)


 ssh.send("\n")
 #print(ssh.recv(3000))
 time.sleep(0.7)

 ssh.send("\n")
 #print(ssh.recv(3000))
 time.sleep(0.7)


 sftp = client.open_sftp()
 file_name = 'wg0-client-'+name+'.conf'
 remote_file_path = '/root/'+file_name
 local_file_path = name+'.conf'
 sftp.get(remote_file_path, local_file_path)
 sftp.close()
 vpn_give=True



 ssh.close()
def delet_profil(name)
 if int(sql_free_value(name))==1 and sql_free_date(name) > (datetime.now()+ timedelta(minutes=1)) and :
 return 0


 

  