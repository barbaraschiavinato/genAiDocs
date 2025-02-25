# 9. Data Manipulation with Pandas

## Prompt

Write a Python script using Pandas to read a CSV file, filter out rows where the column 'Age' is over 50, and save the filtered data to a new CSV file.

## Results

### Amazon Q

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('input_file.csv')

# Filter the DataFrame to keep rows where 'Age' is over 50
filtered_df = df[df['Age'] <= 50]


filtered_df.to_csv('output_file.csv', index=False)
```

Here's how the script works:

1. The `pd.read_csv('input_file.csv')` function reads the input CSV file and creates a Pandas DataFrame `df`.

1. The `df[df['Age'] <= 50]` expression filters the DataFrame to keep only the rows where the 'Age' column is less than or equal to 50.

1. The `filtered_df.to_csv('output_file.csv', index=False)` function writes the filtered DataFrame to a new CSV file named 'output_file.csv'. The `index=False` parameter ensures that the row index is not included in the output file.

Make sure to replace 'input_file.csv' with the actual name of your input CSV file, and 'output_file.csv' with the desired name for the output file.

Note that this script assumes that your CSV file has a column named 'Age'. If the column name is different, you'll need to update the code accordingly.

### GitHub Copilot



```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('input_file.csv')

# Filter the DataFrame to keep rows where 'Age' is 50 or less
filtered_df = df[df['Age'] <= 50]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('output_file.csv', index=False)
```

Please replace `'input_file.csv'` with the path to your input CSV file, and `'output_file.csv'` with the desired path for the output file.

### Axet Gaia


```python
import pandas as pd

# Read the CSV file
data = pd.read_csv('input.csv')

# Filter out rows where 'Age' is over 50
filtered_data = data[data['Age'] <= 50]

# Save the filtered data to a new CSV file
filtered_data.to_csv('output.csv', index=False)
```

**Explanation**

- We start by importing the `pandas` library, which provides powerful data manipulation capabilities.
- Next, we use the `read_csv` function from `pandas` to read the input CSV file and store it in the `data` variable.
- We then filter out rows where the 'Age' column is over 50 by using boolean indexing. This creates a new DataFrame called `filtered_data`.
- Finally, we use the `to_csv` function to save the `filtered_data` DataFrame to a new CSV file called 'output.csv', without including the index column.

This solution follows best practices in Python by using the `pandas` library for efficient data manipulation and by using clear and concise code.

### ChatGpt 4

Here's a Python script that uses the Pandas library to accomplish the task of reading a CSV file, filtering out rows where the 'Age' column values are over 50, and then saving the filtered data to a new CSV file. Make sure you have Pandas installed in your environment, which you can install via pip if you haven't already (`pip install pandas`).

```python
import pandas as pd

def filter_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Filter out rows where 'Age' is greater than 50
    filtered_df = df[df['Age'] <= 50]

    # Save the filtered data to a new CSV file
    filtered_df.to_csv(output_file, index=False)

# Example usage
input_file = 'path_to_your_input_file.csv'
output_file = 'path_to_your_output_file.csv'
filter_data(input_file, output_file)
```
**How to Use This Script**

1. **Prepare Your CSV File**: Ensure your CSV file is correctly formatted and includes an 'Age' column. Place the CSV file in a known directory.
2. **Set File Paths**: Replace `'path_to_your_input_file.csv'` with the actual path to your CSV file. Similarly, adjust `'path_to_your_output_file.csv'` to where you want the filtered data saved.
3. **Run the Script**: Execute the script in your Python environment. This can be done through a command line by running `python your_script_name.py` if saved in a file, or directly in a Python interactive environment.

This script is straightforward and efficient for filtering data based on age criteria. It's a common task in data preprocessing, making this script useful in various data analysis and machine learning preprocessing steps.

### Meta.ai

Here is a Python script using Pandas to achieve this:

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('input.csv')

# Filter out rows where the 'Age' column is over 50
filtered_df = df[df['Age'] <= 50]

# Save the filtered data to a new CSV file
filtered_df.to_csv('output.csv', index=False)
```

Here's how the script works:

1. `pd.read_csv('input.csv') `reads the input CSV file into a Pandas DataFrame.
1. `df['Age'] <= 50` creates a boolean mask to filter out rows where the 'Age' column is greater than 50.
1. `df[...]` applies the filter to the DataFrame, resulting in a new DataFrame with only the rows where 'Age' is less than or equal to 50.
1. `filtered_df.to_csv('output.csv', index=False)` saves the filtered DataFrame to a new CSV file named 'output.csv'. The `index=False` parameter tells Pandas not to include the row indices in the output file.

Make sure to replace 'input.csv' with the path to your input CSV file, and the script will generate a new file named 'output.csv' in the same directory with the filtered data.

Note: This script assumes that the 'Age' column exists in the input CSV file and contains numerical values. If the column name or data type is different, you may need to adjust the script accordingly.

### Gemini


```python
import pandas as pd

# Define the input and output CSV filenames
input_file = "data.csv"  # Replace with your actual input CSV filename
output_file = "filtered_data.csv"  # Replace with your desired output filename

# Read the CSV file using Pandas
data = pd.read_csv(input_file)

# Filter the data where 'Age' is less than or equal to 50 (inclusive)
filtered_data = data[data["Age"] <= 50]

# Save the filtered data to a new CSV file
filtered_data.to_csv(output_file, index=False)

print(f"Data filtered and saved to: {output_file}")
```

**Explanation:**

1. **Import Pandas:** We import the `pandas` library for data manipulation.
2. **Define Filenames:** Define the names of your input and output CSV files (replace with your actual filenames).
3. **Read CSV:** Use `pd.read_csv` to read the data from the input file into a pandas DataFrame named `data`.
4. **Filter Data:** We filter the DataFrame using boolean indexing. We select rows where the value in the "Age" column is less than or equal to 50 (`data["Age"] <= 50`). The filtered data is stored in the `filtered_data` DataFrame.
5. **Save Data:** Use the `to_csv` method on the `filtered_data` DataFrame to save it as a new CSV file with the specified name (`output_file`). The `index=False` argument ensures the row index is not included in the output.
6. **Print Message:** Print a confirmation message indicating the output filename.

**Running the Script:**

1. Save the script as a Python file (e.g., filter_data.py).
2. Make sure the input CSV file is in the same directory as your script.
3. Run the script from your terminal: `python filter_data.py`

This script will read the CSV data, filter by age, and save the filtered data to a new CSV file.  

## Analysis

### Amazon Q
   - **Pros**: Concise and effective script for reading, filtering, and saving data using Pandas.
   - **Cons**: No error handling or validation to ensure the 'Age' column exists.
   - **Code Example**:
     ```python
     import pandas as pd

     # Read the CSV file
     df = pd.read_csv('input_file.csv')

     # Filter the DataFrame to keep rows where 'Age' is 50 or less
     filtered_df = df[df['Age'] <= 50]

     # Save the filtered DataFrame to a new CSV file
     filtered_df.to_csv('output_file.csv', index=False)
     ```

### GitHub Copilot
   - **Pros**: Similar to Amazon Q, efficiently accomplishes the task using Pandas.
   - **Cons**: Like Amazon Q, lacks detailed comments and error handling.
   - **Code Example**:
     ```python
     import pandas as pd

     # Read the CSV file
     df = pd.read_csv('input_file.csv')

     # Filter the DataFrame to keep rows where 'Age' is 50 or less
     filtered_df = df[df['Age'] <= 50]

     # Save the filtered DataFrame to a new CSV file
     filtered_df.to_csv('output_file.csv', index=False)
     ```

### Axet Gaia
   - **Pros**: Clear and detailed explanation of each step, maintaining simplicity.
   - **Cons**: Lacks advanced features or handling of potential exceptions.
   - **Code Example**:
     ```python
     import pandas as pd

     # Read the CSV file
     data = pd.read_csv('input.csv')

     # Filter out rows where 'Age' is over 50
     filtered_data = data[data['Age'] <= 50]

     # Save the filtered data to a new CSV file
     filtered_data.to_csv('output.csv', index=False)
     ```

### ChatGPT 4
   - **Pros**: Encapsulates functionality in a reusable function, adding flexibility and clarity.
   - **Cons**: Could be considered slightly more complex than necessary for very simple tasks.
   - **Code Example**:
     ```python
     import pandas as pd

     def filter_data(input_file, output_file):
         # Read the CSV file
         df = pd.read_csv(input_file)

         # Filter out rows where 'Age' is greater than 50
         filtered_df = df[df['Age'] <= 50]

         # Save the filtered data to a new CSV file
         filtered_df.to_csv(output_file, index=False)
     ```

### Meta.ai
   - **Pros**: Direct implementation, straightforward and efficient.
   - **Cons**: Similar to others, lacks error handling or checks for data integrity.
   - **Code Example**:
     ```python
     import pandas as pd

     # Read the CSV file
     df = pd.read_csv('input.csv')

     # Filter out rows where 'Age' is over 50
     filtered_df = df[df['Age'] <= 50]

     # Save the filtered data to a new CSV file
     filtered_df.to_csv('output.csv', index=False)
     ```

### Gemini
   - **Pros**: Provides a complete and structured approach with clear file path definitions and use of global variables for ID management.
   - **Cons**: While detailed, the inclusion of global variables may not be necessary and could complicate understanding for beginners.
   - **Code Example**:
     ```python
     import pandas as pd

     # Define the input and output CSV filenames
     input_file = "data.csv"  # Replace with your actual input CSV filename
     output_file = "filtered_data.csv"  # Replace with your desired output filename

     # Read the CSV file using Pandas
     data = pd.read_csv(input_file)

     # Filter the data where 'Age' is less than or equal to 50 (inclusive)
     filtered_data = data[data["Age"] <= 50]

     # Save the filtered data to a new CSV file
     filtered_data.to_csv(output_file, index=False)

     print(f"Data filtered and saved to: {output_file}")
     ```

## Conclusion

**Best Implementation**: **ChatGPT 4** offers a well-rounded approach by encapsulating the filtering logic in a function, which not only clarifies the code's purpose but also makes it reusable in larger projects or different contexts. This method adds value by enhancing maintainability and scalability.

**Worst Implementation**: While none of the implementations are inherently poor, the simplicity and lack of error handling in **Meta.ai** and **Amazon Q** make them slightly less robust compared to the detailed approach by **ChatGPT 4**. These simpler scripts do not account for common data issues such as missing columns or incorrect data types, which could lead to runtime errors in practical applications.