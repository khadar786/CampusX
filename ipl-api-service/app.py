from flask import Flask,request,redirect,session,jsonify
import ipl
app=Flask(__name__)
app.secret_key='IPLAPISERVICE#2024'


#http://127.0.0.1:5000/api/teams
#http://127.0.0.1:5000/api/teamvteam?team1=Rajasthan Royals&team2=Royal Challengers Bangalore
#http://127.0.0.1:5000/api/teamvteam?team1=Mumbai%20Indians&team2=Royal%20Challengers%20Bangalore
#https://github.com/campusx-official/ipl-api-service/blob/master/ipl.py

#teamrecord
#http://127.0.0.1:5000/api/team-record?team=Gujarat%20Titans
#players
@app.route('/')
def index():
  return 'Hi'

@app.route('/api/teams')
def teams():
  teams=ipl.teamsAPI()
  return jsonify(teams)

@app.route('/api/players')
def players():
  response=ipl.players()
  return jsonify(response)
  
@app.route('/api/teamvteam')
def teamvteam():
  team1=request.args.get('team1')
  team2=request.args.get('team2')
  response=ipl.team_vs_team(team1,team2)
  return jsonify(response)

@app.route('/api/team-record')
def teamrecord():
  team=request.args.get('team')
  response=ipl.teamRecord(team)
  return jsonify(response)

@app.route('/api/batting-record')
def batting_record():
  pass

@app.route('/api/bowling-record')
def bowling_record():
  pass

if __name__=='__main__':
  app.run(debug=True)