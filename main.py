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

from datetime import date

import pandas as pd

# . . . . . Main Method . . . . .
# . @s: just the main method    .
# . . . . . . . . . . . . . . . .
def main():
    print('\n\n\nRyan, this is python. If you see this by command line output, congrats on running your first program on here.')
    print('now onto testing out one of our libraries, sportsreference')
    print(". . .")
    query_team = input("Who's scheudle would you like to see? (Enter 0 to exit) \n> ")
    while query_team != '0':

        # getting the schedule for the queried team
        team_schedule = Schedule(query_team)
        #team_stats = Teams(query_team)
        #shooting_perc_5(team_schedule)

        # setting up local arrays for the team we just queried
        past_played_games = []
        past_five_games = []
        tot_games_played = 0
        
        '''
        # printing out different team stats.
        print('. . . . . . printing team stats . . . . . . . ')
        # we have to find the team first by going through all the other teams
        for team in Teams():                  
            # once this if statement is successfully done, ie. once we find our team
            if team.name == query_team:
                # it will print the stats that we want
                tot_games_played = team.games_played
                print("total games played =", tot_games_played)
        print('. . . . . . hope that worked . . . . . . ')
        '''

        # this will take the schedule that we got from the querried team and now iterrate through each game in schedule
        for game in team_schedule:
            #print(game.boxscore.pace)
            # this is a huge line. this will decide if the game has been played or not...
            if game.boxscore.pace != None:
                past_played_games.append(game)
                # if the game boxscore pace IS NOT None, meaning there is a pace, then it will continue to run
                #print(game.date)
                #print(game.result)
                query_boxscore = game.boxscore
                #print('trying new strat =', query_boxscore.losing_name)
                #print(query_boxscore)
                print("- game saved -")
            # if the game boxscore pace IS None, that means there will be no more games
            else: 
                print("No more games..")
                break
        
        tot_games_played = len(past_played_games)
        print("Now we will be printing the games played (well, testing with the date) - should be", tot_games_played, "total games")
        for game in past_played_games:
            print(game.date)
        print("Next we will log the last 5 games")
        game_count = 0
        if tot_games_played <= 5:
            for game in past_played_games:
                past_five_games.append(game)
        else: 
            for game in past_played_games:
                game_count += 1
                if game_count > (tot_games_played - 5):
                    past_five_games.append(game)
        print("- - - - -")
        print("Now we will be printing the last 5 games played (well, testing with the date) - should be 5 total games")
        for game in past_five_games:
            print(game.date)
        
        
        query_team = input("\nWho's scheudle would you like to see? (Enter 0 to exit) \n> ")

    '''
    # This is an example of how you can use the Teams object (imported in line 10)
    for team in Teams():
        if team.name == 'Duke':
            print(team.name, team.wins, team.losses)
            print("Duke's turn-over % =", team.turnover_percentage)
    '''

def shooting_perc_5(team_sched):
    print(team_sched)

if __name__ == '__main__':
    main()