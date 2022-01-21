-- SQLite
CREATE TABLE TrackingTime (
id INTEGER PRIMARY KEY AUTOINCREMENT,
start_time datetime,
end_time datetime,
working_time float,
project text
);

-- INSERT Data

INSERT INTO TrackingTime (start_time, project)
VALUES (datetime('now'), "what");

-- Delete Data

Delete from TrackingTime where id = 2;

-- get all projects

SELECT project from TrackingTime GROUP By project;

-- SELECT ALL RECORDS

SELECT * FROM TrackingTime Order by id DESC LIMIT 1;

-- UPDATE Record

UPDATE TrackingTime SET end_time = null WHERE id = 5;

-- DROP ALL Records

DELETE FROM TrackingTime where id > -1;

-- RESET id sequence
UPDATE sqlite_sequence SET seq = 1;