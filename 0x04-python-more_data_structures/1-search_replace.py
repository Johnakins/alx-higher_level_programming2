#!/usr/bin/python3
def search_replace(my_list, find, change):
    n_list = list(map(lambda x: change if x == find else x, my_list))
    return (n_list)
