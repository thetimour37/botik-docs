---
id: parameters
title: Параметры (числа, времена, наборы значений)
---

# Параметры

Все числа и времена спеки — здесь. В блоках — ссылка на параметр. Значение меняется в одном месте и в коде. Время хранится в UTC, отображается в GMT+3.

## Онбординг и контракт (блоки 0–1)

| ID | Значение | Константа в коде | Используется в |
|---|---|---|---|
| P-EVENING-TIME-DEFAULT | 20:00 (GMT+3) | `DEFAULT_EVENING_TIME` в `database_v2.py` | [B1-04](blocks/1-contract.md) |
| P-EVENING-TIME-MIN | 18:00 | `CUSTOM_TIME_MIN` в `handlers/v2.py` | [B1-03](blocks/1-contract.md), [B1-08](blocks/1-contract.md) |
| P-EVENING-TIME-MAX | 22:30 | `CUSTOM_TIME_MAX` в `handlers/v2.py` | [B1-03](blocks/1-contract.md), [B1-08](blocks/1-contract.md) |
| P-CONTRACT-TIME-OPTIONS | 19:00, 20:00, 21:00, 22:00 (кнопки; пятая — «Выбрать другое») | `CONTRACT_TIME_OPTIONS` в `keyboards.py` | [B1-02](blocks/1-contract.md) |
| P-MORNING-TIME | 9:00 пн–пт (GMT+3); окно отправки 30 минут (9:00–9:29) | `MORNING_HOUR`, `MORNING_WINDOW_MINUTES` в `database_v2.py` | [B1-05](blocks/1-contract.md) |

[← К оглавлению](README.md)
