def get_profil(name):
 import paramiko
 import time
 from config import ip_server,password_server
 



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
 local_file_path = '/Users/aboba/Desktop/vpn_bot2/ecom/'+name+'.conf'
 sftp.get(remote_file_path, local_file_path)
 sftp.close()




 ssh.close()



 

  