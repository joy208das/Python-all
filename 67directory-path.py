
import os

# print(os.getcwd())

"""A directory is a location or folder on a 
storage device (like a hard drive) where files and other
 directories can be stored. Directories help organize files by
  grouping them together, much like folders in a filing cabinet. 
  
  In Python, os refers to the os module, 
  which provides a way of using operating system-dependent functionality.
   This module allows you to interact with the underlying operating system,
such as file and directory operations, environment variables, and process management.

os.getcwd() stands for "get current working directory" and
 returns the path of the current working directory.
The os module is part of the Python standard library,
 so it doesn't require any additional installation."""

os.chdir("C:\\Users\\Asus\\OneDrive\\Desktop\\change path")
print(os.getcwd())