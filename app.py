from flask import Flask, render_template, jsonify,request,url_for,redirect
from database import engine
import json
from database import load_clubs_from_db,load_club_from_db
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

if not os.path.exists("polls.csv"):
    structure = {
        "p_id" : [],
        "poll_question" : [],
        "option1": [],
        "option2": [],
        "option3": [],
        "option4": [],
        "option5": [],
        "votes1": [],
        "votes2": [],
        "votes3": [],
        "votes4": [],
        "votes5": []
    }
    
    #converting the dictionary into a pandas dataframe, if the df does not already exists
    pd.DataFrame(structure).set_index("p_id").to_csv("polls.csv")
    
#if the df already exists in the os then we just have to read it 
polls_df = pd.read_csv("polls.csv").set_index("p_id")

@app.route('/home_polls')
def home_polls(): # the index page for polling web app
    return render_template('home_polls.html',polls=polls_df)

@app.route('/polls/<p_id>')
def polls(p_id):
    poll_details = polls_df.loc[int(p_id)]
    return render_template('show_poll.html',poll=poll_details)

@app.route('/vote/<p_id>/<option>')
def vote(p_id,option):
    polls_df.at[int(p_id),'votes'+str(option)] += 1
    polls_df.to_csv("polls.csv")
    poll_details = polls_df.loc[int(p_id)]
    return render_template('show_poll.html',poll=poll_details)
        
@app.route('/interact')
def interact():
    data = request.form
    return render_template('interact.html')

#making a similar csv file to save the users that have visited the site
# if not os.path.exists("users.csv"):
#     users_structure = {
        
#     }

@app.route('/interact/entry',methods=['post'])
def interact_to_club():
    data = request.form
    return render_template('interaction_result.html',user_entry=data)

if __name__ == "__main__":
    app.run(debug=True)
