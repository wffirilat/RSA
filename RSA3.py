import math

primes = []
bprimes = []


def mod(n, a):
    A = n
    terms = [0, 1]
    while n != 1 and a != 1:
        if n > a:
            terms.append(n // a)
            n = n % a
        else:
            terms.append(a // n)
            a = a % n
    inv = terms[1]
    inV = terms[0]
    k = 2
    while k < len(terms):
        inv, inV = inV - (terms[k] * inv), inv
        k += 1
    return inv % A


def primer(t, c):
    new = []
    while c < 100 * t:
        prime = True
        k = 0
        sq = c ** 0.5
        while k < len(primes):
            if c % primes[k] == 0:
                prime = False
            k += 1
            if k > sq:
                break
        if prime:
            primes.append(c)
            new.append(c)
            if c > 11358:
                bprimes.append(c)
        c += 1
    return c, new


def modde(m, dee, en):
    x = str(bin(dee)).lstrip("0b")
    x = x[::-1]
    b = []
    for i in range(0, len(x)):
        b.append(int(x[i]))
    sq = [m]
    for i in range(1, len(x)):
        sq.append((sq[i - 1] ** 2) % en)
    cu = 1
    for i in range(0, len(x)):
        if b[i] == 1:
            cu = (cu * sq[i]) % en

    # M = m
    # for i in range(0,dee -1):
    #    M = (M*m)%en
    return cu


def main():
    c = 2
    t = 116
    c, ignore = primer(t, c)
    print("Hi")
    print("Welcome to Straya's encryption emporium v2.0!")
    print("To begin, pick two distinct primes from this list and enter them "
          "separated by a space. If you'd like bigger primes enter \"more primes\".")
    print(bprimes)
    vinp = False
    while vinp is False:
        command = input("Input: ")
        if command == "more primes":
            print("Coming up.")
            t += 2
            c, new = primer(t, c)
            print(new)
        else:
            commands = command.split(" ")
            if len(commands) < 2:
                print("Too few inputs.")
            elif len(commands) > 2:
                print("Too many inputs.")
            elif (not commands[0].isnumeric) or (not commands[1].isnumeric()):
                try:
                    p = float(commands[0])
                    q = float(commands[1])
                    print("Please enter whole numbers.")
                except ValueError:
                    print("Please enter numbers or ask for more primes.")
            else:
                p = int(commands[0])
                q = int(commands[1])
                if (p not in bprimes) or (q not in bprimes):
                    print("Please pick from the list.")
                elif p == q:
                    print("Please pick distinct primes.")
                else:
                    vinp = True

    print("Ok, now we're in business.")
    n = p * q
    phi = (p - 1) * (q - 1)
    print("Your \"n\" value is " + str(n) + " and its totient (often called phi) is " + str(phi) + ".")
    print("You'll now need to choose an \"e\" value. This number needs to be coprime to " + str(
        phi) + ", which is to say they have no common factors other than 1.")
    es = []
    for x in range(2, phi):
        if math.gcd(x, phi) == 1:
            es.append(x)
        if len(es) == 100:
            break
    print("Here's a list to choose from.")
    print(es)
    vinp = False
    while not vinp:
        command = input("Input: ")
        if not command.isnumeric():
            print("Please pick an item from the list.")
        else:
            e = int(command)
            if e not in es:
                print("Please pick an item from the list.")
            else:
                vinp = True

    d = mod(phi, e)
    print("Ok, we'll just need one more number, your private key \"d\".")
    print("d is " + str(d) + ", the unique number less than " + str(
        phi) + " such that the remainder when its product with e is divided by " + str(phi) + " is 1.")
    print("We've now established a valid RSA encryption system! Share e and n with your friends "
          "to allow them to encrypt messages to send to you, but make sure you keep d a secret!.")
    print("The program will now decrypt encrypted ascii sequences structured as python lists of "
          "integers e.g. \"[1, 2, 3]\". Simply copy and paste one into the console to decrypt it.")
    print("Enter \"values\" to see the values of n and e again or \"quit\" to terminate the program.")

    vinp = False
    while vinp is False:
        command = input("Input: ")
        if command == "quit":
            exit()
        elif command == "values":
            print("n is " + str(n) + " and e is " + str(e) + ".")
        elif command[0] != "[" or command[-1] != "]":
            print("Invalid input")
        else:
            command = command.lstrip("[")
            command = command.rstrip("]")
            seq = command.split(", ")
            out = ""
            succ = True
            for x in seq:
                if not x.isnumeric() or int(x) >= n:
                    print("Invalid list")
                    succ = False
                    break
                else:
                    N = modde(int(x), d, n)
                    N = str(N)
                    while len(N) != 9:
                        N = "0" + N
                    a = int(N[0:3])
                    b = int(N[3:6])
                    g = int(N[6:9])
                    thr = [a, b, g]
                    for i in thr:
                        if i > 128:
                            print("Invalid sequence")
                            succ = False
                            break
                        else:
                            out += chr(i)
            if succ:
                print(out)


if __name__ == '__main__':
    main()
