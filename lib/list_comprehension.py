#!/usr/bin/env python3

def return_evens(num_list):
    for n in range(len(num_list)):
        if num_list[n] % 2 == 0:
            return num_list[n]
    return []

def make_exclamation(sentence_list):
    for i in range(len(sentence_list)):
        sentence_list[i] += '!'
    return sentence_list
