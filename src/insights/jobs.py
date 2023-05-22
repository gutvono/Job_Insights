from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
# Abre o arquivo CSV e retorna os dados no formato de uma lista de dicionários.
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        data = csv.DictReader(file)
        jobs_list = []
        for jobs in data:
            jobs_list.append(jobs)
        return jobs_list


# Identifica quais tipos de empregos existem.
def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    job_types = set()
    for job in jobs_list:
        job_types.add(job['job_type'])
    return job_types


# Filtra os empregos pelo tipo.
def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_list.append(job)
    return jobs_list
