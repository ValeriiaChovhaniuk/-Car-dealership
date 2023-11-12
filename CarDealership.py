import csv

class Employee:
    def __init__(self, full_name, position, phone, email, employee_id):
        self.full_name = full_name
        self.position = position
        self.phone = phone
        self.email = email
        self.employee_id = employee_id

    def to_list(self):
        return [self.full_name, self.position, self.phone, self.email, self.employee_id]

# Sample employee data
employees_data = [
    Employee("Valeriia Chovhaniuk", "Sales Manager", "067-456-7890", "val@ukr.net", "EMP001"),
    Employee("Alex Chovhaniuk", "Marketing Assistant", "067-654-3210", "val@ukr.net", "EMP002")
]

# Save data to a CSV file
def save_employees_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Full Name", "Position", "Phone", "Email", "Employee ID"])
        for employee in data:
            writer.writerow(employee.to_list())

# Save sample employee data to a CSV file
save_employees_to_csv('employees.csv', employees_data)


import csv

class Car:
    def __init__(self, manufacturer, year, model, cost_price, potential_sale_price):
        self.manufacturer = manufacturer
        self.year = year
        self.model = model
        self.cost_price = cost_price
        self.potential_sale_price = potential_sale_price

    def to_list(self):
        return [self.manufacturer, self.year, self.model, self.cost_price, self.potential_sale_price]

# Sample car data
car_data = [
    Car("Toyota", 2022, "RAV4", 25000, 30000),
    Car("Ford", 2023, "Kuga", 28000, 32000),
    Car("Nissan", 2022, "XTrail", 32000, 37000),
    Car("Lexus", 2021, "RX350", 42000, 44000),
    Car("Mercedes", 2023, "GLE200", 33000, 38000)
]

# Save data to a CSV file
def save_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Manufacturer", "Year", "Model", "Cost Price", "Potential Sale Price"])
        for car in data:
            writer.writerow(car.to_list())

# Save sample data to a CSV file
save_to_csv('cars.csv', car_data)


import csv

class Sale:
    def __init__(self, employee, car, sale_date, actual_sale_price):
        self.employee = employee
        self.car = car
        self.sale_date = sale_date
        self.actual_sale_price = actual_sale_price

    def to_list(self):
        return [self.employee, self.car, self.sale_date, self.actual_sale_price]

# Sample sales data
sales_data = [
    Sale("Valeriia Chovhaniuk", "Toyota", "2023-11-12", 30000)
]

# Save data to a CSV file
def save_sales_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Employee", "Car", "Sale Date", "Actual Sale Price"])
        for sale in data:
            writer.writerow(sale.to_list())

# Save sample sales data to a CSV file
save_sales_to_csv('sales.csv', sales_data)


class Employee:
    def __init__(self, full_name, position, phone, email, employee_id):
        self.full_name = full_name
        self.position = position
        self.phone = phone
        self.email = email
        self.employee_id = employee_id

class Car:
    def __init__(self, manufacturer, year, model, cost_price, potential_sale_price):
        self.manufacturer = manufacturer
        self.year = year
        self.model = model
        self.cost_price = cost_price
        self.potential_sale_price = potential_sale_price

class Sale:
    def __init__(self, employee, car, sale_date, actual_sale_price):
        self.employee = employee
        self.car = car
        self.sale_date = sale_date
        self.actual_sale_price = actual_sale_price

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def find_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None


class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        self.cars.remove(car)

    def find_car_by_model(self, model):
        found_cars = [car for car in self.cars if car.model == model]
        return found_cars


class SalesManager:
    def __init__(self):
        self.sales = []

    def add_sale(self, sale):
        self.sales.append(sale)

    def remove_sale(self, sale):
        self.sales.remove(sale)

import csv

class Employee:
    def __init__(self, full_name, position, phone, email, employee_id):
        self.full_name = full_name
        self.position = position
        self.phone = phone
        self.email = email
        self.employee_id = employee_id

    def to_list(self):
        return [self.full_name, self.position, self.phone, self.email, self.employee_id]

class Car:
    def __init__(self, manufacturer, year, model, cost_price, potential_sale_price):
        self.manufacturer = manufacturer
        self.year = year
        self.model = model
        self.cost_price = cost_price
        self.potential_sale_price = potential_sale_price

    def to_list(self):
        return [self.manufacturer, self.year, self.model, self.cost_price, self.potential_sale_price]

class Sale:
    def __init__(self, employee, car, sale_date, actual_sale_price):
        self.employee = employee
        self.car = car
        self.sale_date = sale_date
        self.actual_sale_price = actual_sale_price

    def to_list(self):
        employee_data = self.employee.to_list()
        car_data = self.car.to_list()
        return employee_data + car_data + [self.sale_date, self.actual_sale_price]

class FileManager:
    @staticmethod
    def save_data(data, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in data:
                writer.writerow(obj.to_list())

    @staticmethod
    def load_data(filename):
        data = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                # Add logic to reconstruct Employee, Car, and Sale objects from the CSV row
                # For brevity, direct loading from CSV is demonstrated, but object construction logic is needed
                data.append(row)
        return data

# ReportGenerator and other classes remain unchanged

employees = [Employee("Valeriia Chovhaniuk", "Sales Manager", "0676325412", "val@ukr.net", "EMP001")]
cars = [Car("Toyota", 2022, "RAV4", 25000, 30000)]
sales = [Sale(employees[0], cars[0], "2023-11-12", 30000)]

data_to_save = employees + cars + sales
FileManager.save_data(data_to_save, "data.csv")

loaded_data = FileManager.load_data("data.csv")

class ReportGenerator:
    @staticmethod
    def generate_full_employee_info(data):
        # Generate full employee report from data
        pass

    @staticmethod
    def generate_full_car_info(data):
        # Generate full car report from data
        pass

    @staticmethod
    def generate_full_sale_info(data):
        # Generate full sale report from data
        pass


ReportGenerator.generate_full_employee_info(loaded_data)
ReportGenerator.generate_full_car_info(loaded_data)
ReportGenerator.generate_full_sale_info(loaded_data)
#
# import unittest
# from CarDealership import Employee, Car, Sale, FileManager, ReportGenerator
#
#
# class TestCarDealershipApp(unittest.TestCase):
#     def setUp(self):
#         self.employees = [Employee("Valeriia Chovhaniuk", "Sales Manager", "0676325412", "val@ukr.net", "EMP001")]
#         self.cars = [Car("Toyota", 2022, "RAV4", 25000, 30000)]
#         self.sales = [Sale(self.employees[0], self.cars[0], "2023-11-12", 30000)]
#
#     def test_employee_to_list(self):
#         emp = self.employees[0]
#         expected = ["Valeriia Chovhaniuk", "Sales Manager", "0676325412", "val@ukr.net", "EMP001"]
#         self.assertEqual(emp.to_list(), expected)
#
#     def test_car_to_list(self):
#         car = self.cars[0]
#         expected = ["Toyota", 2022, "RAV4", 25000, 30000]
#         self.assertEqual(car.to_list(), expected)
#
#     def test_sale_to_list(self):
#         sale = self.sales[0]
#         expected = ["Valeriia Chovhaniuk", "Toyota", 2023, "RAV4", 25000, 30000, "2023-11-12", 30000]
#         self.assertEqual(sale.to_list(), expected)
#
#     def test_save_and_load_data(self):
#         file_name = "test_data.csv"
#         # Save test data to a file
#         data_to_save = self.employees + self.cars + self.sales
#         FileManager.save_data(data_to_save, file_name)
#
#         # Load data from the file
#         loaded_data = FileManager.load_data(file_name)
#         expected_loaded_data = [obj.to_list() for obj in data_to_save]
#
#         # Compare saved data with loaded data
#         self.assertEqual(loaded_data, expected_loaded_data)
#
#
#
# if __name__ == '__main__':
#     unittest.main()
