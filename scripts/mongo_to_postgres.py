from pymongo import MongoClient
import psycopg2

mongo = MongoClient(
    "mongodb://mongo_admin:mongo_password@mongo:27017/etl_project?authSource=admin"
)
mdb = mongo["etl_project"]

pg = psycopg2.connect(
    host="postgres",
    port=5432,
    database="etl_warehouse",
    user="etl_user",
    password="etl_password"
)

cur = pg.cursor()

for d in mdb.user_sessions.find():
    cur.execute(
        "insert into staging.user_sessions(session_id,user_id,start_time,end_time) values(%s,%s,%s,%s)",
        (d.get("session_id"),d.get("user_id"),d.get("start_time"),d.get("end_time"))
    )

for d in mdb.event_logs.find():
    cur.execute(
        "insert into staging.event_logs(event_id,user_id,event_type,event_time) values(%s,%s,%s,%s)",
        (d.get("event_id"),d.get("user_id"),d.get("event_type"),d.get("timestamp"))
    )

for d in mdb.support_tickets.find():
    cur.execute(
        "insert into staging.support_tickets(ticket_id,user_id,issue_type,status,created_at,updated_at) values(%s,%s,%s,%s,%s,%s)",
        (
            d.get("ticket_id"),
            d.get("user_id"),
            d.get("issue_type"),
            d.get("status"),
            d.get("created_at"),
            d.get("updated_at")
        )
    )

for d in mdb.user_recommendations.find():
    cur.execute(
        "insert into staging.user_recommendations(user_id,generated_at) values(%s,%s)",
        (d.get("user_id"),d.get("generated_at"))
    )

for d in mdb.moderation_queue.find():
    cur.execute(
        "insert into staging.moderation_queue(review_id,product_id,user_id,text) values(%s,%s,%s,%s)",
        (d.get("review_id"),d.get("product_id"),d.get("user_id"),d.get("text"))
    )

pg.commit()
