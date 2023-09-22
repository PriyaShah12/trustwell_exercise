import pandas as pd
from utilities import path_utils


class Test_001:

    def test_calorie_sheet(self):
        func_name = Test_001.test_calorie_sheet.__name__
        print(func_name)
        file = path_utils.get_file(func_name)
        print("File Name-->", file)
        return file

    @staticmethod
    def calculate_calories(protein, carbs, dietry_fiber, fat, alcohol):
        calories = (4 * protein) + 4*(carbs - dietry_fiber) + (9 * fat) + (7 * alcohol)
        print(calories)
        return calories

    def test_valid_inputs(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[0].tolist())  #Get the First Row of Pandas as a List
        protein, carbs, dietry_fiber, fat, alcohol, exp_total = df.iloc[0].tolist()
        total_calories = Test_001.calculate_calories(protein, carbs, dietry_fiber, fat, alcohol)
        assert exp_total == total_calories

    def test_dietryfiber_greater_than_carbs(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[1].tolist())  #Get the second Row of Pandas as a List
        protein, carbs, dietry_fiber, fat, alcohol, exp_total = df.iloc[1].tolist()
        print("Data is-->", protein, carbs, dietry_fiber, fat, alcohol)
        total_calories = Test_001.calculate_calories(protein, carbs, dietry_fiber, fat, alcohol)
        assert exp_total != total_calories

    '''Assumed that total calorie intake should be hundred'''
    def test_if_total_of_all_intake_is_valid(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[2].tolist())  # Get the third Row of Pandas as a List
        protein, carbs, dietry_fiber, fat, alcohol, exp_total = df.iloc[2].tolist()
        print("Data is-->", protein, carbs, dietry_fiber, fat, alcohol)
        total_calories = Test_001.calculate_calories(protein, carbs, dietry_fiber, fat, alcohol)
        assert exp_total != total_calories




