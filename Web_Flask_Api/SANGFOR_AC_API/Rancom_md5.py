# coding:utf-8:
import random
import hashlib


def stochastic_str():
    result_str = random.randint(19999, 99999)
    return str(result_str)


class Identification(object):
    def __init__(self, password_str):
        self.password_str = password_str
        self.random_str = stochastic_str()
        self._id = str(self.password_str)+str(self.random_str)

    def md5_code(self):
        m = hashlib.md5(self._id.encode(encoding='utf-8'))
        random_str = self.random_str
        return random_str, m.hexdigest()


# if __name__ == '__main__':
#     c = Identification("1")
#     b = c.md5_code()
#     print(list(b))

