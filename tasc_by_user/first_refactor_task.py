from tasc_by_user.utils import get_users_info
from tasc_by_user.models import User


def main():
    #users = get_users_info()
    users = ["Alex 21 alex@21.ru", "MAlex 211 malex@211.ru"]
    keys = ("name", "age", "email")
    actors = []
    for user in users:
        user_params = tuple(user.split())
        params = dict(zip(("name", "age", "email"), user_params))
        actors.append(User(**params))

    return sorted(actors, key=lambda u: u.age, reverse=True)


if __name__ == '__main__':
    print(main())

