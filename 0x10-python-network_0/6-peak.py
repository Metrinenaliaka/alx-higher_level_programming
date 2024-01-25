#!/usr/bin/python3
'''find peak of unsorted list of ints'''


def find_peak(list_of_integers):
    """finds peak of a list"""
    if not list_of_integers:
        return

    end = len(list_of_integers) - 1
    # seaches from index zero to end
    return(peak(list_of_integers, 0, end))


def peak(list_int, low, high):
    """"recursive function that calculates peak"""

    # checks if only 1 variable given
    if low == high:
        return(list_int[high])
    mid = (high + low) // 2
    # checks if first half has the peak
    if list_int[mid] > list_int[mid + 1]:
        return(peak(list_int, low, mid))
    # if the peak is likely on the right half
    return(peak(list_int, mid + 1, high))
