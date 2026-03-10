import random
import uuid
from datetime import datetime, timedelta
from pymongo import MongoClient

client = MongoClient(
    "mongodb://mongo_admin:mongo_password@mongo:27017/etl_project?authSource=admin"
)
db = client["etl_project"]

users=[]
for i in range(200):
    users.append(str(uuid.uuid4()))

products=[]
for i in range(100):
    products.append(str(uuid.uuid4()))

pages=["/home","/catalog","/product","/cart","/checkout"]
actions=["view","click","add_to_cart","purchase"]
issues=["payment","delivery","product_quality","other"]
statuses=["open","in_progress","resolved"]
flags=["spam","offensive","fake"]

def rand_date():
    return datetime.now()-timedelta(days=random.randint(0,30))

for i in range(1000):
    start=rand_date()
    end=start+timedelta(minutes=random.randint(1,60))

    db.user_sessions.insert_one({
        "session_id":str(uuid.uuid4()),
        "user_id":random.choice(users),
        "start_time":start,
        "end_time":end,
        "pages_visited":random.sample(pages,random.randint(1,5)),
        "actions":random.sample(actions,random.randint(1,4))
    })

for i in range(2000):
    db.event_logs.insert_one({
        "event_id":str(uuid.uuid4()),
        "user_id":random.choice(users),
        "event_type":random.choice(actions),
        "timestamp":rand_date()
    })

for i in range(300):
    created=rand_date()

    db.support_tickets.insert_one({
        "ticket_id":str(uuid.uuid4()),
        "user_id":random.choice(users),
        "issue_type":random.choice(issues),
        "status":random.choice(statuses),
        "created_at":created,
        "updated_at":created+timedelta(hours=random.randint(1,48)),
        "messages":[
            {"sender":"user","text":"help","time":created},
            {"sender":"support","text":"ok","time":created+timedelta(hours=1)}
        ]
    })

for i in range(300):
    db.user_recommendations.insert_one({
        "user_id":random.choice(users),
        "generated_at":rand_date(),
        "recommended_products":random.sample(products,random.randint(3,7))
    })

for i in range(200):
    db.moderation_queue.insert_one({
        "review_id":str(uuid.uuid4()),
        "product_id":random.choice(products),
        "user_id":random.choice(users),
        "text":"review text",
        "flags":[random.choice(flags)]
    })

print("done")