import vk_api


def main():
    login, password = "89109970021", "leesyatina11223340"
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.users.get(user_id="mooslyaka")
    print(response)


if __name__ == '__main__':
    main()
