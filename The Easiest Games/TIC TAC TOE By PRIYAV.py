play=input('Do you want to play tic tac toe : ')
player1=input('Enter name of player 1 : ')
player2=input('Enter name of player 2 : ')
while play=='yes':
    win1=0
    win2=0
    a,b,c,d,e,f,g,h,i=' ',' ',' ',' ',' ',' ',' ',' ',' '
    print("Let's play!!")
    print('''             *************
             * 1 * 2 * 3 *
             *************
             * 4 * 5 * 6 *
             *************
             * 7 * 8 * 9 *
             *************''')    
    def status():
        print('''               *************
               *''',a,'''*''',b,'''*''',c,'''*
               *************
               *''',d,'''*''',e,'''*''',f,'''*
               *************
               *''',g,'''*''',h,'''*''',i,'''*
               *************''')
    player=[1,2,1,2,1,2,1,2,1]
    while win1==0 and win2==0:
        for l in player:
            if l==1 and win1==win2==0:
                print(player1,'\'s turn')
            elif l==2 and win1==win2==0:
                print(player2,'\'s turn')
            else:
                pass
            if l==1 and win1==win2==0:
                no=int(input('Please enter a no. where you want to put your mark : '))
                if no==1 and a==' ':
                    a='X'
                elif no==2 and b==' ':
                    b='X'
                elif no==3 and c==' ':
                    c='X'
                elif no==4 and d==' ':
                    d='X'
                elif no==5 and e==' ':
                    e='X'
                elif no==6 and f==' ':
                    f='X'
                elif no==7 and g==' ':
                    g='X'
                elif no==8 and h==' ':
                    h='X'
                elif no==9 and i==' ':
                    i='X'
                else:
                    print('You should have entered a valid no\nNow u miss one turn')
                status()
            elif l==2 and win1==win2==0:
                no=int(input('Please enter a no. where you want to put your mark : '))
                if no==1 and a==' ':
                    a='O'
                elif no==2 and b==' ':
                    b='O'
                elif no==3 and c==' ':
                    c='O'
                elif no==4 and d==' ':
                    d='O'
                elif no==5 and e==' ':
                    e='O'
                elif no==6 and f==' ':
                    f='O'
                elif no==7 and g==' ':
                    g='O'
                elif no==8 and h==' ':
                    h='O'
                elif no==9 and i==' ':
                    i='O'
                else:
                    print('You should have entered a valid no\nNow u miss one turn')
                status()
            if a==b==c=='X':
                win1=1
            elif a==b==c=='O':
                win2=1
            elif d==e==f=='X':
                win1=1
            elif d==e==f=='O':
                win2=1
            elif g==h==i=='X':
                win1=1
            elif g==h==i=='O':
                win2=1
            elif a==d==g=='X':
                win1=1
            elif a==d==g=='O':
                win2=1
            elif h==b==e=='X':
                win1=1
            elif h==e==b=='O':
                win2=1
            elif i==f==c=='X':
                win1=1
            elif c==i==f=='O':
                win2=1
            elif a==e==i=='X':
                win1=1
            elif a==e==i=='O':
                win2=1
            elif g==e==c=='X':
                win1=1
            elif g==e==c=='O':
                win2=1
        if win1==1:
            print(player1,' has won')
        elif win2==1:
            print(player2,' has won')
        else:
            print('Oops! Draw')
            win1=1
            win2=1
    play='no'
    play=input('Do you want to play again?')
print('Thanks for playing, ',player1,' and ',player2)
