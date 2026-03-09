#!/bin/bash

# ============================================================================
# GIT PUSH COMMANDS - DSA Practice Repository
# ============================================================================
# Follow these commands in order to push to GitHub

# Step 1: Initialize Git (ONLY IF FIRST TIME)
# ============================================================================
git init

# Step 2: Add Remote Repository (ONLY IF FIRST TIME)
# ============================================================================
# Replace with your GitHub URL
git remote add origin https://github.com/YOUR_USERNAME/DSA-Practice.git

# Verify remote was added
git remote -v


# Step 3: Configure Git (ONLY IF FIRST TIME)
# ============================================================================
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"


# Step 4: Check Current Status
# ============================================================================
git status


# Step 5: Add All Files
# ============================================================================
git add .

# Or add specific files:
# git add README.md
# git add Arrays/
# git add Strings/


# Step 6: Commit with Message
# ============================================================================
git commit -m "Day 5: Add Longest Palindromic Substring solution + Updated README"

# Better commit message examples:
# git commit -m "Day 5: Add Longest Palindromic Substring + README enhancement"
# git commit -m "Add LeetCode solutions: Median of Two Sorted Arrays"
# git commit -m "Update: Complete DSA practice setup with 5 problems solved"


# Step 7: Push to GitHub
# ============================================================================
git push -u origin main

# Or if your branch is 'master':
# git push -u origin master

# Subsequent pushes (after first push):
# git push


# ============================================================================
# QUICK DAILY ROUTINE (After solving a problem)
# ============================================================================

# Check what changed
git status

# Add files
git add .

# Commit with today's solution
git commit -m "Day X: Add [Problem Name] solution"

# Push
git push


# ============================================================================
# USEFUL COMMANDS
# ============================================================================

# View commit history
git log --oneline

# View what will be committed (before git add)
git diff

# Undo last commit (before push)
git reset --soft HEAD~1

# Undo last commit (remove changes)
git reset --hard HEAD~1

# Check branch name
git branch

# Create new branch
git checkout -b feature/new-feature

# Switch branch
git checkout main

# Delete local branch
git branch -d branch-name

# Update from remote
git pull origin main


# ============================================================================
# TROUBLESHOOTING
# ============================================================================

# If you get "remote already exists" error:
# git remote remove origin
# git remote add origin https://github.com/YOUR_USERNAME/DSA-Practice.git

# If you get "Permission denied" error:
# Make sure you're using HTTPS URL or setup SSH keys
# SSH: git@github.com:YOUR_USERNAME/DSA-Practice.git
# HTTPS: https://github.com/YOUR_USERNAME/DSA-Practice.git

# If you need to pull before pushing:
# git pull origin main --rebase
# Then push again: git push

# Check git config
# git config --list