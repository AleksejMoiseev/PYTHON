from dataclasses import dataclass


# Используем датакласс, так как класс необходим только для хранения данных
@dataclass
class User:
    name: str
    age: int
    email: str

    # Если где-то используется вывод данных в виде строки, то лучше всего определить логику его
    # отображения внутри класса, чтобы в дальнейшем менять ее в одном месте, а не искать по коду
    def __repr__(self):
        return f'{self.name}, age {self.age}, {self.email}'


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

    # Преобразовываем список строк в список объектов пользователей, можно
    # использовать однострочник с компрехеншеном, но будет слишком длинное выражение
    # для одной строки и такого лучше избегать
    users: list[User] = []
    for user_info in users_info:
        user_name, user_age, user_email = user_info.split()
        user = User(name=user_name, age=int(user_age), email=user_email)
        users.append(user)

    # Проверяем список на пустоту, чтобы не получить ошибку в дальнейшем
    if not users:
        print('No users')
        return

    # Делаем начальное значение самого старшего юзера
    oldest_user: User = users[0]

    # Проходимся по каждому юзеру и если его возраст больше текущего самого
    # старшего, то заменяем текущего самого старшего на этого юзера
    for user in users:
        if oldest_user.age < user.age:
            oldest_user = user

    print(f'Oldest user {oldest_user}')


if __name__ == '__main__':
    main()