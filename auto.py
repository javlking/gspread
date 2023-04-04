## В зависимости от бота ##
# Импортировать нужные компоненты из нужной библиотеки (aiogram)
from aiogram import Bot, Dispatcher, executor

## 1 ##
# Подключиться к боту
bot = Bot('token')

## 1 ##
# Рабочее пространство для Обработчика
dp = Dispatcher(bot)

## В зависимости от бота ##
# Создаем обработчики
@dp.message_handler()
# Ответы на те или иные сообщения
async def some_f(message):
    # message.text - это сообщение от пользователя
    if message.text == 'Привет':
        # Ответ на сообщение
        await message.answer('Привет')

    elif message.text == 'Как дела':
        await message.answer('Хорошо\nКак сам?')

    else:
        await message.answer('Не понимаю вас')

## 1 ##
# Запуск всех процессов
executor.start_polling(dp)
