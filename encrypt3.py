def encrypt(s, e, n):
    out = []
    while len(s)%3!=0:
            s+="#"
    for i in range(0,int(len(s)/3)):
        st = s[3*i:3*i+3]
        a,b,c = str(ord(st[0])),str(ord(st[1])),str(ord(st[2]))
        while len(b)!=3:
            b = "0" + b
        while len(c)!=3:
            c = "0" + c
        k = int(a + b + c)
        out.append(modde(k,e,n))
    return(out)
    
def modde(m, dee, en):
    M = m
    for i in range(0,dee -1):
        M = (M*m)%en
    return M

a = True

while a:
    kom = input("Enter a message here (or enter \"quit\" to quit): ")
    N = input("Enter an n value: ")
    while not N.isnumeric():
        print("Please enter an integer value")
        N = input("Enter an n value: ")
    N = int(N)
    E = input("Enter an e value: ")
    while not E.isnumeric():
        print("Please enter an integer value")
        E = input("Enter an e value: ")
    E = int(E)
    print(encrypt(kom, E, N))
