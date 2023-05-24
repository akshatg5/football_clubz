from flask import Flask, render_template, jsonify

app = Flask(__name__)

CLUBS = [
    {
        'id': 1,
        'logo' : 'mancity.png',
        'country' : 'England',
        'club-name': 'Manchester City FC',
        'stadium': 'Etihad Stadium,Manchester,England',
        'net-worth': '4.25 Billion'
    },
    {
        "id": 2,
        'logo' : 'realmadrid.png',
        'country': 'Spain',
        "club-name": "Real Madrid CF",
        "stadium": "Santiago Bernabeu Stadium, Madrid, Spain",
        "net-worth": "4.24 Billion"
    },
    {
        "id": 3,
        'logo' : 'barcelonafc.png',
        'country': 'Spain',
        "club-name": "FC Barcelona",
        "stadium": "Camp Nou, Barcelona, Spain",
        "net-worth": "4.02 Billion"
    },
    {
        "id": 4,
        'logo' : 'manunited.png',
        'country' : 'England',
        "club-name": "Manchester United FC",
        "stadium": "Old Trafford, Manchester, England",
        "net-worth": "3.81 Billion"
    },
    {
        "id": 5,
        'logo' : 'liverpool.png',
        'country' : 'England',
        "club-name": "Liverpool FC",
        "stadium": "Anfield, Liverpool, England",
        "net-worth": "3.30 Billion"
    },
    {
        'id': 6,
        'logo' : 'juventus.png',
        'country' : 'Italy',
        'club-name': 'Juventus FC',
        'stadium': 'Allianz Stadium, Turin, Italy',
        'net-worth': '1.95 Billion'
    },
    {
        'id': 7,
        'logo' : 'psg.png',
        'country' : 'France',
        'club-name': 'Paris Saint-Germain FC',
        'stadium': 'Parc des Princes, Paris, France',
        'net-worth': '1.91 Billion'
    },
    {
        'id': 8,
        'logo' : 'bayern.png',
        'country' : 'Germany',
        'club-name': 'FC Bayern Munich',
        'stadium': 'Allianz Arena, Munich, Germany',
        'net-worth': '1.87 Billion'
    },
    {
        'id': 9,
        'logo' : 'chelsea.png',
        'country' : 'England',
        'club-name': 'Chelsea FC',
        'stadium': 'Stamford Bridge, London, England',
        'net-worth': '1.85 Billion'
    },
    {
        'id': 10,
        'logo' : 'arsenal.png',
        'country' : 'England',
        'club-name': 'Arsenal FC',
        'stadium': 'Emirates Stadium, London, England',
        'net-worth': '1.75 Billion'
    },
    {
        'id': 11,
        'logo' : 'tottenham.png',        
        'country' : 'England',
        'club-name': 'Tottenham Hotspur FC',
        'stadium': 'Tottenham Hotspur Stadium, London, England',
        'net-worth': '1.60 Billion'
    }

]


@app.route('/')
def hello():
    return render_template('home.html',clubs=CLUBS)

@app.route('/api/clubs')
def list_clubs():
    return jsonify(CLUBS)


if __name__ == "__main__":
    app.run(debug=True)