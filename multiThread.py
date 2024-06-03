# Its a simple multithreaing program to perform the opertion of finding the cube and squre the value is passed via args the limit is set in numbers
# This program will show the value of cube and the time taken i have added a dealy of 1 sec to each so see the execution time 
# Simulating a time-consuming task is given 



import threading
import time


# Function to calculate and print squares  and cude of numbers
def calculate_squares(numbers):
    for number in numbers:
        time.sleep(0.2) 
        print(f"Square of {number}: {number * number}")


def calculate_cubes(numbers):
    for number in numbers:
        time.sleep(0.2) 
        print(f"Cube of {number}: {number * number * number}")


if __name__ == "__main__":
    numbers = list(range(1, 11))  

   # tread creation for each task
    thread1 = threading.Thread(target=calculate_squares, args=(numbers,))
    thread2 = threading.Thread(target=calculate_cubes, args=(numbers,))


    # this code  helps to  start the thread
    thread1.start()
    thread2.start()
  

    # Waiting the thread to complete
    thread1.join()
    thread2.join()
   
   # After the operations message is printed 
    print("Done with all calculations!")
