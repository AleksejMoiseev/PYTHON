def get_users_info() -> list[str]:
    """
    Функция, которую трогать не нужно, это некая абстракция получения
    данных из внешнего источника. Считаем что отсюда всегда приходят
    корректные данные, но возможно, что это будет пустой список
    """

    users_amount = int(input('Enter users amount: '))
    users_info: list[str] = [
        input('Enter user info in format {name} {age} {email}: ') for _ in range(users_amount)
    ]
    return users_info


def main():
    users_info: list[str] = get_users_info()

    # Преобразовываем массив строк в массив объектов пользователей
    users: list[tuple] = []
    for user_info in users_info:
        user_name = user_info.split()[0]
        user_age = int(user_info.split()[1])
        user_email = user_info.split()[2]
        users.append((user_name, user_age, user_email))

    # Проходим по пользователям и узнаем кто самый старший
    oldest_user = users[0]
    for user in users:
        is_oldest = True
        for another_user in users:
            if user[1] < another_user[1]:
                is_oldest = False
        if is_oldest:
            oldest_user = user

    print(f'Oldest user {oldest_user[0]}, age {oldest_user[1]}, email {oldest_user[2]}')


if __name__ == '__main__':
    main()