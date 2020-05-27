from datashedder.models import Person, Record
from datashedder.datacleansing import DataCleanser as sut


class TestDataCleanser:
    def test_report_all_unique(self, mocker):
        a = Record(1, Person('foo', 'bar', '03/12/1991', 'f'))
        b = Record(2, Person('baz', 'qux', '03/12/1991', 'f'))

        fuzz = mocker.MagicMock()
        fuzz.is_duplicate.return_value = False

        logger = mocker.MagicMock()

        results = sut([a,b], fuzz, logger).process()

        assert results.total == 2
        assert results.unique == 2
        assert results.different == 2

    def test_report_exact_matches(self, mocker):
        a = Record(1, Person('foo', 'bar', '03/12/1991', 'f'))
        b = Record(2, Person('foo', 'bar', '03/12/1991', 'f'))

        fuzz = mocker.MagicMock()
        fuzz.is_duplicate.return_value = False

        logger = mocker.MagicMock()

        results = sut([a,b], fuzz, logger).process()

        assert results.total == 2
        assert results.unique == 1
        assert results.different == 1

    def test_fuzzy_not_called_if_exact_match(self, mocker):
        a = Record(1, Person('foo', 'bar', '03/12/1991', 'f'))
        b = Record(2, Person('foo', 'bar', '03/12/1991', 'f'))
        c = Record(3, Person('foo', 'bar', '03/12/1991', 'f'))

        fuzz = mocker.MagicMock()
        fuzz.is_duplicate.return_value = False

        logger = mocker.MagicMock()

        results = sut([a,b,c], fuzz, logger).process()

        # One for first entry
        assert fuzz.is_duplicate.call_count == 1

    def test_report_fuzzy_matches(self, mocker):
        a = Record(1, Person('foo', 'bar', '03/12/1991', 'f'))
        b = Record(2, Person('baz', 'qux', '03/12/1991', 'f'))

        fuzz = mocker.MagicMock()
        fuzz.is_duplicate.side_effect = [False, True]

        logger = mocker.MagicMock()

        results = sut([a,b], fuzz, logger).process()

        assert results.total == 2
        assert results.unique == 2
        assert results.different == 1

    def test_fuzzy_called_if_not_exact_match(self, mocker):
        a = Record(1, Person('a', 'bar', '03/12/1991', 'f'))
        b = Record(2, Person('b', 'bar', '03/12/1991', 'f'))
        c = Record(3, Person('c', 'bar', '03/12/1991', 'f'))

        fuzz = mocker.MagicMock()
        fuzz.is_duplicate.return_value = False

        logger = mocker.MagicMock()

        results = sut([a,b,c], fuzz, logger).process()

        # One per record
        assert fuzz.is_duplicate.call_count == 3