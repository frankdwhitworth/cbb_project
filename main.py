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
        # getting next opponent abbr
        next_op_abbr = find_next_opponent_abbr(query_team)
        next_game = find_next_game(query_team)

        # getting the schedule for the queried team
        query_season = query_season_list(query_team)
        query_past_5 = query_past_5_list(query_team, query_season)
        
        # setting up local arrays for the team we just queried
        op_season = query_season_list(next_op_abbr)
        op_past_5 = query_past_5_list(next_op_abbr, op_season)

        # printing last 5 games for query team and their next opponent
        print_past_5(query_team, query_past_5, next_op_abbr, op_past_5)

        print("\nThis is the beginning of the risk assesment for", query_team, "vs.", next_op_abbr, "(", next_game.date, ")")
        
        # This is where we start getting into the good stuff.
        #baseline_comp(query_team, next_op_abbr)
        query_team = input("\nWho's scheudle would you like to see? (Enter 0 to exit) \n> ")





def baseline_comp(query_team, op_team):
    print(query_team)

def query_season_list(query_team):

    team_schedule = Schedule(query_team)
    #team_stats = Teams(query_team)
    #shooting_perc_5(team_schedule)

    # setting up local arrays for the team we just queried
    past_played_games = []
    past_five_games = []
    ot_games_played = 0

    # this will take the schedule that we got from the querried team and now iterrate through each game in schedule
    first_none = 0
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
            #print("- game saved -")
        # if the game boxscore pace IS None, that means there will be no more games
        else: 
            if first_none == 0:
                next_game = game
                next_opponent_name = find_next_opponent_abbr(query_team)
                #print("Trying to find next opponent name =", next_opponent_name)
                first_none = 1
            #print("No more games..")
            break
    return past_played_games


def query_past_5_list(query_team, query_season):
    past_five_games = []
    tot_games_played = len(query_season)

    game_count = 0
    if tot_games_played <= 5:
        for game in query_season:
            past_five_games.append(game)
    else: 
        for game in query_season:
            game_count += 1
            if game_count > (tot_games_played - 5):
                past_five_games.append(game)
    return past_five_games


def find_next_game(query_team):
    team_schedule = Schedule(query_team)
    first_none = 0
    for game in team_schedule:
        if game.boxscore.pace == None and first_none == 0:
            return game


def find_next_opponent_abbr(query_team):
    team_schedule = Schedule(query_team)
    first_none = 0
    for game in team_schedule:
        if game.boxscore.pace == None and first_none == 0:
            return game.opponent_abbr

def print_past_5(query_team, query_past_5, next_op_abbr, op_past_5):
    print(". . . Last 5 games for", query_team, "and", next_op_abbr, "\n")
    print("\t\t", query_team)
    print("--------------------------------------")
    for game in query_past_5:
        print(game.date, "-\t", game.opponent_abbr)
    print()
    print("\t\t", next_op_abbr)
    print("--------------------------------------")
    for game in op_past_5:
        print(game.date, "-\t", game.opponent_abbr)


if __name__ == '__main__':
    main()