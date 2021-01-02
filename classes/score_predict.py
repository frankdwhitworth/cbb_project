#  . . . . . . . . . . . . . . . . . . . . . . . .
#  Created on Jan. 2, 2021
#
#  @author:     dixon
#  @file:       score_predict.py   
#  @summary:    making a class of the beginnig score
#               prediction alg. 
#  . . . . . . . . . . . . . . . . . . . . . . . . 

import pandas as pd
from sportsreference.ncaab.teams import Teams
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


class Score_Predict:
    def online_predictor():
        FIELDS_TO_DROP = ['away_points', 'home_points', 'date', 'location', 'losing_abbr', 'losing_name', 'winner', 'winning_abbr', 'winning_name', 'home_ranking', 'away_ranking']
        dataset = pd.DataFrame()
        teams = Teams()
        for team in teams:
            dataset = pd.concat([dataset, team.schedule.dataframe_extended])
        X = dataset.drop(FIELDS_TO_DROP, 1).dropna().drop_duplicates()
        y = dataset[['home_points', 'away_points']].values
        X_train, X_test, y_train, y_test = train_test_split(X, y)
        parameters = {'bootstrap': False,
                    'min_samples_leaf': 3,
                    'n_estimators': 50,
                    'min_samples_split': 10,
                    'max_features': 'sqrt',
                    'max_depth': 6}
        model = RandomForestRegressor(**parameters)
        model.fit(X_train, y_train)
        print(model.predict(X_test).astype(int), y_test)
