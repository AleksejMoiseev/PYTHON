from typing import List, Tuple
from tasc_by_user.models import User


def get_users_info():
    users_amount = int(input('Enter users amount: '))
    users_info = [
        input('Enter user info in format {name} {age} {email}: ') for _ in range(users_amount)
    ]
    return users_info


def serializer(data: str, keys: Tuple):
    values = tuple(data.split())
    params = dict(zip(keys, values))
    return User(**params)


def sorted_users_by_age(actors: List, reverse=False)->User:
    users = sorted(actors, key=lambda u: u.age, reverse=reverse)
    return users.pop()
