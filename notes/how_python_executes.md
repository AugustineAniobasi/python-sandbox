# Compiler and Interpreter in Python


Python is an hybrid language that utilizes both a compiler and an interpreter to execute python codes. it works by compiling the python code into bytecodes with the aid of a compiler then, translates the bytecode through a python virtual machine(PVM) using an interpreter to machine language for the computer system to execute immediately. Hence, both the compiler and interpreter can both be seen as translators but they work differently, let's take a look at them separately:

**Compiler:** A compiler takes in the entire program (the source code of a high level language) and translates it to into an entirely new program (A low level language mostly machine executable) then the file containing this new low level language can then be executed. Think of it as a book written in English language and it is to be read by a french person. A compiler translaters this book written in English Language(this becomes the high level language) to an entirely new book written in French language (this becomes the low level language usually in machine executable format) so the person(the computer system) can read, understand it and execute the information in it.Take note, the compiler translates the whole source code into a lower level labguage and produces a file that an executable file that needs to be further executed by an individual. A compiler produces an executable file after compilation.
> **Source code &rArr; Compiler &rArr; Executable file**

**Interpreter:** An interpreter on the other hand acts slightly different from a compiler, instead of translating the source code to an executable or a low level file like the compiler, it performs both the translation and execution of the source code immediately. An interpreter operates sequentially, it takes a line or statement of the source code and performs exactly what it specifies without creating a separate, standalone executable file. The translation and execution in an interpreter both occurs immediately on a line of code or statement before moving to another line and if error is detected on any particular line it stops processing the program at that line and returns the error on that line. Think of the workings of an interpreter in this way -  Imagine you are having a conversation with an English speaker(Source code in a particular language) and you only understand French (Computer system), the interpreter now a translator that explains each statement made by the English speaker immediately its been said in french language so you can understand and give a response if there is a need to. An interpreter is a program that reads the source code statement by statement and executes each statement before moving to the next one. once the python script is run, the interpreter doesn't just "read" text it follows a specific internal process which is explained as follows:
> Lexical Analysis (Tokenization) &DoubleLongRightArrow;  Parsing(AST) &DoubleLongRightArrow; Semantic Analysis &DoubleLongRightArrow; Execution/Evaluation 


* Lexical Analysis (Tokenization) : The first thing an interpreter does is the *Tokenization*of a stream of characters, at this stage the interpreter reads a stream of characters  in a line(statement) from the source code and arrange them into tokens. Tokens are the smallest meaningful units of codes such as keywords, identifiers, operators, literals and delimiters that the interpreter understands. To clarify tokenization further, consider a code sample given as:   
   x = y + 5

   Tokens:  
   IDENTIFIER(x), IDENTIFIER(Y), OPERATOR(=), NUMBER(5) 

* Parsing (Syntactic Analysis): After successfully tokenizing a stream of characters, the interpreter takes the tokens created and build a hierarchical structure representing how the code is constructed grammatically. This hierarchical structure is known as Abstract Syntax tree(AST) and it is shown for the code consisder in Tokenization above;  
```
                          =
                         / \
                        x   +
                           / \
                          y   5
```
* Semantic Analysis: At this stage, the AST has been completely formed, the interpreter checks the AST for semantic errors that are valid syntatically and but don't make logical sense, this includes;

    - type checking: Are you adding a string to a number?

    - Scope resolution: Does the variable y exist in the current context?
* Execution/Evaluation: After the AST has been formed and the semantics has been checked to ensure the AST are in order, the next step which is the final step is the execution or evaluation stage and this is where the major difference lies between a compiler and an interpreter.
    * for a compiler the AST will be translated into a low level language mostly machine code and it will be saved to a file, the executable file becomes the output of the compiler
    * for an interpreter, it begins to perform the instructions illustrated in the AST starting from the root. The interpreter uses a ***Tree Traversal algorithm*** to figure out what to do.
    
Modern programming language do not rely any longer on either pure "compiler" or pure "interpreter" instead combine both models and utilize the positives in both model to realize efficiency of the language.
1. Just-in-Time (JIT) Compilation (Java, C#, JavaScript V8):
The system starts as an interpreter for fast startup. When it notices a function is being called thousands of times, it compiles that function to native machine code while the program is running. This gives you the portability and developer speed of an interpreter with performance approaching (but not always equaling) a traditional compiler.

2. Ahead-of-Time (AOT) Compilation (Go, Swift, Rust):
These are traditional compilers, but they are designed to be blazingly fast at compiling, minimizing the developer wait time that historically plagued languages like C++.

> python/python3 <filename>  
command with the file name as a source file contain python codes, it directly perform both the transformation to bytecode and executes this bytecode with the PVM to get a machine language which  and you want to get the bytecode of that script after compilation. Run this command accordingly on the terminal:

## How to Access the bytecode of a python script
Open the terminal of your PC and type the following command sequentially

### Method 1

>>> python or python3
* this command opens the interactive shell of python
>>> import py_compile
* This line imports the py_compile module that gives you access to the compile function
>>> py_compile.compile("<name_of_file>")
* This command will return a __pycache__ folder that contains the bytecode of the python file

### Method 2

Generate bytecode for a single file
>>> python3 -m py_compile my_script.py

This creates: __pycache__/my_script.cpython-3XX.pyc
 (where XX is your Python version, e.g., 312 for Python 3.12)

To view the bytecode use this command 

>>> xxd <bytecode filename>

This command is used to read binary files in hexadecimal format


