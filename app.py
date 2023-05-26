from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
from sqlalchemy import text
from database import engine
import json
from database import load_clubs_from_db


app = Flask(__name__)

# with open('club-details.json','r') as file:
#     club_data = json.load(file)
# club_details = club_data['club-details']

# CLUBS = club_details
# [
#     {
#         'id': 1,
#         'logo' : 'mancity.png',
#         'country' : 'England',
#         'club-name': 'Manchester City FC',
#         'stadium': 'Etihad Stadium,Manchester,England',
#         'net-worth': '4.25 Billion'
#     },
#     {
#         "id": 2,
#         'logo' : 'realmadrid.png',
#         'country': 'Spain',
#         "club-name": "Real Madrid CF",
#         "stadium": "Santiago Bernabeu Stadium, Madrid, Spain",
#         "net-worth": "4.24 Billion"
#     },
#     {
#         "id": 3,
#         'logo' : 'barcelonafc.png',
#         'country': 'Spain',
#         "club-name": "FC Barcelona",
#         "stadium": "Camp Nou, Barcelona, Spain",
#         "net-worth": "4.02 Billion"
#     },
#     {
#         "id": 4,
#         'logo' : 'manunited.png',
#         'country' : 'England',
#         "club-name": "Manchester United FC",
#         "stadium": "Old Trafford, Manchester, England",
#         "net-worth": "3.81 Billion"
#     },
#     {
#         "id": 5,
#         'logo' : 'liverpool.png',
#         'country' : 'England',
#         "club-name": "Liverpool FC",
#         "stadium": "Anfield, Liverpool, England",
#         "net-worth": "3.30 Billion"
#     },
#     {
#         'id': 6,
#         'logo' : 'juventus.png',
#         'country' : 'Italy',
#         'club-name': 'Juventus FC',
#         'stadium': 'Allianz Stadium, Turin, Italy',
#         'net-worth': '1.95 Billion'
#     },
#     {
#         'id': 7,
#         'logo' : 'psg.png',
#         'country' : 'France',
#         'club-name': 'Paris Saint-Germain FC',
#         'stadium': 'Parc des Princes, Paris, France',
#         'net-worth': '1.91 Billion'
#     },
#     {
#         'id': 8,
#         'logo' : 'bayern.png',
#         'country' : 'Germany',
#         'club-name': 'FC Bayern Munich',
#         'stadium': 'Allianz Arena, Munich, Germany',
#         'net-worth': '1.87 Billion'
#     },
#     {
#         'id': 9,
#         'logo' : 'chelsea.png',
#         'country' : 'England',
#         'club-name': 'Chelsea FC',
#         'stadium': 'Stamford Bridge, London, England',
#         'net-worth': '1.85 Billion'
#     },
#     {
#         'id': 10,
#         'logo' : 'arsenal.png',
#         'country' : 'England',
#         'club-name': 'Arsenal FC',
#         'stadium': 'Emirates Stadium, London, England',
#         'net-worth': '1.75 Billion'
#     },
#     {
#         'id': 11,
#         'logo' : 'tottenham.png',        
#         'country' : 'England',
#         'club-name': 'Tottenham Hotspur FC',
#         'stadium': 'Tottenham Hotspur Stadium, London, England',
#         'net-worth': '1.60 Billion'
#     }

# ]
    
    # result_list = result.all()
    # # print(type(result_list[0]))
    # # print(result_list[0])
    # result_dict = result_list[0]._asdict()
    # print(type(result_dict))

@app.route('/')
def hello():
    CLUBS = load_clubs_from_db()
    return render_template('home.html',clubs=CLUBS)

@app.route('/api/clubs')
def list_clubs():
    return jsonify(load_clubs_from_db())


if __name__ == "__main__":
    app.run(debug=True)
