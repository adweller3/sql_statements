# This script returns a create table statement, as well as insert into statement for a #file

# basic flow is:
# 1. main()
	# a. Asks user for filename of csv file
	# b. Calls parse_csv() to read csv file
	# c. Calls user_input() to ask user to identify columns with data types
	# d. Calls create_table() to generate create table and insert statement
	# e. Print create table and insert table statements to a file
	

#Must add error handling (try except), add primary keys, clean data first

#######################ISSUES###########################################
#1. values statement currently contains datatypes - get rid of
#2. Values statement does not use quotes for strings - fix
#####################################################################
import csv

################################################################################################


def parse_csv(fname: str):

	with open(fname, 'r', newline = '') as fhandle:
		csv_text = csv.reader(fhandle, delimiter = ',' )

		#alternative to using next is to keep count of line num, if line num == 1, store in head_row
		head_row = next(csv_text)
		head_row = [s.strip() for s in head_row]
		body = []
		for row in csv_text:
			row_strip = [s.strip() for s in row]
			body.append(row_strip)

	return head_row, body

################################################################################################

#This function asks user what datatypes they want and return a dictionary
#containing field as key and datatype as value
def user_input(head_row):

	

	while True:
		table_name = input("Enter table name:  ")
		print(f"Table name set to:  {table_name}")
		correct = input("Is this correct?  Enter 1 for yes and 2 for no:  ")
		if correct == "1":
			break

	

	while True:
		fields_dict = {}
		for i in head_row:
			data_type = input(f"Enter a data type for {i}:  ")
			fields_dict[i] = data_type

		print(f"Summary of table {table_name}:  ")
		print(fields_dict)
		correct = input("Enter 1 for correct and 2 for not correct:  ")
		if correct == '1':
			break

	return table_name, fields_dict

################################################################################################

def create_table(table_name, fields_dict, body):

	
	#create list of column name - datatype pairs
	ls1 = [" ".join([key, fields_dict[key]]) for key in fields_dict]

	#create list of column names without datatypes for insert statement
	ls2 = [c for c in fields_dict]
# fix commments to be more explanative ######################################################################################
	#create string used in create table
	str1 = ",\n\t".join(ls1)

	#create string used in insert statement
	str2 = ",\n\t".join(ls2)

	create_statement = f"CREATE TABLE {table_name} (\n\t{str1}\n);\n"

	value_list =[]
#IF COLUMN IS A STRING USE SINGLE QUOTES AROUND THAT FIELD
	for row in body:
		value_list.append(f"({", ".join(row)})")

	values = ",\n\t".join(value_list)
	value_str = f"VALUES\n\t{values};"

	insert_statement = f"INSERT INTO {table_name} (\n\t{str2}\n)\n" + \
						value_str 
		
	return create_statement, insert_statement

#################################################################################################

def print_statements(create_statement, insert_statement):

	file_out = input("Enter a filename for the output:  ").replace("\\", "\\\\")

	with open(file_out, "w") as fhandle:
		print(create_statement, file = fhandle)
		print(insert_statement, file = fhandle)

	return None


################################################################################################
################################################################################################

def main():

	fname = input("Enter file name for csv:  ").replace("\\", "\\\\")
	#fname = "C:\\workspace\\python\\sql\\student.csv"

	head_row, body = parse_csv(fname)
	table_name, fields_dict = user_input(head_row)
	create_statement, insert_statement = create_table(table_name, fields_dict, body)	
	print_statements(create_statement, insert_statement)

	

	return None

################################################################################################

if __name__ == "__main__":
	main()


