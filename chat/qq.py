from pydantic import BaseModel


class Model(BaseModel):
    pk: int = None


class User(Model):
    username: str
    email: str
    password: str
    access_token: str = None
    refresh_token: str = None


if __name__ == '__main__':
    u = User(username='aaa', email='ssss', password='ssss')
    print(u.username)
