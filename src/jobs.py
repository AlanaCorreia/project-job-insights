from functools import lru_cache
import csv


@lru_cache
def read(path):

    jobs_list = []

    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        for job in jobs_reader:
            jobs_list.append(job)

    return jobs_list
