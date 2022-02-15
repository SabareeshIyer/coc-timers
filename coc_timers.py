import atexit
from timers import Timers


# Main
timers = Timers()
print("\n1 to add timer \n2 to check next timer \n3 to get all timers\n4 to save and quit\n9 to delete all timers\n")
while True:
    try:
        choice = int(input("\nEnter choice: "))
        if choice == 1:
            name = input("\nEnter base name.\t")
            countdown_time = input("Enter time left.\t")
            timers.add_timer(name, countdown_time)

        if choice == 2:
            timers.check_next_timer()

        if choice == 3:
            timers.show_all_timers()

        if choice == 4:
            timers.quit()
            exit()

        if choice == 9:
            timers.delete_all_timers()

    except ValueError:
        print("Incorrect input. Try again.\n")

    except Exception:
        print("Unforeseen exception. Exiting.")
        timers.quit()