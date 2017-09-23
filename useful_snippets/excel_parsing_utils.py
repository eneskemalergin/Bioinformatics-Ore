# This script contains helper functions to parse data from excel files
# Author: Enes Kemal Ergin

from xlrd import open_workbook # To open and handle excel files
import numpy as np # To use array structure
import csv # Using csv features to create csv files

def workbook_summary(book):
    """Function to print all the necessary summary about the workbook"""
    # Print the number of worksheets in the excel
    print("The number of worksheets inside the file is {0}".format(book.nsheets))
    # Print worksheet names
    print("Worksheet name(s): {0}".format(book.sheet_names()))
    # ToDo: Add more summaries

def worksheet_summary(sheet):
    """Function to print all necessary summary about the worksheet"""
    # Print the number of columns in the worksheet
    print("The number of columns inside the worksheet is {0}".format(sheet.ncols))
    # Print the number of rows in the worksheet
    print("The number of rows inside the worksheet is {0}".format(sheet.nrows))
    # ToDo: Add more summaries

def worksheet_head(sheet):
    """Printing the first 5 rows of the worksheet for better viewing"""
    for rows in range(6):
        curr_row = sheet.row(rows)
        temp_lst = []
        for col in curr_row:
            if col.value != "":
                temp_lst.append(col.value)
        temp_lst = ", ".join(str(elem) for elem in temp_lst)
        print(str(rows), ":" , temp_lst )

def worksheet_basic_view(sheet):
    """Printing the full worksheet for full viewing,
    it wont print the full if worksheet is too big"""
    row_number = sheet.nrows
    col_number = sheet.ncols
    if row_number * col_number >= 1000:
        print("This worksheet is too big to view all content, instead printing first 5 rows")
        return worksheet_head(sheet)
    else:
        for rows in range(row_number):
            curr_row = sheet.row(rows)
            temp_lst = []
            for col in curr_row:
                if col.value != "":
                    temp_lst.append(col.value)
            temp_lst = ", ".join(str(elem) for elem in temp_lst)
            print(str(rows), ":" , temp_lst )


def cell_content_matrix(sheet):
    """Giving a binary summary of the cells in the worksheet,
        if the cell empty 0, if the cell is populated 1"""
    row_number = sheet.nrows
    col_number = sheet.ncols
    if row_number * col_number >= 1000:
        return "This worksheet is too big to create content matrix!"
    else:
        content_matrix = np.zeros([row_number,col_number])

        for cols in range(content_matrix.shape[1]):
            curr_col = sheet.col(cols)
            binary_holder = []
            for rows in curr_col:
                if rows.value != "":
                    binary_holder.append(1)
                else:
                    binary_holder.append(0)
            # Update the column with binary holder
            content_matrix[:,cols] = binary_holder
        print("0: Empty Cells \n1: Populated Cells")
        print(content_matrix)

def write_datasets(book, sheet_start=1, row_start=1, data_path='./'):
    """This functions loops throught worksheets and write them into csv
    book <- xlrd-workbook-object | which book to get datas from
    sheet_start <- int | from which worksheet start writing datasets
    sheet_end <- int | to which worksheet stop writing dataset
    row_start <- int | from which row start writing the dataset
    ignored_sheets <- list[int] | index of worksheets to extract from writing to csv
    data_path <- str | path to save the data to"""
    sheet_end = book.nsheets
    sheet_start = int(sheet_start)
    row_start = int(row_start)
    for i in range(sheet_start, sheet_end):         # loop selected number of times
        # if i in ignored_sheets:
        #     print("Ignored sheet", i, ":", sheet.name)
        #     continue
        # else:
        sheet = book.sheet_by_index(i)              # open the corresponding sheet
        print("Writing for:", sheet.name)           # print the name of the sheet
        data_name = data_path + sheet.name + ".csv" # prepare a data file name
        with open(data_name, "w") as file:          # Open a file to write
            # initialize the csv writer object with comma delimeter
            writer = csv.writer(file, delimiter = ",")
            # write header, with the value of first row of the sheet
            header = [cell.value for cell in sheet.row(row_start)]
            writer.writerow(header) # add the header
            # from the following row start writing the content to the csv file
            for row_idx in range(row_start+1, sheet.nrows):
                row = [int(cell.value) if isinstance(cell.value, float) else cell.value
                                        for cell in sheet.row(row_idx)]
                writer.writerow(row)
