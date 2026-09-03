# Job Application Tracker

## Overfiew

Job application tracker created using Python that can add, view, update, and search through a list of user supplied job applications from the command line. Users enter application details, which are then stored in a list using dictionaries for the duration of the program. The reason I started this project is to deepen my fundamental knowledge of coding outside of a classroom setting, and to learn to think more like a programmer.

## Features

- **Add applications:** Enter a company name, job title, application date, and current status.
- **View applications:** View details of all applications entered by the user.
- **Search applications:** Search through user applications based on either date or company
- **Update status:** Update the status of a selected application (e.g., applied, interviewing, hired, or rejected).

## How It Works

- Each application is created and placed in a dictionary, which is then stored in a list of dictionaries.
- Applications are collected and can be viewed by enumerating through a list of all of the user entered applications.
- A `while` loop is used to run through the functions "while" the program is running, making the application functional until a user decides to quit.
- When searching, a `for` loop is used to loop through a list of applications that compare all available applications against the ones that match the search criteria, either by date or company.

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

- Applications are only temporarily stored, then deleted once the program is no longer running.
- Search functions requires you to type the date or time exactly as you entered.
- Invalid input, such as letters where a number is expected or an out-of-range selection, may cause an error.
