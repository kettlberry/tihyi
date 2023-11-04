import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='vk1.a.4b1-Kuc35EVLfgP5SVDUYO-0aUd8OTmjPDxJYp4TEqTB6BDSHPeN9w9dKd8mAhuj21dRv2LGkMwpvaOFKMH4QWsyx9Siq8jYHpyZl26jj409GRvXtiPUxQ984JiFoFTzLJtO1BGTlUqlfPTu_6s58JGONA8IA7ASSMmraj2ivAIOA1Fc-8bfgx0Ke9BSpqydPWWWoWUqhZ3UT4EDK0-KNA')
vk_session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text, keyboard=None):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard})

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

    # Возвращаем объект клавиатуры и устанавливаем параметр one_time в True
    return keyboard.get_keyboard(one_time=True)

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
                sender(id, 'Условия аренды:'
'\n1. Заказываете микронаушник, договариваемся о месте и времени встречи.'
'\n2. Встречаемся, подключаем, проводим инструкцию.'
'\n3. Оплачиваете аренду, мы выдаём полный комплект + два разных наушника.'
'\n4. Вы оставляете залог.'
'\n5. Сдаёте экзамен. Связываетесь с нами.'
'\n6. Мы встречаемся и обмениваем залог на наш комплект.'
'\n\nВыберите одно из следующих действий:', keyboard=keyboard)
            elif message == 'описание и фото':
                sender(id, 'Здесь вы можете найти описание и фотографии наших продуктов.')
            elif message == 'связь с админом':
                sender(id, 'Связаться с администратором можно по телефону: 123-456-789\nИли по электронной почте: admin@example.com')
