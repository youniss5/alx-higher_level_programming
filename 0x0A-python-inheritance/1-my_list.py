#!/usr/bin/python3
'''Mylist class method'''


class MyList(list):
    '''my list class to print sorted list'''
    def print_sorted(self):
        '''method to print sorted list'''
        print(sorted(self))
