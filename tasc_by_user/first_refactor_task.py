from tasc_by_user.models import User

keys = ("name", "age", "email")


def main():
    actors = ["Alex 21 alex@21.ru", "MAlex 211 malex@211.ru", "KAlex 45 malex@er.ru"]
    if not actors:
        return "List is empty"
    old_user = User(name='default', age=0, email='default')
    for actor in actors:
        user = User.serializer(actor)
        if user > old_user:
            old_user = user
    if not old_user:
        return f'Oldest user - None'
    return f'Oldest user - {old_user}'


if __name__ == '__main__':
    print(main())