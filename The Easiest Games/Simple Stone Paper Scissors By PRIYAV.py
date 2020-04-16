play=input("Do you want to play stone, paper and scissors : ")
import random
i,j=0,0
while play=='yes':
    i,j=0,0
    while i<=4 and j<=4:
        comp=random.randint(1,3)
        choice=input('Enter your choice : ')
        if choice=='stone' or choice=='paper' or choice=='scissors':
            if comp==1:
                compc='stone'
            elif comp==2:
                compc='paper'
            else:
                compc='scissors'
            if compc=='stone' and choice=='scissors':
                    i+=1
            elif choice=='stone' and compc=='scissors':
                    j+=1
            elif compc=='paper' and choice=='scissors':
                    j+=1
            elif choice=='paper' and compc=='scissors':
                    i+=1
            elif compc=='paper' and choice=='stone':
                    i+=1
            elif choice=='paper' and compc=='stone':
                    j+=1
            score=str([j,i])
            print("Your choice:{0:s}     Computers choice:{1:s}    Score:{2:s}".format(choice,compc,score))
    if i==5:
        print('Computer won and you lose')
    else:
        print('Computer lose and you won')
    play=input('Do you want to play again?')
    
    
