#!/usr/bin/env python3

import redis

r = redis.Redis( host='redis-0.redis',
                 port=6379)
r.set('count', 0)
print("Content-type: text/html")
print("")
print("<html><body>")
print("<p>Reset counter!<br /></p>")
print("</body></html>")
