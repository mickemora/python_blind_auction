# Python Blind Auction

This repository contains a simple command-line **Blind Auction** program built in Python.

The application collects bidder names and bid amounts, stores each bid, and identifies the highest bidder once all bids have been entered.

## Project Overview

This project simulates a basic blind auction process.

In a blind auction, bidders submit their bids without seeing the other bids. After all bids are submitted, the program compares the submitted amounts and announces the winner.

The program prompts each user for:

- Bidder name
- Bid amount
- Whether there are additional bidders

When there are no more bidders, the program identifies and displays the highest bidder.

## Main Objective

The objective of this project is to practice foundational Python programming concepts by building a simple interactive command-line application.

The project demonstrates how to:

- Capture user input
- Store structured data
- Use dictionaries
- Use lists
- Loop until a condition is met
- Compare numeric values
- Create and call functions
- Display a final result based on collected data

## Repository Structure

```text
.
├── main.py
├── art.py
└── README.md
```

## Technologies Used

- Python

No external libraries are required.

## File Descriptions

### `main.py`

This is the main application file.

It imports and displays the auction logo from `art.py`:

```python
import art
print(art.logo)
```

The script then initializes the main control variables:

```python
other_bidders = "yes"
bidders = {}
final_list = []
```

The application collects bidder information in a loop and stores each bidder as a dictionary:

```python
bidders = {
    "name": name,
    "bid": bid,
}
```

Each dictionary is appended to `final_list`:

```python
final_list.append(bidders)
```

When there are no more bidders, the program calls:

```python
identify_highest_bidder(final_list)
```

### `art.py`

This file stores the ASCII art logo used by the program.

The logo represents an auction gavel and is displayed when the program starts.

## Main Function

The main function in the program is:

```python
def identify_highest_bidder(dictionary):
```

Despite the parameter name, the function receives a list of bidder dictionaries.

It loops through each bidder record, compares bid amounts, and tracks the highest bid and bidder name.

When complete, it prints the winner:

```text
The highest bidder is: [name] with a bid of $[amount] dollars.
```

## How the Program Works

The application follows this flow:

```text
Start program
    ↓
Display auction logo
    ↓
Ask for bidder name
    ↓
Ask for bid amount
    ↓
Store bidder and bid
    ↓
Ask if there are more bidders
    ↓
More bidders?
    → Yes: continue collecting bids
    → No: identify highest bidder
    ↓
Display winner
```

## Example Interaction

```text
What's your name? mike
What's your bid? $100
are there any other bidders? Type Yes or No : yes
Bye
What's your name? ana
What's your bid? $150
are there any other bidders? Type Yes or No : no
The highest bidder is: ana with a bid of $150 dollars.
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/mickemora/python_blind_auction.git
```

2. Navigate into the project directory:

```bash
cd python_blind_auction
```

3. Run the application:

```bash
python main.py
```

Depending on your environment, you may need to use:

```bash
python3 main.py
```

## Key Programming Concepts Demonstrated

This project demonstrates several core Python concepts:

- Variables
- User input
- String normalization with `.lower()`
- Integer conversion with `int()`
- Dictionaries
- Lists
- Appending items to a list
- While loops
- For loops
- Functions
- Conditional logic
- Value comparison
- Tracking maximum values
- Importing from another Python file
- ASCII art display

## Known Issues / Improvement Opportunities

The current code is a learning exercise and has several areas that could be improved:

- The `identify_highest_bidder()` parameter is named `dictionary`, but it actually receives a list of dictionaries.
- The program does not validate non-numeric bid input.
- The program does not handle negative bids.
- The screen-clearing function is commented out.
- The message `Bye` is printed between bidders instead of clearing the screen.
- Bidder names are converted to lowercase, which may remove preferred capitalization.
- The code does not handle ties between bidders.

## Potential Enhancements

Future improvements could include:

- Add input validation for bids
- Prevent negative or zero-value bids
- Handle ties between bidders
- Replace `Bye` with a clear-screen function
- Preserve bidder name capitalization
- Refactor the bidder collection logic into functions
- Rename variables for clarity
- Add automated tests
- Add support for saving auction results to a file
- Add a replay option for multiple auctions
- Convert the program into a web-based bidding form

## Summary

This project is a simple Python command-line blind auction program. It is useful for practicing user input, dictionaries, lists, loops, functions, and comparison logic. The program collects bids from multiple users and identifies the highest bidder at the end of the auction.
