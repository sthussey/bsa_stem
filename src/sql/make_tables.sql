DROP TABLE requirements;

CREATE TABLE requirements (
    merit_badge VARCHAR(32),
    req_id VARCHAR(8),
    req_desc VARCHAR(2048),
    PRIMARY KEY (merit_badge, req_id)
);

DROP TABLE completions;

CREATE TABLE completions (
    scout_name VARCHAR(32),
    merit_badge VARCHAR(32),
    req_id VARCHAR(8),
    complete BOOLEAN,
    PRIMARY KEY (scout_name, merit_badge, req_id)
)