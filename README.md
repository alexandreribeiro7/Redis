# Redis - Estudos, Segurança e Observabilidade

## Objetivo

Este projeto foi criado para consolidar conhecimentos práticos sobre Redis, explorando desde operações básicas até recursos avançados de segurança, replicação, monitoramento e análise de desempenho em tempo real.

---

## Tecnologias Utilizadas

- Redis 8.x
- Redis Insight
- Redis Cloud
- Grafana
- Docker
- Docker Network
- Redis CLI

---

## Conteúdos Abordados

### Manipulação de Dados

- Strings
- Lists
- Sets
- Sorted Sets
- Hashes
- Operações CRUD
- Consultas e gerenciamento de chaves

### Persistência

- RDB
- AOF
- Redis Storage
- Backup e recuperação

### TTL e Expiração

- Definição de TTL
- Expiração automática
- Estratégias de cache

### Redis Pub/Sub

- Publicação de mensagens
- Assinatura de canais
- Comunicação em tempo real

### Replicação

- Configuração Master/Replica
- Sincronização de dados
- Alta disponibilidade

### Segurança

- ACL (Access Control List)
- Criação de usuários
- Permissões por comando
- Controle de acesso por padrão de chaves
- Persistência das ACLs
- Armazenamento seguro de credenciais utilizando SHA-256

### Redis Cloud

- Criação de instâncias
- Conexão remota
- Administração de banco gerenciado

### Redis Insight

- Visualização de dados
- Administração de chaves
- Monitoramento de operações
- Análise de desempenho

### Monitoramento e Observability

- Integração Redis + Grafana
- Configuração via Docker
- Dashboards em tempo real
- Métricas de:

  - Throughput (Ops/sec)
  - Uso de memória
  - Número de chaves
  - Conexões
  - Tráfego de rede
  - Uptime
  - Evictions

---

<img width="1920" height="972" alt="Imagem colada" src="https://github.com/user-attachments/assets/a19adffc-d57b-4de1-82bf-062c52dae403" />


## Arquitetura

```text

┌─────────────┐
│   Grafana   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Redis    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ RedisInsight│
└─────────────┘




