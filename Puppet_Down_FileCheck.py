import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
with open('Puppet_Down_Hosts.txt') as file_handler:
        list = [str(line).rstrip('\n') for line in file_handler]
for i in list:
    try:
        ssh.connect(i +'.domain.com', port=22, username='admin', password ='password')
        stdin, stdout, stderr = ssh.exec_command('find /service/puppet -name "down"')
        output = stdout
        print i + '\n'.join(output)
    except:
        print i + " Connection Rejected"
        continue
if output != None:
    stdin, stdout, stderr = ssh.exec_command('cat /service/puppet/down')
    down_file = stdout
    for p in down_file: print p
    ssh.close()
