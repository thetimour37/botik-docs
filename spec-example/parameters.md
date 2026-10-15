---
id: PARAMETERS
title: Параметры
status: согласовано
---

# Параметры

Все числа и времена бота в одном месте. В блоках стоит ссылка сюда, а не само число. Если нужно поменять значение, меняем здесь и в коде.

> Пример. Показана часть параметров.

## Время вечера

| Параметр | Значение | Где в коде |
|---|---|---|
| P-EVENING-DEFAULT | 20:00 (GMT+3) | `database_v2.DEFAULT_EVENING_TIME` |
| P-EVENING-MIN | 18:00 | `handlers/v2.CUSTOM_TIME_MIN` |
| P-EVENING-MAX | 22:30 | `handlers/v2.CUSTOM_TIME_MAX` |

## Окна ожидания

| Параметр | Значение | Где в коде |
|---|---|---|
| P-EVENING-QUESTIONS | не более 2 вопросов | `handlers/evening.py` |
| P-EVENING-REPLY-MIN | 30 минут на ответ | `handlers/evening.py` |
| P-EVENING-TOTAL-MIN | 90 минут на весь вечер | `handlers/evening.py` |

## Молчание

| Параметр | Значение | Где в коде |
|---|---|---|
| P-SILENCE-DAYS | 3 будних дня | `database_v2.SILENCE_DAYS` |
| P-SILENCE-CHECKS | не более 3 проверок | `database_v2.MAX_SILENCE_CHECKS` |

[← К оглавлению](README.md)
