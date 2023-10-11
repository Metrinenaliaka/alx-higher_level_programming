#!/usr/bin/python3
def search_replace(my_list, search, replace):
    m_list = []
    for i in my_list:
        if i == search:
            m_list.append(replace)
        else:
            m_list.append(i)
    return m_list
