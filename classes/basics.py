#  . . . . . . . . . . . . . . . . . . . . . . . .
#  Created on Dec. 26, 2020
#
#  @author:     dixon
#  @file:       basics.py   
#  @summary:    making a class of the basic funcs
#               so that main.py looks better 
#  . . . . . . . . . . . . . . . . . . . . . . . . 

from sportsreference.ncaab.teams import Teams
from sportsreference.ncaab.boxscore import Boxscore
from sportsreference.ncaab.schedule import Schedule


class Basics:
    def query_season_list(query_team):
        team_schedule = Schedule(query_team)
        # setting up local arrays for the team we just queried
        past_played_games = []
        past_five_games = []
        ot_games_played = 0
        # this will take the schedule that we got from the querried team and now iterrate through each game in schedule
        first_none = 0
        for game in team_schedule:
            if game.boxscore.pace != None:
                past_played_games.append(game)
                query_boxscore = game.boxscore
            else: 
                if first_none == 0:
                    next_game = game
                    next_opponent_name = Basics.find_next_opponent_abbr(query_team)
                    first_none = 1
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

    def find_query_abbr(query_team):
        first_none = 0
        for team in Teams():
            if team.name == query_team or team.abbreviation == query_team:
                return team.abbreviation

    def find_op_abbr(query_team):
        team_schedule = Schedule(query_team)
        for game in team_schedule:
            return game.opponent_abbr


    def find_next_opponent_abbr(query_team):
        team_schedule = Schedule(query_team)
        first_none = 0
        for game in team_schedule:
            if game.boxscore.pace == None and first_none == 0:
                return game.opponent_abbr

    def print_past_5(query_abbr, query_past_5, next_op_abbr, op_past_5):
        print(". . . \nLast 5 games for", query_abbr, "and", next_op_abbr, "\n")
        print("\t\t", query_abbr)
        print("--------------------------------------------")
        for game in query_past_5:
            print(game.date, "-\t", game.opponent_abbr)
        print()
        print("\t\t", next_op_abbr)
        print("--------------------------------------------")
        for game in op_past_5:
            print(game.date, "-\t", game.opponent_abbr)

    def past_5_to_boxscores(past_5):
        past_5_boxscores=[]
        for game in past_5:
            past_5_boxscores.append(game.boxscore)
        return past_5_boxscores