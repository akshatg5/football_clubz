from sqlalchemy import create_engine
from sqlalchemy import text
import pymysql
import os
import pymysql.cursors
import os
import pandas as pd

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
        
def add_interaction_to_db(user_entry):
    with engine.connect() as conn:
        query = text(f"INSERT INTO interactions(full_name,age,club_name,best_manager, best_player, best_cf, best_m,best_cb, best_gk) VALUES (:full_name,:age,:club_name,:best_manager,:best_player,:best_cf,:best_m,:best_cb,:best_gk)")
        
        conn.execute(query,{
            'full_name' : user_entry['full_name'],
            'age' : user_entry['age'],
            'club_name' : user_entry['club_name'],
            'best_manager' : user_entry['best_manager'],
            'best_player' : user_entry['best_player'],
            'best_cf' : user_entry['best_cf'],
            'best_m' : user_entry['best_m'],
            'best_cb': user_entry['best_cb'],
            'best_gk': user_entry['best_gk']
        })
        
def load_all_from_interactions():
    query = "select * from interactions"
    df = pd.read_sql(query,con=engine)
    return df
    # with engine.connect() as conn:        
    #     stats = conn.execute(text("select * from interactions"))
        
    # df = pd.DataFrame(stats.fetchall(),columns=stats.keys())
    # return df

# def load_clubs_from_db():
#     with engine.connect() as conn :
#         result = conn.execute(text("select * from clubs"))
    
#     club_details = []
#     for row in result.all():
#         club_details.append(row._asdict())
#     return club_details


        
    

