def get_profil(name):
 import paramiko
 import time



 client = paramiko.SSHClient()
 client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


 print("get_profil")

 with open('ip.txt', 'r') as file:
    ip = file.read().strip()
 with open('password_server.txt', 'r') as file:
    password_server = file.read().strip()


 client.connect(ip, username='root', password=password_server)


 ssh = client.invoke_shell()
 #print(ssh.recv(3000))
 time.sleep(1)

 ssh.send("./wireguard-install.sh\n")
 #print(ssh.recv(3000))
 time.sleep(1)

 ssh.send("1\n")
 #print(ssh.recv(3000))
 time.sleep(1)

 ssh.send(name+"\n")
 #print(ssh.recv(3000))
 time.sleep(1)


 ssh.send("\n")
 #print(ssh.recv(3000))
 time.sleep(1)

 ssh.send("\n")
 #print(ssh.recv(3000))
 time.sleep(1)


 sftp = client.open_sftp()
 file_name = 'wg0-client-'+name+'.conf'
 remote_file_path = '/root/'+file_name
 local_file_path = '/Users/aboba/Desktop/vpn_bot2/ecom/'+file_name
 sftp.get(remote_file_path, local_file_path)
 sftp.close()




 ssh.close()



 

  