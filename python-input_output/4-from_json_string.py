#!/usr/bin/python3
import json
""" Function that returns an object represented by a json string. """


def from_json_string(my_str):
    """ Return an object represented by a json string"""
    return json.loads(my_str)
