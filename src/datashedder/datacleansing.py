from .models import Results


class DataCleanser:
    def __init__(self, datasource, fuzzy_searcher, duplicate_logger):
        self.datasource = datasource
        self.fuzzy = fuzzy_searcher
        self.duplicate_logger = duplicate_logger

    def process(self):
        uniques = set()
        total = 0
        exact_duplicates = 0
        fuzzy_duplicates = 0

        for record in self.datasource:
            total += 1

            (line, person) = record

            if person in uniques:
                exact_duplicates += 1
                self.duplicate_logger.log_duplicate(record, False)
                continue

            if self.fuzzy.is_duplicate(uniques, person):
                fuzzy_duplicates += 1
                self.duplicate_logger.log_duplicate(record, True)
                continue


            uniques.add(person)

        return Results(
            total=total,
            unique=total-exact_duplicates,
            different=len(uniques)
        )
