import pexpect as px
child=px.spawn('ssh manjusha@192.168.149.1')
child.expect("password:")
child.sendline('Cloud@123')
print(child.before)
child.close()