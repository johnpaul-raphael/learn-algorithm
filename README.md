# Learn Algorithm — Python DSA & Interview Prep

A structured learning repository for Python fundamentals, data structures, and algorithms — organized around LeetCode problems and the Striver's A2Z DSA sheet.

---

## Repository Structure

```
learn-algorithm/
├── python-fundamentals.ipynb         # Python basics, strings, loops
├── python-oops-basic.ipynb           # OOP: classes, inheritance, polymorphism
├── string_manipulation.ipynb         # 13 string algorithm problems
├── leetcode algorithm.ipynb          # Sliding window, sorting, Kadane's
├── leetcode_problems.ipynb           # LeetCode problem solutions
├── common class discussion.ipynb     # Number theory, matrices, patterns
├── strivers-a2z-dsa-sheet.ipynb      # Striver's A2Z DSA roadmap
├── Java_vs_Python_LeetCode_CheatSheet.pdf
├── system_design_roadmap.pdf
├── interview_prep_tracker 2025.xlsx
├── leetcode problem list.xlsx
└── README.md
```

---

## Learning Path

Follow the notebooks in this order:

| Step | Notebook | Topics |
|------|----------|--------|
| 1 | `python-fundamentals.ipynb` | Loops, strings, slicing, comprehensions, modulo |
| 2 | `python-oops-basic.ipynb` | Classes, inheritance, polymorphism, encapsulation, abstraction |
| 3 | `string_manipulation.ipynb` | String algorithms — rotation, compression, palindromes |
| 4 | `leetcode algorithm.ipynb` | Sliding window, binary search, sorting algorithms, Kadane's |
| 5 | `strivers-a2z-dsa-sheet.ipynb` | Sorting, arrays, bit manipulation, XOR patterns |
| 6 | `leetcode_problems.ipynb` | Applied LeetCode problem solutions |
| 7 | `common class discussion.ipynb` | Number theory, matrix traversal, DP, pattern printing |

---

## Topics Covered

### Python Fundamentals
- String operations: reverse, split, slice, replace, vowel filter
- List operations: comprehensions, reversal, slicing
- Loops and conditionals
- `divmod`, modulo operations

### Object-Oriented Programming
- Class definition, `__init__`, attributes
- Single, multiple, multilevel, and hierarchical inheritance
- Polymorphism via method overriding
- Encapsulation: public / protected `_` / private `__`
- Abstraction with `ABC` and `@abstractmethod`
- Exception handling: `try / except / else / finally`

### String Algorithms
- Reverse every k-character chunk
- Left rotate string by k positions
- Run-length encoding (compress/expand)
- Count palindromic substrings of length k
- Check if one string is a rotation of another
- Remove duplicates, invert case, replace digits with names
- Longest run of identical characters

### Sorting Algorithms
| Algorithm | Time Complexity | Space |
|-----------|----------------|-------|
| Bubble Sort | O(n²) | O(1) |
| Selection Sort | O(n²) | O(1) |
| Insertion Sort | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) avg | O(log n) |

### Search Algorithms
- Linear Search — O(n)
- Binary Search — O(log n)

### Array Techniques
- Sliding window (fixed and dynamic)
- Two-pointer technique
- Kadane's Algorithm (max/min subarray)
- Circular subarray: `total_sum - min_subarray`
- Streak counting pattern
- Sort Colors (Dutch National Flag — 0, 1, 2)

### Bit Manipulation (XOR Patterns)
- Find the single number when all others appear twice
- Missing number in a range
- Two unique numbers when all others appear twice
- Single number when others appear three times

### LeetCode Problems Solved

| # | Problem | Technique |
|---|---------|-----------|
| 20 | Valid Parentheses | Stack |
| 22 | Generate Parentheses | Recursion |
| 32 | Longest Valid Parentheses | Stack / DP |
| 53 | Maximum Subarray | Kadane's Algorithm |
| 75 | Sort Colors | Two-pointer (DNF) |
| 80 | Remove Duplicates II | Two-pointer |
| 121 | Best Time to Buy and Sell Stock | Greedy |
| 125 | Valid Palindrome | Two-pointer |
| 152 | Maximum Product Subarray | DP (track max & min) |
| 260 | Single Number III | XOR / Bit manipulation |
| 268 | Missing Number | XOR |
| 301 | Remove Invalid Parentheses | BFS / Backtracking |
| 496 | Next Greater Element | Monotonic Stack |
| 678 | Valid Parenthesis String | Greedy |
| 918 | Maximum Sum Circular Subarray | Kadane's variant |
| 1021 | Remove Outermost Parentheses | Stack counter |

### Number Theory
- Ugly Numbers (factors: 2, 3, 5 only)
- Digital Root / Digital Sum
- Happy Number (sum of squares of digits)
- Digit sum of n!

### Matrix Traversal
- Row-wise and column-wise iteration
- Main diagonal (top-left to bottom-right)
- Anti-diagonal (top-right to bottom-left)

### Pattern Printing
- Square, triangle, number pyramids
- Staircase number patterns

---

## Reference Materials

| File | Purpose |
|------|---------|
| `Java_vs_Python_LeetCode_CheatSheet.pdf` | Side-by-side syntax comparison for interviews |
| `system_design_roadmap.pdf` | System design interview roadmap |
| `interview_prep_tracker 2025.xlsx` | Track problems solved, difficulty, and review dates |
| `leetcode problem list.xlsx` | Curated problem list organized by topic |

---

## What to Learn Next

These topics are not yet in the repo — work through them in order:

### Data Structures
- [ ] Linked List (singly, doubly, circular)
- [ ] Stack and Queue (array-based and linked-list-based)
- [ ] Hash Map / Hash Set (collision handling, chaining)
- [ ] Binary Tree and Binary Search Tree
- [ ] Heap / Priority Queue
- [ ] Graph (adjacency list and matrix)
- [ ] Trie (prefix tree)

### Algorithms
- [ ] BFS and DFS (trees and graphs)
- [ ] Backtracking (subsets, permutations, N-Queens)
- [ ] Dynamic Programming (0/1 knapsack, LCS, LIS, coin change)
- [ ] Greedy Algorithms (activity selection, Huffman)
- [ ] Divide and Conquer (binary search variations)
- [ ] Union-Find / Disjoint Set

### Python-Specific Skills
- [ ] `collections` module: `deque`, `Counter`, `defaultdict`, `OrderedDict`
- [ ] `heapq` module for min/max heaps
- [ ] `bisect` module for binary search on sorted lists
- [ ] Generators and iterators
- [ ] Decorators and context managers
- [ ] Time and space complexity analysis for every solution

---

## How to Use

```bash
# Clone the repo
git clone <repo-url>
cd learn-algorithm

# Open in VS Code
code .

# Or start Jupyter
jupyter notebook
```

Open any `.ipynb` file in VS Code or JupyterLab to run cells interactively.

---

## Progress Tracking

Use `interview_prep_tracker 2025.xlsx` to log:
- Problems attempted and solved
- Difficulty level (Easy / Medium / Hard)
- Techniques used
- Review dates for spaced repetition

---

*Personal learning repository — Python DSA and interview preparation.*
