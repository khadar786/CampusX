import pandas as pd
import numpy as np
import json

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)
      
ipl_matches='https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv'
matches=pd.read_csv(ipl_matches)

ipl_ball = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRu6cb6Pj8C9elJc5ubswjVTObommsITlNsFy5X0EiBY7S-lsHEUqx3g_M16r50Ytjc0XQCdGDyzE_Y/pub?output=csv"
balls = pd.read_csv(ipl_ball)

ball_withmatch = balls.merge(matches, on='ID', how='inner').copy()
ball_withmatch['BowlingTeam'] = ball_withmatch.Team1 + ball_withmatch.Team2
ball_withmatch['BowlingTeam'] = ball_withmatch[['BowlingTeam', 'BattingTeam']].apply(lambda x: x.values[0].replace(x.values[1], ''), axis=1)
batter_data = ball_withmatch[np.append(balls.columns.values, ['BowlingTeam', 'Player_of_Match'])]

def teamsAPI():
  teams=list(set(list(matches['Team1'])+list(matches['Team2'])))
  teams_dict={
    'teams':teams
  }
  return teams_dict

def team_vs_team(team1,team2):
  valid_teams=list(set(list(matches['Team1'])+list(matches['Team2'])))
  
  if team1 in valid_teams and team2 in valid_teams:
    temp_df=matches[(matches['Team1']==team1) & (matches['Team2']==team2) | (matches['Team1']==team2) & (matches['Team2']==team1)]
    total_matches=temp_df.shape[0]

    matches_won_team1=temp_df['WinningTeam'].value_counts()[team1]
    matches_won_team2=temp_df['WinningTeam'].value_counts()[team2]
    draws=total_matches-(matches_won_team1+matches_won_team2)

    response={
        'total_matches':str(total_matches),
        team1:str(matches_won_team1),
        team2:str(matches_won_team2),
        'draws':str(draws)
      }
    return response
  else:
    return {'message':'Invalid team name'}
  

def players():
  Team1Players=list(set([j for i in matches['Team1Players'] for j in list(i[1:-1].split(','))]))
  Team2Players=list(set([j for i in matches['Team2Players'] for j in list(i[1:-1].split(','))]))
  players=Team1Players+Team2Players
  players=list(set(map(lambda player:player.split("'")[1],players)))
  players_dict={
    'players':sorted(players),
    'total':len(players)
  }
  return players_dict

def teamRecord(team):
    df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)].copy()
    mp = df.shape[0]
    won = df[df.WinningTeam == team].shape[0]
    nr = df[df.WinningTeam.isnull()].shape[0]
    loss = mp - won - nr
    nt = df[(df.MatchNumber == 'Final') & (df.WinningTeam == team)].shape[0]
    return {'matchesplayed': mp,
            'won': won,
            'loss': loss,
            'noResult': nr,
            'title': nt}
