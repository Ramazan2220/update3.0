#!/bin/bash

echo "🚀 УСТАНОВКА INSTAGRAM TELEGRAM BOT"
echo "===================================="
echo ""

# Проверяем наличие Python3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 не найден. Установите Python3 и попробуйте снова."
    exit 1
fi

echo "✅ Python3 найден: $(python3 --version)"
echo ""

# Создаем виртуальное окружение
echo "📦 Создание виртуального окружения..."
python3 -m venv bot_env
echo "✅ Виртуальное окружение создано"
echo ""

# Активируем окружение
echo "🔧 Активация окружения..."
source bot_env/bin/activate
echo "✅ Окружение активировано"
echo ""

# Обновляем pip
echo "⬆️ Обновление pip..."
pip install --upgrade pip
echo "✅ pip обновлен"
echo ""

# Устанавливаем зависимости
echo "📥 Установка зависимостей..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ Зависимости установлены"
else
    echo "❌ Файл requirements.txt не найден!"
    exit 1
fi
echo ""

# Создаем конфигурацию
echo "⚙️ Настройка конфигурации..."
if [ -f "config.example.py" ] && [ ! -f "config.py" ]; then
    cp config.example.py config.py
    echo "✅ Конфигурационный файл создан"
    echo "⚠️  ВНИМАНИЕ: Отредактируйте config.py и укажите токены ботов!"
else
    echo "✅ Конфигурационный файл уже существует"
fi
echo ""

# Создаем директории
echo "📁 Создание директорий..."
mkdir -p data/logs data/accounts data/media devices email_logs
echo "✅ Директории созданы"
echo ""

# Инициализируем базу данных
echo "🗄️ Инициализация базы данных..."
python -c "from database.db_manager import init_db; init_db(); print('✅ База данных инициализирована')" 2>/dev/null || echo "⚠️  База данных будет инициализирована при первом запуске"
echo ""

echo "🎉 УСТАНОВКА ЗАВЕРШЕНА!"
echo "======================"
echo ""
echo "📋 СЛЕДУЮЩИЕ ШАГИ:"
echo ""
echo "1️⃣ Отредактируйте config.py:"
echo "   nano config.py"
echo ""
echo "2️⃣ Укажите токены ботов:"
echo "   TELEGRAM_TOKEN = \"ваш_токен_основного_бота\""
echo "   ADMIN_BOT_TOKEN = \"ваш_токен_админ_бота\""
echo ""
echo "3️⃣ Запустите бота:"
echo "   source bot_env/bin/activate"
echo "   python main.py"
echo ""
echo "🔧 Для постоянного запуска используйте systemd (см. QUICK_SERVER_SETUP.md)"
echo ""
echo "✅ Готово! Ваш бот готов к запуску с Lazy Loading оптимизацией!" 