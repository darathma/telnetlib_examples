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
tnconn.write(b'hostname jeremiah_py\n')
tnconn.write(b'end\n')
tnconn.write(b'copy running-config startup-config\n')
tnconn.write(b'\n')
tnconn.write(b'exit\n')

print(tnconn.read_all().decode('ascii'))
