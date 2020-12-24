#  . . . . . . . . . . . . . . . . . . . . . . . .
#  Created on Dec. 23, 2020
#
#  @author:     dixon
#  @file:       main.py   
#  @summary:    to evaluate the risk of betting on 
#               different CBB teams
#  . . . . . . . . . . . . . . . . . . . . . . . . 

from sportsreference.ncaab.teams import Teams
from sportsreference.ncaab.boxscore import Boxscore
from sportsreference.ncaab.schedule import Schedule
# . . . . . Main Method . . . . .
# . @s: just the main method    .
# . . . . . . . . . . . . . . . .
def main():
    print('\n\n\nRyan, this is python. If you see this by command line output, congrats on running your first program on here.')
    print('now onto testing out one of our libraries, sportsreference')
    print(". . .")
    query_team = "example"
    while query_team != 0:
        query_team = input("Who's scheudle would you like to see? (Enter 0 to exit)")
        if query_team == 0:
            continue
        team_schedule = Schedule(query_team)
        for game in team_schedule:
            print(game.date)
            print(game.result)
            query_boxscore = game.boxscore
            print(query_boxscore)
            print("- - - - - - - - - - - - -")
    '''
    # This is an example of how you can use the Teams object (imported in line 10)
    for team in Teams():
        if team.name == 'Duke':
            print(team.name, team.wins, team.losses)
            print("Duke's turn-over % =", team.turnover_percentage)
    '''



if __name__ == '__main__':
    main()