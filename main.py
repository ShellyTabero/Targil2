import sys
from data import Data
from districts import Districts
import statistics

THRESHOLD_NOT_GREEN = 10


def question1(data1):
    print("Question 1:")
    district = Districts(data1)
    district.filter_districts({'S', 'L'})
    district.print_details(["hospitalized_with_symptoms", "intensive_care", "total_hospitalized", "home_insulation"],
                           [statistics.mean, statistics.median])


def question2(data2):
    print("\nQuestion 2:")
    district = Districts(data2)
    district.determine_day_type()
    dictionary = district.get_districts_class()
    count_not_green = 0
    lockdown = "No"
    total_districts = len(dictionary.keys())
    for value in dictionary.values():
        if value == "not green":
            count_not_green += 1
    if count_not_green > THRESHOLD_NOT_GREEN:
        lockdown = "Yes"

    print(f"Number of districts: {total_districts}")
    print(f"Number of not green districts: {count_not_green}")
    print(f"Will a lockdown be forced on whole of Italy?: {lockdown}")


def main(argv):
    data1 = Data(argv[1])
    question1(data1)
    data2 = Data(argv[1])
    question2(data2)


if __name__ == '__main__':
    main(sys.argv)

