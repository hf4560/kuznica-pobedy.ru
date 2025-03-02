import redis

# Подключаемся к Redis (предположим, что Redis работает локально на порту 6379)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Проверяем подключение
try:
    redis_client.ping()
    print("Redis server is connected!")
except redis.ConnectionError:
    print("Could not connect to Redis server!")
