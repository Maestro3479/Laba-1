TempStr = ''
file = open('7tx.txt', 'r')
TempList = [i.replace('\n', '') for i in file] #
for i in TempList:
    if i.startswith('www.'):
        Tempstr = 'https://' + i
        if not i.endswith('.com'):
            Tempstr += '.com'
        print(Tempstr)
