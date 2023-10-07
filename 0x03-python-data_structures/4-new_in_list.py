#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    m_list = my_list.copy()
    if idx < 0 or idx > length:
        return m_list
    m_list[idx] = element
    return m_list
