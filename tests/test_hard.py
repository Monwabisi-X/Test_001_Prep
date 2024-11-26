import unittest
import inspect
from student_code_hard import *

class TestUsingImports(unittest.TestCase):
    def test_using_imports(self):
        with open('student_code.py', 'r') as file:
            contents = file.read()
        if 'import' in contents:
            self.fail('Source file should not make use of imports')

class TestPerformanceEvaluation(unittest.TestCase):
    def test_performance_evaluation_pass(self):
        self.min_passing_grade = 75
        if 'sum' in evaluate_performance.__code__.co_names or 'len' in evaluate_performance.__code__.co_names:
            self.fail("Function evaluate_perfomance should not use sum() or len().")
        self.assertEqual(evaluate_performance([80, 70, 90], self.min_passing_grade), "Pass", "Performance evaluation failed for passing case.")

    def test_performance_evaluation_fail(self):
        if 'sum' in evaluate_performance.__code__.co_names or 'len' in evaluate_performance.__code__.co_names:
            self.fail("Function evaluate_perfomance should not use sum() or len().")
        self.min_passing_grade = 75
        self.assertEqual(evaluate_performance([60, 70, 50], self.min_passing_grade), "Fail", "Performance evaluation failed for failing case.")


class TestCumulativePerformance(unittest.TestCase):
    def test_cumulative_performance(self):
        scores = {"Math": 65, "English": 85, "Science": 50}
        expected_output = {"average": 66.67, "below_average": ["Math", "Science"]}
        if 'sum' in calculate_cumulative_performance.__code__.co_names or 'len' in calculate_cumulative_performance.__code__.co_names:
            self.fail("Function calculate_cumulative_performance should not use sum() or len().")
        self.assertEqual(calculate_cumulative_performance(scores), expected_output, "Cumulative performance calculation failed.")

class TestClassRanking(unittest.TestCase):
    def test_class_ranking(self):
        students = [("Alice", 85), ("Bob", 70), ("Charlie", 90)]
        expected_output = [("Charlie", 90), ("Alice", 85), ("Bob", 70)]
        result = rank_students(students)
        if 'sorted' in rank_students.__code__.co_names or 'sort' in rank_students.__code__.co_names:
            self.fail("Function rank_students should not use sorted() or sort().")
        self.assertEqual(result, expected_output, "Class ranking failed.")

class TestLoopWithConditions(unittest.TestCase):
    def test_return_even_numbers(self):
        if '%' in inspect.getsource(even_numbers):
            self.fail("Function even_numbers should not use %.")
        self.assertEqual(even_numbers(20), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], "Even numbers from 1 to 20 failed.")

    def test_print_odd_numbers(self):
        if '%' in inspect.getsource(odd_numbers):
            self.fail("Function odd_numbers should not use %.")
        self.assertEqual(odd_numbers(20), [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], "Odd numbers from 1 to 20 failed.")


class TestLoopWithInput(unittest.TestCase):
    def test_read_numbers_until_zero(self):
        input_numbers = [1, 2, 3, 0]
        if 'sum' in sum_numbers_until_zero.__code__.co_names:
            self.fail("Function sum_numbers_until_zero should not use sum.")
        self.assertEqual(sum_numbers_until_zero(input_numbers), 6, "Summing numbers until 0 failed.")


class TestLoopWithCollections(unittest.TestCase):
    def test_sum_dictionary_values(self):
        dict_values = {'a': 1, 'b': 2, 'c': 3}
        if 'sum' in sum_dictionary_values.__code__.co_names:
            self.fail("Function sum_dictionary_values should not use sum.")
        self.assertEqual(sum_dictionary_values(dict_values), 6, "Summing values in a dictionary failed.")

    def test_sum_unique_elements(self):
        elements = [1, 2, 2, 3]
        if 'set' in sum_unique_elements.__code__.co_names or 'sum' in sum_unique_elements.__code__.co_names:
            self.fail("Function sum_unique_elements should not use set or sum.")
        self.assertEqual(sum_unique_elements(elements), 6, "Summing unique elements failed.")

class TestSpecialUseOfControlStatements(unittest.TestCase):
    def test_skip_divisible_by_num(self):
        if '%' in inspect.getsource(skip_divisible_by_num):
            self.fail("Function skip_divisible_by_num should not use %.")
        self.assertEqual(skip_divisible_by_num(3, 20), [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20], "Skipping numbers divisible by 3 failed.")
        self.assertEqual(skip_divisible_by_num(5, 15), [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14], "Skipping numbers divisible by 5 failed.")
        self.assertEqual(skip_divisible_by_num(6, 15), [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15], "Skipping numbers divisible by 6 failed.")


class InputTransformation(unittest.TestCase):
    def test_transform_string(self):
        text = 'hello, world'
        transform = ['Uppercase', 'Capitalize', 'Lowercase']
        
        result = transform_string(text, transform[0])
        if 'upper' in transform_string.__code__.co_names:
            self.fail("Function transform_string should not use upper().")
        self.assertEqual(result, 'HELLO, WORLD', "Uppercase transformation test failed.")
        
        result = transform_string(text, transform[1])
        if 'capitalize' in transform_string.__code__.co_names:
            self.fail("Function transform_string should not use capitalize().")
        self.assertEqual(result, 'Hello, world', "Capitalize transformation test failed.")
        
        result = transform_string(text, transform[2])
        if 'lower' in transform_string.__code__.co_names:
            self.fail("Function transform_string should not use lower().")
        self.assertEqual(result, text, "Lowercase transformation test failed.")

class DataAggregation(unittest.TestCase):
    def test_sum_and_average(self):
        numbers = [5, 15, 25]
        if 'len' in sum_and_average.__code__.co_names or 'sum' in sum_and_average.__code__.co_names:
            self.fail("Function sum_and_average should not use len() or sum().")
        total, average = sum_and_average(numbers)
        self.assertEqual(total, 45, "Sum test failed.")
        self.assertEqual(average, 15.0, "Average test failed.")

    def test_word_frequency_count(self):
        words = ['cat', 'dog', 'dog']
        frequency = word_frequency_count(words)
        if 'set' in word_frequency_count.__code__.co_names or '.count' in word_frequency_count.__code__.co_names:
            self.fail("Function word_frequency_count should not use set or .count.")
        self.assertEqual(frequency, {'cat': 1, 'dog': 2}, "Word frequency count test failed.")

class DataFiltering(unittest.TestCase):
    def test_filter_even_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        if '%' in inspect.getsource(filter_even_numbers):
            self.fail("Function filter_even_numbers should not use %.")
        evens = filter_even_numbers(numbers)
        self.assertEqual(evens, [2, 4, 6, 8], "Filter even numbers test failed.")


class TestSimpleAlgorithms(unittest.TestCase):
    def test_find_median_unsorted(self):
        if 'sort' in find_median.__code__.co_names or 'sorted' in find_median.__code__.co_names:
            self.fail("Function find_median should not use sort or sorted.")
        self.assertEqual(find_median([7, 3, 1, 5]), 4, "Unsorted list test failed.")

    def test_find_median_decimal(self):
        if 'sort' in find_median.__code__.co_names or 'sorted' in find_median.__code__.co_names:
            self.fail("Function find_median should not use sort or sorted.")
        self.assertEqual(find_median([1.5, 3.5, 2.5]), 2.5, "Decimal numbers test failed.")


class TestBasicProblemSolving(unittest.TestCase):
    def test_reverse_string(self):
        if 'sorted' in reverse_string.__code__.co_names or 'sort' in reverse_string.__code__.co_names or '[::-1]' in inspect.getsource(reverse_string):
            self.fail("Function reverse_string should not use sorted, sort, or [::-1].")
        self.assertEqual(reverse_string("hello"), "olleh", "Reverse string test failed.")
        self.assertEqual(reverse_string("hello, world"), "dlrow ,olleh", "Reverse string 'hello, world' test failed.")

    def test_find_largest_number(self):
        if 'max' in largest_number.__code__.co_names:
            self.fail("Function largest_number should not use max().")
        self.assertEqual(largest_number([4, 2, 9, 7]), 9, "Find largest number test failed.")

    def test_count_character_occurrences(self):
        if 'count' in count_character_occurrences.__code__.co_names:
            self.fail("Function count_character_occurrences should not use .count.")
        self.assertEqual(count_character_occurrences("banana", "a"), 3, "Count character occurrences test failed.")

if __name__ == "__main__":
    unittest.main()
