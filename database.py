from sqlalchemy import create_engine
from sqlalchemy import text
import pymysql
from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb
import pymysql.cursors
import os

db_connection_string = os.environ.get('FC_DETAILS')

# db_connection_string = "mysql+pymysql://sji3rdx843ns67x8yzkp:pscale_pw_34O8ntSvuQITT6jNnxlQ9ft4y7Uw3JJcVAIRuxvo4PV@aws.connect.psdb.cloud/football_clubz?charset=utf8mb4"

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
        result = conn.execute(text("select * from club"))
    
    club_details = []
    for row in result.all():
        club_details.append(row._asdict())
    return club_details

