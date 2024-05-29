# Odd or Even

## Instructions

Write a program to determine if a given number is odd or even.

Even numbers can be divided by 2 without any remainder.

**Example:**

- 42 is even because 42 ÷ 2 = 21. Since 21 is a whole number, 42 is even.
- 37 is odd because 37 ÷ 2 = 18.5. Since 18.5 is not a whole number and has a remainder of 0.5, 37 is odd.

The modulo operator in Python is represented by the percentage sign (%). It provides the remainder of a division.

**Examples:**

- 10 ÷ 2 = 5 with no remainder: `10 % 2 = 0`
- 9 ÷ 2 = 4 with a remainder of 1: `9 % 2 = 1`
- 25 ÷ 4 = 6 with a remainder of 1: `25 % 4 = 1`

Your output should match the format exactly, including the positions of commas and periods.

### Example Input 1

```python
37
```

### Example Output 1

```python
This is an odd number.
```

### Example Input 2

```python
42
```

### Example Output 2

```python
This is an even number.
```

When you run your program, the output should be:

**Example:**

```python
37
This is an odd number.
```

## Hint

All even numbers can be divided by 2 with 0 remainder.

Test the modulo operation with some odd numbers:

- `7 % 2`
- `11 % 2`
- `15 % 2`

Then test with some even numbers:

- `8 % 2`
- `12 % 2`
- `16 % 2`

Notice the common result for even and odd numbers.
