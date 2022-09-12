from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    jobs_list = []

    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        for job in jobs_reader:
            jobs_list.append(job)

    return jobs_list
