import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    decode_responses=True
)

# Cria o objeto pubsub
pubsub = r.pubsub()

# Usa o .subscribe() p/ fazer a subscription no tópico e escutar por mensagem
pubsub.subscribe('data_channel')

# .listen() retorna um generator que pode ser iterado p/ escutar mensagens do publisher
try:
    for message in pubsub.listen():
        print(message)  # <- Você pode aplicar qualquer tratamento de dados aqui (e não apenas imprimir)
except KeyboardInterrupt:
    print("\nInterrupted by user — unsubscribing and closing pubsub...")
    try:
        pubsub.unsubscribe()
    except Exception:
        pass
finally:
    pubsub.close()