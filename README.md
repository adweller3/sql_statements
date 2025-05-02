This Python script outputs the CREATE TABLE and INSERT INTO statements for MySQL to make the table for a given csv file.  
The script asks the user for the filename of the csv file and asks for a table name.  It then stores the first 
line of the csv file which is assumed to be the header row and asks the user to define the data type of each 
column name.  The script will then ask the user for an output file name to store the CREATE TABLE and INSERT 
INTO statements, and generate the output for those statements and write them to the file.

Note: One thing that needs to be implemented is to have the script quote the text fields in the statements.
