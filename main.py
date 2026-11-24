from report_generator import (
    generate_student_report,
    generate_performance_summary
)

from array_operations import (
    display_student_marks,
    display_sliced_marks,
    display_array_shape
)

from performance_analysis import (
    calculate_total,
    calculate_average,
    calculate_percentage,
    find_highest_marks,
    find_lowest_marks,
    apply_bonus_marks,
    subject_wise_bonus,
    aggregate_sum,
    aggregate_mean,
    aggregate_std,
    aggregate_max_min,
    subject_analysis
)

from comparison import (
    compare_addition,
    compare_multiplication,
    compare_execution_time,
    compare_memory_usage
)


def main():

    while True:

        print("\n========================================")
        print(" STUDENT PERFORMANCE ANALYTICS SYSTEM")
        print("========================================")

        print("1. Display Student Records")
        print("2. View Individual Student Marks")
        print("3. Display Sliced Marks")
        print("4. Display Array Shape and Reshaping")
        print("5. Calculate Total Marks")
        print("6. Calculate Average Marks")
        print("7. Calculate Percentage")
        print("8. Find Highest Marks")
        print("9. Find Lowest Marks")
        print("10. Apply Bonus Marks")
        print("11. Subject Wise Bonus")
        print("12. Statistical Analysis")
        print("13. Subject Analysis")
        print("14. NumPy vs Python Lists")
        print("15. Generate Student Report")
        print("16. Generate Performance Summary")
        print("17. Exit")

        choice = input("\nEnter Your Choice: ").strip()

        if choice == "1":
            display_student_marks()

        elif choice == "2":
            display_student_marks()

        elif choice == "3":
            display_sliced_marks()

        elif choice == "4":
            display_array_shape()

        elif choice == "5":
            calculate_total()

        elif choice == "6":
            calculate_average()

        elif choice == "7":
            calculate_percentage()

        elif choice == "8":
            find_highest_marks()

        elif choice == "9":
            find_lowest_marks()

        elif choice == "10":
            apply_bonus_marks()

        elif choice == "11":
            subject_wise_bonus()

        elif choice == "12":
            aggregate_sum()
            aggregate_mean()
            aggregate_std()
            aggregate_max_min()

        elif choice == "13":
            subject_analysis()

        elif choice == "14":
            compare_addition()
            compare_multiplication()
            compare_execution_time()
            compare_memory_usage()

        elif choice == "15":
            generate_student_report()

        elif choice == "16":
            generate_performance_summary()

        elif choice == "17":
            print("\nThank You for Using Student Analytics System!")
            break

        else:
            print("\nInvalid Choice! Please Try Again.")


if __name__ == "__main__":
    main()
    