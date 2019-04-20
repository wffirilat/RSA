def encrypt(s, e, n):
    out = []
    for x in s:
        out.append(modde(ord(x),e,n))
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
    
