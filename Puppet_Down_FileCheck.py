import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
list = ["abc-123","abc-124","abc-125"] # Random Dummy hosts for reference
for i in list:
    ssh.connect(i+'.domain.com', port=22, username='admin', password ='admin')
    stdin, stdout, stderr = ssh.exec_command('find /service/puppet -name "down"')
    output = stdout
    print i +'\n'.join(output)
    if output > 5:
        stdin, stdout, stderr = ssh.exec_command('cat /service/puppet/down')
        down_file = stdout
        for p in down_file: print p
    ssh.close()
