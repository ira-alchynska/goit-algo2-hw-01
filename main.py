import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def find_min_max(arr):
    """
    Finds the minimum and maximum elements in an array using the "divide and conquer" method.

    Parameters:
    arr (list of numbers): input list of numbers of arbitrary length.

    Returns:
    tuple: (min_value, max_value)

    Algorithm complexity: O(n)
    """
    logging.debug(f"Processing array: {arr}")
    n = len(arr)
    if n == 0:
        raise ValueError("Array cannot be empty")
    # If one element
    if n == 1:
        logging.debug(f"Single element found: {arr[0]}")
        return arr[0], arr[0]
    # If two elements
    if n == 2:
        result = (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
        logging.debug(f"Two elements found: {arr}, result: {result}")
        return result

    # Recursive splitting
    mid = n // 2
    logging.debug(f"Splitting array: {arr[:mid]} and {arr[mid:]}")
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Combining results
    overall_min = left_min if left_min < right_min else right_min
    overall_max = left_max if left_max > right_max else right_max
    logging.debug(f"Combined results for {arr}: min={overall_min}, max={overall_max}")
    return overall_min, overall_max


# Usage examples
if __name__ == "__main__":
    example = [3, 1, 4, 1, 5, 9, 2, 6, 1]
    minimum, maximum = find_min_max(example)
    logging.info(f"Minimum: {minimum}, Maximum: {maximum}") 