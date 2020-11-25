#opens the file called logger.text and w+ is write
file_builder = open("logger.text", "w+") #the w+ is the overwrite or what your writing
# # write the file and put the str in it 
# file_builder.write("Hey, I'm in a file!")
# #close the file 
# file_builder.close()
for i in range(100): # if you use only write you will overwrite all of the content in the file 
    file_builder.write(f"I'm on line {i + 1}\n")

file_builder.close() #after the loop is done running it will close 

open_function_information = ''' 
open(file, mode)
Parameter Values
Parameter	Description
file	The path and name of the file
mode	A string, define which mode you want to open the file in:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''