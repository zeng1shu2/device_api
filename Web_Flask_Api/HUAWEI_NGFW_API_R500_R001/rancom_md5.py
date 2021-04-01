# coding:utf-8:
import random
import hashlib


def stochastic_str():
    result = random.randint(600000, 9000000)
    result_str = str(result)
    return result_str


class Identification(object):
    password_str = '1'
    random_str = stochastic_str()
