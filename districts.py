from data import Data

class Districts:

    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        districts_lst = self.dataset.get_all_districts()
        new_lst = []

        for region in districts_lst:
            if region[0] in letters:
                new_lst.append(region)

        self.dataset.set_districts_data(new_lst)

    def print_details(self, features, statistic_functions):

        for category in features:
            results = []
            print(category, end=": ")
            for method in statistic_functions:
                temp_result = str(method(self.dataset.get_data()[category]))
                results.append(temp_result)
            print(", ".join(results))

    def determine_day_type(self):
        day_type_values = []
        new_positives = self.dataset.get_data()["new_positives"]
        resigned_healed = self.dataset.get_data()["resigned_healed"]
        for new_positive_i, resigned_healed_i in zip(new_positives, resigned_healed):
            if resigned_healed_i - new_positive_i > 0:
                day_type_values.append(1)
            else:
                day_type_values.append(0)
        self.dataset.add_category("day_type", day_type_values)

    def get_districts_class(self):
        dictionary = {}
        day_type_lst = self.dataset.get_data()["day_type"]
        new_positives_lst = self.dataset.get_data()["new_positives"]

        for region in self.dataset.get_all_districts():
            count = 0
            for day_type, district in zip(day_type_lst, new_positives_lst):
                if region == district:
                    count += day_type
            if count > 340:
                dictionary[region] = "green"
            else:
                dictionary[region] = "not green"
        return dictionary