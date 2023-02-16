from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        data = csv.DictReader(file)
        jobs_list = []
        for jobs in data:
            jobs_list.append(jobs)
        return jobs_list
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    job_types = set()
    for job in jobs_list:
        job_types.add(job['job_type'])
    return job_types
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    
    raise NotImplementedError
