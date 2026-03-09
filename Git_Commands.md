# 🚀 Git Commands Guide — DSA Practice Repository

<div align="center">

![Git](https://img.shields.io/badge/Version%20Control-Git-red?style=for-the-badge&logo=git)
![GitHub](https://img.shields.io/badge/Platform-GitHub-black?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Guide-Complete-brightgreen?style=for-the-badge)

**Master Git in 5 minutes | Push code like a pro 🎯**

</div>

---

## 📌 Table of Contents

1. [⚡ Quick Start](#-quick-start---30-seconds)
2. [📚 Step-by-Step Setup](#-step-by-step-setup-first-time-only)
3. [🎯 Daily Workflow](#-daily-workflow-after-solving-problems)
4. [💡 Common Commands](#-common-commands)
5. [🛠️ Advanced Git](#️-advanced-git-commands)
6. [❌ Troubleshooting](#-troubleshooting--error-fixes)
7. [📝 Commit Message Examples](#-commit-message-examples)

---

## ⚡ Quick Start — 30 Seconds

> **First time? Copy-paste this entire block:**

```bash
cd DSA-Practice
git init
git remote add origin https://github.com/YOUR_USERNAME/DSA-Practice.git
git add .
git commit -m "Day 5: Add Longest Palindromic Substring + Premium README"
git push -u origin main
```

✅ **Done!** Your code is live on GitHub.

---

## 📚 Step-by-Step Setup (First Time Only)

### Step 1️⃣: Initialize Repository

```bash
# Navigate to your project folder
cd DSA-Practice

# Initialize git
git init
```

**What it does:** Creates a `.git` folder to track changes.

---

### Step 2️⃣: Add GitHub as Remote

```bash
# Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/DSA-Practice.git

# Verify connection
git remote -v
```

**What it does:** Links your local folder to GitHub.

---

### Step 3️⃣: Configure Your Identity

```bash
# Set your name (visible in commits)
git config --global user.name "Your Name"

# Set your email (must match GitHub email)
git config --global user.email "your.email@example.com"
```

**What it does:** Stamps your name on every commit. 🏷️

---

### Step 4️⃣: Add Your Files

```bash
# Add all files
git add .

# Or add specific folders:
git add README.md
git add Arrays/
git add Strings/
```

**What it does:** Stages files for commit.

---

### Step 5️⃣: Create Your First Commit

```bash
git commit -m "Initial commit: Day 5 DSA solutions with 5 problems solved"
```

**What it does:** Saves a snapshot of your code with a message.

---

### Step 6️⃣: Push to GitHub

```bash
# First push (use -u flag)
git push -u origin main

# Future pushes (simpler)
git push
```

✨ **Magic happens!** Your code is now on GitHub.

---

## 🎯 Daily Workflow (After Solving Problems)

### Option 1: Fast (Recommended) ⚡

```bash
git add . && git commit -m "Day X: Add [Problem Name]" && git push
```

---

### Option 2: Step-by-Step 🚶

```bash
# 1️⃣ See what changed
git status

# 2️⃣ Add files
git add .

# 3️⃣ Commit
git commit -m "Day 6: Add Longest Substring Without Repeating Characters"

# 4️⃣ Push
git push
```

---

### ✅ Daily Routine Checklist

- [ ] Solved the problem ✨
- [ ] Tested locally 🧪
- [ ] Created normal + LeetCode versions 📝
- [ ] Updated progress in README 📊
- [ ] Ran `git add .` 📦
- [ ] Committed with clear message 💾
- [ ] Pushed to GitHub 🚀

---

## 💡 Common Commands

### 📊 View Your Work

```bash
# See all changes since last commit
git status

# See what changed in files
git diff

# View commit history (one line per commit)
git log --oneline

# View detailed commit history
git log

# See commits in fancy format
git log --graph --oneline --all
```

---

### 🔄 Undo & Revert

```bash
# Undo changes (before git add)
git checkout -- filename.py

# Unstage files (undo git add)
git reset filename.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (remove changes)
git reset --hard HEAD~1
```

⚠️ **Warning:** `--hard` deletes changes permanently!

---

### 📥 Update From GitHub

```bash
# Pull latest changes
git pull origin main

# Pull and rebase (cleaner history)
git pull origin main --rebase
```

---

## 🛠️ Advanced Git Commands

### 🌿 Branch Management

```bash
# See all branches
git branch

# Create new branch
git checkout -b feature/problem-name

# Switch to existing branch
git checkout main

# Delete local branch
git branch -d branch-name

# Delete remote branch
git push origin --delete branch-name
```

---

### 📝 Advanced Commits

```bash
# Commit with interactive mode
git commit -i

# Ammend last commit (fix message)
git commit --amend -m "New message"

# Commit specific changes (interactive)
git add -p

# Cherry-pick specific commit
git cherry-pick commit-hash
```

---

### 🏷️ Tags (Mark Releases)

```bash
# Create a tag
git tag v1.0.0

# Push tags to GitHub
git push origin --tags

# View all tags
git tag -l
```

---

## ❌ Troubleshooting & Error Fixes

### 🔴 "fatal: not a git repository"

```bash
❌ Problem: Git not initialized in this folder

✅ Solution:
git init
```

---

### 🔴 "fatal: remote origin already exists"

```bash
❌ Problem: Remote already added

✅ Solution:
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/DSA-Practice.git
```

---

### 🔴 "Permission denied (publickey)"

```bash
❌ Problem: SSH key not configured

✅ Solution 1 (Use HTTPS):
git remote set-url origin https://github.com/YOUR_USERNAME/DSA-Practice.git
git push

✅ Solution 2 (Setup SSH):
ssh-keygen -t ed25519 -C "your.email@example.com"
# Then add the key to GitHub Settings
```

---

### 🔴 "Please pull before pushing"

```bash
❌ Problem: Remote has newer changes

✅ Solution:
git pull origin main
git push
```

---

### 🔴 "Your branch and 'origin/main' have diverged"

```bash
❌ Problem: Conflicting history

✅ Solution:
git pull origin main --rebase
git push
```

---

### 🔴 "fatal: 'origin' does not appear to be a 'git' repository"

```bash
❌ Problem: Remote not configured

✅ Solution:
git remote add origin https://github.com/YOUR_USERNAME/DSA-Practice.git
git push -u origin main
```

---

### ✅ Check Your Git Config

```bash
# View all settings
git config --list

# View user name
git config --global user.name

# View user email
git config --global user.email
```

---

## 📝 Commit Message Examples

### ✅ Good Commit Messages

```bash
# Daily problem solving
git commit -m "Day 5: Add Longest Palindromic Substring (Medium)"

# Multiple problems
git commit -m "Day 5-6: Add Palindrome + Binary Search solutions"

# With description
git commit -m "Add Median of Two Sorted Arrays

- Binary search approach: O(log(m+n))
- Space complexity: O(1)
- Tested with 10+ edge cases"

# Conventional commits
git commit -m "feat: Add string algorithms (palindrome, substring)"
git commit -m "fix: Correct edge case handling in Two Sum"
git commit -m "docs: Update README with progress tracker"
git commit -m "refactor: Optimize space complexity to O(1)"
```

---

### ❌ Bad Commit Messages

```bash
# ❌ Too vague
git commit -m "update"
git commit -m "fix bugs"

# ❌ Too long
git commit -m "Added a new solution for problem 4 which is about finding the median of two sorted arrays"

# ❌ Unclear
git commit -m "xyz"
git commit -m "asdf"
```

---

## 🎨 Conventional Commit Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types:
- **feat** — New feature/solution
- **fix** — Bug fix
- **docs** — Documentation update
- **refactor** — Code reorganization
- **perf** — Performance improvement
- **test** — Test additions
- **style** — Code style (formatting)

### Example:
```bash
git commit -m "feat(arrays): add median of two sorted arrays solution

- Implements binary search approach
- Time complexity: O(log(m+n))
- Space complexity: O(1)
- All edge cases tested"
```

---

## 🚀 Pro Tips for Recruiters 👀

### 💎 Tips for Impressive Git History

1. **Commit Frequently**
   ```bash
   # Good: Multiple small commits
   Day 1: Add Two Sum (brute force)
   Day 1: Optimize Two Sum with HashMap
   Day 1: Add test cases
   
   # Bad: One giant commit
   Day 1: Everything done
   ```

2. **Write Descriptive Messages**
   ```bash
   ✅ "feat(strings): Add longest palindromic substring with expand-around-center approach"
   ❌ "update"
   ```

3. **Keep Commits Clean**
   ```bash
   git add .              # Add only relevant files
   git commit -m "..."    # One logical change per commit
   git push               # Push daily
   ```

4. **Use Branches for Features**
   ```bash
   git checkout -b feature/binary-search
   # Solve problems
   git push origin feature/binary-search
   # Create Pull Request on GitHub
   ```

---

## 📊 Git Statistics (Impress Recruiters!)

### View Contributions

```bash
# See lines added/removed
git log --stat

# See who wrote what
git blame filename.py

# See your contribution summary
git shortlog -sn
```

### GitHub Statistics
- 📈 Green squares = Active days
- 📊 Consistent commits = Dedicated developer
- 💬 Clear messages = Professional coder

---

## 🎓 Learning Resources

| Resource | Link |
|----------|------|
| 📚 Official Git Docs | https://git-scm.com/doc |
| 🎬 Interactive Git Tutorial | https://learngitbranching.js.org |
| 🐙 GitHub Guides | https://guides.github.com |
| 📖 Pro Git Book | https://git-scm.com/book |

---

## 🎯 Quick Reference Card

```
┌─────────────────────────────────────────┐
│         GIT COMMAND CHEATSHEET          │
├─────────────────────────────────────────┤
│ git init                  → Initialize  │
│ git add .                 → Stage files  │
│ git commit -m "msg"       → Save        │
│ git push                  → Upload      │
│ git pull                  → Download    │
│ git status                → See changes │
│ git log --oneline         → History     │
│ git branch                → List branch │
│ git checkout -b name      → New branch  │
│ git merge branch-name     → Merge      │
└─────────────────────────────────────────┘
```

---

## ✨ Final Checklist Before Pushing

- ✅ Code is tested and working
- ✅ No syntax errors or warnings
- ✅ All files are properly formatted
- ✅ README is updated with progress
- ✅ Commit message is clear and descriptive
- ✅ No sensitive information (passwords, API keys)
- ✅ .gitignore is configured properly
- ✅ No large files (>100MB)

---

<div align="center">

### 🎓 You're Ready!

**Now commit your code and show it to the world! 🌍**

```bash
git add .
git commit -m "Day 5: DSA solutions + professional setup"
git push
```

### Every commit is a step forward! 🚀

---

**Last Updated:** January 2025  
**Maintained by:** Your Name  
**Status:** 🟢 Complete & Tested

[⬆ back to top](#-git-commands-guide--dsa-practice-repository)

</div>