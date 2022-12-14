from src.jobs import read


def get_unique_job_types(path):

    jobs_list = read(path)
    job_type_list = []

    for job in jobs_list:
        if job["job_type"] not in job_type_list:
            job_type_list.append(job["job_type"])

    return job_type_list


def filter_by_job_type(jobs, job_type):

    return [job for job in jobs if job_type == job["job_type"]]


def get_unique_industries(path):

    jobs_list = read(path)
    industries_list = []

    for job in jobs_list:
        if job["industry"] not in industries_list and job["industry"] != "":
            industries_list.append(job["industry"])

    return industries_list


def filter_by_industry(jobs, industry):

    return [job for job in jobs if industry == job["industry"]]


def get_max_salary(path):

    jobs_list = read(path)

    max_salaries_filtered = [
        int(job["max_salary"])
        for job in jobs_list
        if job["max_salary"].isdigit()
    ]

    return max(max_salaries_filtered)


def get_min_salary(path):

    jobs_list = read(path)
    min_salaries = []

    for job in jobs_list:
        min_salary_job = job["min_salary"]

        if min_salary_job.isdigit():
            min_salaries.append(int(min_salary_job))

    return min(min_salaries)


def matches_salary_range(job, salary):

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min salary or max salary doesn't exists")

    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError(
            "min salary, max salary or salary aren't valid integers"
        )

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min salary is greather than max salary")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):

    result = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)

        except ValueError:
            pass

    return result
