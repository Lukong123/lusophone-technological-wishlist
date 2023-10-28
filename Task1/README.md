### Task 1

#### Summary
Our JavaScript code takes the provided *data array*, processes the creation dates, formats them, and generates a string with the formatted information for each page.
It then displays the formatted results in the HTML document while also showing the code itself.

### Specification
- It defines an array called `data` that holds information about different pages, including their *page IDs*, *creation dates*, and *titles*.

- It processes the data array using the `map` method to extract the creation date from each object.

- For each object in the data array, it converts the `creation_date` string into a `Date` object.

- It formats the date using the `toLocaleDateString` method with the specified options to obtain a formatted date string.

- It constructs a string for each page, including the page's title, page ID, and formatted creation date.

- It assigns the resulting string to the `results` variable.

- It updates the content of the HTML element with the ID **results** to display the formatted results.

- It retrieves the JavaScript code from within the HTML document itself and displays it in the HTML element with the ID **code**.