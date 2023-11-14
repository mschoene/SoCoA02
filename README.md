# SoCoA02
Welcome to the Little German Language (LGL) user guide, where everything is 3 times more complicated to formulate. Enjoy!

# Usage
## Basics
To test the basic functionality of the LGL run the following command:
```console
python lgl_language.py example_operations.gsc
```
This will print the result of a while loop, setting the values doubled and squared in a list each. 
These lists are then used to define two dictionaries, where 2 values are afterwards updated. In the end the dictionaries are combined together.

## Class Functionality
To see the class functionality run the following command:
```console
python lgl_interpreter.py example_class.gsc 
```
This returns a value of about 0.96 for the sum of the densities.

## Tracing Functionality
To trace the duration of the functions defined in lgl run:
```console
python lgl_interpreter.py example_trace.gsc --trace trace_file.log
```

## Pretty Reporting
To see the number of calls, total and average run time of each of the functions defined in lgl in the example_trace.gsc, run:
```console
python reporting.py trace_file.log
```
## Supported Operations 
### Mathematical Operations
- Multiplication: do_multiplizieren
- Division: do_dividieren (Does not allow division by zero)
- Power: do_hochstellen
- Addition: do_addieren
- Absolute Value: do_absolutwert
- Subtraction: do_subtrahieren

### Comparison Operations
- Less Than: do_kleiner_als

### Looping
- While Loop: do_waehrend

### Arrays
- Create Array: do_liste
- Get Value at Index: do_abrufen_listenObj
- Set Value at Index: do_setzen_listenObj

### Dictionaries
- Create Dictionary: do_woerterbuch
- Get Value by Key: do_abrufen_schluessel
- Set Value by Key: do_setzen_schluessel_wert
- Dictionary Union: do_woerterbuch_vereinigung

### Class Functionalities
- Define Class: do_klasse
- Create Class Instance: do_klassen_instanz
- Call Class Method: do_klassen_aufrufen
- Look for parent object recursively: do_klassen_finden

### Other Operations
- Function Definition: do_funktion
- Function Call: do_aufrufen
- Set Variable: do_setzen
- Get Variable Value: do_abrufen
- Print: do_drucken
- Sequential Execution: do_abfolge
