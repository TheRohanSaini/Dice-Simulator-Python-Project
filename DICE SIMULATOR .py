import random

print("┌─────────┐");
print("│         │");
print("│  DICE   │");
print("│         │");
print("└─────────┘");
g=0
r=0
t=[]
total=0
v=int(input("HOW MANY TIMES DICE WILL ROLL?"))
for i in range(v):

    n=input("PRESS G TO ROLL DICE").lower()
    if n=="g":
        r=random.randint(1,6)
        t.append(r)
        if r==1:
            print("┌─────────┐");
            print("│         │");
            print("│    ●    │");
            print("│         │");
            print("└─────────┘");
        if r==2:
            print("┌─────────┐");
            print("│  ●      │");
            print("│         │");
            print("│      ●  │");
            print("└─────────┘");
        if r==3:
            print("┌─────────┐");
            print("│ ●       │");
            print("│    ●    │");
            print("│       ● │");
            print("└─────────┘");
        if r==4:
            print("┌─────────┐");
            print("│ ●     ● │");
            print("│         │");
            print("│ ●     ● │");
            print("└─────────┘");
        if r==5:
            print("┌─────────┐");
            print("│ ●     ● │");
            print("│    ●    │");
            print("│ ●     ● │");
            print("└─────────┘");
        if r==6:
            print("┌─────────┐");
            print("│ ●     ● │");
            print("│ ●     ● │");
            print("│ ●     ● │");
            print("└─────────┘");

        print(r)

for i in t:
    total+=i
print("YOUR TOTAL IS=", total)
print("your total is")