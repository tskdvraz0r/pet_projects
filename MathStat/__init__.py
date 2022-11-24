class Math:
    class Cube:
        @staticmethod
        def volume(rib_length: float) -> float:
            """
            :param rib_length: cube rib length
            :return: f(x) = rib_length ** 3  # cube volume
            """

            return rib_length ** 3

        @staticmethod
        def square(rib_length: float) -> float:
            """
            :param rib_length: cube rib length
            :return: f(x) = 6 * rib_length ** 2  # cube square
            """

            return 6 * rib_length ** 2

    @staticmethod
    def sum_of_squares(a: float, b: float) -> float:
        """
        :param a: 1st number
        :param b: 2nd number
        :return: f(x) = a ** 2 + b ** 2
        """

        return a ** 2 + b ** 2

    @staticmethod
    def square_of_sums(a: float, b: float) -> float:
        """
        :param a: 1st number
        :param b: 2nd number
        :return: f(x) = (a + b) ** 2
        """

        return (a + b) ** 2

    class Progression:
        @staticmethod
        def arithmetic(a_1: float, diff: float, a_n: float) -> float:
            """
            An arithmetic progression or arithmetic sequence (AP) is a sequence of numbers such that the difference
            between the consecutive terms is constant. For instance, the sequence 5, 7, 9, 11, 13, 15, . . . is an
            arithmetic progression with a common difference of 2.
            (c) wiki

            :param a_1: the first member of the progression
            :param diff: progression difference
            :param a_n: the last member of the progression
            :return: f(x) = a_1 + diff * (a_n - 1)  # arithmetic progression
            """

            return a_1 + diff * (a_n - 1)

        @staticmethod
        def geometric(b_1: float, diff: float, b_n: float) -> float:
            """
            In mathematics, a geometric progression, also known as a geometric sequence, is a sequence of non-zero
            numbers where each term after the first is found by multiplying the previous one by a fixed,
            non-zero number called the common ratio. For example, the sequence 2, 6, 18, 54, ... is a geometric
            progression with common ratio 3. Similarly 10, 5, 2.5, 1.25, ... is a geometric sequence with common
            ratio 1/2.
            (c) wiki

            :param b_1: the first member of the progression
            :param diff: progression difference
            :param b_n: the last member of the progression
            :return: f(x) = b_1 * diff ** (b_n - 1)  # geometric progression
            """

            return b_1 * diff ** (b_n - 1)


class Statistic:
    pass


class Time:
    def minutes_to_hhmm(minutes: int):
        """
        :param minutes: sum of minutes
        :return: datetime.time(hour = minutes // 60, minute = minutes % 60)
        """

        from datetime import time

        return time(hour=minutes // 60, minute=minutes % 60)