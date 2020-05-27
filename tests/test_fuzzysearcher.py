from datashedder.fuzzysearcher import FuzzySearcher
from datashedder.models import Person

class TestExternalLib:
    def test_distance(self):
        """This is a garbage test, but meh makes me feel better"""
        a = FuzzySearcher.distance('foo', 'foo')
        assert a == 0

        b = FuzzySearcher.distance('foo', 'aoo')
        assert b == 1

        c = FuzzySearcher.distance('wilyam premadasta', 'william premadasa')
        assert c == 3

class TestFuzzySearcher:
    def test_is_duplicate_within_tolerance(self):
        a = Person('wilyam','premadasta','03/12/1991','f')
        b = Person('william','premadasa','03/12/1991','f')
        sut = FuzzySearcher(3)
        assert sut.is_duplicate([a], b)

    def test_is_duplicate_outside_tolerance(self):
        a = Person('wilyam','premadasta','03/12/1991','f')
        b = Person('william','premadasa','03/12/1991','f')
        sut = FuzzySearcher(2)
        assert not sut.is_duplicate([a], b)