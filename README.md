# Job Application Tracker

## Overview

Job application tracker created using Python that can add, view, update, and search through a list of user supplied job applications from the command line. Users enter application details, which are then stored in a list using dictionaries for the duration of the program. The reason I started this project is to deepen my fundamental knowledge of coding outside of a classroom setting, and to learn to think more like a programmer.

## Features

- **Add applications:** Enter a company name, job title, application date, and current status.
- **View applications:** View details of all applications entered by the user.
- **Search applications:** Search through user applications based on either date or company.
- **Update status:** Update the status of a selected application (e.g., applied, interviewing, hired, or rejected).

## How It Works

- Each application is represented as a dictionary and appended to the applications list.
- enumerate() is used to display applications with numbered selections.
- The while loop keeps displaying the menu while program_is_running is True.
- The search for loop compares each application against the search criteria and appends matches to a separate list.

## Technologies Used

- Python 3
- Git and GitHub

## Getting Started

### Prerequisites

- Python 3 installed on your computer

### Installation

1. Clone the repository:

```bash
git clone https://github.com/brendenrobinson1/job-application-tracker.git
```

2. Navigate into the project directory:

```bash
cd job-application-tracker
```

3. Run the application:

```bash
python3 AppJobTracker.py
```

Windows users may need to run:

```bash
python AppJobTracker.py
```

## Example Usage

After adding applications, users can search for matching records by company:

```text
Would you like to search by date or company? company
What is the name of the company you applied for? Acme Corporation

1: Role: Security Analyst Company: Acme Corporation Status: Applied
2: Role: Software Developer Company: Acme Corporation Status: Interviewing
```

## Current Limitations

- Applications are only temporarily stored, then lost once the program is no longer running.
- Search requires you to type the application date or campany name exactly as you entered.
- Invalid input, such as letters where a number is expected or an out-of-range selection, may cause an error.

## What I Learned

This project taught me how the concepts I’ve learned separately come together to make a complete program work. I’ve learned to approach code from a problem-solving standpoint and think of programming concepts as tools. The Job Application Tracker also helped me learn how to translate pseudocode into actual code, something I hadn’t previously practiced. Through trial and error, I’ve gotten better at understanding how control flow determines when and how often code executes, as well as the role proper indentation plays in Python


## Planned Improvements

### Version 2.0.0

- [ ] Add file persistence so applications remain available after the program closes.
- [ ] Add input validation for menu choices and application selections.
- [ ] Add error handling to prevent invalid input from crashing the program.
- [ ] Support case-insensitive searches.
- [ ] Organize repeated operations into reusable functions.
- [ ] Apply additional secure coding practices.
