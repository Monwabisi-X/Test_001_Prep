import unittest
from student_code import *

class TestSumOfSquares(unittest.TestCase):
    def test_sum_of_squares_basic(self):
        self.assertEqual(sum_of_squares(3), 14, "Basic test failed: sum_of_squares(3)")

    def test_sum_of_squares_edge(self):
        self.assertEqual(sum_of_squares(0), 0, "Edge case failed: sum_of_squares(0)")

    def test_sum_of_squares_large(self):
        self.assertEqual(sum_of_squares(100), 338350, "Large input test failed.")

    def test_sum_of_squares_negative(self):
        with self.assertRaises(ValueError):
            sum_of_squares(-5)

class TestPerformanceEvaluation(unittest.TestCase):
    def test_performance_evaluation_pass(self):
        min_passing_grade = 75
        self.assertEqual(evaluate_performance([80, 70, 90], min_passing_grade), "Pass", "Performance evaluation failed for passing case.")

    def test_performance_evaluation_fail(self):
        min_passing_grade = 75
        self.assertEqual(evaluate_performance([60, 70, 50], min_passing_grade), "Fail", "Performance evaluation failed for failing case.")


class TestCumulativePerformance(unittest.TestCase):
    def test_cumulative_performance(self):
        scores = {"Math": 65, "English": 85, "Science": 50}
        expected_output = {"average": 66.67, "below_average": ["Math", "Science"]}
        self.assertEqual(calculate_cumulative_performance(scores), expected_output, "Cumulative performance calculation failed.")

class TestImprovementOverTime(unittest.TestCase):
    def test_improvement_over_time(self):
        scores = [50, 55, 70, 85]
        expected_output = {"trend": "positive", "improved": True}
        self.assertEqual(analyze_improvement(scores), expected_output, "Improvement analysis failed.")

class TestClassRanking(unittest.TestCase):
    def test_class_ranking(self):
        students = [("Alice", 85), ("Bob", 70), ("Charlie", 90)]
        expected_output = [("Charlie", 90), ("Alice", 85), ("Bob", 70)]
        self.assertEqual(rank_students(students), expected_output, "Class ranking failed.")

class TestLoopWithConditions(unittest.TestCase):
    def test_return_even_numbers(self):
        self.assertEqual(even_numbers(20), [2,4,6,8,10,12,14,16,18,20], "Even numbers from 1 to 20 failed.")

    def test_print_odd_numbers(self):
        self.assertEqual(odd_numbers(20), [1,3,5,7,9,11,13,15,17,19], "Odd numbers from 1 to 20 failed.")

    def test_sum_multiples_of_num(self):
        self.assertEqual(sum_multiples_of_num(3, 10), 165, "Sum of multiples of 3 between 1 and 50 failed.")
        self.assertEqual(sum_multiples_of_num(5, 10), 275, "Sum of multiples of 5 between 1 and 10 failed.")
        self.assertEqual(sum_multiples_of_num(8, 10), 440, "Sum of multiples of 8 between 1 and 10 failed.")
    
    def test_skip_specific_value(self):
        self.assertEqual(skip_num(5,10), [1, 2, 3, 4, 6, 7, 8, 9, 10], "Skipping 5 in loop from 1 to 10 failed.")
        self.assertEqual(skip_num(7,10), [1, 2, 3, 4, 5, 6, 8, 9, 10], "Skipping 5 in loop from 1 to 10 failed.")
        self.assertEqual(skip_num(3,10), [1, 2, 4, 5, 6, 7, 8, 9, 10], "Skipping 5 in loop from 1 to 10 failed.")

class TestLoopTermination(unittest.TestCase):
    def test_break_on_specific_value(self):
        self.assertEqual(break_test(5, 10), [1, 2, 3, 4], "Loop termination on specific value failed.")

class TestLoopWithInput(unittest.TestCase):
    def test_read_numbers_until_zero(self):
        input_numbers = [1, 2, 3, 0]
        self.assertEqual(sum_numbers_until_zero(input_numbers), 6, "Summing numbers until 0 failed.")

    def test_count_positive_numbers(self):
        self.assertEqual(count_positive_numbers([-1, 2, 3, -4, 5]), 3, "Counting positive numbers failed.")

class TestLoopWithCollections(unittest.TestCase):
    def test_sum_dictionary_values(self):
        dict_values = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(sum_dictionary_values(dict_values), 6, "Summing values in a dictionary failed.")

    def test_sum_unique_elements(self):
        elements = [1, 2, 2, 3]
        self.assertEqual(sum_unique_elements(elements), 6, "Summing unique elements failed.")

class TestSpecialUseOfControlStatements(unittest.TestCase):
    def test_skip_divisible_by_num(self):
        self.assertEqual(skip_divisible_by_num(3, 20), [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20], "Skipping numbers divisible by 3 failed.")
        self.assertEqual(skip_divisible_by_num(5, 15), [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14], "Skipping numbers divisible by 5 failed.")
        self.assertEqual(skip_divisible_by_num(6, 15), [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15], "Skipping numbers divisible by 6 failed.")

class SimpleDataProcessing(unittest.TestCase):
    def test_square_numbers(self):
        numbers = [1, 2, 3]
        self.assertEqual(square_numbers(numbers), [1, 4, 9], "Square numbers test failed.")

class InputTransformation(unittest.TestCase):
    def test_transform_string(self):
        text = 'hello, world'
        transform = ['Uppercase', 'Capitalize', 'Lowercase']
        self.assertEqual(transform_string(text, transform[0]), 'HELLO, WORLD', "Uppercase transformation test failed.")
        self.assertEqual(transform_string(text, transform[1]), 'Hello, world', "Capitalize transformation test failed.")
        self.assertEqual(transform_string(text, transform[2]), text, "Lowercase transformation test failed.")

class DataAggregation(unittest.TestCase):
    def test_sum_and_average(self):
        numbers = [5, 15, 25]
        total, average = sum_and_average(numbers)
        self.assertEqual(total, 45, "Sum test failed.")
        self.assertEqual(average, 15.0, "Average test failed.")

    def test_word_frequency_count(self):
        words = ['cat', 'dog', 'dog']
        frequency = word_frequency_count(words)
        self.assertEqual(frequency, {'cat': 1, 'dog': 2}, "Word frequency count test failed.")

class DataFiltering(unittest.TestCase):
    def test_filter_even_numbers(self):
        numbers = [1, 2, 3, 4]
        evens = filter_even_numbers(numbers)
        self.assertEqual(evens, [2, 4], "Filter even numbers test failed.")


class TestSimpleAlgorithms(unittest.TestCase):
    def test_find_median_odd_length(self):
        self.assertEqual(find_median([1, 3, 5]), 3, "Odd length test failed.")

    def test_find_median_unsorted(self):
        self.assertEqual(find_median([7, 3, 1, 5]), 4, "Unsorted list test failed.")

    def test_find_median_empty_list(self):
        with self.assertRaises(ValueError):
            find_median([])

    def test_find_median_duplicates(self):
        self.assertEqual(find_median([1, 1, 1]), 1, "Duplicate values test failed.")

    def test_find_median_non_integer(self):
        with self.assertRaises(TypeError):
            find_median(["a", 1])

    def test_find_median_large_input(self):
        self.assertEqual(find_median(list(range(1, 10**6 + 1))), 500000.5, "Large input test failed.")

    def test_find_median_decimal(self):
        self.assertEqual(find_median([1.5, 3.5, 2.5]), 2.5, "Decimal numbers test failed.")

class TestBasicProblemSolving(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh", "Reverse string test failed.")

    def test_find_largest_number(self):
        self.assertEqual(largest_number([4, 2, 9, 7]), 9, "Find largest number test failed.")

    def test_is_prime(self):
        self.assertTrue(is_prime(29), "Check if number is prime test failed.")

    def test_count_character_occurrences(self):
        self.assertEqual(count_character_occurrences("banana", "a"), 3, "Count character occurrences test failed.")

if __name__ == "__main__":
    unittest.main()
