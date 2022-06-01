import random

while True:
    print()
    thing = input("Enter operation: ")
    if "+" in thing:
        pieces = thing.split("+")
        jk = (int(pieces[0]) + int(pieces[1]))
        ikr = random.random()
        oper = random.randint(1,4)
        if oper == 1:
            print(jk+ikr)
        if oper == 2:
            print(jk*ikr)
        if oper == 3:
            print(jk - ikr)
        if oper == 4:
            print(jk/ikr)
    if "-" in thing:
        pieces = thing.split("-")
        jk = (int(pieces[0]) - int(pieces[1]))
        ikr = random.random()
        oper = random.randint(1,4)
        if oper == 1:
            print(jk+ikr)
        if oper == 2:
            print(jk*ikr)
        if oper == 3:
            print(jk - ikr)
        if oper == 4:
            print(jk/ikr)
    if "*" in thing:
        pieces = thing.split("*")
        jk = (int(pieces[0]) * int(pieces[1]))
        ikr = random.random()
        oper = random.randint(1,4)
        if oper == 1:
            print(jk+ikr)
        if oper == 2:
            print(jk*ikr)
        if oper == 3:
            print(jk - ikr)
        if oper == 4:
            print(jk/ikr)
    if "/" in thing:
        pieces = thing.split("/")
        jk = (int(pieces[0]) / int(pieces[1]))
        ikr = random.random()
        oper = random.randint(1,4)
        if oper == 1:
            print(jk+ikr)
        if oper == 2:
            print(jk*ikr)
        if oper == 3:
            print(jk - ikr)
        if oper == 4:
            print(jk/ikr)
