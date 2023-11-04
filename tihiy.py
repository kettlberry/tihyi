import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='vk1.a.qnbdmOe7uUL5JadRaFqGXlFH_ZiOOgk1cxvLWU7JviM1VDVbATpRzHTYUEWu3BN8ASwiBqlDttgHfdTje1RR2UmRhZcY0EzSbONh4kSiW6y7edZ89oxuIi_ZnybvH7DKg78rEoOKmJkovxgUfKcjq_O0Gc2apPcwLov28iukIbJu2ni_hyTZLVs9VDXinDgnqkwGApXsYkOpoa9ZiiETqA')
vk_session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text, photos=None, keyboard=None):
    # Отправляем текстовое сообщение
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard})
    # Отправляем фотографии, если они указаны
    if photos:
        vk_session.method('messages.send', {'user_id': id, 'message': '', 'random_id': 0, 'attachment': photos})

print('VK бот запущен')

def generate_inline_keyboard():
    # Создаем объект клавиатуры
    keyboard = VkKeyboard(inline=True)

    # Добавляем первую кнопку "Условия аренды" с синим цветом и фиксированной шириной
    keyboard.add_button('Условия аренды', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()

    # Добавляем вторую кнопку "Описание и фото" с зеленым цветом и фиксированной шириной
    keyboard.add_button('Описание и фото', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()

    # Добавляем третью кнопку "Связь с админом" с красным цветом и фиксированной шириной
    keyboard.add_button('Связь с админом', color=VkKeyboardColor.NEGATIVE)

    # Возвращаем объект клавиатуры
    return keyboard.get_keyboard()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id
            if message == 'начать':
                keyboard = generate_inline_keyboard()  # Генерируем inline клавиатуру
                sender(id, 'Рад приветствовать тебя в сообществе “ТИХИЙ ГЕНИЙ”'
'\nПредполагаю, что тебе понадобилась помощь, и мы с удовольствием её окажем 😉'
'\nЧуть ниже прайс-лист, а также ссылочки для связи с админом и описанием условий аренды. '
'\nПиши, мы всегда на связи 📝'
'\n'
'\n• Аренда наушника – 500 рублей (1 день)'
'\n• Залог – 2000 рублей'
'\n• Помощь ассистента – 250 рублей'
'\n'
'\nP.S. Минимальный срок аренды - 1 день📅'
'\nДоставка обсуждается индивидуально🚚', keyboard=keyboard)
            elif message == 'условия аренды':
                sender(id, '\n1. Заказываете микронаушник, договариваемся о месте и времени встречи.'
'\n2. Встречаемся, подключаем, проводим инструкцию.'
'\n3. Оплачиваете аренду, мы выдаём полный комплект + два разных наушника.'
'\n4. Вы оставляете залог.'
'\n5. Сдаёте экзамен. Связываетесь с нами.'
'\n6. Мы встречаемся и обмениваем залог на наш комплект.'
'\n\nВыберите одно из следующих действий:', keyboard=keyboard)
            elif message == 'описание и фото':
                text = 'Качественные магнитные наушники премиального класса. В отличие от капсульных, в которые вставляется батарейка, здесь установлен аккумулятор, которого хватает более чем на 4 часа разговора. Благодаря Bluetooth версии 5.0 качество разговора остаётся идеальным, вне зависимости от того, как далеко расположен телефон.  Специальная усиливающая антенна позволяет не перебить сигнал наушника в случае, если человек сидящий рядом с вами тоже одел наушник.'
                # Замените 'photo123_456' и 'photo789_012' на ссылки на фотографии
                photos = [f'photo123_456', f'photo789_012']
                sender(id, text, photos=photos, keyboard=keyboard)
            elif message == 'связь с админом':
                sender(id, 'Что вас интересует?', keyboard=keyboard)
