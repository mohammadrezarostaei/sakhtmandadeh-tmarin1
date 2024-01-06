import time
import random
import matplotlib.pyplot as plt

def custom_sort(data):
    sorted_data = sorted(data, key=lambda x: (x['First Name'], x['Last Name']))
    return sorted_data

def generate_random_data(size):
    first_names = ['Raj', 'Suraj', 'Karan', 'Jade', 'Kiran', 'Armaan', 'Jaya', 'Ingrid', 'Aahana', 'Kumar', 'Seth', 'Canary', 'Galore', 'Thakur']
    last_names = ['Nayyar', 'Sharma', 'Kumar', 'Canary', 'Thakur', 'Sharma', 'Kamla', 'Kumar', 'Sharma', 'Galore', 'Seth', 'Dadra', 'Maverick', 'Arora']

    data = [{'First Name': random.choice(first_names), 'Last Name': random.choice(last_names)} for _ in range(size)]
    return data

def simulate_external_code():
    # Given data
    data = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    # Sort the data using the external sort function
    sorted_data_external = custom_sort(data)

    # Print the sorted data
    print(sorted_data_external)

    # Check if the sorted list matches the expected result
    if sorted_data_external == expected_sorted_list:
        print("The lists are equal.")
    else:
        print("The lists are not equal.")

simulate_external_code()
