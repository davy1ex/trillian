from vk_api import VkApi
from settings import VK_GROUP_TOKEN


def auth():
        session = VkApi(token=VK_GROUP_TOKEN)
        return session.get_api()


def main():
    vk = auth()
    if vk.users.get(user_id='154597302', fields='online'):
        vk.messages.send(user_id='154597302', message='хуй', random_id='235')


if __name__ == '__main__':
    main()
