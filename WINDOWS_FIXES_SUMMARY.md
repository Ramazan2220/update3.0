# ИСПРАВЛЕНИЯ ДЛЯ WINDOWS СЕРВЕРА

## ✅ ИСПРАВЛЕННЫЕ ПРОБЛЕМЫ

### 1. ❌ → ✅ Кодировка UTF-8
**Проблема:** UnicodeEncodeError при выводе русского текста и эмодзи
**Решение:** Создан `start_bot_windows.py` с правильной настройкой кодировки

### 2. ❌ → ✅ instagram_service ошибка
**Проблема:** `name 'instagram_service' is not defined`
**Решение:** Заменил `instagram_service.get_decrypted_password()` на `account.password`
**Файл:** `services/advanced_warmup.py` строка 187

### 3. ❌ → ✅ story_selector и reels_selector не определены
**Проблема:** `name 'story_selector' is not defined`
**Решение:** 
- Добавил глобальные селекторы в `publish_handlers.py`
- Создал функцию `initialize_selectors()`
- Добавил инициализацию в `start_story_publish()` и `start_reels_publish()`

### 4. ❌ → ✅ public_graphql_request патч
**Проблема:** `got multiple values for argument 'query_hash'`
**Решение:** Заменил фиксированные параметры на `*args, **kwargs`
**Файл:** `instagram/client_patch.py` строка 358

### 5. ❌ → ✅ save_session импорт
**Проблема:** `cannot import name 'save_session'`
**Решение:** Заменил на `cl.dump_settings()`
**Файл:** `services/advanced_warmup.py` строки 213-216

### 6. ✅ Добавлены обработчики прокси кнопок
**Решение:** Добавил обработчики:
- `test_proxy_handler`
- `change_proxy_handler` 
- `proxy_stats_handler`
**Файл:** `telegram_bot/handlers/account_handlers.py`

## 🚀 СПОСОБЫ ЗАПУСКА

### Вариант 1 - Простой
```batch
start_windows_server.bat
```

### Вариант 2 - Ручной
```powershell
chcp 65001
set PYTHONIOENCODING=utf-8
set PYTHONLEGACYWINDOWSSTDIO=utf-8
python start_bot_windows.py
```

## 📋 ОЖИДАЕМЫЙ РЕЗУЛЬТАТ

- ✅ Кодировка UTF-8 работает без ошибок
- ✅ Клиенты создаются для прогрева аккаунтов  
- ✅ Кнопки прокси работают
- ✅ Публикация Stories и Reels работает
- ✅ Логи чистые без UnicodeError
- ✅ Сессии сохраняются правильно

## ⚠️ ОСТАВШИЕСЯ ПРЕДУПРЕЖДЕНИЯ (НЕ КРИТИЧНЫЕ)

1. `UserWarning: python-telegram-bot is using upstream urllib3` - не влияет на работу
2. `UserWarning: pkg_resources is deprecated` - не влияет на работу
3. `UserWarning: If 'per_message=False'` - не влияет на работу

Эти предупреждения можно игнорировать. 