class Math:
    class Cube:
        @staticmethod
        def value(rib_length: float) -> float:
            """
            :param rib_length:
            :return:
            """

            return rib_length ** 3

        @staticmethod
        def square(rib_length: float) -> float:
            """
            :param rib_length:
            :return:
            """

            return 6 * rib_length ** 2

    class Progression:
        @staticmethod
        def arithmetic(a_1: float, diff: float, a_n: float) -> float:
            """
            :param a_1:
            :param diff:
            :param a_n:
            :return:
            """

            return a_1 + diff * (a_n - 1)

        @staticmethod
        def geometric(b_1: float, q: float, b_n: float) -> float:
            """
            :param b_1:
            :param q:
            :param b_n:
            :return:
            """

            return b_1 * q ** (b_n - 1)


class Statistic:
    pass
