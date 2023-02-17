from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)
    industries = set()
    for job in jobs_list:
        if len(job['industry']) >= 1:
            industries.add(job['industry'])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_list = []
    for job in jobs:
        if job['industry'] == industry:
            jobs_list.append(job)
    return jobs_list
