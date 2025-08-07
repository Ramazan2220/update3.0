#!/usr/bin/env python3
"""
ФИНАЛЬНЫЙ ТЕСТ ИНТЕГРИРОВАННОЙ СИСТЕМЫ
Проверяет работу новой системы синхронизации через старые функции
"""

import sys
import time
import os

sys.path.insert(0, './utils')
sys.path.insert(0, './admin_bot')

def test_integrated_system():
    """Тестирует интегрированную систему"""
    print("🔧 ТЕСТ ИНТЕГРИРОВАННОЙ СИСТЕМЫ")
    print("=" * 80)
    
    user_id = 6626270112
    
    try:
        # Импортируем старые функции (которые теперь используют новую систему)
        from utils.access_manager import has_access, add_user_access, remove_user_access, delete_user_completely, force_sync_access
        
        print("✅ Импорт функций успешен")
        
        # 1. Начальная проверка
        print(f"\n1️⃣ НАЧАЛЬНОЕ СОСТОЯНИЕ:")
        initial_access = has_access(user_id)
        print(f"   has_access({user_id}): {initial_access}")
        
        # 2. Добавляем пользователя
        print(f"\n2️⃣ ДОБАВЛЯЕМ ПОЛЬЗОВАТЕЛЯ:")
        add_result = add_user_access(user_id)
        print(f"   add_user_access({user_id}): {add_result}")
        
        # Сразу проверяем доступ
        access_after_add = has_access(user_id)
        print(f"   has_access({user_id}) сразу после добавления: {access_after_add}")
        
        # 3. Удаляем пользователя
        print(f"\n3️⃣ УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ:")
        remove_result = delete_user_completely(user_id)
        print(f"   delete_user_completely({user_id}): {remove_result}")
        
        # Сразу проверяем доступ
        access_after_remove = has_access(user_id)
        print(f"   has_access({user_id}) сразу после удаления: {access_after_remove}")
        
        # 4. Тестируем синхронизацию
        print(f"\n4️⃣ ТЕСТИРУЕМ СИНХРОНИЗАЦИЮ:")
        sync_result = force_sync_access()
        print(f"   force_sync_access(): {sync_result}")
        
        # 5. Результат
        print(f"\n🏁 РЕЗУЛЬТАТ ТЕСТА:")
        print(f"   Начальное состояние: {initial_access}")
        print(f"   После добавления: {access_after_add}")
        print(f"   После удаления: {access_after_remove}")
        
        if not initial_access and access_after_add and not access_after_remove:
            print(f"\n🎉 СИСТЕМА РАБОТАЕТ ИДЕАЛЬНО!")
            print(f"   ✅ Добавление: мгновенно")
            print(f"   ✅ Удаление: мгновенно")
            print(f"   ✅ Синхронизация: автоматическая")
            return True
        else:
            print(f"\n❌ ЕСТЬ ПРОБЛЕМЫ:")
            if initial_access:
                print(f"   ❌ Пользователь был в системе изначально")
            if not access_after_add:
                print(f"   ❌ Добавление не сработало")
            if access_after_remove:
                print(f"   ❌ Удаление не сработало")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка тестирования: {e}")
        import traceback
        traceback.print_exc()
        return False

def simulate_admin_bot_operations():
    """Симулирует операции админ бота"""
    print(f"\n🤖 СИМУЛЯЦИЯ ОПЕРАЦИЙ АДМИН БОТА")
    print("=" * 80)
    
    user_id = 6626270112
    
    try:
        # Импортируем функции, которые использует админ бот
        from utils.access_manager import add_user_access, delete_user_completely, has_access
        
        print(f"📋 Симулируем сценарий:")
        print(f"   1. Админ добавляет пользователя")
        print(f"   2. Проверяем что основной бот видит пользователя")
        print(f"   3. Админ удаляет пользователя")
        print(f"   4. Проверяем что основной бот НЕ видит пользователя")
        
        # Добавляем пользователя (как админ бот)
        print(f"\n🟢 АДМИН: Добавляю пользователя {user_id}")
        add_result = add_user_access(user_id)
        print(f"   Результат: {add_result}")
        
        # Проверяем доступ (как основной бот)
        print(f"🤖 ОСНОВНОЙ БОТ: Проверяю доступ для {user_id}")
        access_result = has_access(user_id)
        print(f"   Результат: {access_result}")
        
        if access_result:
            print(f"   ✅ Основной бот ВИДИТ пользователя!")
        else:
            print(f"   ❌ Основной бот НЕ ВИДИТ пользователя!")
        
        # Ждем немного
        time.sleep(0.5)
        
        # Удаляем пользователя (как админ бот)
        print(f"\n🔴 АДМИН: Удаляю пользователя {user_id}")
        remove_result = delete_user_completely(user_id)
        print(f"   Результат: {remove_result}")
        
        # Проверяем доступ (как основной бот)
        print(f"🤖 ОСНОВНОЙ БОТ: Проверяю доступ для {user_id}")
        access_result_after = has_access(user_id)
        print(f"   Результат: {access_result_after}")
        
        if not access_result_after:
            print(f"   ✅ Основной бот НЕ ВИДИТ удаленного пользователя!")
        else:
            print(f"   ❌ Основной бот ВСЕ ЕЩЕ ВИДИТ удаленного пользователя!")
        
        return access_result and not access_result_after
        
    except Exception as e:
        print(f"❌ Ошибка симуляции: {e}")
        return False

def main():
    print("🚀 ФИНАЛЬНЫЙ ТЕСТ НОВОЙ СИСТЕМЫ СИНХРОНИЗАЦИИ")
    print("=" * 100)
    
    # Основной тест
    basic_test_result = test_integrated_system()
    
    # Симуляция реального сценария
    simulation_result = simulate_admin_bot_operations()
    
    print(f"\n🏆 ФИНАЛЬНЫЕ РЕЗУЛЬТАТЫ:")
    print("=" * 100)
    print(f"   Базовый тест: {'✅ ПРОШЕЛ' if basic_test_result else '❌ НЕ ПРОШЕЛ'}")
    print(f"   Симуляция админ бота: {'✅ ПРОШЕЛ' if simulation_result else '❌ НЕ ПРОШЕЛ'}")
    
    if basic_test_result and simulation_result:
        print(f"\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        print(f"🚀 НОВАЯ СИСТЕМА СИНХРОНИЗАЦИИ ГОТОВА К ИСПОЛЬЗОВАНИЮ!")
        print(f"🔄 Перезапустите админ бот и основной бот для применения изменений")
        print(f"📖 Читайте MIGRATION_GUIDE.md для подробностей")
    else:
        print(f"\n⚠️ ЕСТЬ ПРОБЛЕМЫ!")
        print(f"🔧 Проверьте логи и повторите тестирование")
        print(f"🔄 Возможно нужен rollback из backup_old_sync/")

if __name__ == "__main__":
    main() 