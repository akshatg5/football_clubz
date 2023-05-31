from sqlalchemy import create_engine
from sqlalchemy import text
import pymysql
import os
import pymysql.cursors
import os

db_connection_string = os.environ.get('FC_DETAILS')

# SSL configuration options
ssl_args = {
    'ssl': {
        'ssl_ca': '/path/to/ca.crt',
        'ssl_cert': '/path/to/client.crt',
        'ssl_key': '/path/to/client.key'
    }
}

engine = create_engine(db_connection_string,connect_args=ssl_args)

def load_clubs_from_db():
    with engine.connect() as conn :
        result = conn.execute(text("select * from clubs"))
    
    club_details = []
    for row in result.all():
        club_details.append(row._asdict())
    return club_details

def load_club_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text(f"select * from clubs WHERE id = {id}")
        )
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()
        
def add_interaction_to_db(interaction):
    with engine.connect() as conn:
        query = text("INSERT INTO interactions (full_name, age, email, phone, favclub, goat, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
        
        try:
            conn.execute(query,
                         interaction['full_name'],
                         interaction['age'],
                         interaction['email'],
                         interaction['phone'],
                         interaction['favclub'],
                         interaction['goat'],
                         interaction['created_at'],
                         interaction['updated_at']
                         )
            conn.commit()
        except KeyError as e:
            print(f"Error: Missing key '{e.args[0]}' in the 'interaction' dictionary.")


        
    

