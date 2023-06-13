import json
import random

name_list = ["Brinda", "Aditya", "Rohit", "Kalpana", "Chandana", "Ashwini", "Praneeth"]
age_list = [24, 25, 30, 28, 31, 27, 29]
salary_list = [6000, 4500, 8000, 5000, 3500, 6000, 9500]


def lambda_handler(event, context):
    # TODO implement
    random_index = random.randint(0,6)
    # mock_data = {}
    # mock_data['emp_name'] = name_list[random_index]
    # mock_data['emp_age'] = age_list[random_index]
    # mock_data['emp_salary'] = salary_list[random_index]
    # #print(mock_data)
    # return mock_data
    return {
        "emp_name" : name_list[random_index],
        "emp_age" : age_list[random_index],
        "emp_salary" : salary_list[random_index]
    }
