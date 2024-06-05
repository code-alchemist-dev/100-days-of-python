# Treasure Map

## Instructions

You are tasked with creating a program that marks a specific spot on a map with an "X".

In the initial code, there is a variable named `map` that contains a nested list. When printed, this nested list appears as follows:

```python
[['⬜️', '⬜️', '⬜️'], 
 ['⬜️', '⬜️', '⬜️'], 
 ['⬜️', '⬜️', '⬜️']]
```

The code includes new lines (`\n`) to format the three rows into a square for better readability, as shown below:

```python
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```

This layout simulates coordinates on a real map.

Your task is to develop a program that allows a user to mark a square on this map using a two-digit input. The first digit specifies the column (horizontal position), and the second digit specifies the row (vertical position).

1. **Input Conversion:** Your program must first take user input and convert it into a usable format.
2. **Update Map:** Use the formatted input to update the nested list by placing an "X" at the specified coordinates.

### Example

**Example Input 1:**

- Column 2, Row 3 should be entered as `23`.

**Example Output 1:**

```python
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
```

**Example Input 2:**

- Column 3, Row 1 should be entered as `31`.

**Example Output 2:**

```python
['⬜️', '⬜️', 'X']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```

### Example Execution

When the program is executed, the output should resemble the following:

```python
[['⬜️', '⬜️', '⬜️'],
 ['⬜️', '⬜️', '⬜️'],
 ['⬜️', 'X', '⬜️']]
```

### Hint

- Remember that lists in Python are zero-indexed.
- The variable `map` refers to a nested list and is not related to the `map` function in Python.
