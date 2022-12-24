import time

with open("day.txt") as f:
    data = f.read()

if __name__ == "__main__":
    start_time = time.perf_counter()
    # Start of Code

    print(data)

    # End of Code

    end_time = time.perf_counter()
    print("Elapsed time:", end_time - start_time)
