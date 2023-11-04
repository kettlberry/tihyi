# Создано в Bot Creator
# Автор - Булат Заляльдинов
import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token = 'vk1.a.1hE4h27tfLS1XW-VfMKm4IZSKIzC7_WtF7wM6Icv9haKlWdvTXgenfVI3l-fmXRiH8sAHc2s45HaJNUfK7IiOKSjLbGGkIkSmFiC5FUy1q886NRhWjzafbYJkICy8rPDeeq-4kmDO74ENI0VocxE7OdUg9UTv1qPHnz2pls6GnrhYUUUUxEMX0t3ByO78GTLYfZ4vleskVkm3CIqgw3WuA')
vk_session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text):
	vk_session.method('messages.send', { 'user_id' : id, 'message' : text, 'random_id' : 0})

print('VK бот запущен')
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			message = event.text.lower()
			id = event.user_id
			if message == 'начать':
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
'\nДоставка обсуждается индивидуально🚚')

