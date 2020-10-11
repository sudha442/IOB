def add_enterprise_resource(host,username,pw,cli):
    import paramiko
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=pw)
        
        #Executing the CLI
        stdin,stdout,stderr=ssh.exec_command("pwd")
        pwd_out = stdout.read()

        stdin,stdout,stderr=ssh.exec_command(cli,get_pty=True)
        
        for line in iter(stdout.readline, ""):
            print(line, end="")

        ssh.close()
        
        return True
    except Exception as e:
        print(e)
        return False