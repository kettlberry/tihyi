import vk_api
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

def generate_inline_keyboard():
    keyboard = VkKeyboard(inline=True)
    keyboard.add_button('Условия аренды', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Описание и фото', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Связь с админом', color=VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()

vk_session = vk_api.VkApi(token='vk1.a.qnbdmOe7uUL5JadRaFqGXlFH_ZiOOgk1cxvLWU7JviM1VDVbATpRzHTYUEWu3BN8ASwiBqlDttgHfdTje1RR2UmRhZcY0EzSbONh4kSiW6y7edZ89oxuIi_ZnybvH7DKg78rEoOKmJkovxgUfKcjq_O0Gc2apPcwLov28iukIbJu2ni_hyTZLVs9VDXinDgnqkwGApXsYkOpoa9ZiiETqA')
vk_session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

print('VK бот запущен')

keyboard = generate_inline_keyboard()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id
            random_id = random.getrandbits(31)  # Генерация случайного random_id

            if message == 'начать':
                vk_session_api.messages.send(user_id=id, message='Рад приветствовать тебя в сообществе “ТИХИЙ ГЕНИЙ”'
'\nПредполагаю, что тебе понадобилась помощь, и мы с удовольствием её окажем 😉'
'\nЧуть ниже прайс-лист, а также ссылочки для связи с админом и описанием условий аренды. '
'\nПиши, мы всегда на связи 📝'
'\n'
'\n• Аренда наушника – 500 рублей (1 день)'
'\n• Залог – 2000 рублей'
'\n• Помощь ассистента – 250 рублей'
'\n'
'\nP.S. Минимальный срок аренды - 1 день📅'
'\nДоставка обсуждается индивидуально🚚', random_id=random_id, keyboard=keyboard)
            elif message == 'условия аренды':
                vk_session_api.messages.send(user_id=id, message='\n1. Заказываете микронаушник, договариваемся о месте и времени встречи.'
'\n2. Встречаемся, подключаем, проводим инструкцию.'
'\n3. Оплачиваете аренду, мы выдаём полный комплект + два разных наушника.'
'\n4. Вы оставляете залог.'
'\n5. Сдаёте экзамен. Связываетесь с нами.'
'\n6. Мы встречаемся и обмениваем залог на наш комплект.'
'\n\nВыберите одно из следующих действий:', random_id=random_id)
                # Удаляем кнопку "Условия аренды" из клавиатуры
                keyboard = generate_inline_keyboard()
            elif message == 'описание и фото':
                vk_session_api.messages.send(user_id=id, message='Качественные магнитные наушники премиального класса. В отличие от капсульных, в которые вставляется батарейка, здесь установлен аккумулятор, которого хватает более чем на 4 часа разговора. Благодаря Bluetooth версии 5.0 качество разговора остаётся идеальным, вне зависимости от того, как далеко расположен телефон.  Специальная усиливающая антенна позволяет не перебить сигнал наушника в случае, если человек сидящий рядом с вами тоже одел наушник.', random_id=random_id)
                # Удаляем кнопку "Описание и фото" из клавиатуры
                keyboard = generate_inline_keyboard()
            elif message == 'связь с админом':
                vk_session_api.messages.send(user_id=id, message='Что вас интересует?', random_id=random_id)
