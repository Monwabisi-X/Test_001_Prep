"""Learning Outcome: Functions"""
def sum_of_squares(n: int):
    """
    Calculate the sum of the squares of all integers from 1 to n.

    Parameters:
    n (int): A non-negative integer up to which the squares will be summed.

    Returns:
    int: The sum of the squares of all integers from 1 to n.

    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return sum(i ** 2 for i in range(1, n + 1))

def evaluate_performance(grades: list, min_pass: int):
    """
    Evaluate the performance based on a list of grades and a minimum passing grade.

    Parameters:
    grades (list): A list of integers representing student grades.
    min_pass (int): The minimum average grade required to pass.

    Returns:
    str: "Pass" if the average grade is greater than or equal to min_pass, otherwise "Fail".
    """
    average = sum(grades) / len(grades)  
    return "Pass" if average >= min_pass else "Fail"

def calculate_cumulative_performance(scores: dict):
    """
    Calculate the cumulative performance based on student scores.

    Parameters:
    scores (dict): A dictionary where keys are subject names and values are the corresponding scores.

    Returns:
    dict: A dictionary containing the average score and a list of subjects where the score is below average.
    """
    average = sum(scores.values()) / len(scores)
    return {"average": round(average, 2), "below_average": [key for key, val in scores.items() if val < average]}

def analyze_improvement(scores: list):
    """
    Analyze the improvement trend based on a list of scores.

    Parameters:
    scores (list): A list of integers representing scores over time.

    Returns:
    dict: A dictionary containing the trend of improvement ("positive", "negative", or "neutral") 
          and a boolean indicating whether there has been an improvement.
    """
    trend = "positive" if scores[-1] > scores[0] else "negative" if scores[-1] < scores[0] else "neutral"
    improved = scores[-1] > scores[0]
    return {"trend": trend, "improved": improved}

def rank_students(students: list[tuple[str, int]]):
    """
    Rank students based on their scores.

    Parameters:
    students (list): A list of tuples where each tuple contains a student's name and their score.

    Returns:
    list: A sorted list of tuples in descending order based on scores.
    """
    return sorted(students, key=lambda x: x[1], reverse=True)

"""Learning Outcome: Basic Loops"""
def even_numbers(n: int):
    """
    Generate a list of even numbers from 1 to n.

    Parameters:
    n (int): The upper limit for generating even numbers.

    Returns:
    list: A list of even integers from 1 to n.
    """
    return [i for i in range(1, n + 1) if i % 2 == 0]

def odd_numbers(n: int):
    """
    Generate a list of odd numbers from 1 to n.

    Parameters:
    n (int): The upper limit for generating odd numbers.

    Returns:
    list: A list of odd integers from 1 to n.
    """
    return [i for i in range(1, n + 1) if i % 2 != 0]

def sum_multiples_of_num(num: int, length: int):
    """
    Calculate the sum of multiples of a given number up to a specified length.

    Parameters:
    num (int): The number whose multiples are to be summed.
    length (int): The upper limit for the range of multiples.

    Returns:
    int: The sum of multiples of num from 1 to length.
    """
    return sum([x * num for x in range(length + 1)])

def skip_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping a specific number.

    Parameters:
    n (int): The number to skip.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n.
    """
    return [x for x in range(1, length + 1) if x != n]

def break_test(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, stopping when a specific number is encountered.

    Parameters:
    n (int): The number at which to stop adding to the list.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n and stopping before it.
    """
    list_ = []
    for x in range(1, length + 1):
        if x == n:
            break
        list_.append(x)
    return list_

def sum_numbers_until_zero(nums: list):
    """
    Calculate the sum of numbers in a list until a zero is encountered.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The sum of integers in the list up to (but not including) the first zero.
    """
    return sum(nums[:nums.index(0)])

def count_positive_numbers(nums: list):
    """
    Count the number of positive integers in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The count of positive integers in the list.
    """
    return len([x for x in nums if x > 0])

def sum_dictionary_values(dictionary: dict):
    """
    Calculate the sum of all values in a dictionary.

    Parameters:
    dictionary (dict): A dictionary with numeric values.

    Returns:
    int: The sum of all values in the dictionary.
    """
    return sum(x for x in dictionary.values())

def sum_unique_elements(elements: list):
    """
    Calculate the sum of unique elements in a list.

    Parameters:
    elements (list): A list of integers.

    Returns:
    int: The sum of unique integers in the list.
    """
    return sum(x for x in set(elements))

def skip_divisible_by_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping those that are divisible by a specific number.

    Parameters:
    n (int): The number to skip multiples of.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding those divisible by n.
    """
    return [x for x in range(1, length + 1) if x % n != 0]

"""Learning Outcome: Processing Data"""

def square_numbers(nums: list):
    """
    Calculate the square of each number in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    list: A list containing the squares of the input integers.
    """
    return [x ** 2 for x in nums]

def transform_string(input: str, transform: str):
    """
    Transform a string based on the specified transformation type.

    Parameters:
    input (str): The string to be transformed.
    transform (str): The type of transformation ('capitalize', 'upper', 'lower').

    Returns:
    str: The transformed string.

    Raises:
    ValueError: If the transformation type is unknown.
    """
    if transform.lower() == "capitalize":
        return input.capitalize()
    elif transform.lower() == "uppercase":
        return input.upper()
    elif transform.lower() == "lowercase":
        return input.lower()
    else:
        raise ValueError("Unknown transform: {}".format(transform))
    
def sum_and_average(nums: list[int]):
    """
    Calculate the sum and average of a list of numbers.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    tuple: A tuple containing the sum and average of the numbers.
    """
    return (sum(x for x in nums), sum(nums) / len(nums))

def word_frequency_count(words: list[str]):
    """
    Count the frequency of each word in a list.

    Parameters:
    words (list[str]): A list of words.

    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    return {word: words.count(word) for word in set(words)}

def filter_even_numbers(nums: list[int]):
    """
    Filter out even numbers from a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    list: A list containing only the even integers from the input list.
    """
    return [x for x in nums if x % 2 == 0]

"""Learning Outcome: Simple Algorithms(Problem Solving)"""

def find_median(nums: list[int]):
    if not nums:
        raise ValueError("The list cannot be empty.")
    
    nums.sort()
    mid = len(nums) // 2
    return (nums[mid] + nums[mid - 1]) / 2 if len(nums) % 2 == 0 else nums[mid]

def reverse_string(input: str):
    return input[::-1]

def largest_number(nums: list[int]):
    return max(nums)

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_character_occurrences(word_sentence: str, char_count: str):
    return word_sentence.count(char_count)