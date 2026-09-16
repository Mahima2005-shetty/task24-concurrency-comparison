import asyncio
import multiprocessing
import threading
import time


# --------------------------------------------------
# I/O-BOUND WORKLOAD
# --------------------------------------------------

def io_task(task_id):
    """Simulates an I/O-bound operation using sleep."""
    time.sleep(0.5)
    return f"Task {task_id} completed"


async def async_io_task(task_id):
    """Simulates an I/O-bound operation using asyncio."""
    await asyncio.sleep(0.5)
    return f"Task {task_id} completed"


# --------------------------------------------------
# CPU-BOUND WORKLOAD
# --------------------------------------------------

def cpu_task(n):
    """Performs CPU-intensive calculation."""
    total = 0

    for i in range(n):
        total += i * i

    return total


# --------------------------------------------------
# THREADING
# --------------------------------------------------

def run_threading(task_count):
    start = time.perf_counter()

    threads = []

    for task_id in range(task_count):
        thread = threading.Thread(
            target=io_task,
            args=(task_id,)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.perf_counter()

    return end - start


# --------------------------------------------------
# MULTIPROCESSING
# --------------------------------------------------

def run_multiprocessing(task_count):
    start = time.perf_counter()

    numbers = [3_000_000] * task_count

    with multiprocessing.Pool() as pool:
        pool.map(cpu_task, numbers)

    end = time.perf_counter()

    return end - start


# --------------------------------------------------
# ASYNCIO
# --------------------------------------------------

async def run_asyncio(task_count):
    start = time.perf_counter()

    tasks = [
        async_io_task(task_id)
        for task_id in range(task_count)
    ]

    await asyncio.gather(*tasks)

    end = time.perf_counter()

    return end - start


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

def main():
    task_count = 10

    print("=" * 60)
    print("TASK 24: THREADING vs MULTIPROCESSING vs ASYNCIO")
    print("=" * 60)

    print(f"\nNumber of tasks: {task_count}")

    # Threading - I/O bound
    print("\nRunning Threading (I/O-bound)...")
    threading_time = run_threading(task_count)
    print(f"Threading execution time: {threading_time:.4f} seconds")

    # Asyncio - I/O bound
    print("\nRunning AsyncIO (I/O-bound)...")
    asyncio_time = asyncio.run(run_asyncio(task_count))
    print(f"AsyncIO execution time: {asyncio_time:.4f} seconds")

    # Multiprocessing - CPU bound
    print("\nRunning Multiprocessing (CPU-bound)...")
    multiprocessing_time = run_multiprocessing(task_count)
    print(
        f"Multiprocessing execution time: "
        f"{multiprocessing_time:.4f} seconds"
    )

    # Comparison
    print("\n" + "=" * 60)
    print("EXECUTION TIME COMPARISON")
    print("=" * 60)

    print(f"Threading        : {threading_time:.4f} seconds")
    print(f"AsyncIO          : {asyncio_time:.4f} seconds")
    print(f"Multiprocessing  : {multiprocessing_time:.4f} seconds")

    print("\n" + "=" * 60)
    print("USE CASES")
    print("=" * 60)

    print("Threading:")
    print("- Suitable for I/O-bound tasks")
    print("- Useful for file operations, network requests, APIs")

    print("\nAsyncIO:")
    print("- Suitable for high-volume asynchronous I/O")
    print("- Useful for APIs, web servers and network operations")

    print("\nMultiprocessing:")
    print("- Suitable for CPU-bound tasks")
    print("- Useful for data processing and computational workloads")


if __name__ == "__main__":
    main()