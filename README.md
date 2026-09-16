\# Task 24: Threading vs Multiprocessing vs AsyncIO



\## Objective



The objective of this task is to implement and compare three Python concurrency approaches:



\- Threading

\- Multiprocessing

\- AsyncIO



The same type of workload is tested using suitable concurrency techniques, and their execution times are compared.



\## Technologies Used



\- Python

\- Threading

\- Multiprocessing

\- AsyncIO

\- Time module



\## Project Structure



```text

task24-concurrency-comparison/

│

├── main.py

├── performance\_results.txt

├── README.md

└── venv/

Implementations

1\. Threading



Python's threading module is used for an I/O-bound workload.



The program creates multiple threads that simulate I/O operations using time.sleep().



Threading is useful for:



File operations

Network requests

API calls

Other I/O-bound operations

2\. Multiprocessing



Python's multiprocessing module is used for a CPU-bound workload.



Multiple processes perform computational calculations in parallel.



Multiprocessing is useful for:



CPU-intensive calculations

Data processing

Computational workloads

Parallel processing

3\. AsyncIO



Python's asyncio module is used for asynchronous I/O operations.



Multiple asynchronous tasks are scheduled using asyncio.gather().



AsyncIO is useful for:



Network applications

Web servers

API requests

High-volume I/O operations

Execution



Run the program using:



python main.py

Performance Results



The test was performed with 10 tasks.



Method	Workload	Execution Time

Threading	I/O-bound	0.5087 seconds

AsyncIO	I/O-bound	0.5102 seconds

Multiprocessing	CPU-bound	1.1227 seconds



Execution times may vary between runs depending on system resources and background processes.



Analysis



Threading and AsyncIO completed the simulated I/O-bound workload in approximately the same time.



Threading is useful when working with blocking I/O operations.



AsyncIO provides an asynchronous programming model that is particularly useful when an application needs to manage many I/O operations concurrently.



Multiprocessing is appropriate for CPU-bound workloads because separate processes can execute computational work independently.



Conclusion



Threading, Multiprocessing, and AsyncIO are designed for different types of workloads.



Use Threading for suitable I/O-bound operations.

Use AsyncIO for large numbers of asynchronous I/O operations.

Use Multiprocessing for CPU-bound computational workloads.



The appropriate concurrency model depends on the workload and application requirements.



