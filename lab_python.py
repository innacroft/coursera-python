#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        data= csv.DictReader(open(csv_file_location), dialect='empDialect')
        employee_list=[]
        for row in data:
                employee_list.append(row)
        return employee_list


read_employees('home/student/data/employees.csv')
