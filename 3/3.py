from abc import ABCMeta, abstractmethod


class MyInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self):
        """Вернуть название операции"""

    @abstractmethod
    def get_sign(self):
        """Вернуть знак операции"""

    @abstractmethod
    def estimate(self, a, b):
        """Вернуть результат операции"""


class Addition(MyInterface):

    def get_name(self):
        return "Сложение"

    def get_sign(self):
        return "+"

    def estimate(self, a, b):
        return a + b


class Subtraction(MyInterface):

    def get_name(self):
        return "Вычитание"

    def get_sign(self):
        return "-"

    def estimate(self, a, b):
        return a - b


class Multiplication(MyInterface):

    def get_name(self):
        return "Умноэение"

    def get_sign(self):
        return "*"

    def estimate(self, a, b):
        return a * b


class Maximum(MyInterface):

    def get_name(self):
        return "Максимум"

    def get_sign(self):
        return "MAX"

    def estimate(self, a, b):
        return max(a, b)


a = Maximum()
print(a.estimate(4, 8))
