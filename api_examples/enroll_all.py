import requests

username = 'shen'  # fill in
password = 'shenlee@53'  # fill in
base_url = 'http://127.0.0.1:8000/api/'
url = f'{base_url}courses/'

available_courses = []

while url is not None:
    print(f'Loading courses from {url}')
    r = requests.get(url, auth=(username, password))  # add auth if needed
    response = r.json()
    url = response['next']
    courses = response['results']

    # collect course titles
    available_courses += [course['title'] for course in courses]

    # enroll in courses
    for course in courses:
        course_id = course['id']
        course_title = course['title']
        r = requests.post(
            f'{base_url}courses/{course_id}/enroll/',
            auth=(username, password)
        )
        if r.status_code == 200:
            print(f'Successfully enrolled in {course_title}')
        else:
            print(f'Failed to enroll in {course_title}: {r.status_code}')

# print(f'Available courses: {", ".join(available_courses)}')
