import numpy as np
from student_data import student_names, subjects, student_marks


def display_student_marks():

    print("\n--- INDIVIDUAL STUDENT MARKS ---")

    for i in range(len(student_names)):

        print("\nStudent:", student_names[i])

        for j in range(len(subjects)):

            print(subjects[j], ":", student_marks[i, j])


def display_sliced_marks():

    print("\n--- FIRST THREE STUDENTS ---")

    print(student_marks[:3])

    print("\n--- FIRST THREE SUBJECTS ---")

    print(student_marks[:, :3])

    print("\n--- LAST TWO STUDENTS ---")

    print(student_marks[-2:])


def display_array_shape():

    print("\n--- ARRAY INFORMATION ---")

    print("Original Array:")
    print(student_marks)

    print("Array Shape:", student_marks.shape)

    print("Array Dimensions:", student_marks.ndim)

    print("Total Elements:", student_marks.size)

    reshaped_array = student_marks.reshape(25, 1)

    print("\nReshaped Array:")
    print(reshaped_array)

    print("New Shape:", reshaped_array.shape)