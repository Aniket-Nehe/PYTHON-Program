letters = [
    ['h', 'o', 'l', 'i', 'd', 'a', 'y'],
    ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'],
    ['b', 'o', 'o', 't', 'c', 'a', 'm', 'p'],
    ['f', 'l', 'o', 'w', 'c', 'h', 'a', 'r', 't'],
    ['w', 'o', 'r', 'd', 's', 'c', 'a', 'p', 'e', 's']]

words = [
    ["hi", "hay", "day", "had", "lay", "dal", "lad", "lid", "hold", "lady", "hail"],
    ["go", "an", "in", "no", "on", "map", "mom", "gap", "gag", "pig", "man", "ping", "pong", "pram", "prom", "ramp"],
    ["am", "at", "to", "cab", "cap", "cob", "cop", "map", "mop", "act", "bat", "camp", "comb", "boom", "pact",
     "atom"],
    ["of", "at", "or", "to", "caw", "cow", "how", "who", "calf", "claw", "flaw", "flow", "fowl", "wolf", "crow",
     "half"],
    ["we", "do", "as", "cap", "caw", "cop", "cow", "paw", "cod", "dew", "pad", "cape", "cope", "crap", "crew",
     "crop", "pace"]]


lives = 2
level = 0
Score = 0

while level < len(letters):
    if lives > 0:
        print(f"Level {level + 1}")
        print("Create 3 words using the given letters:")

        for letter in letters[level]:
            print(letter, end='')
        print()

        count = 0
        oldword=""
        while count < 3:
            word = input("Enter a word: ").lower()
            
            if  word!=oldword:   
                if word in words[level]:
                    count +=1
                    Score +=1
                    oldword=word
                else:
                    print("❌Wrong guess❌")
                    lives -=1  
                    Score -=1
                    print(f"Lives remeining: {lives}")
                    
                    if lives == 0:
                        print("Game Over👻")
                        break
                    
            else:
                print("❌Wrong guess❌")
                lives -=1  
                Score -=1
                print(f"Lives remeining: {lives}")

                if lives == 0:
                    print("Game Over👻")
                    break
    
        else:
            choice = input("Do you want to continue to next level? (y/n) ").lower()
            if(choice == 'y'):
                level += 1
                    
            else:
                print()
                print('Thanks for playing the game!!!')
                print(f'Your score is {Score}')
                break
                                
    else:
        print('Game Over 👻, Thanks for playing the game!!!')
        print(f'Your score is {Score}')    
        break
    
if level==5:
    if lives > 0:
       print("Congratulations🥳! You have completed all levels😊")
       print(f"Your Score is : {Score}")
        
    
        