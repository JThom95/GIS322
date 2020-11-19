### Import modules
import random

### Create list of teams 
teams = ['Team 1','Team 2','Team 3','Team 4','Team 5','Team 6','Team 7','Team 8','Team 9','Team 10']

### Create team performance fucntion 'order()'
def order():
    #Create final list
    newList = []
    while len(teams) != 0:
        i = random.randint(0,(len(teams)-1))
        newList.append(teams[i])
        teams.pop(i)
    if len(teams) == 0:
      print('Everything checks out!')
    print(newList)

order()