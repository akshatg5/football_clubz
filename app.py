from flask import Flask, render_template, jsonify,request,url_for,redirect,make_response
from database import engine
import json
import requests
from database import load_clubs_from_db,load_club_from_db,add_interaction_to_db
import pandas as pd
import os.path


app = Flask(__name__)

# with open('club-details.json','r') as file:
#     club_data = json.load(file)
# club_details = club_data['club-details']
    
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

@app.route('/club/<id>')
def show_club(id):
    CLUB = load_club_from_db(id)
    if not CLUB:
        return render_template('notfound.html',club=CLUB),404
    else:
        return render_template('club-page.html',club=CLUB)

@app.route("/clubs")
def clubs_list():
    CLUBS = load_clubs_from_db()
    return render_template('club-list.html',clubs=CLUBS)

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

@app.route('/contactus')
def contact_us():
    return render_template('contactus.html')

# if not os.path.exists("polls.csv"):
#     structure = {
#         "p_id" : [],
#         "poll_question" : [],
#         "option1": [],
#         "option2": [],
#         "option3": [],
#         "option4": [],
#         "option5": [],
#         "votes1": [],
#         "votes2": [],
#         "votes3": [],
#         "votes4": [],
#         "votes5": []
#     }
    
#     #converting the dictionary into a pandas dataframe, if the df does not already exists
#     pd.DataFrame(structure).set_index("p_id").to_csv("polls.csv")
    
# #if the df already exists in the os then we just have to read it 
# polls_df = pd.read_csv("polls.csv").set_index("p_id")

# @app.route('/home_polls')
# def home_polls(): # the index page for polling web app
#     return render_template('home_polls.html',polls=polls_df)

# @app.route('/polls/<p_id>')
# def polls(p_id):
#     poll_details = polls_df.loc[int(p_id)]
#     return render_template('show_poll.html',poll=poll_details)

# @app.route('/vote/<p_id>/<option>')
# def vote(p_id,option):
#     if request.cookies.get(f"votes_{p_id}_cookie") is None:
#         polls_df.at[int(p_id),'votes'+str(option)] += 1
#         polls_df.to_csv("polls.csv")
#         response = make_response(redirect(url_for('polls',p_id=p_id)))
#         response.set_cookie(f"votes_{p_id}_cookie",str(option))
#         return response
#     else:
#         return "Cannot vote more than once!!"
        
@app.route('/interact',methods =['GET'])
def interact():
    data = request.form
    football_managers = [
    "Sir Alex Ferguson", 
    "Jose Mourinho", 
    "Pep Guardiola", 
    "Carlo Ancelotti", 
    "Johan Cruyff",
    "Zinedine Zidane",
    "Arsène Wenger",
    "Bob Paisley",
    "Bill Shankly",
    "Matt Busby",
    "Ernst Happel",
    "Arrigo Sacchi",
    "Rinus Michels",
    "Udo Lattek",
    "Helenio Herrera",
    "Marcello Lippi",
    "Vicente del Bosque",
    "Louis van Gaal",
    "Otto Rehhagel",
    "Brian Clough",
    "Lionel Scaloni"
]
    
    best_players = [
    "Pelé",
    "Diego Maradona",
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Johan Cruyff",
    "Franz Beckenbauer",
    "Michel Platini",
    "Alfredo Di Stefano",
    "Ferenc Puskás",
    "Zinedine Zidane",
    "Ronaldinho",
    "Ronaldo Nazário",
    "George Best",
    "Marco van Basten",
    "Lev Yashin",
    "Eusébio",
    "Bobby Charlton",
    "Garrincha",
    "Zico",
    "Roberto Baggio"
]

    best_cfs= [
    "Robert Lewandowski",
    "Harry Kane",
    "Erling Haaland",
    "Karim Benzema",
    "Romelu Lukaku",
    "Kylian Mbappé",
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Sergio Agüero",
    "Luis Suárez",
    "Pelé",
    "Diego Maradona",
    "Ronaldo Nazário",
    "Ferenc Puskás",
    "Gerd Müller",
    "Marco van Basten",
    "Thierry Henry",
    "Gabriel Batistuta",
    "Eusébio",
    "Romário"
]

    best_ms= [
    "Jude Bellingham",
    "Kevin De Bruyne",
    "Luka Modrić",
    "N'Golo Kanté",
    "Toni Kroos",
    "Paul Pogba",
    "Andrés Iniesta",
    "Sergio Busquets",
    "Frenkie de Jong",
    "Bruno Fernandes",
    "Joshua Kimmich",
    "Pelé",
    "Diego Maradona",
    "Zinedine Zidane",
    "Johan Cruyff",
    "Michel Platini",
    "Xavi Hernández",
    "Andrés Iniesta",
    "Franz Beckenbauer",
    "Lothar Matthäus",
    "Alfredo Di Stefano"
]
    best_cbs = [
    "Virgil van Dijk",
    "Sergio Ramos",
    "Kalidou Koulibaly",
    "Raphael Varane",
    "Aymeric Laporte",
    "Giorgio Chiellini",
    "Matthijs de Ligt",
    "Milan Škriniar",
    "Harry Maguire",
    "Joel Matip",
    "Franco Baresi",
    "Franz Beckenbauer",
    "Fabio Cannavaro",
    "Bobby Moore",
    "Alessandro Nesta",
    "Carles Puyol",
    "Paolo Maldini",
    "Ronald Koeman",
    "Marcel Desailly",
    "Franco Baresi"
]
    
    best_gks = [
    "Manuel Neuer",
    "Alisson Becker",
    "Jan Oblak",
    "Ederson",
    "Marc-André ter Stegen",
    "Thibaut Courtois",
    "Keylor Navas",
    "Hugo Lloris",
    "David de Gea",
    "Gianluigi Donnarumma",
    "Lev Yashin",
    "Dino Zoff",
    "Gordon Banks",
    "Peter Schmeichel",
    "Oliver Kahn",
    "Iker Casillas",
    "Gianluigi Buffon",
    "Sepp Maier",
    "Ricardo Zamora",
    "Neville Southall"
]


    return render_template('interact.html',
                           football_managers=football_managers, 
                           best_players = best_players,
                           best_cfs = best_cfs,
                           best_ms = best_ms,
                           best_cbs = best_cbs,
                           best_gks = best_gks)

#making a similar csv file to save the users that have visited the site
# if not os.path.exists("users.csv"):
#     users_structure = {
        
#     }

@app.route('/interact/entry',methods=['post'])
def interact_to_club():
    data = request.form
    add_interaction_to_db(data)
    return render_template('interaction_result.html',user_entry=data)


if __name__ == "__main__":
    app.run(debug=True)
