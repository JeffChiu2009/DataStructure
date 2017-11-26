#!python

from strings import contains, index_of, find_all_indexes
import unittest


class StringsTest(unittest.TestCase):

    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        # assert contains('abc', '') is True  # all strings contain empty string
        assert contains('abc', 'a') is True  # single letters are easy
        assert contains('abc', 'b') is True
        assert contains('abc', 'c') is True
        assert contains('abc', 'ab') is True  # multiple letters are harder
        assert contains('abc', 'bc') is True
        assert contains('abc', 'abc') is True  # all strings contain themselves
        assert contains('aaa', 'a') is True  # multiple occurrences
        assert contains('aaa', 'aa') is True  # overlapping pattern


    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains('abc', 'z') is False  # remember to test other letters
        assert contains('abc', 'ac') is False  # important to test close cases
        assert contains('abc', 'az') is False  # first letter, but not last
        assert contains('abc', 'abz') is False  # first 2 letters, but not last


    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains('ababc', 'ab') is True  # multiple occurrences
        assert contains('banana', 'na') is True  # multiple occurrences
        assert contains('ababc', 'abc') is True  # overlapping prefix
        assert contains('bananas', 'nas') is True  # overlapping prefix
        assert contains('bananas', 'bananas') is True  # overlapping prefix

    def test_index_of_with_matching_patterns(self):
        assert index_of('abc', '') == 0  # all strings contain empty string
        assert index_of('abc', 'a') == 0  # single letters are easy
        assert index_of('abc', 'b') == 1
        assert index_of('abc', 'c') == 2
        assert index_of('abc', 'ab') == 0  # multiple letters are harder
        assert index_of('abc', 'bc') == 1
        assert index_of('abc', 'abc') == 0  # all strings contain themselves
        assert index_of('aaa', 'a') == 0  # multiple occurrences
        assert index_of('aaa', 'aa') == 0  # overlapping pattern
        assert index_of('thisisabsolutelycrazy', 't') == 0
        assert index_of('abcdef', 'abcdef') == 0  # all strings contain
        assert index_of('abcdef', 'abcdef') == 0  # all strings contain
        assert index_of('aaaaaab', 'aaab') ==3 # really tricky cases
        
    def test_index_of_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert index_of('abc', 'z') is None  # remember to test other letters
        assert index_of('abc', 'ac') is None  # important to test close cases
        assert index_of('abc', 'az') is None  # first letter, but not last
        assert index_of('abc', 'abz') is None  # first 2 letters, but not last


    def test_index_of_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert index_of('ababc', 'abc') == 2  # overlapping prefix
        assert index_of('bananas', 'nas') == 4  # overlapping prefix
        assert index_of('abcabcabc', 'abc') == 0  # multiple occurrences
        assert index_of('abcabcab', 'abc') == 0  # multiple occurrences
        assert index_of('abcabcdef', 'abcd') == 3  # overlapping prefix
        assert index_of('abcabcdef', 'abcdef') == 3  # overlapping prefix
        assert index_of('abcabcdabcde', 'abcde') == 7  # overlapping prefix
        assert index_of('abcabcdabcde', 'abcd') == 3  # multiple occurrences, overlapping prefix
        assert index_of('abra cadabra', 'abra') == 0  # multiple occurrences
        assert index_of('abra cadabra', 'adab') == 6  # overlapping prefix

    def test_find_all_indexes_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_all_indexes('abc', '') == [0, 1, 2]  # all strings contain empty string
        assert find_all_indexes('abc', 'a') == [0]  # single letters are easy
        assert find_all_indexes('abc', 'b') == [1]
        assert find_all_indexes('abc', 'c') == [2]
        assert find_all_indexes('abc', 'ab') == [0]  # multiple letters are harder
        assert find_all_indexes('abc', 'bc') == [1]
        assert find_all_indexes('abc', 'abc') == [0]  # all strings contain themselves
        assert find_all_indexes('aaa', 'a') == [0, 1, 2]  # multiple occurrences
        assert find_all_indexes('aaa', 'aa') == [0, 1]  # overlapping pattern
        # TODO: Write more positive test cases with assert equal list statements
        # ...

    def test_find_all_indexes_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_all_indexes('abc', 'z') == []  # remember to test other letters
        assert find_all_indexes('abc', 'ac') == []  # important to test close cases
        assert find_all_indexes('abc', 'az') == []  # first letter, but not last
        assert find_all_indexes('abc', 'abz') == []  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert equal list statements
        # ...

    def test_find_all_indexes_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indexes('ababc', 'abc') == [2]  # overlapping prefix
        assert find_all_indexes('bananas', 'nas') == [4]  # overlapping prefix
        assert find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences
        assert find_all_indexes('abcabcab', 'abc') == [0, 3]  # multiple occurrences
        assert find_all_indexes('abcabcdef', 'abcd') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdef', 'abcdef') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcde') == [7]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcd') == [3, 7]  # multiple occurrences, overlapping prefix
        assert find_all_indexes('abra cadabra', 'abra') == [0, 8]  # multiple occurrences
        assert find_all_indexes('abra cadabra', 'adab') == [6]  # overlapping prefix



if __name__ == '__main__':
    unittest.main()
