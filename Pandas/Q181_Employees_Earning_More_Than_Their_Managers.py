import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.copy()
    salary_by_id = employee.set_index('id')['salary']
    employee['manager_salary'] = employee['managerId'].map(salary_by_id)
    result = employee[employee['salary'] > employee['manager_salary']][['name']]
    result = result.rename(columns={'name': 'Employee'})
    return result