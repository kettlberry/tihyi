# Создано в Bot Creator
# Автор - Булат Заляльдинов
import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token = 'vk1.a.ZIra4SVC4Y_eYmjvSLnKLkNhhCA_pdtTm10J1CLPh2_oUUe-15_MAM2uJWp2MF8osHYN6DviwEzsNqY5Ni6Zl0yDxV-43_2zKyw2JW80BjHdpN4Z6g7td9iaQd2y3KQd1OTbDPSlHDiTpDYh35LjPYgWtSiq6vLmqUwIRo583ltBoqPhBu_LNsIqbqlaw8a-PoslR9VsU-Rzx9I7YbP5PQ')
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

