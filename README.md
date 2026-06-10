# CodeQL Vulnerability Analysis & Fix Workflow

## Project Overview

This project is a learning resource designed to understand **CodeQL's behavior and detection capabilities** through a practical scenario: introducing a security vulnerability, observing CodeQL's analysis failure, and then applying a fix to see how CodeQL handles the remediation.

## Learning Objectives

- Understand how CodeQL detects SQL injection vulnerabilities
- Observe CodeQL check behavior in a pull request lifecycle
- Learn how CodeQL re-analyzes code after a fix commit is pushed
- Understand the transition from fail to passing security checks
- Explore CodeQL's incremental analysis capabilities

## Scenario

1. **Initial State**: A developer introduces a SQL injection vulnerability (unsanitized query parameters)
2. **CodeQL Check Fails**: The mandatory CodeQL analysis check fails on the pull request
3. **Developer Fixes the Issue**: A new commit is pushed that properly parameterizes the SQL query
4. **CodeQL Re-analysis**: CodeQL automatically re-runs on the new commit
5. **Check Passes**: The vulnerability is resolved and the check transitions to passing

## What You'll Learn

- **Vulnerability Detection**: How CodeQL identifies SQL injection patterns
- **PR Workflow Integration**: How CodeQL integrates into GitHub's PR checks
- **Real-time Analysis**: How CodeQL re-evaluates code on new commits
- **Security Best Practices**: Proper parameterized query implementation

## Key Concepts

### SQL Injection Vulnerability
- Unsanitized user input concatenated directly into SQL queries
- Example: `query = "SELECT * FROM users WHERE id=" + userId`

### Parameterized Queries (Fix)
- Using placeholders and parameter binding
- Example: `query = "SELECT * FROM users WHERE id = ?"`
- Eliminates the vulnerability by separating code from data

### CodeQL Analysis
- Automatic static analysis on pull requests
- Detects security vulnerabilities and code quality issues
- Provides real-time feedback in the PR lifecycle

