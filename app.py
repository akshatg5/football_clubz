from flask import Flask, render_template, jsonify
from database import engine
import json
from database import load_clubs_from_db


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


if __name__ == "__main__":
    app.run(debug=True)
