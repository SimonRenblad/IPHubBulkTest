# IPHubBulkTest
A python solution for bulk testing IP addresses using the IPHub API

## Guide

1. Download the files in this repository as a ZIP file, and unzip in target directory

### Python Set-up

2. Download Python3 at https://www.python.org/downloads/, consult https://realpython.com/installing-python/ for assistance or google "python get started"
3. Check that the Python version is 3.0 or higher using 'python --version' or 'py --version' in the terminal / command line
4. Navigate to the target directory in the terminal / command line. MacOS: https://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855 Windows: https://www.computerhope.com/issues/chusedos.htm

### Getting the API Key

5. Go to the IPHub.info website
6. Register an account using email and password and confirm email
7. Click on 'Pricing', then below the plans there is a link to a free plan, click it
8. Copy the API key displayed to the clip board

### Configuration File

9. In the target directory, one of the downloaded files is called 'configip.py'
10. Open this file using Notepad or any other text editor to see it's contents
11. On the line saying API_KEY = "", paste the API key from the clip board in between the quotation marks
12. Fill in the INPUT_FILE, GOOD_OUTPUT_FILE and BAD_OUTPUT_FILE as filenames ending in .txt in between the quotation marks
13. Set the BLOCK_CONSTRAINT to 1 or 2. By default it is 1 when you download the files.
14. Close the 'configip.py'

### Prepare the input file

15. Convert the list of IP addresses to a .txt (raw text) format with each address on a separate line of the file
16. If using the free plan, make sure to only list less than 1000 addresses per file, since there is a 1000 queries per day limit
17. Make sure this .txt file has the same name as put in INPUT_FILE from step 12

### Running the tests

18. In the command line / terminal, in the target directory, run the bulk_test_ip.py file using 'py bulk_test_ip.py' or 'python bulk_test_ip.py'
19. If there are no errors, the command line will be idle for a while, be patient since the API is quite slow at testing the addresses
20. When finished, the program prints that it has finished, as well as the number of tests completed
21. The output can be found in the same directory as the names defined by GOOD_OUTPUT_FILE and BAD_OUTPUT_FILE in step 12
