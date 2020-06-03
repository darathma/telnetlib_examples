import getpass
import telnetlib

ip = '10.0.0.2'
user = input('Enter your username: ')
password = getpass.getpass()

tnconn = telnetlib.Telnet(ip)
tnconn.read_until(b'Username: ')
tnconn.write(user.encode('ascii') + b'\n') 

if password:
    tnconn.read_until(b'Password: ')
    tnconn.write(password.encode('ascii') + b'\n')
tnconn.write(b'enable\n')
if password:
    tnconn.read_until(b'Password: ')
    tnconn.write(password.encode('ascii') + b'\n')
tnconn.write(b'config t\n')
for x in range (200, 210):
	tnconn.write(b'vlan ' + str(x).encode('ascii') + b'\n')
	tnconn.write(b'name Data_vlan_' + str(x).encode('ascii') + b'\n')
tnconn.write(b'end\n')
tnconn.write(b'terminal length 0\n')
tnconn.write(b'show vlan brief\n')
tnconn.write(b'copy running-config startup-config\n')
tnconn.write(b'\n')
tnconn.write(b'exit\n')

print(tnconn.read_all().decode('ascii'))
