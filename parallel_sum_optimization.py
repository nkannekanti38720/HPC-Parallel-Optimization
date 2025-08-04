# parallel_sum_of_squares.py

from concurrent.futures import ThreadPoolExecutor
import time

# Function to calculate sum of squares of a list
def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

# Function to split the list and process in parallel
def parallel_sum_of_squares(numbers):
    # Split the numbers into two halves for parallel processing
    mid_point = len(numbers) // 2
    with ThreadPoolExecutor() as executor:
        # Execute the sum_of_squares function on each half of the list in parallel
        results = executor.map(sum_of_squares, [numbers[:mid_point], numbers[mid_point:]])
    # Return the total sum of squares
    return sum(results)

# Main function to test the performance
def main():
    # Generate a large list of numbers (for example, 1 million numbers)
    numbers = list(range(1, 1000001))
    
    # Measure the time it takes to compute sum of squares serially
    start_time = time.time()
    serial_result = sum_of_squares(numbers)
    serial_time = time.time() - start_time
    print(f"Serial computation result: {serial_result}")
    print(f"Serial computation time: {serial_time:.6f} seconds")
    
    # Measure the time it takes to compute sum of squares in parallel
    start_time = time.time()
    parallel_result = parallel_sum_of_squares(numbers)
    parallel_time = time.time() - start_time
    print(f"Parallel computation result: {parallel_result}")
    print(f"Parallel computation time: {parallel_time:.6f} seconds")
    
    # Show performance improvement
    speedup = serial_time / parallel_time
    print(f"Speedup achieved: {speedup:.2f}x")

if __name__ == "__main__":
    main()
