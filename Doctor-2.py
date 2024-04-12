#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Doctor Module


# In[2]:


# Person class
class Person:
    def __init__(self, first_name, last_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


# In[3]:


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


# In[4]:


# Menu for doctor log in

while True:
    doctor_login = input("Enter your username: ")
    doctor_password = input("Enter the password: ")
    print("\n")

    if doctor_login == "chief" and doctor_password == "12345":
        try:
            print("Hello Doctor. What would you like to do?")
            print("1. Create doctor login") # Doctor login works!
            print("2. Create nurse login")
            print("3. Create patient") # Creating patient works! 
            print("4. Update or View patient details") # Add with meds, patient assignment
            print("5. Order lab tests to patient")
            print("6. Discharge patient\n") # Discharge patient works! Needs more editing

            choice = int(input("Please select an option from 1-6."))
            # Add a new doctor and store information on the doctor
            if (choice == 1):
                new_doctor = Doctor.add_doc_to_directory()
                print("\nDoctor has been successfully added!")

                # Add the doctor to the directory using (doctor_id, password) as key
                print("\nDoctor Directory:")
                for (doctor_id, password), doctor_info in Doctor.doctor_directory.items():
                    print(f"Profile for {doctor_info.get_full_name()}, {doctor_info.department}")
                    print(f"Doctor ID: {doctor_info.doctor_id}")
                    print(f"Doctor Password: {doctor_info.password}\n")
            
            # Optional - Nurse Login        
            elif (choice == 2): 
                nurse_login = "nurse_login"

            # Create a new patient.
            elif (choice == 3):
                Doctor.create_patient()

            # View an existing patient
            elif (choice == 4):
                patient_id = input("Enter Patient ID to view details.")
                Doctor.view_patient_details(patient_id)

            # Add a lab test with the cost to the existing patient
            elif (choice == 5):
                add_lab_order = "add_lab_order"

            # Discharge patient
            elif (choice == 6):
                Patient_Discharge.options()
            else:
                print("Please enter a number from 1-6.")

        except:
            print(f"\nAn error occurred in the main menu.")
            continue  # Continue to the next iteration of the loop

    else:
        print("\nIncorrect username or password. Please try again.")
        break  # Continue to the next iteration of the loop

