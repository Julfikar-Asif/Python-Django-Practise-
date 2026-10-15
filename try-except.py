# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# try:
#     print(x)

# except:
#     print("Something else went wrong.")
# else:
#     print("Nothing went wrong.")

# finally:
#     print("This will always be executed.")


try:
   f= open("demofile.txt")
   try:
       f.write("Lorum Ipsum")
   except:  
       print("Something went wrong when writing to the file.")
   finally:
       f.close()
except:
    print("Something else went wrong.")