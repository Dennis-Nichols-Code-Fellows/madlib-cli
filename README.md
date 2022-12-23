# LAB - Class 03

## Project: Madlib-cli
### Author: Dennis Nichols

## How to run

`python madlib.py`

## Tests

- run with pytest-watch
- tests included:
  - checking that template file read in correctly
  - check that template string and parts of speech are able to be extracted
  - check that merging user words and the template works
  - check that FileNotFoundError is appropriately raised.
  - Check that templates with multi-word prompts are properly parsed
  - Check that user input of empty strings, numbers, and symbols are properly handled

**Note that running the tests has problems once the full game is written because of the presence of input functions. If you need to check the tests, first comment out the game logic and just leave the functions in the madlib.py file**
