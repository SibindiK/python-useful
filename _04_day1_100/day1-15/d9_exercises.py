# dictionaries

# grading criteria
'''
Scores 91-100: Grade = "Outstanding"
Scores 81-90: Grade = "Exceeds Expectation"
Scores 71-80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Failed"
'''
# students dictionary
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

grades = ["Outstanding", "Exceeds Expectation", "Acceptable", "Failed"]
student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = grades[0]
    elif student_scores[student] >= 81:
        student_grades[student] = grades[1]
    elif student_scores[student] >= 71:
        student_grades[student] = grades[2]
    elif student_scores[student] <= 70:
        student_grades[student] = grades[3]
print(student_grades)

# nested lists of dictionaries
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },

]


def add_new_country(country, visits, cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
