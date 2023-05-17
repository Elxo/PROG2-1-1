
saraksts = open('filmas.txt', 'r')
saraksts.close()
class Filma:
    def __init__(self, nosaukums, rezisors, vertejumi):
        self.nosaukums = nosaukums
        self.rezisors = rezisors
        self.vertejums = vertejumi


def movie():
        saraksts = open('filmas.txt', 'a')
        nosaukums = input('Ievadiet Filmas nosaukumu: ')
        saraksts.write(nosaukums )
        saraksts.write("; ")
        rezisors = input('Ievadiet režisora vārdu: ')
        saraksts.write(rezisors)
        saraksts.write("; ")
        vertejumi = input ('Ievadiet savu vērtējumu:')
        saraksts.write(vertejumi)
        saraksts.write("""
     """)
        saraksts.close
        
        return nosaukums, vertejumi, rezisors


# jauna filmas vērtējuma ievade.
def jauns_vertejums():
    jvertejums = ('')
    while True:
        jvertejums = float(input("Filmas vērtējums: "))
        if jvertejums > 5 or jvertejums < 0.5:
         print("Vērtējumam jābūt no pus zvaigznes  līdz piecām zvaigznēm")
         jvertejums = float(input("Filmas vērtējums: "))
        
        elif jvertejums == 5:
            break
        elif jvertejums > 0.5 and jvertejums <= 5:
            break       

        return jvertejums
    
    
    
#Izmantotāja konsoles iespejas arguments
print('''Sveicināts! 
Lai pievienotu jaunu filmu spied 1
Filmu saraksta apskatīšanai spied 2
Jauna vērtējuma pievienošanai spied 3
Lai beigtu darbu spied 4''')
x = int(input(' Kādudarbību vēlaties veikt? :'))
# Lietotāja  izvēlne 
while x !=4:
    
    if x == 0:
        break
   
        

    elif x == 1:
         movie()
         break



    elif x == 2:
        saraksts = open('filmas.txt', 'r')
        print(saraksts.read())
        saraksts.close()
        break

    elif x == 3:
        jauns_vertejums()
        break

        


print('Uzredzēšanos!')

pass


