import itertools
import pprint

from param import Parameterized, Number, List, ClassSelector

marketer_id = itertools.count(1)


def banner():
    _ = "=" * 80
    _ += "\n"
    return _


class Marketer(Parameterized):
    id = Number()
    front_line_target = Number(5)

    def __init__(self, **params):
        super().__init__(**params)
        self.id = next(marketer_id)
        self.front_line = []

    @property
    def sponsoring_goals_met(self):
        return len(self.front_line) == self.front_line_target

    def recruiting_strategy(self):
        """Employ a strategy to recruit new marketers.

        Default algorithm recruits 1 new marketer.
        """
        new_marketer = Marketer()
        return [new_marketer]

    def recruit(self):
        if self.sponsoring_goals_met:
            return []
        else:
            new_marketers = self.recruiting_strategy()
            self.front_line.extend(new_marketers)
            return new_marketers

    def __str__(self):
        front_line_pprint = pprint.pformat(self.front_line, width=1, indent=8)
        result = 'Marketer {} has sponsored for the following {} marketers:\n\t{}'.format(
            self.id, len(self.front_line), front_line_pprint
        )
        return result


Marketer.param.add_parameter('sponsor', ClassSelector(class_=Marketer))
Marketer.param.add_parameter('front_line', List([], item_type=Marketer, instantiate=True))


class Network(Parameterized):
    marketers = List([], item_type=Marketer, instantiate=True)

    def recruit(self):
        new_marketers = []
        for marketer in self.marketers:
            new_marketers.extend(marketer.recruit())
        self.marketers.extend(new_marketers)

    def __str__(self):
        result = f"Total marketers {len(self.marketers)}.\n"
        for marketer in self.marketers:
            result = result + str(marketer) + "\n"
        return result


def main(months=3):
    network = Network()
    network.marketers.append(Marketer())

    for month in range(months):
        print(f"{banner()}\nMonth {month}: {network}")

        network.recruit()

        print(f"\tRecruiting complete. Updated status for month: {network}")


if __name__ == '__main__':
    main()
