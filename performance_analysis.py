import numpy as np
from student_data import student_names, subjects, student_marks


def calculate_total():

    print("\n--- STUDENT TOTAL MARKS ---")

    total_marks = np.sum(student_marks, axis=1)

    for i in range(len(student_names)):

        print(student_names[i], ":", total_marks[i], "/ 500")


def calculate_average():

    print("\n--- STUDENT AVERAGE MARKS ---")

    average_marks = np.mean(student_marks, axis=1)

    for i in range(len(student_names)):

        print(student_names[i], ":", round(average_marks[i], 2))


def calculate_percentage():

    print("\n--- STUDENT PERCENTAGE ---")

    total_marks = np.sum(student_marks, axis=1)

    percentage = (total_marks / 500) * 100

    for i in range(len(student_names)):

        print(student_names[i], ":", round(percentage[i], 2), "%")


def find_highest_marks():

    print("\n--- HIGHEST MARKS ---")

    highest_marks = np.max(student_marks, axis=1)

    for i in range(len(student_names)):

        print(student_names[i], ":", highest_marks[i])


def find_lowest_marks():

    print("\n--- LOWEST MARKS ---")

    lowest_marks = np.min(student_marks, axis=1)

    for i in range(len(student_names)):

        print(student_names[i], ":", lowest_marks[i])

def apply_bonus_marks():

    print("\n--- BONUS MARKS ---")

    bonus = 5

    updated_marks = student_marks + bonus

    print("Original Marks:")
    print(student_marks)

    print("\nUpdated Marks:")
    print(updated_marks)

def subject_wise_bonus():

    print("\n--- SUBJECT WISE BONUS ---")

    bonus = np.array([5, 3, 4, 2, 5])

    updated_marks = student_marks + bonus

    print("Subject Bonus:", bonus)

    print("\nUpdated Student Marks:")
    print(updated_marks)

def display_updated_records():

    bonus = 5

    updated_marks = student_marks + bonus

    print("\n--- UPDATED STUDENT RECORDS ---")

    for i in range(len(student_names)):

        print(student_names[i], ":", updated_marks[i])

def aggregate_sum():

    print("\nTotal Marks:", np.sum(student_marks))

def aggregate_mean():

    print("\nAverage Marks:", np.mean(student_marks))

def aggregate_std():

    print("\nStandard Deviation:", np.std(student_marks))

def aggregate_max_min():

    print("\nMaximum Marks:", np.max(student_marks))

    print("Minimum Marks:", np.min(student_marks))

def subject_analysis():

    print("\n--- SUBJECT WISE ANALYSIS ---")

    subject_average = np.mean(student_marks, axis=0)

    for i in range(len(subjects)):

        print(subjects[i], "Average:", round(subject_average[i], 2))

