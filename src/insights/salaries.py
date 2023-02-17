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
    
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
