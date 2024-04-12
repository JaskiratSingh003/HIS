#!/usr/bin/env python
# coding: utf-8

# In[132]:


# Doctor module


# In[133]:


class Person:
    def __init__(self, first_name, last_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


# In[134]:


"""
Doctor Module: doctor must login. Default login: Doctor ID = chief, Password = 12345. Doctors can create new doctors (ID and password); Create patients. 
Create/view all patient details; order lab tests (with costs) to a patient. Discharge patient. First name, last name, specialty, phone number.
"""


# In[135]:


# Doctor module

class Doctor(Person):
    doctor_directory = {}
    
    def __init__(self, first_name, last_name, department, doctor_id, password):
        super().__init__(first_name, last_name, department)
        self.doctor_id = doctor_id
        self.password = password

    def get_doc_id_pass(self):
        return self.doctor_id, self.password

    # Creating new doctor w/ ID and password - store in directory
    def add_doc_to_directory():
        # Doctor inputs
        first_name = input("First name: ")
        last_name = input("Last name: ")
        department = input("Department: ")
        doctor_id = input("Create a username for the doctor: ")
        password = input("Create a password for the doctor: ")
        
        # Return new Doctor object and add to directory
        new_doctor = Doctor(first_name, last_name, department, doctor_id, password)
        Doctor.doctor_directory[(doctor_id, password)] = new_doctor
        return new_doctor

    def create_patient():
        new_patient = get_patient_info()
        if new_patient is None:
            return None
        else:
            Patient.patient_records[new_patient.patient_id] = new_patient
            print("\nPatient has been successfully added into the system!")
        return new_patient

    def view_patient_details(patient_id):
        if patient_id in Patient.patient_records:
            print("\nPatient Details:")
            Patient.patient_records[patient_id].display_profile()
        else:
            print("Patient not found in records.")

    def order_lab_tests():
        patient_id = input("Enter Patient ID to add test order: ")
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            test_name = input("Enter lab test name: ")
            test_cost = float(input("Enter cost of test: "))
            patient.add_lab_test(test_name, test_cost)
            print(f"Lab test '{test_name}' has been successfully ordered for {patient.get_full_name()}")
        else:
            print("Patient not found in records.")

    def discharge_patient():
        patient_id = input("Enter Patient ID to discharge: ")
        if patient_id in Patient.patient_records:
            discharged_patient = Patient.patient_records.pop(patient_id)
            print(f"{discharged_patient.get_full_name()} has been discharged.")
        else:
            print("Patient not found in records.")


# In[136]:


# Patient Module

class Patient(Person):
    patient_records = {}
    
    def __init__(self, first_name, last_name, department, patient_id, age, address, admit_date):
        super().__init__(first_name, last_name, department) # Call the __init__ method of the superclass (Person)
        self.patient_id = patient_id
        self.age = age
        self.address = address
        self.admit_date = admit_date
        self.medical_costs = []  # List to store medical costs

        Patient.patient_records[self.patient_id] = self

    def display_profile(self):
        print(f"Name: {self.get_full_name()}")
        print(f"Patient ID: {self.patient_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Admit Date: {self.admit_date}")
        print(f"Total Medical Bill: ${self.get_total_bill():,.2f}")

    def add_medical_cost(self, cost):
        """Add a medical cost to the patient's record."""
        self.medical_costs.append(cost)

    def add_lab_test(self, test_name, test_cost):
        """Add a lab test to the patient's record."""
        self.medical_costs.append(test_cost)
        print(f"The following lab test has been ordered successfully for patient {self.get_full_name()}: {test_name}")

    def get_total_bill(self):
        """Calculate the total medical bill."""
        return sum(self.medical_costs)

# Function to get patient information from user input
def get_patient_info():
    first_name = input("Enter patient's first name (or 'q' to quit): ")  # Get the patient's first name from the user
    if first_name.lower() == 'q':  # If the user enters 'q', return None and quit
        return None
    last_name = input("Enter patient's last name: ")  # Get the patient's last name from the user
    department = input("Enter department: ")
    patient_id = input("Enter patient's ID: ")  # Get the patient's ID from the user
    age = int(input("Enter patient's age: "))  # Get the patient's age from the user and convert it to an integer
    address = input("Enter patient's address: ")  # Get the patient's address from the user
    admit_date = input("Enter patient's admit date: ")  # Get the patient's admit date from the user

    # Return a new Patient object with the input information
    return Patient(first_name, last_name, department, patient_id, age, address, admit_date)


# In[137]:


# Discharge Module
class Patient_Discharge(Person):
    def __init__(self, first_name, last_name, department, Discharge):
        super().__init__(self, first_name, last_name, department)
        self.Discharged = Discharged
    def options():
        flag = True        
        while flag == True:
            print(f"Please enter an option one of the following options\n")
            print(f"The options are:\n 'Exit' To Leave the System. \n 'Discharge' to Discharge a Patient \n 'Return' to Return to Main Menu.")
            user_input = input().capitalize()
            
            if user_input == 'Exit':
                print("You have entered {self.user_input} and have left the system")
                flag = False
            
            if user_input == 'Discharge':
                flag = False

            if user_input == 'Return':
                flag = False

            else: 
                print("Hmm, seems like an error occured, please try again.\n")
        
        while flag == False:
            return

# Patient_1 = Patient_Discharge("John", "Doe", "Pysch Ward", "False")


#Patient_Discharge.options()


# In[138]:


# Menu for doctor log in

while True:
    doctor_login = input("Enter your username: ")
    doctor_password = input("Enter the password: ")
    print("\n")

    if doctor_login == "chief" and doctor_password == "12345":
        try:
            print("Hello Doctor. What would you like to do?")
            print("1. Create doctor login") # Good
            print("2. Create nurse login")
            print("3. Create patient")
            print("4. Update or View patient details") # Add with meds, patient assignment
            print("5. Order lab tests to patient")
            print("6. Discharge patient\n")

            choice = int(input("Please select an option from 1-6."))
            if (choice == 1):
                new_doctor = Doctor.add_doc_to_directory()
                print("\nDoctor has been successfully added!")

                # Add the doctor to the directory using (doctor_id, password) as key
                print("\nDoctor Directory:")
                for (doctor_id, password), doctor_info in Doctor.doctor_directory.items():
                    print(f"Profile for {doctor_info.get_full_name()}, {doctor_info.department}")
                    print(f"Doctor ID: {doctor_info.doctor_id}")
                    print(f"Doctor Password: {doctor_info.password}\n")
                    
            elif (choice == 2): # Create nurse Login
                print("nurse login")
            
            elif (choice == 3): # Create patient
                Doctor.create_patient()
                
            elif (choice == 4): # View patient
                patient_id = input("Enter Patient ID to view details.")
                Doctor.view_patient_details(patient_id)
                    
            elif (choice == 5): # Order lab tests
                Doctor.order_lab_tests()

            elif (choice == 6): 
                #Patient_Discharge.options()
                Doctor.discharge_patient()
            else:
                print("Please enter a number from 1-6.")

        except:
            print(f"\nAn error occurred in the main menu.")
            continue  # Continue to the next iteration of the loop

    else:
        print("\nIncorrect username or password. Please try again.")
        break  # Continue to the next iteration of the loop


# In[ ]:




