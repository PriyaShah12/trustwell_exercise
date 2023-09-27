import pandas as pd
import pytest
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
            assert expected == total_calories,'Check all inputs'
        else:
            assert False

    '''This method will test if dietry-fiber is greater than carbs then calorie count 
        doesn't match as expected'''
    @pytest.mark.xfail
    def test_dietry_fiber_greater_than_carbs(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[1].tolist())  # Get the second Row from excel using Pandas as a List
        protein, carbs, dietry_fiber, fat, alcohol, expected = df.iloc[1].tolist()
        total_calories = Test_001.calculate_calories(protein, carbs, dietry_fiber, fat, alcohol)
        print(f'total_calories is {total_calories}')
        assert expected == total_calories,'If dietry-fiber is greater than carbs then calorie count does not calculate as expected'

    '''This method will test if dietry-fiber is greater than carbs and calorie count comes negative
        which is not as expected'''
    @pytest.mark.xfail
    def test_negative_calorie_count(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[2].tolist())  # Get the third Row from excel using Pandas as a List
        protein, carbs, dietry_fiber, fat, alcohol, expected = df.iloc[2].tolist()
        total_calories = Test_001.calculate_calories(protein, carbs, dietry_fiber, fat, alcohol)
        print(f'total_calories is {total_calories}')
        assert total_calories == expected, "If dietry-fiber is greater than carbs then calorie count comes negative which is not as expected"

    '''This method will test if negative dietry-fiber is provided then calorie 
        count is not as expected (Assuming negative value should be considerd zero)'''
    @pytest.mark.xfail
    def test_if_dietry_fiber_is_negative(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        print(df.iloc[3].tolist())  # Get the third Row from excel using Pandas as a List
        protein, carbs, dietry_fiber, fat, alcohol, expected = df.iloc[3].tolist()
        total_calories = Test_001.calculate_calories(protein, carbs, dietry_fiber, fat, alcohol)
        print(f'total_calories is {total_calories}')
        assert total_calories == expected, "If negative input is provided then calorie count does not match as expeceted"

    '''This method will test invalid inputs that is alphanumeric or string'''
    @pytest.mark.xfail
    def test_calories_with_string_or_alphanumeric_as_input(self):
        file = self.test_calorie_sheet()
        df = pd.read_excel(file)
        print(df)
        protein, carbs, dietry_fiber, fat, alcohol, expected = df.iloc[4].tolist()
        print(df.iloc[4].tolist())
        val = Test_001.is_number(protein, carbs, dietry_fiber, fat, alcohol)
        protein1, carbs2, dietry_fiber3, fat4, alcohol5, expected6 = df.iloc[5].tolist()
        print(df.iloc[5].tolist())
        another_val = Test_001.is_number(protein1, carbs2, dietry_fiber3, fat4, alcohol5)
        print(f'Val is {val} and another_val is {another_val}')
        if val == True and another_val == True:
            assert True
        elif val == False and another_val == False:
            assert False, "Inputs are string or alphanumeric"
        elif val == False:
            assert False, "Inputs are string"
        elif another_val == False:
            assert False, "Inputs are alphanumeric"

    @staticmethod
    def is_number(*s):
        for input in (s):
            print(input, '->', isinstance(input, int))
            if isinstance(input, int) != True:
                return False
        return True
































