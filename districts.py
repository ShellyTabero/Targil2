MINIMUM_TO_BE_GREEN = 340
GOOD_DAY = 1
BAD_DAY = 0


class Districts:

    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        """
        Updates the dataset so it will contain only the district's names that starts with letters in the given set
        :param letters: A set of letters
        :returns: None
        """
        districts_lst = self.dataset.get_all_districts()
        new_lst = []

        for region in districts_lst:
            if region[0] in letters:
                new_lst.append(region)

        self.dataset.set_districts_data(new_lst)

    def print_details(self, features, statistic_functions):
        """
        Prints statistic data on the dataset according to the given features and statistic functions
        :param features: A list of features
        :param statistic_functions: A list of statistic functions
        :returns: None
        """
        for category in features:
            results = []
            print(category, end=": ")
            for method in statistic_functions:
                temp_result = str(method(self.dataset.get_data()[category]))
                results.append(temp_result)
            print(", ".join(results))

    def determine_day_type(self):
        """
        Adds a key to the dictionary that contains whether it's a good or a bad day
        :param: None
        :returns: None
        """
        day_type_values = []
        new_positives = self.dataset.get_data()["new_positives"]
        resigned_healed = self.dataset.get_data()["resigned_healed"]
        for new_positive_i, resigned_healed_i in zip(new_positives, resigned_healed):
            if resigned_healed_i - new_positive_i > 0:
                day_type_values.append(GOOD_DAY)
            else:
                day_type_values.append(BAD_DAY)
        self.dataset.add_category("day_type", day_type_values)

    def get_districts_class(self):
        """
        determines whether a district in the dataset is green or not green
        :param: None
        :returns: A dictionary of the dataset with a new key containing whether a district  is green or not
        """
        dictionary = {}
        day_type_lst = self.dataset.get_data()["day_type"]
        district_lst = self.dataset.get_data()["denominazione_region"]

        for region in self.dataset.get_all_districts():
            count = 0
            for day_type, district in zip(day_type_lst, district_lst):
                if region == district:
                    count += day_type
            if count > MINIMUM_TO_BE_GREEN:
                dictionary[region] = "green"
            else:
                dictionary[region] = "not green"
        return dictionary
