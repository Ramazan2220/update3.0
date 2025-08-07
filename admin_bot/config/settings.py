#!/usr/bin/env python3
"""
⚙️ Настройки админ бота
"""

import os
from pathlib import Path

# Токен админ бота
ADMIN_BOT_TOKEN = os.getenv('ADMIN_BOT_TOKEN')

# Если не установлен отдельный токен, используем токен админки (для разработки)
if not ADMIN_BOT_TOKEN:
    # Используем только админский токен, НЕ основной
    ADMIN_BOT_TOKEN = '7775814314:AAE27Z2NvgUNl5zR1tnACrTPRu5hmkPjlBc'
    print("⚠️ ВНИМАНИЕ: Используется основной токен бота для админ панели!")
    print("🔧 Для продакшена создайте отдельного бота через @BotFather")

# Сообщения бота
MESSAGES = {
    'start': '🤖 Добро пожаловать в админ панель!',
    'main_menu': '🏠 Главное меню',
    'users_menu': '👥 Управление пользователями',
    'no_permission': '❌ У вас нет прав для выполнения этого действия',
    'error': '❌ Произошла ошибка. Попробуйте еще раз',
    'success': '✅ Операция выполнена успешно'
}

# Команды бота
BOT_COMMANDS = [
    ("start", "Главное меню"),
    ("users", "Управление пользователями"),
    ("stats", "Статистика"),
    ("help", "Помощь")
]

# Настройки уведомлений
NOTIFICATION_SETTINGS = {
    'enable_user_notifications': True,
    'enable_system_notifications': True,
    'notification_timeout': 30
}

# Настройки рассылок
BROADCAST_SETTINGS = {
    'max_message_length': 4096,
    'batch_size': 100,
    'delay_between_batches': 1.0
}
