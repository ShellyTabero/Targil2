import pandas

class Data:

    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def get_all_districts(self):
        return list(set(self.data["denominazione_region"]))

    def set_districts_data(self, districts):
        temp_data = {}
        all_features = list(self.data.keys())
        for key in all_features:
            temp_data.setdefault(key, [])

        for index, region in enumerate(self.data["denominazione_region"]):
            if region in districts:
                for key in all_features:
                    temp_data[key].append(self.data[key][index])
        for key in all_features:
            self.data[key] = temp_data[key]

    def get_data(self):
        return self.data

    def add_category(self, category, value):
        self.data[category] = value
