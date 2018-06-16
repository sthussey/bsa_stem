from sqlalchemy.sql import text

connect_string = 'mysql+pymysql://scout:stem2018@localhost/stem'

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

