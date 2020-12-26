#  . . . . . . . . . . . . . . . . . . . . . . . .
#  Created on Dec. 26, 2020
#
#  @author:     dixon
#  @file:       confidence_letdown.py   
#  @summary:    our second model, that finds the
#               team that over performed, or won
#               against a better team and then 
#               predicts that they will under perform
#               and has a letdown
#  . . . . . . . . . . . . . . . . . . . . . . . . 

from sportsreference.ncaab.teams import Teams
from sportsreference.ncaab.boxscore import Boxscore
from sportsreference.ncaab.schedule import Schedule

class Confidence_Letdown:
    def confidence_letdown(query_past_5, op_past_5, query_team, next_op_abbr):
        print("\nBeginning of Confidence_Letdown model\n")
        count = 1
        print(query_team, " past 5")
        for game in query_past_5:
            print("Game", count, "\n. . .")
            print("Home team defensive rating =", game.home_defensive_rating)
            print("Home team offensive rating =", game.home_offensive_rating)
            print("Away team defensive rating =", game.away_defensive_rating)
            print("Away team offensive rating =", game.away_offensive_rating)
            print("- Ranking -")
            print("Home team ranking =", game.home_ranking)
            print("Away team ranking =", game.away_ranking)
            count += 1
        count = 1
        print("\n-----------------\n")
        print(next_op_abbr, " past 5")
        for game in op_past_5:
            print("Game", count)
            print("Home team defensive rating =", game.home_defensive_rating)
            print("Home team offensive rating =", game.home_offensive_rating)
            print("Away team defensive rating =", game.away_defensive_rating)
            print("Away team offensive rating =", game.away_offensive_rating)
            print("- Ranking -")
            print("Home team ranking =", game.home_ranking)
            print("Away team ranking =", game.away_ranking)
            print(". . . ")
            count += 1
