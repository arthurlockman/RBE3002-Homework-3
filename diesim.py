from random import SystemRandom


class DieSim:
    """
    This class allows for simulating a "fair" die by using a random
    number generator.
    """

    def __init__(self, minimum, maximum, die=1):
        """
        Initialize the die sim.
        :param minimum: Minimum die value.
        :param maximum: Maximum die value.
        :param die: Number of die to simulate.
        """
        self.min = minimum
        self.max = maximum
        self.die = die
        self.r = SystemRandom()

    def roll(self):
        """
        Roll the die/dice. If there are multiple dice, the
        results will be added together.
        :return: Returns an int between min and max.
        """
        die_sum = 0
        for i in range(0, self.die):
            die_sum += self.r.randint(self.min, self.max)
        return die_sum

    def roll_n(self, times):
        """
        Roll dice N times and return distribution.
        :param times: The number of rolls.
        :return: A dict of the distribution of results.
        """
        distribution = {}
        for j in range(self.min, (self.max * self.die) + 1):
            distribution[j] = 0.0
        for j in range(0, times):
            distribution[self.roll()] += 1.0
        for j in range(1, (self.max * self.die) + 1):
            distribution[j] /= times
        return distribution


if __name__ == '__main__':
    print 'Running die sim.'
    die1 = DieSim(1, 6)
    die2 = DieSim(1, 6, 2)

    print '\n----------PROBLEM 4----------'
    print 'Rolling 100 times.'
    distribution_1 = die1.roll_n(100)

    print 'Rolling 1000 times.'
    distribution_2 = die1.roll_n(1000)

    print 'Rolling 10,000 times.'
    distribution_3 = die1.roll_n(10000)

    print distribution_1, distribution_2, distribution_3

    print '\n----------PROBLEM 5----------'
    print 'Rolling 100 times.'
    distribution_1 = die2.roll_n(100)

    print 'Rolling 1000 times.'
    distribution_2 = die2.roll_n(1000)

    print 'Rolling 10,000 times.'
    distribution_3 = die2.roll_n(10000)

    print distribution_1, distribution_2, distribution_3
