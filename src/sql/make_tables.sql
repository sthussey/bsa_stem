CREATE TABLE requirements (
    merit_badge VARCHAR(32),
    req_id VARCHAR(8),
    req_desc VARCHAR(2048)
);

CREATE TABLE completion (
    scout_name VARCHAR(32),
    merit_badge VARCHAR(32),
    req_id VARCHAR(8),
    complete BOOLEAN,
    PRIMARY KEY (scout_name, merit_badge, req_id)
)