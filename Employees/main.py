from Employees.config import parse_conf
from Employees.helpers import read_data, serializer
from Employees.models import Employee


def get_employees():
    data = read_data()
    users = serializer(data)
    employees = []
    for employee in users:
        params = {
            'name': employee.name,
            'position': employee.position,
            'working_hours': employee.hours,
            'plan_completion': employee.plan,
            'experience': employee.experiens,
            'kpi': employee.kpi,
            'config': parse_conf[employee.position]

        }
        employees.append(Employee(**params))
    return employees


def main():
    employees = get_employees()

    employees_salary_by_name = []
    employees_with_kpi = []
    employees_with_plan_completion = []

    for e in employees:
        employees_salary_by_name.append((e.name, e.payroll()))
        employees_with_kpi.append((e.name, e.kpi))
        employees_with_plan_completion.append((e.name, e.plan_completion))

    employees_salary_by_name.sort(key=lambda employee: employee[1], reverse=True)
    employee_with_max_kpi = max(employees_with_kpi, key=lambda employee: employee[1])
    employees_with_max_plan_completion = max(employees_with_plan_completion, key=lambda employee: employee[1])
    print(f'Employee with max kpi {employee_with_max_kpi[0]}')
    print(f'Employee with max plan completion {employees_with_max_plan_completion[0]}')
    employees_salary = ''
    for employee_name, salary in employees_salary_by_name:
        employees_salary += f'{employee_name} salary {salary} \n'
    print(f'Employees salary: \n{employees_salary}')


if __name__ == '__main__':
    main()