#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Person:
    def __init__(self, name, age, email, phone):
        self.name = name  # Set the name of the person
        self.age = age  # Set the age of the person
        self.email = email  # Set the email of the person
        self.phone = phone  # Set the phone number of the person

    def display_profile(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Phone: {self.phone}")


class Patient(Person):
    def __init__(self, first_name, last_name, patient_id, age, address, admit_date):
        super().__init__(f"{first_name} {last_name}", age, "", "")  # Call the __init__ method of the superclass (Person)
        self.patient_id = patient_id
        self.address = address
        self.admit_date = admit_date
        self.medical_costs = []  # List to store medical costs

    def add_medical_cost(self, cost):
        """Add a medical cost to the patient's record."""
        self.medical_costs.append(cost)

    def get_total_bill(self):
        """Calculate the total medical bill."""
        return sum(self.medical_costs)

    def get_masked_name(self):
        """Get the masked name (initials)."""
        masked_first_name = self.name.split()[0][0] + "***"
        masked_last_name = self.name.split()[1][0] + "***"
        return f"{masked_first_name} {masked_last_name}"


# Function to get patient information from user input
def get_patient_info():
    first_name = input("Enter patient's first name (or 'q' to quit): ")  # Get the patient's first name from the user
    if first_name.lower() == 'q':  # If the user enters 'q', return None and quit
        return None
    last_name = input("Enter patient's last name: ")  # Get the patient's last name from the user
    patient_id = input("Enter patient's ID: ")  # Get the patient's ID from the user
    age = int(input("Enter patient's age: "))  # Get the patient's age from the user and convert it to an integer
    address = input("Enter patient's address: ")  # Get the patient's address from the user
    email = input("Enter your email address: ") # Get the patient's email from the user
    phone = input("Enter your phone no. : ") # Get the patient's phone no. from the user
    admit_date = input("Enter patient's admit date: ")  # Get the patient's admit date from the user

    # Return a new Patient object with the input information
    return Patient(first_name, last_name, patient_id, age, address, admit_date)


# Main loop to allow user to enter multiple patient profiles
while True:
    patient = get_patient_info()  # Call the function to get patient's information from user input and store it in the 'patient' variable
    if patient is None:  # If the function returns None (i.e., the user entered 'q' to quit), break the loop
        break

    # Display patient details
    print(f"Patient ID: {patient.patient_id}")
    print(f"Name: {patient.get_masked_name()}")
    print(f"Age: {patient.age}")
    print(f"Address: {patient.address}")
    print(f"Admit Date: {patient.admit_date}")

    # Add medical costs
    while True:
        cost = input("Enter a medical cost (or 'q' to finish): ")  # Get the medical cost from the user
        if cost.lower() == 'q':
            break
        patient.add_medical_cost(float(cost))  # Add the medical cost to the patient's record

    print(f"Total Medical Bill: ${patient.get_total_bill():,.2f}")
    patient.display_profile()  # Display the patient's profile
    print()  # Print a newline for better readability

