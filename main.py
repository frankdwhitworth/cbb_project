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

from classes.basics import Basics
from classes.models.four_factor import Four_Factor
from classes.models.confidence_letdown import Confidence_Letdown

# . . . . . Main Method . . . . .
# . @s: just the main method    .
# . . . . . . . . . . . . . . . .
def main():
    print(". . .")
    query_team = input("Who's scheudle would you like to see? (Enter 0 to exit) \n> ")
    while query_team != '0':
        # getting next opponent abbr
        query_abbr = Basics.find_query_abbr(query_team)
        next_op_abbr = Basics.find_next_opponent_abbr(query_team)
        next_game = Basics.find_next_game(query_team)
        # getting the schedule for the queried team
        query_season = Basics.query_season_list(query_team)
        query_past_5 = Basics.query_past_5_list(query_team, query_season)
        # setting up local arrays for the team we just queried
        op_season = Basics.query_season_list(next_op_abbr)
        op_past_5 = Basics.query_past_5_list(next_op_abbr, op_season)
        # printing last 5 games for query team and their next opponent
        Basics.print_past_5(query_team, query_past_5, next_op_abbr, op_past_5)
        # Getting the boxscores for the past 5 games
        query_5_boxscores = Basics.past_5_to_boxscores(query_past_5)
        op_5_boxscores = Basics.past_5_to_boxscores(op_past_5)
        # That's it for prep, let's move to risk assesment
        print("\nThis is the beginning of the risk assesment for", query_team, "vs.", next_op_abbr, "(", next_game.date, ")")
        # This is where we get the teams in a dictionary so that we can see all of their stats.
        team_stats = teams_dict(query_team, next_op_abbr)
        # Now, we will do the basic four factor comparison
        Four_Factor.four_factors(team_stats)
        # Now we will do the confidence_letdown
        Confidence_Letdown.confidence_letdown(query_5_boxscores, op_5_boxscores, query_team, next_op_abbr)

        query_team = input("\nWho's scheudle would you like to see? (Enter 0 to exit) \n> ")


def confidence_letdown(query_past_5, op_past_5):
    print()

def teams_dict(query_abbr, op_team):
    team_stats={}
    for team in Teams(): 
        # this is the if conditional for the query team        
        if team.name == query_abbr or team.abbreviation.lower() == query_abbr:
            team_stats['query'] = team
            query = team.abbreviation.lower()
            ''' print(query, "(the query) was found!") '''
        # this is the if conditional for the oponenet
        elif team.name == op_team or team.abbreviation.lower() == op_team:
            team_stats['op'] = team
            op = team.abbreviation.lower()
            ''' print(op, "(the op) was found") '''
    return team_stats



if __name__ == '__main__':
    main()