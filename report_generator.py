import os
import numpy as np

from student_data import student_names, subjects, student_marks
def generate_student_report():

    os.makedirs("output", exist_ok=True)

    file_path = "output/student_report.txt"

    total_marks = np.sum(student_marks, axis=1)

    average_marks = np.mean(student_marks, axis=1)

    percentage = (total_marks / 500) * 100

    with open(file_path, "w") as file:

        file.write("=" * 60 + "\n")
        file.write("       STUDENT PERFORMANCE ANALYTICS REPORT\n")
        file.write("=" * 60 + "\n\n")

        for i in range(len(student_names)):

            file.write(f"Student Name: {student_names[i]}\n")

            file.write("-" * 40 + "\n")

            for j in range(len(subjects)):

                file.write(
                    f"{subjects[j]}: {student_marks[i, j]}\n"
                )

            file.write(f"Total Marks: {total_marks[i]}/500\n")

            file.write(
                f"Average Marks: {average_marks[i]:.2f}\n"
            )

            file.write(
                f"Percentage: {percentage[i]:.2f}%\n"
            )

            file.write("\n" + "=" * 60 + "\n\n")

    print("\nStudent Report Generated Successfully!")
    print("Saved Location:", file_path)

def generate_performance_summary():

    os.makedirs("output", exist_ok=True)

    file_path = "output/performance_summary.txt"

    subject_average = np.mean(student_marks, axis=0)

    total_marks = np.sum(student_marks, axis=1)

    highest_index = np.argmax(total_marks)

    with open(file_path, "w") as file:

        file.write("=" * 50 + "\n")
        file.write("       PERFORMANCE SUMMARY REPORT\n")
        file.write("=" * 50 + "\n\n")

        file.write(
            f"Total Students: {len(student_names)}\n"
        )

        file.write(
            f"Overall Average: {np.mean(student_marks):.2f}\n"
        )

        file.write(
            f"Highest Subject Mark: {np.max(student_marks)}\n"
        )

        file.write(
            f"Lowest Subject Mark: {np.min(student_marks)}\n"
        )

        file.write(
            f"Standard Deviation: {np.std(student_marks):.2f}\n\n"
        )

        file.write(
            f"Top Performing Student: {student_names[highest_index]}\n"
        )

        file.write(
            f"Total Marks: {total_marks[highest_index]}/500\n\n"
        )

        file.write("SUBJECT-WISE AVERAGE\n")

        file.write("-" * 40 + "\n")

        for i in range(len(subjects)):

            file.write(
                f"{subjects[i]}: {subject_average[i]:.2f}\n"
            )

    print("\nPerformance Summary Generated Successfully!")
    print("Saved Location:", file_path)