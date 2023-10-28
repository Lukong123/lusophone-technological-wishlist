### Task 2
This code reads a CSV file containing URLs, and for each URL, it uses *multithreading* to concurrently send HEAD requests and retrieve the status codes.
The status codes are then printed to the console.

The code imports the required modules: `csv`, `requests`, and `concurrent.futures`. These modules provide functionality for working with CSV files, making HTTP requests, and implementing multithreading, respectively.

The **get_status_code** function takes a URL as input and attempts to obtain the status code for that URL by sending a HEAD request using the requests library.If successful, it prints the status code and the URL. If an exception occurs during the request, it captures the error message and prints an error statement.

The **get_status_from_csv_file** function takes a file path as input, opens the CSV file specified by the path, and creates a reader object using the `csv.reader` function to read the contents of the file.

The `next(reader)` line is used to skip the header row in the CSV file.

The function then extracts the URLs from the CSV file by iterating over the reader object and creating a list of the first item in each row.

To speed up the process, the code utilizes **multithreading**. It creates a `ThreadPoolExecutor` object, which manages a pool of worker threads.

The `executor.map function` is used to concurrently execute the get_status_code function for each URL in the urls list. This distributes the work across multiple threads, allowing the code to make multiple HTTP requests simultaneously.

The *file_path variable* is set to the path of the CSV file to be processed.
**Note**
You need to replace it with the appropriate file path for your specific use case.

Finally, the **get_status_from_csv_file** function is called with the provided `file_path`, triggering the execution of the code.
