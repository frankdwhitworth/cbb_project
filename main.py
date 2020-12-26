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
        '''query_abbr = find_query_abbr(query_team)'''
        next_op_abbr = find_next_opponent_abbr(query_team)
        '''next_game = find_next_game(query_team)'''
        # getting the schedule for the queried team
        query_season = query_season_list(query_team)
        query_past_5 = query_past_5_list(query_team, query_season)
        # setting up local arrays for the team we just queried
        op_season = query_season_list(next_op_abbr)
        op_past_5 = query_past_5_list(next_op_abbr, op_season)
        # printing last 5 games for query team and their next opponent
        print_past_5(query_team, query_past_5, next_op_abbr, op_past_5)
        print("\nThis is the beginning of the risk assesment for", query_team, "vs.", next_op_abbr, "(", next_game.date, ")")
        # This is where we get the teams in a dictionary so that we can see all of their stats.
        team_stats = teams_dict(query_team, next_op_abbr)
        # Now, we will do the basic four factor comparison
        #four_factors(team_stats)
        query_team = input("\nWho's scheudle would you like to see? (Enter 0 to exit) \n> ")


def confidence_letdown(query_past_5, op_past_5):
    print()

def four_factors(team_stats):
    # We are first initializing the ratings at zero
    query_rating = 0
    op_rating = 0
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # First, we will do the query rating 
    query_team = team_stats['query']
    team_stats['q_field_goal_%'] = query_team.field_goal_percentage * 100
    team_stats['q_turnover_%'] = query_team.turnover_percentage
    # We are correcting the turnover % because we need to have a higher % be best
    #       and normally with turnovers, having a lower rebound % is best
    team_stats['q_turnover_corrected'] = 100 - team_stats['q_turnover_%']
    team_stats['q_total_rebound_%'] = query_team.total_rebound_percentage
    team_stats['q_free_throw_%'] = query_team.free_throw_percentage * 100
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # I want to implement strenght_of_schedule soon, but not right now
    #       it will give us a rating where negative is easier than average (0.00) 
    #       and positive is harder than average (0.00)
    #team_stats['schedule']
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Now we will do the op rating
    op_team = team_stats['op']
    team_stats['op_field_goal_%'] = op_team.field_goal_percentage * 100
    team_stats['op_turnover_%'] = op_team.turnover_percentage
    # We are correcting the turnover % because we need to have a higher % be best
    # and normally with turnovers, having a lower rebound % is best
    team_stats['op_turnover_corrected'] = 100 - team_stats['op_turnover_%']
    team_stats['op_total_rebound_%'] = op_team.total_rebound_percentage
    team_stats['op_free_throw_%'] = op_team.free_throw_percentage * 100
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Next, we are moving onto find the max_stats
    #       so that we can weight the given team
    #       stats to make our percentages work
    max_stats_dict = max_stats()
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Now we are going to figure out the curve of the stats
    #       We will put the curve inside its own dictionary
    #       just to be consistent and orderly
    stats_curve={}
    stats_curve['fg_curve'] = 100 - max_stats_dict['max_field_goal_perc']
    stats_curve['t_curve'] = 100 - max_stats_dict['max_turnover_perc']
    stats_curve['r_curve'] = 100 - max_stats_dict['max_rebound_perc']
    stats_curve['ft_curve'] = 100 - max_stats_dict['max_free_throw_perc']
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Now that we have the curves figured out, we will add them to our 
    #       already determined season stats for the query
    #       team and the opposition, making a new dictionary
    corrected_stats={}
    corrected_stats['q_field_goal_%'] = team_stats['q_field_goal_%'] + stats_curve['fg_curve']
    corrected_stats['q_turnover_%'] = team_stats['q_turnover_corrected'] + stats_curve['t_curve']
    corrected_stats['q_total_rebound_%'] = team_stats['q_total_rebound_%'] + stats_curve['r_curve']
    corrected_stats['q_free_throw_%'] = team_stats['q_free_throw_%'] + stats_curve['ft_curve']
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Now we will do the op corrected stats
    corrected_stats['op_field_goal_%'] = team_stats['op_field_goal_%'] + stats_curve['fg_curve']
    corrected_stats['op_turnover_%'] = team_stats['op_turnover_corrected'] + stats_curve['t_curve']
    corrected_stats['op_total_rebound_%'] = team_stats['op_total_rebound_%'] + stats_curve['r_curve']
    corrected_stats['op_free_throw_%'] = team_stats['op_free_throw_%'] + stats_curve['ft_curve']
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Let's test to see if it worked
    '''print(corrected_stats)
    for elem in corrected_stats:
        print(elem, "=", corrected_stats[elem]) '''
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Great, it works. Let's move onto the weights:
    #       field goals = 40%
    #       turnovers = 25%
    #       rebounds = 20%
    #       free throws = 15%
    # Let's initialize the ratings
    query_rating = 0
    op_rating = 0
    # Now the weights
    fg_weight = 40
    t_weight = 25
    r_weight = 20
    ft_weight = 15
    # Now add the ratings up, first query team
    query_rating += (fg_weight * corrected_stats['q_field_goal_%'])
    query_rating += (t_weight * corrected_stats['q_turnover_%'])
    query_rating += (r_weight * corrected_stats['q_total_rebound_%'])
    query_rating += (ft_weight * corrected_stats['q_free_throw_%'])
    # Now onto op team
    op_rating += (fg_weight * corrected_stats['op_field_goal_%'])
    op_rating += (t_weight * corrected_stats['op_turnover_%'])
    op_rating += (r_weight * corrected_stats['op_total_rebound_%'])
    op_rating += (ft_weight * corrected_stats['op_free_throw_%'])
    # Let's divide them by 100 to get a % (1-100)
    query_rating /= 100
    op_rating /= 100
    # Now print them
    ''' print("\nquery_rating =", query_rating)
    print("op_rating =", op_rating)
    print() '''
    # just trying out their rating system
    min_and_max_ranks = min_and_max_ratings()
    # trying out to see if i can weigh them like i did
    min_rank = min_and_max_ranks[0]
    max_rank = min_and_max_ranks[1]
    curve = min_rank * -1
    top_max = curve + max_rank
    team_stats['q_rank'] = (query_team.simple_rating_system + curve) / top_max
    team_stats['op_rank'] = (op_team.simple_rating_system + curve) / top_max
    ''' print("adjusted q_rank =", team_stats['q_rank'])
    print("adjusted o_rank =", team_stats['op_rank']) '''
    # Now we have our new ranks
    print("\nFour Factor Rating")
    print(query_team.name, " rating =", query_rating * team_stats['q_rank'])
    print(op_team.name, " rating =", op_rating * team_stats['op_rank'])



def max_stats():
    max_stats={}
    max_stats['max_field_goal_perc'] = 0
    max_stats['max_turnover_perc'] = 0
    max_stats['max_rebound_perc'] = 0
    max_stats['max_free_throw_perc'] = 0
    for team in Teams():
        if isinstance(team.field_goal_percentage, float):
            temp_fgp = team.field_goal_percentage * 100
            temp_tp = 100 - team.turnover_percentage
            temp_rp = team.total_rebound_percentage
            temp_ftp = team.free_throw_percentage * 100
            if temp_fgp > max_stats['max_field_goal_perc']:
                max_stats['max_field_goal_perc'] = temp_fgp
            if temp_tp > max_stats['max_turnover_perc']:
                max_stats['max_turnover_perc'] = temp_tp
            if temp_rp > max_stats['max_rebound_perc']:
                max_stats['max_rebound_perc'] = temp_rp
            if temp_ftp > max_stats['max_free_throw_perc']:
                max_stats['max_free_throw_perc'] = temp_ftp
    return max_stats

def min_and_max_ratings():
    min_rating = 0
    max_rating = 0
    min_and_max = []
    for team in Teams():
        if isinstance(team.simple_rating_system, float):
            if team.simple_rating_system < min_rating:
                min_rating = team.simple_rating_system
            elif team.simple_rating_system > max_rating:
                max_rating = team.simple_rating_system
    min_and_max.append(min_rating)
    min_and_max.append(max_rating)
    return min_and_max

def teams_dict(query_abbr, op_team):
    team_stats={}
    for team in Teams(): 
        # this is the if conditional for the query team        
        if team.name == query_abbr or team.abbreviation.lower() == query_abbr:
            team_stats['query'] = team
            query = team.abbreviation.lower()
            print(query, "(the query) was found!")
        # this is the if conditional for the oponenet
        elif team.name == op_team or team.abbreviation.lower() == op_team:
            team_stats['op'] = team
            op = team.abbreviation.lower()
            print(op, "(the op) was found") 
    print(team_stats)
    return team_stats

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
                next_opponent_name = find_next_opponent_abbr(query_team)
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



if __name__ == '__main__':
    main()