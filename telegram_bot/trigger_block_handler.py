#!/usr/bin/env python3
"""
🚫 Триггерный обработчик блокировки пользователей

Перехватывает специальные сообщения о блокировке и мгновенно блокирует доступ
"""

import logging
from telegram import Update
from telegram.ext import CallbackContext

# Совместимость с разными версиями python-telegram-bot
try:
    from telegram.ext import ApplicationHandlerStop
except ImportError:
    # Для старых версий python-telegram-bot
    class ApplicationHandlerStop(Exception):
        """Исключение для остановки обработки в старых версиях telegram-bot"""
        pass

logger = logging.getLogger(__name__)

# КРИТИЧЕСКИ ВАЖНО: Триггерный текст должен ТОЧНО совпадать
TRIGGER_BLOCK_MESSAGE = "🚫 Ваш доступ к боту заблокирован администратором"

def handle_trigger_block_message(update: Update, context: CallbackContext):
    """
    Обрабатывает триггерные сообщения о блокировке для мгновенной блокировки пользователя
    
    Логика:
    1. Проверяет, является ли сообщение триггерным
    2. Если да - мгновенно блокирует пользователя
    3. Останавливает дальнейшую обработку
    """
    try:
        # Проверяем, есть ли сообщение
        if not update.message or not update.message.text:
            return  # Пропускаем, если нет текста
        
        user_id = update.effective_user.id
        message_text = update.message.text.strip()
        
        # Проверяем, является ли это триггерным сообщением блокировки
        if message_text == TRIGGER_BLOCK_MESSAGE:
            logger.info(f"🚫 ТРИГГЕР БЛОКИРОВКИ: Пользователь {user_id} получил триггерное сообщение")
            
            # МГНОВЕННАЯ БЛОКИРОВКА пользователя
            try:
                from telegram_bot.middleware.smart_access_check import force_block_user
                force_block_user(user_id)
                logger.info(f"🔒 Пользователь {user_id} мгновенно заблокирован через триггер")
                
            except ImportError:
                logger.warning("Smart access check недоступен для триггерной блокировки")
            
            # Обновляем access_manager
            try:
                from utils.access_manager import remove_user_access
                remove_user_access(user_id)
                logger.info(f"🗑️ Пользователь {user_id} удален из access_manager")
                
            except ImportError:
                logger.warning("Access manager недоступен для триггерной блокировки")
            
            # Отправляем финальное сообщение о блокировке
            try:
                update.message.reply_text(
                    "🚫 Ваш доступ заблокирован.\n\n"
                    "Обратитесь к администратору для получения информации.",
                    parse_mode='HTML'
                )
                logger.info(f"📨 Отправлено финальное сообщение о блокировке пользователю {user_id}")
                
            except Exception as e:
                logger.error(f"Ошибка отправки финального сообщения: {e}")
            
            # КРИТИЧЕСКИ ВАЖНО: Останавливаем дальнейшую обработку
            logger.info(f"🛑 Остановка обработки для заблокированного пользователя {user_id}")
            raise ApplicationHandlerStop
            
    except ApplicationHandlerStop:
        # Перебрасываем исключение для остановки обработки
        raise
        
    except Exception as e:
        logger.error(f"Ошибка в триггерном обработчике блокировки: {e}")
        # НЕ останавливаем обработку при ошибках, чтобы не блокировать бота 