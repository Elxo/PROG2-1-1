import random
command = ""
#aizstāvējs
x = 0
limenis1 = 1000
limenis2 = 10000
limenis3 = 100000
limenis4 = 1000000
limenis5 = 10000000
limenis6 = 1000000000
limenis7 = 100000000000
limenis8 = 10000000000000
limenis9 = 10000000000000000
limenis10 = 1000000000000000000
limenis11 = 1000000000000000000000
limenis12 = 100000000000000000000000
limenis13 = 10000000000000000000000000
limenis14 = 10000000000000000000000000000
speletaja_limenis = x
dzivibas = 100
kaujas_punkti=0
kopejie_punkti = x


while command.lower != "pamest":
    command.lower = input("Cīnīties vai pamest? ")
    if command.lower == 'cīnīties' or 'c':
        dzivibas = dzivibas - random.randint(12, 26)
        kaujas_punkti = kaujas_punkti + random.randint(10, 30)
        if dzivibas < 0:
            print('Spēles Beigas')
            #Datus nosūta  uz datni.
    elif command.lower == "pamest":
        print ('Spēles beigas')
        #Datu sūtīšana uz datni


if kaujas_punkti >= limenis1:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis2:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis3:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis4:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis5:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis6:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis7:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis8:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis9:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis10:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis11:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis12:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis13:
    print("Urrrā esi sasniedzis nākamo līmeni")
if kaujas_punkti >= limenis14:
    print("Urrrā esi sasniedzis nākamo līmeni")


