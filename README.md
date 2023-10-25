# lusophone-technological-wishlist

## Task 1 - [T347737](https://phabricator.wikimedia.org/T347737)
- Came up with a javascript script to display display all the contents of **data** in the format
**ARTICLE TITLE" (Page ID PAGEID) was created at MONTH DAY, YEAR.**

## Task 2 - [T347784](https://phabricator.wikimedia.org/T347784)
- Downloaded csv file with several urls
- Wrote two functions **get_status_code** to get the status code from a url and  **get_status_from_csv_file** to get status code from urls in a csv file
- The output gives **(status code) url** unless where we have an error message where we have 
**An error occurred while processing url: error message**
- This function made use of **multithreading** to make it run faster