# Email Inbox Parser

This script connects to an IMAP mailbox (e.g., Gmail) and retrieves the latest emails from the inbox. It then extracts relevant information such as the date, sender, subject, and text content of each email and saves it in a CSV file.

## Prerequisites

- Python 3.x
- `imaplib`, `email`, `csv`, `logging`, `os`, `ssl` libraries
- Beautiful Soup (`bs4`) library

## Setup

1. Save the script in a file named `email_parser.py`.

2. Create a file named `credentials.txt` in the same directory as the script. In this file, provide your email address on the first line and your password on the second line.

3. Set the `credential_path` variable in the script to the path of the `credentials.txt` file.

4. Set the `csv_path` variable in the script to the desired path for the output CSV file.

5. Modify the `N` variable in the `main()` function to specify the number of latest emails to fetch. Set it equal to `total_no_of_mails` to fetch all emails in the inbox.

6. Run the script:

   ```bash
   python email_parser.py
   ```

## Output

The script will create a CSV file at the specified `csv_path` location. The CSV file will contain the following columns: "Date", "From", "Subject", "Text mail". Each row represents an email with its corresponding information.

## Note

- This script assumes that the emails in the inbox are in HTML format. It uses Beautiful Soup to extract plain text from HTML emails.
- Attachments are not processed in this script.