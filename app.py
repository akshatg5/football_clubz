from flask import Flask, render_template, jsonify,request
from database import engine
import json
from database import load_clubs_from_db,load_club_from_db,add_interaction_to_db


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

@app.route('/interact')
def interact():
    data = request.form
    add_interaction_to_db(data)
    return render_template('interact.html')

@app.route('/interact/entry',methods=['post'])
def interact_to_club():
    data = request.form
    add_interaction_to_db(data)
    return render_template('interaction_result.html',user_entry=data)

if __name__ == "__main__":
    app.run(debug=True)
