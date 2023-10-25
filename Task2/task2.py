import csv
import requests
import concurrent.futures


def get_status_code(url):
    """
    Obtaining status code from a given url
    """
    try:
        r = requests.head(url)
        print(f'({r.status_code}) {url}')
    except requests.exceptions.RequestException as e:
        error_message = str(e)
        print(f"An error occurred while processing {url}: {error_message.split(': ', 1)[1]}")

def process_csv_file(file_path):
    """
    Obtaining url status code from a csv file
    while making use of multithreading to speed up the process
    """
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        urls = [item[0] for item in reader]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(get_status_code, urls)
       