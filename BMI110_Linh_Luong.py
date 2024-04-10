#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Doctor module


# In[2]:


class Person:
    def __init__(self, first_name, last_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


# In[ ]:


"""
Doctor Module: doctor must login. Default login: Doctor ID = chief, Password = 12345. Doctors can create new doctors (ID and password); Create patients. 
Create/view all patient details; order lab tests (with costs) to a patient. Discharge patient. First name, last name, specialty, phone number.
"""


# In[3]:


class Doctor(Person):

    def __init__(self, first_name, last_name, department, doctor_id, password):
        super().__init__(first_name, last_name, department)
        self.doctor_id = doctor_id
        self.password = password

    def get_doc_id_pass(self):
        return self.doctor_id, self.password

    # Creating new doctor w/ ID and password - store in directory
    doctor_directory = {}
    def add_doc_to_directory(self):
        doc_id_pass = self.get_doc_id_pass()
        Doctor.doctor_directory[doc_id_pass] = self


while True:
    doctor_login = input("Enter your username: ")
    doctor_password = input("Enter the password: ")
    print("\n")

    if doctor_login == "chief" and doctor_password == "12345":
        try:
            first_name = input("First name: ")
            last_name = input("Last name: ")
            department = input("Department: ")
            doctor_id = input("Create a username for the doctor: ")
            password = input("Create a password for the doctor: ")
            
            new_doctor = Doctor(first_name, last_name, department, doctor_id, password)

            # Add the doctor to the directory using (doctor_id, password) as key
            new_doctor.add_doc_to_directory()
            print("\nDoctor has been successfully added!")

        except:
            print(f"\nAn error occurred.")
            continue  # Continue to the next iteration of the loop

    else:
        print("\nIncorrect username or password. Please try again.")
        break  # Continue to the next iteration of the loop

    print("\nDoctor Directory:")
    for (doctor_id, password), doctor_info in Doctor.doctor_directory.items():
        print(f"Profile for {doctor_info.get_full_name()}, {doctor_info.department}")
        print(f"Doctor ID: {doctor_info.doctor_id}")
        print(f"Doctor Password: {doctor_info.password}\n")

    print("End of doctor directory.")


# In[ ]:


while True:
    doctor_login = input("Enter your username: ")
    doctor_password = input("Enter the password: ")
    print("\n")

    if doctor_login == "chief" and doctor_password == "12345":
        try:
            print("Hello Doctor. What would you like to do?")
            print("1. Create doctor login")
            print("2. Create nurse login")
            print("3. Create patient")
            print("4. Update or View patient details") # Add with meds, patient assignment
            print("5. Order lab tests to patient")
            print("6. Discharge patient")

            choice = int(input("Please select an option from 1-6.")
                if (choice == 1):
                    self.create_new_doctor()

        except:
            print(f"\nAn error occurred.")
            continue  # Continue to the next iteration of the loop

    else:
        print("\nIncorrect username or password. Please try again.")
        break  # Continue to the next iteration of the loop

