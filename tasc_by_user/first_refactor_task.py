from tasc_by_user.utils import serializer, sorted_users_by_age


keys = ("name", "age", "email")


def main():
    actors = ["Alex 21 alex@21.ru", "MAlex 211 malex@211.ru"]
    if not actors:
        return "List is empty"
    users = []
    for actor in actors:
        user = serializer(actor, keys)
        users.append(user)
    old_user = sorted_users_by_age(users)
    return f'Oldest user - {old_user}'


if __name__ == '__main__':
    print(main())