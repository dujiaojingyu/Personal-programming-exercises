__author__ = "Narwhale"

import redis

r = redis.Redis(host='192.168.123.96', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))