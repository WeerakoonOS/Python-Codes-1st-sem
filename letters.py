##letters = ['a','r','c','b','n','l','o','p','e','i']
##lists=[]
##string=input('Enter the letter: ')
##if string in letters:
##    print(string+' is avilable!')
##else:
##    print('input is not available!')

lists=[]
for i in range (21):
    if i%3!=0:
        lists.append(i)
    else:
        continue
print(lists)
