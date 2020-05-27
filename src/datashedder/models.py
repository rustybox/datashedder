import collections


Record = collections.namedtuple('Record', 'line_num person')
Results = collections.namedtuple('Results', 'total unique different')


class Person:
    def __init__(self, given_name, surname, dob, sex):
        self.given_name = given_name
        self.surname = surname
        self.dob = dob
        self.sex = sex

    @property
    def full_name(self):
        return f'{self.given_name} {self.surname}'

    def __repr__(self):
        props = (self.given_name, self.surname, self.dob, self.sex)
        return 'Person({!r},{!r},{!r},{!r})'.format(*props)

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            repr(self) == repr(other)
        )
