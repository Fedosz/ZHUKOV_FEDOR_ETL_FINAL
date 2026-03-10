CREATE TABLE IF NOT EXISTS staging.user_sessions(
id SERIAL PRIMARY KEY,
session_id TEXT,
user_id TEXT,
start_time TIMESTAMP,
end_time TIMESTAMP
);

CREATE TABLE IF NOT EXISTS staging.event_logs(
id SERIAL PRIMARY KEY,
event_id TEXT,
user_id TEXT,
event_type TEXT,
event_time TIMESTAMP
);

CREATE TABLE IF NOT EXISTS staging.support_tickets(
id SERIAL PRIMARY KEY,
ticket_id TEXT,
user_id TEXT,
issue_type TEXT,
status TEXT,
created_at TIMESTAMP,
updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS staging.user_recommendations(
id SERIAL PRIMARY KEY,
user_id TEXT,
generated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS staging.moderation_queue(
id SERIAL PRIMARY KEY,
review_id TEXT,
product_id TEXT,
user_id TEXT,
text TEXT
);

CREATE TABLE IF NOT EXISTS mart.user_activity(
user_id TEXT,
sessions_count INT,
events_count INT
);

CREATE TABLE IF NOT EXISTS mart.support_stats(
issue_type TEXT,
tickets_count INT
);
