import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='vk1.a.4b1-Kuc35EVLfgP5SVDUYO-0aUd8OTmjPDxJYp4TEqTB6BDSHPeN9w9dKd8mAhuj21dRv2LGkMwpvaOFKMH4QWsyx9Siq8jYHpyZl26jj409GRvXtiPUxQ984JiFoFTzLJtO1BGTlUqlfPTu_6s58JGONA8IA7ASSMmraj2ivAIOA1Fc-8bfgx0Ke9BSpqydPWWWoWUqhZ3UT4EDK0-KNA')
vk_session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text, keyboard=None):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard})

print('VK бот запущен')

def generate_keyboard():
    keyboard = VkKeyboard(one_time=True)

    # Добавляем первую кнопку
    keyboard.add_button('Кнопка 1', color=VkKeyboardColor.PRIMARY)

    # Добавляем вторую кнопку
    keyboard.add_button('Кнопка 2', color=VkKeyboardColor.PRIMARY)

    # Добавляем третью кнопку
    keyboard.add_button('Кнопка 3', color=VkKeyboardColor.PRIMARY)

    # Конечно, вы можете добавить больше кнопок, если нужно

    # Помещаем клавиатуру в сообщение
    keyboard = keyboard.get_keyboard()

    return keyboard

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id
            if message == 'начать':
                keyboard = generate_keyboard()  # Генерируем клавиатуру
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
