# Brute Force Attack with Web Scraping

## Project Overview

This project demonstrates the implementation of brute-force attacks and dictionary attacks on a web application login page. The attack techniques involve password cracking with different character sets and web scraping techniques using Selenium. The goal is to simulate security testing scenarios on a Flask-based login page.

### Types of Attacks Implemented:
1. **Dictionary Attack**:  
   Attempting to guess passwords using a predefined list of potential passwords.
   
2. **Brute-Force Attack**:  
   Exhaustively trying all possible combinations of characters for a password with fixed length:
   - **Case 1**: Passwords with digits (`0-9`).
   - **Case 2**: Passwords containing lowercase and uppercase letters (`a-z`, `A-Z`), digits (`0-9`), and special characters.

## Folder Structure

- **App login folder**:  
  Contains the login page of the web application built using Flask.
  
- **attaqueDIC+FORCE.py**:  
  Implements both dictionary and brute-force attacks:
  - **Dictionary Attack**: Attempts to crack passwords by iterating over a list of common passwords.
  - **Brute-Force Attack**: Attempts all possible combinations for 5-character passwords with:
    - **Case 1**: Using only numbers (`0-9`).
    - **Case 2**: Using letters (`a-z`, `A-Z`), numbers (`0-9`), and special characters.

- **attaqueSelenium.py**:  
  This file implements brute-force and dictionary attacks by automating the login process using **Selenium**, a web scraping and browser automation library in Python. The script interacts with the Flask login page, simulating attempts to log in by testing different password combinations.

## Password Parameters

### 1. **Case 1: Numeric Only Passwords (0-9)**
   - Passwords of length 5.
   - Each character can take values between `0` and `9` (10 possible values per character).

### 2. **Case 2: Alphanumeric + Special Characters**
   - Passwords of length 5.
   - Each character can take values from:
     - Lowercase letters (`a-z`): 26 values
     - Uppercase letters (`A-Z`): 26 values
     - Digits (`0-9`): 10 values
     - Special characters:  
       `['~', ':', " ' ", '+', '[', '\\', '@', '^', '{', '%', '(', '-', ' " ', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']`

