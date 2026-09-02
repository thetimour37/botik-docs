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

  repo_botik -- "push → автодеплой" --> railway
  railway --> db
  railway --> bot
  bot --> claude
  bot --> db
```

`repo-botik-docs` не подключён к деплою — используется отдельно для планирования (см. `CLAUDE.md`), связи с `railway-botik` нет.
