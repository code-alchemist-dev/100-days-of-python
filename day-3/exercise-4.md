# Love Compatibility Calculator

## Instructions

This program calculates the compatibility between two individuals by generating a "love score."

To determine the love score between two people:

1. Take both names and count the occurrences of the letters in the word "TRUE."
2. Count the occurrences of the letters in the word "LOVE."
3. Combine these counts to create a two-digit number.

### Interpretation of the Love Score

- For love scores less than 10 or greater than 90, the message should be:
  "Your score is **x**, you go together like coke and mentos."

- For love scores between 40 and 50, the message should be:
  "Your score is **y**, you are alright together."

- For all other scores, simply display the score:
  "Your score is **z**."

### Example Calculation

#### Input

```python
name1 = "Alice Johnson"
name2 = "Bob Smith"
```

#### Calculation

- T occurs 1 time
- R occurs 0 times
- U occurs 1 time
- E occurs 1 time

Total for "TRUE" = 3

- L occurs 1 time
- O occurs 2 times
- V occurs 0 times
- E occurs 1 time

Total for "LOVE" = 4

#### Love Score

Love Score = 34

#### Output

"Your score is 34."

### Example Scenarios

#### Example Input 1

```python
name1 = "Kanye West"
name2 = "Kim Kardashian"
```

#### Example Output 1

```python
Your score is 42, you are alright together.
```

#### Example Input 2

```python
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
```

```python
Your score is 73.
```

### Testing and Validation

Ensure that your output matches one of the following formats:

- "Your score is 47, you are alright together."
- "Your score is 125, you go together like coke and mentos."
- "Your score is 54."

### Score Comparison Table

Use the table below to verify your results:

| Name 1                  | Name 2                | Score |
|-------------------------|-----------------------|-------|
| Catherine Zeta-Jones    | Michael Douglas       | 99    |
| Brad Pitt               | Jennifer Aniston      | 73    |
| Prince William          | Kate Middleton        | 67    |
| Bright Mabuza           | Lebohang Maloka       | 53    |
| Kanye West              | Kim Kardashian        | 42    |
| Beyonce                 | Jay-Z                 | 23    |
| John Lennon             | Yoko Ono              | 18    |

### Useful Tips

- The `lower()` function converts all characters in a string to lowercase. More details can be found [here](https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python).
- The `count()` function returns the number of occurrences of a substring in a string.
