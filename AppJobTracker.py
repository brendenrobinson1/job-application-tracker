"""App Job Tracker"""


"""initialized list and dictionaries for job applications/Start program"""
applications = []
program_is_running = True


"""Prompt to greet user and have them make initial selection"""
name_input = input("What is your name? ")
print("Hello, " + name_input + "!")


"""While loop to display menu selections and perform selected task while program is running"""
while program_is_running:


 """Initial menu display"""
 print()
 print("===========================")
 print(" Job Application Tracker")
 print("===========================")
 print()
 print("1. Add Application")
 print("2. View Applications")
 print("3. Search Applications")
 print("4. Update Status")
 print("5. Exit")
 print()
 print()


 """Initial selection prompt"""
 selection_input = input("Select an option: ")


 """Exit condition where user ends program with 5"""
 if selection_input == "5":
    print("Sayonara sucker!")
    program_is_running = False


    """Allows users to updated selected applications"""
 elif selection_input == "4":
    print("===========================")
    print(" Update Status Selected.")
    print("===========================")
    print()
    print()
    """for loop, enumerating through applications list"""
    for start, application in enumerate(applications, start=1):
        print(f"{start}: Role: " + application['title'] + " Company: " + application['company'] + " Status: " + application['status'])

    status_change_input = int(input("Select an application to update the status of: "))
    selected_application = applications[status_change_input - 1]
    selected_application['status'] = input("What is the new status?: ")
    for start, application in enumerate(applications, start=1):
        print(f"{start}: Role: " + application['title'] + " Company: " + application['company'] + " Status: " + application['status'])

    status_change_verify = input('Are the changes made correct? ')
    if status_change_verify == "no":
        selected_application['status'] = input("What is the new status?: ")

    elif status_change_verify == "yes":
        print("Status Updated Successfully")


    """Allows user to search through applications list"""
 elif selection_input == "3":
    print("===========================")
    print("Search Applications Selected.")
    print("===========================")
    print()
    print()
    search_type_input = input("Would you like to search by date or company? ")

    """creates list of applications matching the search criteria"""
    matching_applications = []
    if search_type_input == "date":
        search_date_input = input("What is the date of the application? ")

        """for loop, enumerating through applications list of applications matching the search criteria"""
        for application in applications:
            if search_date_input == application['date']:
                matching_applications.append(application)

    if search_type_input == "company":
        search_company_input = input("What is the name of the company you applied for? ")
        for application in applications:
            if search_company_input == application['company']:
                matching_applications.append(application)

    for start, application in enumerate(matching_applications, start=1):
        print(f"{start}: Role: " + application['title'] + " Company: " + application['company'] + " Status: " + application['status'])



    """Displays information about all added applications including company name, job title and date"""
 elif selection_input == "2":
    print("===========================")
    print("View Applications Selected.")
    print("===========================")
    print()
    print()
    for start, application in enumerate(applications, start=1):
        print(f"{start}: Role: " + application['title'] + " Company: " + application['company'] + " Status: " +
              application['status'])


    """Adds application to applications list"""
 elif selection_input == "1":
    print("Add Application Selected.")
    company_name_input = input("What is the company name? ")
    job_title_input = input("What is the job title? ")
    date_applied_input = input("What is the date of the application? ")
    Status_input = input("What is the status? ")


    """Dictionary of applications"""
    application = {'company': company_name_input,
                    'title': job_title_input,
                    'date': date_applied_input,
                    'status': Status_input}


    """Appending newly added applications to applications list"""
    applications.append(application)


    """Print summary of recently added job application"""
    print()
    print("===========================")
    print("   Application Summary")
    print("===========================")
    print("Company name: " + company_name_input)
    print("Job title: " + job_title_input)
    print("Date: " + date_applied_input)
    print("Status: " + Status_input)

 else:
    """End of program/while loop/invalid option selected"""
    print("Invalid Option Selected.")







