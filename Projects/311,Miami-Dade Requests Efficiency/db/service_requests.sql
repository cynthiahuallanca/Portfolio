DROP DATABASE IF EXISTS services_311_db;
CREATE DATABASE services_311_db;

USE services_311_db;

DROP TABLE IF EXISTS requests_311;
CREATE TABLE requests_311 (
  id INT AUTO_INCREMENT NOT NULL,
  issue_type TEXT,
  case_owner TEXT,
  case_owner_description TEXT,
  street_address TEXT,
  city TEXT,
  state TEXT,
  zip_code DOUBLE,
  neighborhood_district TEXT,
  ticket_created_date_time TEXT,
  ticket__last_update_date_time TEXT,
  ticket_closed_date_time TEXT,
  ticket_status TEXT,
  location_city TEXT,
  latitude DOUBLE,
  longitude DOUBLE,
  method_received TEXT,
  goal_days INT,
  actual_completed_days DOUBLE,
  primary key(id)
);

SELECT * FROM requests_311;