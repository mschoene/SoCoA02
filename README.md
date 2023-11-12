# SoCoA02
Welcome to the Little German Language (LGL) user guide, where everything is 3 times more complicated to formulate. Enjoy!

# Usage
## Basics
To test the basic functionality of the LGL run the following comand:
python lgl_language.py example_operations.gsc

## Class functionality
python lgl_interpreter.py example_class.gsc 
outputs −−−−→ 0.96 or similar

## Tracing functionality
python lgl_interpreter.py example_trace.gsc --trace trace_file.log


## Pretty reporting
To see the number of calls, total and average run time of each of the functions run:

python reporting.py trace_file.log