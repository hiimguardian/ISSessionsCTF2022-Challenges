from pwn import *

def solve(s: str):
    s = s.replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace("\n", "")
    print(s)
    l = s.split(" ")
    base = []
    for c in l:
        if c != '*':
            base.append(int(c))

    base.sort()
    print(base)

    ans = []
    for i in range(base[0] + 1, base[len(base) - 1]):
        if i not in base:
            ans.append(str(i))
    return " ".join(ans)


p = remote("challenges.issessions.ca", 5105)

p.readline()
p.readline()
p.readline()    

while True:
    x = p.readline().decode("utf-8")

    ans = solve(x)
    print(ans)

    p.sendline(ans.encode("utf-8"))