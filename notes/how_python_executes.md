# Python compiler or Interpreter

```
Python is an hybrid language that utilizes both a compiler and interpreter to execute python codes. it works by compiling the python code into bytecodes with the aid of a compiler and then further more through a python virtual machine uses an interpretr to translates the bytecodes to machine language for the computer system to execute. Once you have a python script and you want to get the bytecode of that script after compilation. Run this command accordingly on the terminal:

>>> python or python3
* this command opens the interactive shell of python
>>> import py_compile
* This line imports the py_compile module that gives you access to the compile function
>>> py_compile.compile("<name_of_file>")
* This command will return a __pycache__ folder that contains the bytecode of the python file
```
