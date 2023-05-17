saraksts = open('main.txt', 'r')
teksts = ""
i = 0
teksts = saraksts.read()
words = teksts.split()

biezums = {}
for word in words:
    biezums[word] = teksts.count(word)


vardudaudzums = sorted(biezums.items(), key = lambda x: (-x[1], x[0]))

for word in vardudaudzums:
     if len(word[0]) >= 4 and i <= 3:
            print(word[0])
            i = i+1




    
    
