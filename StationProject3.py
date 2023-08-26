import time

def Timer():
    try:
        user_input = input("Enter time: ")
        hours, minutes, seconds = map(int, user_input.split(':'))

        total_seconds = hours * 3600 + minutes * 60 + seconds

        while total_seconds >= 0:
            print(f"Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}", end='\r')
            time.sleep(1)

            total_seconds -= 1
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60

        print("\nTime's up!")

    except ValueError:
        print("Invalid input. Please use the format 'hh:mm:ss'.")



if __name__ == "__main__":
    Timer()
