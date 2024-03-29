# CPE 202 Project 4
# Name: Ashley Sutter
# Student ID: 011278952
# Date (last modified): 3/4/2019
#
# Project 4
# Section 5
# Purpose: Create a concordance using a heap
# additional comments
 
from hash_quad import *
import string
import os.path
from os import path

class Concordance:

    def __init__(self, capacity = 191):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        if path.exists(filename) == False:
            raise FileNotFoundError
        f = open(filename, 'r')
        stopwords = f.read().split()
        for i in range(len(stopwords)):
            self.stop_table[i+1] = stopwords[i]
        f.close()
        print (self.stop_table)

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        if path.exists(filename) == False:
            raise FileNotFoundError

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
