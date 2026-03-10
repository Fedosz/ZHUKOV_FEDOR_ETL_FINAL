Pipeline

generate\_data

↓

mongo\_to\_postgres

↓

build\_marts

MongoDB



Коллекции:



user\_sessions

event\_logs

support\_tickets

user\_recommendations

moderation\_queue



Данные генерируются скриптом generate\_data.py.



PostgreSQL

staging

staging.user\_sessions

staging.event\_logs

staging.support\_tickets

staging.user\_recommendations

staging.moderation\_queue

mart

mart.user\_activity

mart.support\_stats

