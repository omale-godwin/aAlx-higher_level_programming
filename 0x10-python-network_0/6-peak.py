#!/usr/bin/python3
""" Function that finds a peak of unsorted integers. """


def find_peak(list_of_integers: list) -> int:
    """
    Finds a peak in a list of integers.

   

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int: The peak element in the list.

    """

    # If list is empty or None
    if not list_of_integers:
        return None

    # Get the middle index (if the list is even, use the left of the 2 middle
    list_len = len(list_of_integers)
    mid = (list_len // 2) - 1 if list_len % 2 == 0 else list_len // 2

    if list_len == 1:
        return list_of_integers[0]

    if list_len == 2:
        return max(list_of_integers)

    # If the middle element is larget than its neighbours, return it
    if (
        list_of_integers[mid - 1]
        <= list_of_integers[mid]
        >= list_of_integers[mid + 1]
    ):
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
