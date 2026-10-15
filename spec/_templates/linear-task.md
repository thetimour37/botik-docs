# Шаблон описания задачи Linear

Скопировать в описание новой задачи (правило п. 7 в `spec/README.md`). Ссылки на спеку — на GitHub: `https://github.com/thetimour37/botik-docs/blob/main/spec/…`.

```markdown
## Что меняется
Одна-две фразы: поведение бота с точки зрения пользователя.

## Критерий готовности
- Проверяемое условие 1
- Проверяемое условие 2

## Блок и правила
Блок N, правила BN-01, BN-02 (новые или меняемые).

## Текст Насти
Нужен / не нужен. Если нужен: ключ в `texts.py` или `prompts.py`, кто и когда пишет; бот не придумывает текст сам.

## Затронутые файлы
- Код: `handlers/…`, `texts.py` (репозиторий botik)
- Тесты: `tests/…` (в тесте — номер правила)
- Спека: файлы ниже

## Спека
- Блок: https://github.com/thetimour37/botik-docs/blob/main/spec/blocks/N-имя.md
- Команды: https://github.com/thetimour37/botik-docs/blob/main/spec/commands.md
- Параметры: https://github.com/thetimour37/botik-docs/blob/main/spec/parameters.md
- Решения: https://github.com/thetimour37/botik-docs/blob/main/spec/decisions/ГГГГ-ММ-ДД-slug.md
- Карточка: https://github.com/thetimour37/botik-docs/blob/main/tasks/N-имя.md
```

Метки: «Тимур» или «Настя», тип (Task / Feature). Описание писать с настоящими переводами строк.
