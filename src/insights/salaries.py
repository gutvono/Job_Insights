from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    salaries = []
    for job in jobs_list:
        max_salary = job['max_salary']
        if max_salary.isnumeric():
            salaries.append(int(max_salary))
    return max(salaries)


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    salaries = []
    for job in jobs_list:
        min_salary = job['min_salary']
        if min_salary.isnumeric():
            salaries.append(int(min_salary))
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    # O try está tratando os seguintes casos:
    # - Chaves min_salary ou max_salary não existem
    # - Valores não numéricos tanto nas chaves de job quanto em salary

    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])
        salary_input = int(salary)

    except(ValueError, TypeError, KeyError):
        raise ValueError

    if min_salary > max_salary:
        raise ValueError

    return min_salary <= salary_input <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except(ValueError):
            print("This job isn't in the range")

    return jobs_list
