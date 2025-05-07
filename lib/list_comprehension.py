#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if not n % 2]

def make_exclamation(sentence_list):
    return [f"{str}!" for str in sentence_list]