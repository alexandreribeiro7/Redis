import redis

# Inicia a instancia
r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    decode_responses=True # <- garante que os dados binarios vão ser decoded
)

while True:
    message = input("REALTIME PUSH NOTIFICATION - Digite a Mensagem: ")
    r.publish("data_channel", message)