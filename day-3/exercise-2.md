# Leap Year Challenge

## Instructions

Write a program to determine whether a given year is a leap year. A standard year has 365 days, whereas a leap year has 366 days, with an extra day in February. The concept of leap years is quite intriguing; for a more detailed explanation, please refer to the following video:

[Leap Year Explained](https://www.youtube.com/watch?v=xX96xng7sAE)

### Determining a Leap Year

A year qualifies as a leap year if it meets the following criteria:

1. The year is evenly divisible by 4.
2. However, if the year is evenly divisible by 100, it is **not** a leap year unless:
3. The year is also evenly divisible by 400.

#### Examples

**Year 2000:**

- 2000 ÷ 4 = 500 (Leap Year)
- 2000 ÷ 100 = 20 (Not a Leap Year)
- 2000 ÷ 400 = 5 (Leap Year!)

Thus, the year 2000 is a leap year.

**Year 2100:**

- 2100 ÷ 4 = 525 (Leap Year)
- 2100 ÷ 100 = 21 (Not a Leap Year)
- 2100 ÷ 400 = 5.25 (Not a Leap Year)

Therefore, the year 2100 is not a leap year.

**Important:** Ensure that your output format matches the example output exactly, including the placement of commas and periods.

### Example Inputs and Outputs

**Example Input 1:**

```python
2400
```

**Example Output 1:**

```python
Leap year.
```

**Example Input 2:**

```python
1989
```

**Example Output 2:**

```python
Not leap year.
```

### Hint

To better understand the rules, consider creating a flowchart at [draw.io](https://www.draw.io). If you encounter difficulties, you can view a flowchart I created for this purpose.
