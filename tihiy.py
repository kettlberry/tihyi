import vk_api
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='vk1.a.qnbdmOe7uUL5JadRaFqGXlFH_ZiOOgk1cxvLWU7JviM1VDVbATpRzHTYUEWu3BN8ASwiBqlDttgHfdTje1RR2UmRhZcY0EzSbONh4kSiW6y7edZ89oxuIi_ZnybvH7DKg78rEoOKmJkovxgUfKcjq_O0Gc2apPcwLov28iukIbJu2ni_hyTZLVs9VDXinDgnqkwGApXsYkOpoa9ZiiETqA')
vk_session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

print('VK бот запущен')

def generate_inline_keyboard(has_description_button=True, has_rent_conditions_button=True):
    keyboard = VkKeyboard(inline=True)
    if has_description_button:
        keyboard.add_button('Описание и фото', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
    if has_rent_conditions_button:
        keyboard.add_button('Условия аренды', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
    keyboard.add_button('Связь с админом', color=VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id
            random_id = random.getrandbits(31)  # Генерация случайного random_id

            if message == 'начать':
                keyboard = generate_inline_keyboard(has_description_button=True, has_rent_conditions_button=True)
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
                keyboard = generate_inline_keyboard(has_description_button=True, has_rent_conditions_button=False)
                vk_session_api.messages.send(user_id=id, message='\n1. Заказываете микронаушник, договариваемся о месте и времени встречи.'
'\n2. Встречаемся, подключаем, проводим инструкцию.'
'\n3. Оплачиваете аренду, мы выдаём полный комплект + два разных наушника.'
'\n4. Вы оставляете залог.'
'\n5. Сдаёте экзамен. Связываетесь с нами.'
'\n6. Мы встречаемся и обмениваем залог на наш комплект.'
'\n\nВыберите одно из следующих действий:', random_id=random_id, keyboard=keyboard)
            elif message == 'описание и фото':
                # Обработка действия "Описание и фото"
                pass
            elif message == 'связь с админом':
                # Обработка действия "Связь с админом"
                pass
