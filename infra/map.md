# Карта инфраструктуры — botik

Собрана из `registry.yaml`. Общий уровень — только крупные блоки.  

```mermaid
graph LR
  repo_botik["repo-botik<br/>GitHub: botik"]
  repo_docs["repo-botik-docs<br/>GitHub: botik-docs"]
  railway["railway-botik<br/>Railway"]
  db["db-botik-pg<br/>PostgreSQL"]
  bot["bot-anastasia<br/>Telegram: Анастасия"]
  claude["api-anthropic<br/>Claude API"]
  jarvis["jarvis<br/>AI-ассистент"]
  bot_jarvis["bot-jarvis<br/>Telegram: @ameripresso_jarvis_bot"]

  repo_botik -- "push → автодеплой" --> railway
  railway --> db
  railway --> bot
  bot --> claude
  bot --> db
  jarvis -- "deploy key, запись" --> repo_docs
  bot_jarvis --> jarvis
```

`repo-botik-docs` не подключён к деплою — используется отдельно для планирования (см. `CLAUDE.md`), связи с `railway-botik` нет. `jarvis` — внешний относительно инфраструктуры `botik` AI-ассистент, подключён только к `repo-botik-docs` (запись через deploy key).
