# This script opens excel files to parse the worksheets into
#  csv file to ease the upcoming data handling processes
#  The general usage of this is proteomics data
# Author: Enes Kemal Ergin

## Import the necessary libraries
from optparse import OptionParser # Command line parser
from xlrd import open_workbook # To open and handle excel files
from excel_utils import *
import time

# Function to print the time elapsed in a better looking way
def pretty_timer(start, end):
    exec_time = (end - start)/60
    if exec_time >= 1.0:
        print("Execution time is:", format(exec_time, '.2f'), "minutes")
    elif exec_time < 1.0:
        print("Execution time is:", format(exec_time, '.2f'), "seconds")

def summaries(book): #, index_sheet):
    ## Summary of the excel workbook
    print("Summarizing the full workbook:")
    workbook_summary(book)
    print()
    # # Get the index sheet by the index
    # print("Summarizing index worksheet:")
    # worksheet_summary(index_sheet)
    # print()
    # Summarizing all the datas in one loop:
    print("Summarizing all the workbook at once:")
    for i in range(book.nsheets):
        sheet = book.sheet_by_index(i) # open the corresponding sheet
        print("#"*100)
        print("Looking at:", sheet.name) # print the name of the sheet
        print()
        worksheet_summary(sheet)
        print()
        worksheet_basic_view(sheet)
        print()


def write_description(index_sheet, new_path):
    print("Writing a data description from the index worksheet")
    full_lst = []
    for rows in range(index_sheet.nrows):
        full_row =  index_sheet.row(rows)
        temp_lst = []
        non_str_flag = False
        for col in full_row:
            if col.value != "": # if rowxcol is not empty
                if type(col.value) != str:
                    non_str_flag = True
                temp_lst.append(col.value)
            else:
                continue
        if len(temp_lst) != 0:
            if non_str_flag: # if there is non str element in list
                full_lst.append(" - ".join(str(elem) for elem in temp_lst))
            else:
                full_lst.append(" - ".join(temp_lst))

    # Write the data description created from the index worksheet to text file
    with open((new_path + "data.description.txt"), 'w') as file:
        for item in full_lst:
            file.write("%s\n" % item)


def main():
    # Usage has the 2 mandatory input from user.
    usage = 'usage: %prog [options]  <folder_path> <file_name> <sheet_start> <row_start>'
    # Followings are options that user can change
    parser = OptionParser(usage)
    parser.add_option('-d', dest='rootDir', type='str', default='.', help='Root directory of the project [Default: %default]')
    # store the parser results into variables options, args
    (options,args) = parser.parse_args()
    # Check if user put 4 mandatory arguments
    if len(args) != 4 :
        print(args)
        print(options)
        print(len(args))
        parser.error('Must provide folder_path, file_name, sheet_start, and row_start') # Error message
    # If so,
    else:
        # Assign the inputs to variables
        folder_path = args[0]
        file_name = args[1]
        sheet_start = args[2]
        row_start = args[3]

    start_time = time.time()
    # Define the paths to use
    data_path = folder_path + "data/full/"
    file_path = data_path + file_name
    new_path = folder_path + "data/new/"

    # Open the workbook
    sub_start = time.time()
    print("Opening the excel file")
    book = open_workbook(file_path)
    sub_end = time.time()
    pretty_timer(sub_start, sub_end)

    # Call summaries function to print summary of the worksheets
    summaries(book)
    # Create an index_sheet and write index
    index_sheet = book.sheet_by_index(0)
    write_description(index_sheet, new_path)

    # Then write all worksheets to csv
    write_datasets(book, sheet_start, row_start, new_path)

    ## Time elapsed
    end_time = time.time()
    pretty_timer(start_time, end_time)
    print("Script ended!")

if __name__ == '__main__':
    main()
