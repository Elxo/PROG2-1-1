cels = ['Dienvidi', 'Ziemeļi', 'Rietumi', 'Austrumi', 'Austrumi', 'Ziemeļi',  'Rietumi', 'Rietumi', 'Rietumi', 'Rietumi', 'Rietumi', 'Rietumi', 'Dienvidi','Dienvidi','Dienvidi','Dienvidi','Dienvidi','Dienvidi','Dienvidi','Dienvidi','Dienvidi','Dienvidi','Dienvidi']
Z = 0
D = 0
R = 0 
A = 0
z = ('Ziemeļi')
r = ('Rietumi')
d = ('Dienvidi')
a = ('Austrumi')
X=0
i=0

for DP in cels:
    
    if cels[X] == z:
     Z+=1
     X += 1
    elif cels[X] == r:
        R+=1
        X += 1
    elif cels[X] == d:
        D+=1
        X += 1
    elif cels[X] == a:
        A+=1
        X += 1
    elif X == len(cels):
        break

if Z == D and A==R:
    print("STĀVI UZ VIETAS")

elif D > Z:
    D-=Z 
    print(f'Jādodas uz dienvidiem {D} reizi(es)')
elif Z > D:
    Z-=D
    print(f'Jādodas uz ziemeļiem {Z} rezi(es)')


if Z == D and A==R:
    i+=1
elif A > R:
    A-=R
    print(f'Jādodas uz austrumiem {A} reizi(es)')
elif R>A:
    R-=A
    print(f'Jādodas uz Rietumiem {R} reizi(es)')




        