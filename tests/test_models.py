from datashedder.models import Person


class TestPerson:
    def test_person_unique_if_all_attributes_match(self):
        a = Person('foo', 'bar', '03/12/1991', 'f')
        b = Person('foo', 'bar', '03/12/1991', 'f')

        unique = {a, b}
        assert len(unique) == 1

    def test_person_distinct_if_any_attributes_not_match(self):
        a = Person('foo', 'bar', '03/12/1991', 'f')
        b = Person('foo', 'bar', '03/12/1991', 'm')

        unique = {a, b}
        assert len(unique) == 2

    def test_person_full_name_combines_given_and_surname(self):
        sut = Person('foo', 'bar', '03/12/1991', 'f')
        assert sut.full_name == 'foo bar'
