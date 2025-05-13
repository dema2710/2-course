"""Basic connection example.
"""

import redis
import datetime
r = redis.Redis(
    host='redis-10996.crce175.eu-north-1-1.ec2.redns.redis-cloud.com',
    port=10996,
    decode_responses=True,
    username="default",
    password="sdBCvCGymgyODhJKBrjvyfgaOjtqNTB9",
)


# r.set('myKey','secret data')
# r.set('myKeyTTL23', 'secter dataTTL32', ex=15)
# r.set('myKeyTTL23666666666666', 'secter dataTTL32', exat=datetime.datetime(year=2025,month=5,day=15,hour=3))

# r.lpush('myList', 'elem1left0')
# r.rpush('myList', 'elem right', 565)
# r.expire('myList', 3500)
# data = r.lrange('myList', 0, 1)
# print(data)

# data = r.get('myKey')
# print(data)

# r.delete('myList')

# r.hset('user:12345654', mapping={'name': 'Alise', 'age':56})
# r.hset('user:12345654', mapping={'city':'Odesa'})
# r.hset('user:12345654', mapping={'age':15})
# r.expire('user:12345654', 3500)

# data = r.hgetall('user:12345654')
# print(data)

# r.incr('views', 6)
# print(r.get('views'))
r.publish('weather', 'from pycharm')
pubsub = r.pubsub()
pubsub.subscribe('news')
pubsub.subscribe('weather')
for message in pubsub.listen():
    print(message)