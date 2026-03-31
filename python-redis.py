
import redis

r = redis.Redis(host='localhost', port=6379, db=0)


# exemplo hash
def hash_example():
    r.hset('user:1000', 'name', 'John Doe')
    r.hset('user:1000', 'email', 'john.doe@example.com')
    r.hset('user:1000', 'age', 30)
    
    
# recuperando dados do hash
user = r.hgetall('user:1000')
print(f"Hash User: {user}")

# Atualizando um campo no hash
r.hset('user:1000', 'age', 40)

# Recuperando um campo específico do hash
age = r.hget('user:1000', 'age')
print(f"Age: {age}")

# Exemplo de List
def list_example():
    r.rpush('tasks', 'task1')
    r.rpush('tasks', 'task2')
    r.rpush('tasks', 'task3')
    
# Recuperando dados da lista
tasks = r.lrange('tasks', 0, -1)
print(f"exemplo da lista - Tasks: {tasks}")

# Removendo e retornando o primeiro item da lista
tasks = r.lpop('tasks')
print(f"exemplo da lista - Removed Task: {tasks}")

# Recuperando o tamanho da lista
size = r.llen('tasks')
print(f"list Size: {size}")

# Exemplo Set
def set_example():
    r.sadd('tags', 'java')
    r.sadd('tags', 'c#')
    r.sadd('tags', 'ts')
    
# Recupenrando dados do set
tags = r.smembers('tags')
print(f"Set tags: {tags}")

# Verificando a existência de um membro no set
is_member = r.sismember('tags', 'java')
print(f"Is 'java' a member for tags? {is_member}")

# Removendo um membro do set
r.srem('tags', 'database')

# Exemplo de Ordered Set
def sorted_set_exemple():
    # Adicionando dados aos sorted Set
    r.zadd('leaderboard', {'Alice': 100, 'Bob': 200, 'Charlie': 150})
    
# Recuperando todos os membros do sorted set com suas pontuações
leaderboard = r.zrange('leaderboard', 0, -1, withscores=True)
print(f"Sorted set example - Leaderboard: {leaderboard}")

# Atualizando a pontuação de um membro
r.zincrby('leaderboard', 50, 'Alice')

# Reperando a pontuação de um membro especifico
score = r.zscore('leaderboard', 'Alice')
print(f"Alice Updated score: {score}")

# Recuperando os membros com pontuação entre um intervalo especifico

top_players = r.zrangebyscore('leaderboard', 100, 200, withscores=True)
print(f"Top Players: {top_players}")

#Executando os exemplos
hash_example()
list_example()
set_example()
sorted_set_exemple()