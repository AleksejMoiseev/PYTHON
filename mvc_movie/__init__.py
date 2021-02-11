import yaml


class Actor:

    def __init__(self, name, last_name, role):
        self.__name = name
        self.__last_name = last_name
        self.__role = role

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, val):
        self.__last_name = val

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    def __str__(self):
        return f" Actor: name {self.name}, last_name {self.last_name} in role {self.role}"

    def __repr__(self):
        return "{'name': self.name, 'last_name': self.last_name, 'role': self.role}"

    def return_dict(self):
        data_dict = {'name': self.name, 'last_name': self.last_name, 'role': self.role}
        return data_dict

    def to_yml(self):
        with open("movies.dump", "wt") as file:
            data_to_yml = self.return_dict()
            yaml.dump(data=data_to_yml, stream=file)

    @classmethod
    def from_yml(cls):
        with open("movies.dump", "rt") as file:
            str_obj = yaml.safe_load(file)
            return cls(**str_obj)




class Movie:

    def __init__(self, title, date_realized, actor):
        self.title = title
        self.date_realized = date_realized
        self.actor = actor

    def __str__(self):
        movie_str = f" Film_title:  {self.title}" + "\n " + f"realized: -  {self.date_realized}\n Actors:  \n"
        for act in self.actor:
            movie_str = movie_str + str(act) + "\n"
        return movie_str

    def list_of_actors_transfer_in_dict(self):
        list_actors_in_dict = []
        for act in self.actor:
            list_actors_in_dict.append(act.return_dict())
        return list_actors_in_dict


    def to_yml(self):
        with open("movies.dump", "wt") as file:
            data_to_yml = {
                "title": self.title,
                "date_realized": self.date_realized,
                "actor": self.list_of_actors_transfer_in_dict()
            }
            yaml.dump(data=data_to_yml, stream=file)

    @classmethod
    def from_yml(cls):
        with open("movies.dump", "rt") as file:
            str_obj = yaml.safe_load(file)
            for act in str_obj["actor"]:
                act = Actor(**act)
                print(act)
            return str_obj["actor"]



if __name__ == '__main__':
    actor = Actor(name="Peter", last_name="First", role="King")
    peter = [
        Actor(name="Peter", last_name="First", role="main_Hero"),
        Actor(name="Kira", last_name="Knightley", role="Joan Clarke"),
        Actor(name="Benedict", last_name="Cumberbatch", role="Alan Turing")
    ]
    movie1 = Movie(title="First Peter", date_realized=2020, actor=peter)
    # print(movie1.list_of_actors_transfer_in_dict())
    movie1.to_yml()
    print(movie1.from_yml())