# File Splitter

This script allows you to split a CSV or TXT file into multiple smaller files based on a specified index.

## Prerequisites

- Python 3.x
- Pandas library

## Usage

1. Clone the repository or download the script.
2. Make sure you have the Pandas library installed. If not, install it using the following command:

   ```
   pip install pandas
   ```

3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the following command:

   ```
   python script.py <filename> <split_number>
   ```

   Replace `<filename>` with the name of the file you want to split (CSV or TXT), and `<split_number>` with the desired index for splitting.

6. The script will create a directory called "file_split" to store the split files. If the directory already exists, its contents will be deleted.
7. The input file will be split into multiple smaller files based on the specified index.

**Note:** The script assumes that the input file has no header row.

## Example

```
python script.py data.csv 1000
```

The above example will split the "data.csv" file into multiple smaller files, each containing 1000 rows of data.

## Output

The split files will be saved in the "file_split" directory. Each split file will be named "split_fileX.csv" or "split_fileX.txt", where X represents the file number.

## License

This project is licensed under the [MIT License](LICENSE).