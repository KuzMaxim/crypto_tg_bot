import redis

# Настройка Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Пример добавления пользователя
def add_user(username: str, email: str):
    r.set(username, email)
    print(f'User {username} added with email: {email}')

# Пример извлечения пользователя
def get_user(username: str):
    email = r.get(username)
    if email:
        return f'User {username} found with email: {email.decode()}'
    return f'User {username} not found'

# Пример использования
add_user('john_doe', 'john@example.com')
print(get_user('john_doe'))
