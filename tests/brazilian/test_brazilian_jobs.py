from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs_list = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    expectedKeys = ["title", "salary", "type"]

    for job in jobs_list:
        for key in expectedKeys:
            assert key in job.keys()
