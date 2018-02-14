sum=(50)
print("#Rules#")
print(".Some coins are selected/")
print(".Player1 take some coins from the objects but not all/")
print(".Player2 take some coins but not more than double that player1 has taken/")
print(".Player1 take some coins but not more than double that player2 has taken/")
print(".The player who take the final coin(s) is the winner/")
print("*****")
print("press <<start>>")
S=input()
if("start"==S) or ("START"==S):
 print("sum:",sum)
 print("player1:")
 playerone = int(input())
 while(True):
    if(0<playerone<=sum):
        sum-=playerone
        print("sum:",sum)
        if(sum<=0):
            break
        while(True):
            while(sum<=0):
                break
            if(sum>0):
                print("player2:")
                playertwo=int(input())
                if((0<playertwo<=sum) and (playertwo<=(2*(playerone)))):
                    sum-=playertwo 
                    print("sum:",sum)
                    if(sum<=0):    
                       print("Player2 is The Winner")
                       break
                    while(True):
                        print("player1:")
                        playerone=int(input())
                        if((0<playerone<=sum) and (playerone<=(2*(playertwo)))):
                            sum-=playerone
                            print("sum:",sum)
                            if(sum<=0):
                                print("Player1 is The Winner")
                            break
                        print("play again")
                else:
                    print("play again")
                      
