IPL 1st Inning Score Prediction using Machine Learning
The Dataset contains ball by ball information of the matches played between IPL Teams of Season 1 to 10, i.e. from 2008 to 2017.
This Machine Learning model adapts a Regression Appoach to predict the score of the First Inning of an IPL Match.
The Dataset can be downloaded from Kaggle https://www.kaggle.com/datasets/yuvrajdagur/ipl-dataset-season-2008-to-2017 IPL Dataset Season 2008 to 2017

Dataset consists following columns:
• mid: Unique match id.
• date: Date on which the match was played.
• venue: Stadium where match was played.
• batting_team: Batting team name.
• bowling_team: Bowling team name.
• batsman: Batsman who faced that particular ball.
• bowler: Bowler who bowled that particular ball.
• runs: Runs scored by team till that point of instance.
• wickets: Number of Wickets fallen of the team till that point of instance.
• overs: Number of Overs bowled till that point of instance.
• runs_last_5: Runs scored in previous 5 overs.
• wickets_last_5: Number of Wickets that fell in previous 5 overs.
• striker: max(runs scored by striker, runs scored by non-striker).
• non-striker: min(runs scored by striker, runs scored by non-striker).
• total: Total runs scored by batting team at the end of first innings.