# SoCoA02
Welcome to the Little German Language (LGL) user guide, where everything is 3 times more complicated to formulate. Enjoy!

# Usage
## Basics
To test the basic functionality of the LGL run the following command:
python lgl_language.py example_operations.gsc

This will print the result of a while loop, setting the values doubled and squared in a list each. 
These lists are then used to define two dictionaries, where 2 values are afterwards updated. In the end the dictionaries are combined together.

## Class functionality
To see the class functionality run the following command:

python lgl_interpreter.py example_class.gsc 

This returns a value of about 0.96.

## Tracing functionality
python lgl_interpreter.py example_trace.gsc --trace trace_file.log


## Pretty reporting
To see the number of calls, total and average run time of each of the lgl in the example trace run:

python reporting.py trace_file.log
