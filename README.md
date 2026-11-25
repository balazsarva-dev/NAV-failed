[**Play it in the browser**](https://balazsarva-dev.github.io/NAV-failed/)

# Python Game Center

Small Python console games (calculator, quadratic equation solver, chicken & rabbit puzzle, number guessing, lotto, rock-paper-scissors).

## Play in the browser

The unchanged Python code runs in the browser via [PyScript](https://pyscript.net) (Pyodide / WebAssembly).

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

A static server is required (opening `index.html` via `file://` does not work). `mini-coi.js` enables cross-origin isolation so `input()` works on static hosts such as GitHub Pages or Vercel.

## Run in the terminal

```bash
cd python
python3 main.py
```

## Project structure

```
index.html      # browser entry point (PyScript terminal)
pyscript.toml   # maps python/*.py into the browser's virtual filesystem
mini-coi.js     # service worker for cross-origin isolation
python/         # the original Python sources
```

### Task
Let's solve a classic Chinese puzzle using Python! The puzzle is as follows: "In a yard, rabbits and chickens are basking in the sun. I was able to count a total of 35 heads and 94 legs. How many chickens and rabbits were there in the yard?" Hint: use a for loop to count all possible solutions! The perfect solution is a function(s) that: generally finds a solution for any number of heads and legs (if it exists) asks for the data to do so, checks the input data (e.g. text, float, negative integer), checks whether the problem has or is even possible to solve based on the data (e.g. odd legs). prints out the possible solution, solutions In this case, the number of heads and legs is the input parameter, and the number of rabbits/chickens is the output of the function.


### Task
Creating a 4-operation calculator using Python.

Operations:
- addition
- subtraction
- multiplication
- division

The ideal solution offers a menu from which you can select what operation you want to perform (selecting 1-4 is the 4 basic operations, to do this, it requests the data (referring to it according to the operation), checks the data, performs the operation, and prints the result with formatting to include both the incoming data and the result, offers the menu again.

### Task
Quadratic equation solver using Python.

The ideal solution checks the data, based on the Discriminant, writes out how many solutions the equation has, and calculates them. It uses regex when the user enters the equation during the process to decide whether it is valid or not. 

### Task
Lotto game.

### Task
Rock, scissors, paper game.
