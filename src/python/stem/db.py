from sqlalchemy.sql import text
from sqlalchemy import create_engine


connect_string = 'mysql+pymysql://scout:stem2018@localhost/stem'
engine = create_engine(connect_string)

add_requirement_query = text(
    "INSERT INTO requirements (merit_badge, req_id, req_desc) "
    "VALUES (:merit_badge, :req_id, :req_desc);"
)

get_requirement_query = text(
    "SELECT * FROM requirements "
    "WHERE merit_badge = :merit_badge;"
)

set_completion_query = text(
    "INSERT INTO completion (scout_name, merit_badge, req_id, complete) "
    "VALUES (:scout_name, :merit_badge, :req_id, :complete) "
    "ON DUPLICATE KEY UPDATE;"
)

get_completions_query = text(
    "SELECT * FROM completion "
    "WHERE merit_badge = :merit_badge "
    " AND scout_name = :scout_name;"
)

def add_requirement(merit_badge, req_id, requirement):
    try:
        conn = engine.connect()
        conn.execute(add_requirement_query, merit_badge=merit_badge, req_id=req_id, req_desc=requirement)
    finally:
        conn.close()
        
def get_requirements(merit_badge):
    """Retrieve all requirements for ``merit_badge``."""
    try:
        conn = engine.connect()
        rs = conn.execute(get_requirement_query, merit_badge=merit_badge).fetchall()
        return [dict(r) for r in rs]
    finally:
        conn.close()

def get_completions(merit_badge, scout_name):
    """Retrieve all completed requirements for ``scout_name`` on ``merit_badge``."""
    try:
        conn = engine.connect()
        rs = conn.execute(get_completions_query, merit_badge=merit_badge, scout_name=scout_name).fetchall()
        return [dict(r) for r in rs]
    finally:
        conn.close()
    
def update_completion(merit_badge, scout_name, req_id, complete):
    """Set req_id to complete for scout_name on merit_badge."""
    try:
        conn = engine.connect()
        rs = conn.execute(set_completion_query,
                          merit_badge=merit_badge,
                          scout_name=scout_name,
                          req_id=req_id,
                          complete=complete)
    finally:
        conn.close()