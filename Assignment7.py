# Info:-
# Name   : Maaz 
# Dept   : CO-B
# Batch  : 4
# Sub    : Python Assignment-7
# Topic  :-
# 1) Create a function with a default parameter "file" storing the file path
# 2) Open the "file" in append mode
# 3) Use writelines() method to add your roll number, name, and class
# 4) Use readines() method to print your data in the prompt
# Note: Use try...except block with suitable exception class
# Date   : 21-06-2023

# Program:-
import os;

def filePathFunc(file="Information.txt"):
    return file;

try:
    FileName=os.path.basename(filePathFunc());
    File=open(filePathFunc(),"a+t");
    File.writelines(["Roll no. : 109\n","Name     : Maaz\n","Class    : SYCO-B\n"]);
    File.seek(0);
    print(f"Content of {FileName} (by 'File.readlines()') :-\n{File.readlines()}\n");
except FileNotFoundError as fnfe:
    print(f"{type(fnfe).__name__} : File not present at given path.");
except Exception as e:
    print(f"{type(e).__name__} : Something went wrong.");

# Output:-
# Content of Information.txt (by 'File.readlines()') :-
# ['Details :-\n', 'Roll no. : 109\n', 'Name     : Maaz\n', 'Class    : SYCO-B']

# File (Information.txt before appending):-
# Details :-
# 

# File (Information.txt after appending):-
# Details :-
# Roll no. : 109
# Name     : Maaz
# Class    : SYCO-B
# 

#######################################################################################
# [Alternate way]:-

# Program:-
import os;

def fileFunction(file="Information.txt"):
    try:
        FileName=os.path.basename(file)
        File=open(file,"a+t")
        File.writelines(["Roll no. : 109\n","Name     : Maaz\n","Class    : SYCO-B\n"])
        File.seek(0)
        print(f"Content of {FileName} (by 'File.readlines()') :-\n{File.readlines()}\n")
    except FileNotFoundError as fnfe:
        print(f"{type(fnfe).__name__} : File not present at given path.")
    except Exception as e:
        print(f"{type(e).__name__} : Something went wrong.")
    finally:
        return;

# Driver code:-
fileFunction();

# Output:-
# Content of Information.txt (by 'File.readlines()') :-
# ['Details :-\n', 'Roll no. : 109\n', 'Name     : Maaz\n', 'Class    : SYCO-B']

# File (Information.txt before appending):-
# Details :-
# 

# File (Information.txt after appending):-
# Details :-
# Roll no. : 109
# Name     : Maaz
# Class    : SYCO-B
# 


