import pandas as pd
from utilities import path_utils
import allure


class Test_001:

    '''This method will read the test data excel file'''
    def test_calorie_sheet(self):
        func_name = Test_001.test_calorie_sheet.__name__
        print(func_name)
        file = path_utils.get_file(func_name)
        print("File Name-->", file)
        return file

    '''This method will calculate calories as per given formula'''
    @staticmethod
    def calculate_calories(protein, carbs, dietry_fiber, fat, alcohol): #verify BODMAS
        calories = (4 * protein) + 4*(carbs - dietry_fiber) + (9 * fat) + (7 * alcohol)
        print(calories)
        return calories

    '''This method will test happy path where all inputs are integers and carbs is
    greater than dietry-fiber'''
    def test_calorie_count_with_valid_inputs(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[0].tolist())  # Get the first Row from excel using Pandas as a List
        protein, carbs, dietry_fiber, fat, alcohol, expected = df.iloc[0].tolist()
        if carbs >= dietry_fiber:
            total_calories = Test_001.calculate_calories(protein, carbs, dietry_fiber, fat, alcohol)
            print(f'total_calories is {total_calories}')
            assert expected == total_calories,'Carbs is greater than dietry-fiber and all inputs are positive'
        else:
            assert False

    '''This method will test if dietry-fiber is greater than carbs then calorie count 
        doesn't match as expected because absolute value is not taken'''
    def test_dietry_fiber_greater_than_carbs(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[1].tolist())  # Get the second Row from excel using Pandas as a List
        protein, carbs, dietry_fiber, fat, alcohol, expected = df.iloc[1].tolist()
        total_calories = Test_001.calculate_calories(protein, carbs, dietry_fiber, fat, alcohol)
        print(f'total_calories is {total_calories}')
        assert expected == total_calories,'If dietry-fiber is greater than carbs then calorie count does not match'


    '''This method will test if dietry-fiber is greater than carbs and calorie count comes negative
    which is not as expected'''
    def test_negative_calorie_count(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[2].tolist())  # Get the third Row from excel using Pandas as a List
        protein, carbs, dietry_fiber, fat, alcohol, expected = df.iloc[2].tolist()
        total_calories = Test_001.calculate_calories(protein, carbs, dietry_fiber, fat, alcohol)
        print(f'total_calories is {total_calories}')
        assert total_calories == expected, "if dietry-fiber is greater than carbs then calorie count comes negative which is not as expected"

    '''def test_should_not_calculate_if_any_input_is_string(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[1].tolist())  # Get the third Row of Pandas as a List
        [protein, carbs, dietry_fiber, fat, alcohol, expected]= df.iloc[1].tolist()
        print("Data is-->", protein, carbs, dietry_fiber, fat, alcohol, expected)
        self.calculate_calories(protein, carbs, dietry_fiber, fat, alcohol)


    def test_if_any_or_all_inputs_are_string(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[1].tolist())  #Get the second Row of Pandas as a List
        # protein, carbs, dietry_fiber, fat, alcohol, expected = df.iloc[1].tolist()
        l = df.iloc[1].tolist()
        print(l)
        # new_lst = l.pop()
        # for item in new_lst:
        #     print(item)'''









