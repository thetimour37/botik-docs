---
id: parameters
title: Параметры (числа, времена, наборы значений)
---

# Параметры

Все числа и времена спеки — здесь. Проверка соответствия констант значениям таблицы — `tests/test_spec_parameters.py` в репозитории botik. В блоках — ссылка на параметр. Значение меняется в одном месте и в коде. Время хранится в UTC, отображается в GMT+3.

## Онбординг и контракт (блоки 0–1)

| ID | Значение | Константа в коде | Используется в |
|---|---|---|---|
| P-EVENING-TIME-DEFAULT | 20:00 (GMT+3) | `DEFAULT_EVENING_TIME` в `database_v2.py` | [B1-04](blocks/1-contract.md), [B4-01](blocks/4-evening.md), [B5-13](blocks/5-silence.md) |
| P-EVENING-TIME-MIN | 18:00 | `CUSTOM_TIME_MIN` в `handlers/v2.py` | [B1-03](blocks/1-contract.md), [B1-08](blocks/1-contract.md), [B4-08](blocks/4-evening.md) |
| P-EVENING-TIME-MAX | 22:30 | `CUSTOM_TIME_MAX` в `handlers/v2.py` | [B1-03](blocks/1-contract.md), [B1-08](blocks/1-contract.md), [B4-08](blocks/4-evening.md) |
| P-CONTRACT-TIME-OPTIONS | 19:00, 20:00, 21:00, 22:00 (кнопки; пятая — «Выбрать другое») | `CONTRACT_TIME_OPTIONS` в `keyboards.py` | [B1-02](blocks/1-contract.md) |
| P-TIMEZONE-OFFSET | GMT+3 (МСК): границы суток («после 00:00», «до конца дня»), время показа и ввода; хранение в UTC | `MSK_OFFSET` в `database_v2.py` | [B2-10](blocks/2-focus.md), [B3-05](blocks/3-daily.md) |
| P-MORNING-TIME | 9:00 пн–пт (GMT+3); окно отправки 30 минут (9:00–9:29) | `MORNING_HOUR`, `MORNING_WINDOW_MINUTES` в `database_v2.py` | [B1-05](blocks/1-contract.md) |

## Ежедневный сбор и фокус (блоки 2–3)

| ID | Значение | Константа в коде | Используется в |
|---|---|---|---|
| P-SCORE-RANGE | оценка запроса 1–10 | регулярное выражение `_SCORE_RE` в `handlers/focus.py`, `request_score_keyboard` в `keyboards.py` | [B2-05](blocks/2-focus.md), [B2-16](blocks/2-focus.md) |
| P-FOCUS-CLARIFY-MAX | 2 готовых уточняющих вопроса | длина `FOCUS_CLARIFY_QUESTIONS` в `texts.py` | [B2-08](blocks/2-focus.md) |
| P-FOCUS-MSG-LIMIT | 20 сообщений пользователя на этап фокуса | `FOCUS_MSG_LIMIT` в `handlers/focus.py` | [B2-10](blocks/2-focus.md) |
| P-STAGE-MIN-HOURS | срок этапа: до конца дня (GMT+3), но не меньше 3 часов от начала | `STAGE_MIN_HOURS` в `database_v2.py` (используется в `block2_deadline`) | [B2-06](blocks/2-focus.md), [B2-10](blocks/2-focus.md), [B2-13](blocks/2-focus.md), [B2-17](blocks/2-focus.md) |
| P-FOCUS-OPTIONS-COUNT | 3 варианта фокуса | `FOCUS_OPTIONS_COUNT` в `prompts.py` (обрезка списка вариантов в `handlers/focus.py` и `handlers/weekly.py`; то же число стоит в текстах промптов `FOCUS_DIALOG_PROMPT`, `WEEKLY_FOCUS_OPTIONS_PROMPT`, `FOCUS_CHANGE_OPTIONS_PROMPT`) | [B2-11](blocks/2-focus.md), [B3-20](blocks/3-daily.md) |
| P-MORNING-VARIANTS | 5 вариантов утреннего сообщения | длина `MORNING_MESSAGES` в `texts.py` | [B3-02](blocks/3-daily.md), [B3-03](blocks/3-daily.md) |
| P-DAILY-TEXT-REPLIES | первые 3 сообщения дня — реакция текстом | `DAILY_TEXT_REPLIES` в `database_v2.py` | [B3-08](blocks/3-daily.md) |
| P-REACTION-EMOJI | 👍 (✅ и 🤍 Telegram не допускает) | `REACTION_EMOJI` в `handlers/observation.py` | [B3-09](blocks/3-daily.md) |
| P-OFFTOPIC-OFFERS-PER-DAY | 1 предложение запомнить тему в день | `OFFTOPIC_OFFERS_PER_DAY` в `database_v2.py` (реализовано датой последнего предложения `users.topic_offer_on` в `handlers/observation.py`) | [B3-16](blocks/3-daily.md) |
| P-FOCUS-CHANGE-OWN-MAX-HOURS | 24 часа на фразу и подтверждение при «Свой фокус» | `FOCUS_CHANGE_OWN_MAX_HOURS` в `database_v2.py` | [B3-20](blocks/3-daily.md) |
| P-VOICE-MAX-SECONDS | голосовое длиннее 180 секунд не распознаётся (просьба записать короче) | `VOICE_MAX_SECONDS` в `services/voice.py` | [B3-21](blocks/3-daily.md) |
| P-VOICE-MODEL | модель распознавания речи: `whisper-large-v3-turbo` (Groq) | `VOICE_MODEL` в `services/voice.py` | [B3-21](blocks/3-daily.md) |

## Вечер и молчание (блоки 4–5)

Время вечера по умолчанию и диапазон своего времени — в разделе «Онбординг и контракт» (P-EVENING-TIME-DEFAULT, P-EVENING-TIME-MIN, P-EVENING-TIME-MAX).

| ID | Значение | Константа в коде | Используется в |
|---|---|---|---|
| P-EVENING-ANSWER-WAIT-MIN | 30 минут на ответ на любой вечерний вопрос | `EVENING_ANSWER_WAIT_MINUTES` в `database_v2.py` | [B4-05](blocks/4-evening.md), [B4-11](blocks/4-evening.md), [B4-13](blocks/4-evening.md) |
| P-EVENING-MAX-QUESTIONS | не больше 2 уточняющих вопросов за вечер | `EVENING_MAX_QUESTIONS` в `database_v2.py` | [B4-06](blocks/4-evening.md), [B4-09](blocks/4-evening.md) |
| P-EVENING-MAX-MIN | весь вечер не дольше 90 минут (1,5 часа) | `EVENING_MAX_MINUTES` в `database_v2.py` | [B4-07](blocks/4-evening.md) |
| P-EVENING-START-WINDOW-MIN | окно начала вечера 30 минут после времени из контракта | `EVENING_START_WINDOW_MINUTES` в `database_v2.py` | [B4-04](blocks/4-evening.md) |
| P-EVENING-INVITE-VARIANTS | 3 варианта вопроса-приглашения | длина `EVENING_INVITE_MESSAGES` в `texts.py` | [B4-12](blocks/4-evening.md) |
| P-CLOSING-VARIANTS | 3 варианта закрывающего сообщения (у каждого пара: 1-й и 2-й день молчания) | длина `CLOSING_EMPTY_DAY` в `texts.py` | [B4-14](blocks/4-evening.md), [B4-15](blocks/4-evening.md) |
| P-SILENCE-DAYS | 3 будних дня без сообщений до проверки (и между проверками) | `SILENCE_DAYS` (переменная окружения, по умолчанию 3) в `database_v2.py` | [B5-02](blocks/5-silence.md), [B5-08](blocks/5-silence.md) |
| P-MAX-SILENCE-CHECKS | до 3 проверок без ответа, затем `dormant` | `MAX_SILENCE_CHECKS` (переменная окружения, по умолчанию 3) в `database_v2.py` | [B5-08](blocks/5-silence.md) |
| P-SILENCE-CHECK-VARIANTS | 5 вариантов проверки №1 | длина `SILENCE_DAY3_MESSAGES` в `texts.py` | [B5-03](blocks/5-silence.md) |
| P-PAUSE-ACK-VARIANTS | 6 вариантов признания паузы | длина `PAUSE_ACK_MESSAGES` в `texts.py` | [B5-05](blocks/5-silence.md) |
| P-WEEKLY-ON-PAUSE-VARIANTS | 2 варианта заготовки недельного резюме на паузе | длина `WEEKLY_ON_PAUSE_MESSAGES` в `texts.py` | [B5-16](blocks/5-silence.md) |

## Недельный цикл и сессия (блок 6)

| ID | Значение | Константа в коде | Используется в |
|---|---|---|---|
| P-WEEKLY-TIME | суббота 9:00 (GMT+3); в воскресенье 9:00 кнопка «Изучил» считается нажатой | `WEEKLY_HOUR` в `database_v2.py` | [B6-01](blocks/6-weekly.md), [B6-19](blocks/6-weekly.md), [B6A-06](blocks/6a-session.md) |
| P-WEEKLY-WINDOW-MIN | окно отправки субботы 60 минут (9:00–9:59) | `WEEKLY_WINDOW_MINUTES` в `database_v2.py` | [B6-01](blocks/6-weekly.md) |
| P-WEEKLY-CHOICE-WAIT-MIN | 60 минут на «Что влияло?» и выбор фокуса | `WEEKLY_CHOICE_WAIT_MINUTES` в `database_v2.py` | [B6-20](blocks/6-weekly.md) |
| P-WEEKLY-OWN-MAX-HOURS | 24 часа: предел остановки таймера при «Своём фокусе» (допущение) | `WEEKLY_OWN_MAX_HOURS` в `database_v2.py` | [B6-21](blocks/6-weekly.md) |
| P-NEWCOMER-MIN-WEEKDAYS | первая суббота новичка: минимум 3 будних дня с фиксации фокуса | `NEWCOMER_MIN_WEEKDAYS` в `database_v2.py` | [B6-02](blocks/6-weekly.md) |
| P-WEEKLY-FEW-OBSERVATIONS | «наблюдений мало»: меньше 3 за неделю (допущение) | `FEW_OBSERVATIONS` в `services/stars.py` | [B6-07](blocks/6-weekly.md) |
| P-STARS-VOLUME-THRESHOLDS | пороги звёздочек объёма: 1 / 4 / 8 / 13 / 20 наблюдений (1–5 звёзд; предложение разработки, пороги задают Тимур и Настя) | `VOLUME_THRESHOLDS` в `services/stars.py` | [B6-05](blocks/6-weekly.md), [B6-10](blocks/6-weekly.md) |
| P-STARS-MAX | максимум 5 звёзд (регулярность — 0–5 по будним дням) | `MAX_STARS` в `services/stars.py` | [B6-10](blocks/6-weekly.md) |
| P-SESSION-MINUTES | сессия — 60 минут | `SESSION_MINUTES` в `database_v2.py` | [B6A-03](blocks/6a-session.md), [B6A-07](blocks/6a-session.md) |

## Месячный срез и дашборд (блок 7)

| ID | Значение | Константа в коде | Используется в |
|---|---|---|---|
| P-MONTHLY-MIN-DAYS | срез приходит, если со старта прошло больше 10 дней (строго больше 240 часов) | `MONTHLY_MIN_DAYS` в `database_v2.py` | [B7-02](blocks/7-monthly.md) |
| P-MONTHLY-STEP-WAIT-MIN | 60 минут на каждый шаг среза (оценка, выбор запроса, новый запрос, оценка нового) | `MONTHLY_STEP_WAIT_MINUTES` в `database_v2.py` | [B7-07](blocks/7-monthly.md), [B7-08](blocks/7-monthly.md), [B7-11](blocks/7-monthly.md), [B7-12](blocks/7-monthly.md) |
| P-DASHBOARD-WEEKS | дашборд показывает 4 последние недели (включая текущую) | `DASHBOARD_WEEKS` в `handlers/commands.py` | [B7-15](blocks/7-monthly.md) |

## Служебные команды

| ID | Значение | Константа в коде | Используется в |
|---|---|---|---|
| P-BUG-REPORTS-PER-HOUR | не больше 3 отчётов `/bug` в час от одного пользователя | `BUG_REPORTS_PER_HOUR` в `handlers/bug.py` | [CMD-BUG](commands.md) |
| P-BUG-WAIT-MIN | ожидание описания ошибки после `/bug` — 15 минут, потом сообщение снова обычное | `BUG_WAIT_MINUTES` в `handlers/bug.py` | [CMD-BUG](commands.md) |

[← К оглавлению](README.md)
