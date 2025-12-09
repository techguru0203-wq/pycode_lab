# 🚀 Overview

### pycode_lab contains five small Python programs, each focusing on a specific algorithmic problem or logic pattern. They require no external dependencies and run on any modern Python 3 interpreter.

### Each script is self-contained, easy to read, and includes example usage at the bottom.

## 📁 Included Scripts
###  1. league_table.py

Implements a LeagueTable class that:

Stores players

Tracks wins and scores

Ranks them by score (with number of games as a tiebreaker)

Example output:
Chris

### 2. icecream_machine.py

Generates all combinations of:

Ingredients

Toppings

Great example of a Cartesian product using simple Python loops.

Example output:
```bash
[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
```
### 3. sorted_search.py

Implements: 
```bash
count_numbers(sorted_list, less_than)
```

Uses binary search logic to count how many values in a sorted list are less than a given number.

Example output:
```text
2
```

### 4. two_sum.py

Classic algorithm problem:
```bash
find_two_sum(nums, target)
```

Returns indices of two values that sum to a target.
Efficient solution using a dictionary for O(n) lookups.

Example output:
```text
(0, 3)
```

5. merge_names.py

Merges two lists of names and removes duplicates using set operations.

Example output:
```text
['Sophia', 'Olivia', 'Ava', 'Emma']
```

---

## 🧰 Tech Stack

Language: Python 3.6+

Dependencies: None (standard library only)

Optional: Python virtual environment (venv)

No frameworks. No extra requirements. Zero setup complexity.

---

## ▶️ How to Run

### 1.Clone the repository:
```bash
git clone https://github.com/your-username/pycode_lab.git
```

```bash
cd pycode_lab
```

### 2.(Optional) Create and activate a virtual environment:
```bash    
python3 -m venv .venv
```

```bash
source .venv/bin/activate     # Windows: .venv\Scripts\activate
```

### 3.Run any example script:
```bash
python league_table.py
```

```bash
python icecream_machine.py
```

```bash
python sorted_search.py
```

```bash
python two_sum.py
```

```bash
python merge_names.py
```


---


## 🔄 Continuous Integration (Optional)

A simple GitHub Actions CI workflow is included to automatically run each script on:

    Every push

    Every pull request

This ensures everything keeps working as you update the repo.