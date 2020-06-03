import getpass
import wexpect
import re

user = input('Enter your username: ')
password = getpass.getpass()


file = open('multi_switches.txt', mode = 'r')

for host in file:
    IP = host.strip()
    print('Configuring Switch ' + (IP))
    tnconn = wexpect.spawn('cmd.exe')
    #result = tnconn.expect(['Username:', wexpect.TIMEOUT])
    #if result != 0:
        #print('Failure creating session for' + IP)
        #exit()
    #tnconn.sendline(user)
    print(tnconn.readline())
    print(tnconn.before)
    result = tnconn.expect(['>', wexpect.TIMEOUT])
    if result != 0:
        print('Failure entering username ' + user)
        exit()
    info = f'ssh.exe {user}@{IP}'
    tnconn.sendline(info)
    print(tnconn.readline())
    print(tnconn.before)
    result = tnconn.expect(['Password: ', wexpect.TIMEOUT])
    if result != 0:
        print('Failure entering usernametest ' + user)
        exit()
    tnconn.sendline(password)
    result = tnconn.expect(['>', '#', wexpect.TIMEOUT])
    if result == 0:
        tnconn.sendline(enable)
        result = tnconn.expect(['Password:', wexpect.TIMEOUT])
        if result != 0:
            print('Failure with enable command')
            exit()
        tnconn.sendline(password)
        result = tnconn.expect(['#', wexpect.TIMEOUT])
        if result != 0:
            print('Failure entering enable mode')
            exit()
    elif result == 1:
        continue
    tnconn.sendline('terminal length 0')
    result = tnconn.expect(['#', wexpect.TIMEOUT])
    if result != 0:
        print('Failure entering enable mode')
        exit()
    tnconn.sendline('show version')
    result = tnconn.expect(['#', wexpect.TIMEOUT])
    if result == 0:
        print('Command sent successfully')
    elif result != 0:
        print('Command failure')
        exit()
    show_ver_output = tnconn.before
    print(show_version_output)
