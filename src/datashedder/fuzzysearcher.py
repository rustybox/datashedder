import Levenshtein


class FuzzySearcher:
    def __init__(self, tolerance):
        self.tolerance = tolerance

    @staticmethod
    def distance(a, b):
        return Levenshtein.distance(a,b)

    def is_duplicate(self, all, new):
        for person in all:
            if FuzzySearcher.distance(person.full_name, new.full_name) <= self.tolerance:
                return True

        return False
