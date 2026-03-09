# 🚀 DSA Mastery — Python Edition

> **Solving LeetCode problems systematically. One problem per day. Consistency over perfection.**

<div align="center">

![Python](https://img.shields.io/badge/Language-Python%203.11%2B-blue?style=for-the-badge&logo=python)
![LeetCode](https://img.shields.io/badge/LeetCode-Accepted-brightgreen?style=for-the-badge&logo=leetcode)
![Problems](https://img.shields.io/badge/Problems%20Solved-5-brightgreen?style=for-the-badge)
![Streak](https://img.shields.io/badge/🔥%20Current%20Streak-Day%205-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active%20Development-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

**[Problems](#-problems-solved) • [Structure](#-folder-structure) • [How to Use](#-how-to-run) • [Progress](#-progress-tracker) • [Contribute](#-contributing)**

</div>

---

## 👨‍💻 About Me

| Aspect | Details |
|--------|---------|
| 🎓 **Education** | B.Tech Computer Science & Engineering — 2nd Year |
| 🐍 **Language** | Python (3.11+) with Modern Syntax |
| 🎯 **Goals** | Placement Preparation • Internship Hunt • Strong DSA Foundation |
| 💼 **Focus** | LeetCode Hard/Medium Problems • System Design Fundamentals |

---

## 📊 Quick Stats

```
Total Problems:  5
├── 🟢 Easy:     2 
├── 🟡 Medium:   2
├── 🔴 Hard:     1
└── ⏳ In Progress: 2

Current Streak: 🔥 Day 5
Best Time: Early Morning (6-8 AM)
```

---

## 📂 Folder Structure

```
DSA-Practice/
│
├── 📋 README.md
├── 📄 LICENSE
├── .gitignore
│
├── 🎯 Arrays/
│   ├── concatenation_of_array.py
│   ├── two_sum.py
│   └── median_of_two_sorted_arrays.py
│
├── 🔗 LinkedList/
│   ├── add_two_numbers.py
│   └── add_two_numbers_leetcode.py
│
├── 📝 Strings/
│   ├── longest_substring.py
│   ├── longest_substring_leetcode.py
│   ├── longest_palindromic_substring.py
│   └── longest_palindromic_substring_leetcode.py
│
├── 🌳 Trees/ (In Progress)
│   └── (Coming Soon)
│
├── 🔍 BinarySearch/ (In Progress)
│   └── (Coming Soon)
│
└── 💾 Solutions_Archive/
    └── (Backup solutions with multiple approaches)
```

---

## ✅ Problems Solved

### 📌 Problem Table

| # | Day | Topic | Problem | Level | Status | Time | Space | Approach |
|---|-----|-------|---------|-------|--------|------|-------|----------|
| 1 | Day 1 | Arrays | [Concatenation of Array](./Arrays/concatenation_of_array.py) | 🟢 Easy | ✅ Accepted | O(n) | O(n) | Linear Scan |
| 2 | Day 2 | Arrays | [Two Sum](./Arrays/two_sum.py) | 🟢 Easy | ✅ Accepted | O(n) | O(n) | HashMap |
| 3 | Day 3 | Linked List | [Add Two Numbers](./LinkedList/) | 🟡 Medium | ✅ Accepted | O(max(m,n)) | O(max(m,n)) | Dummy Node + Carry |
| 4 | Day 4 | Strings | [Longest Substring Without Repeating Characters](./Strings/) | 🟡 Medium | ✅ Accepted | O(n) | O(min(m,n)) | Sliding Window + HashMap |
| 5 | Day 5 | Strings | [Longest Palindromic Substring](./Strings/longest_palindromic_substring_leetcode.py) | 🟡 Medium | ✅ Accepted | O(n²) | O(1) | Expand Around Center |

---

## 🎯 Today's Focus: Median of Two Sorted Arrays

### Problem Details
```
LeetCode #4 | Hard Level
Given two sorted arrays nums1 and nums2 of size m and n
Return the median of the two sorted arrays
Constraint: O(log(m+n)) Time Complexity Required
```

### Solution Approach
```python
Binary Search on Smaller Array
├── Partition both arrays at positions
├── Ensure: left_partition_max ≤ right_partition_min
├── Handle even/odd length cases
└── Time: O(log(min(m,n))) ✅
    Space: O(1) ✅
```

### Files Available
- 📄 **[Normal Solution](./Arrays/median_of_two_sorted_arrays.py)** — Full implementation with tests
- 🎯 **[LeetCode Format](./Arrays/median_of_two_sorted_arrays_leetcode.py)** — Submission-ready code

---

## 💡 My Approach to Problem Solving

```mermaid
graph LR
    A["📖 Read & Understand"] --> B["🧠 Identify Pattern"]
    B --> C["⚡ Brute Force"]
    C --> D["🚀 Optimize"]
    D --> E["✍️ Code"]
    E --> F["🧪 Test Edge Cases"]
    F --> G["📤 Submit"]
    G --> H["💾 Archive"]
```

### Key Principles
1. **Understand First** — Read problem 2-3 times
2. **Brute Force First** — Always start simple
3. **Pattern Recognition** — Identify data structure needs
4. **Optimize Smartly** — Use better data structures/algorithms
5. **Test Thoroughly** — Edge cases matter!
6. **Comment Generously** — Future you will thank you
7. **Archive Solutions** — Build a reference library

---

## 🚀 How to Run

### Prerequisites
```bash
Python 3.11+
pip install -r requirements.txt  # (if needed)
```

### Run Individual Problems

#### Arrays
```bash
# Concatenation of Array
python Arrays/concatenation_of_array.py

# Two Sum
python Arrays/two_sum.py

# Median of Two Sorted Arrays
python Arrays/median_of_two_sorted_arrays.py
```

#### Strings
```bash
# Longest Palindromic Substring
python Strings/longest_palindromic_substring.py
```

#### Linked List
```bash
# Add Two Numbers
python LinkedList/add_two_numbers.py
```

### Run LeetCode Format
```bash
# Copy the *_leetcode.py file content to LeetCode editor
# All solutions are tested and ready for submission
```

---

## 📈 Progress Tracker

### By Difficulty
```
🟢 Easy:   ████████░░ 40% (2/5)
🟡 Medium: ██████████ 40% (2/5)
🔴 Hard:   ██░░░░░░░░ 20% (1/5)
```

### By Topic
```
Arrays:       ███░░░░░░░░ 30% (3/10)
Strings:      ██░░░░░░░░░ 20% (2/10)
LinkedList:   ██░░░░░░░░░ 10% (1/10)
Trees:        ░░░░░░░░░░░  0% (0/10)
Graphs:       ░░░░░░░░░░░  0% (0/10)
DP:           ░░░░░░░░░░░  0% (0/10)
```

### Streak & Consistency
```
Current Streak:     🔥 5 Days
Longest Streak:     5 Days
Problems This Week: 5
Problems This Month: 5
```

---

## 📚 Problem Topics Roadmap

### Phase 1: Foundation (Current Phase)
- [x] **Arrays** — Basic operations, searching, sorting
- [x] **Strings** — Substring, palindrome, patterns
- [x] **Linked Lists** — Traversal, manipulation
- [ ] **Hash Maps** — Next week

### Phase 2: Intermediate (Next)
- [ ] **Stack & Queue** — LIFO, FIFO problems
- [ ] **Binary Search** — Search problems
- [ ] **Recursion** — DFS, backtracking

### Phase 3: Advanced
- [ ] **Trees** — BST, traversals, paths
- [ ] **Graphs** — BFS, DFS, shortest path
- [ ] **Dynamic Programming** — Optimization problems

---

## 🎓 Code Quality Standards

Each solution includes:

✅ **Clear Comments** — Explain the logic  
✅ **Type Hints** — Full Python 3.9+ annotations  
✅ **Docstrings** — Problem statement + approach  
✅ **Edge Cases** — Handled explicitly  
✅ **Test Cases** — Comprehensive validation  
✅ **Complexity Analysis** — Time & Space explained  
✅ **Modern Python** — Latest syntax & best practices  

### Example Structure
```python
"""
Problem #XXX: Problem Name
Difficulty: Medium | Time: O(n) | Space: O(n)
Approach: Description of the approach
"""

from typing import List

class Solution:
    def solveProblem(self, param: List[int]) -> int:
        """
        Core function with full docstring.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Implementation
        pass
```

---

## 🔧 Technologies & Tools

| Tool | Usage |
|------|-------|
| **Python 3.11+** | Core language with modern syntax |
| **LeetCode** | Problem source & validation |
| **Git** | Version control |
| **GitHub** | Repository hosting |
| **VS Code** | Development environment |

---

## 📖 Resources Used

### Learning Platforms
- 🎯 [LeetCode](https://leetcode.com) — Problem source
- 🎬 [GeeksforGeeks](https://www.geeksforgeeks.org) — DSA concepts
- 📚 [InterviewBit](https://www.interviewbit.com) — Interview prep
- 💻 [HackerRank](https://www.hackerrank.com) — Extra practice

### Reference Books
- "Cracking the Coding Interview" — McDowell
- "Introduction to Algorithms" — CLRS
- "Competitive Programming" — Halim & Halim

---

## 🎬 Getting Started

### For Beginners
1. Clone the repository
2. Start with **Easy problems** (Arrays folder)
3. Read both normal & LeetCode solutions
4. Run tests locally before submitting
5. Try harder variations once confident

### For Advanced Users
1. Focus on **Medium & Hard** problems
2. Optimize space/time complexities
3. Try multiple approaches
4. Contribute optimizations back

---

## 💪 Daily Routine

```
6:00 AM — Wake up & coffee ☕
6:30 AM — Read 1 new problem
7:00 AM — Solve on paper (10 min)
7:10 AM — Code solution (20 min)
7:30 AM — Debug & test (10 min)
8:00 AM — Push to GitHub & move on 🚀
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

### To Submit Optimizations
1. Fork the repository
2. Create a new branch (`git checkout -b optimization/problem-name`)
3. Make changes with clear comments
4. Commit with descriptive messages
5. Push and create a Pull Request

### To Report Issues
- Open an issue with problem details
- Include input/output expectations
- Provide test cases if possible

### Code Style
```bash
# Format code
python -m black your_file.py

# Check linting
python -m pylint your_file.py
```

---

## 📊 Performance Metrics

### Success Rate
```
LeetCode Submissions: 5/5 ✅ 100%
Test Cases Passed:    45/45 ✅ 100%
```

### Time to Solve (Average)
```
Easy:     8 mins
Medium:   22 mins
Hard:     45+ mins
```

---

## 🎯 Next Steps (This Week)

- [ ] Solve 2 more Medium problems
- [ ] Start Hash Map topic
- [ ] Review binary search basics
- [ ] Practice recursion fundamentals

---

## 📞 Connect With Me

| Platform | Handle |
|----------|--------|
| 🐙 GitHub | [@yourusername](https://github.com) |
| 💼 LinkedIn | [Your Name](https://linkedin.com) |
| 🐦 Twitter | [@yourhandle](https://twitter.com) |
| 📧 Email | your.email@example.com |

---

## 📝 License

This project is licensed under the **MIT License** — feel free to use it for learning.

```
MIT License
Copyright (c) 2024 Your Name
Permission is hereby granted...
```

---

## 🙏 Acknowledgments

Special thanks to:
- LeetCode community for amazing problems
- GeeksforGeeks for clear explanations
- Open-source Python community

---

<div align="center">

### 💭 Remember
```
"The only way to do great work is to love what you do." — Steve Jobs

Keep coding, keep learning, keep pushing! 🚀
```

**Last Updated:** January 2025  
**Next Update:** Weekly  
**Status:** 🟢 Actively Maintained

[⬆ back to top](#-dsa-mastery--python-edition)

</div>