def commaCode(spam):
    print('\'',end='')
    for i in range(len(spam)-1):
        print(spam[i],end=', ')
    print('and '+spam[-1]+'\'')

L= ['apples', 'bananas', 'tofu', 'cats']
commaCode(L)

def commaCode2(spam):
    s=''
    for i in range(len(spam)-1):
        s += spam[i]+', '
    return ('\''+s+'and '+spam[-1]+'\'')

L= ['apples', 'bananas', 'tofu', 'cats']
print(commaCode2(L))
