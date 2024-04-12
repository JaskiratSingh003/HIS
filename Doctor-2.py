#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Doctor Module


# In[2]:


# Person class
class Person:

    # We will be keeping the full name and department consistent across all modules.
    def __init__(self, first_name, last_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    # Obtain the full name of anyone in the hospital.
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


# In[3]:


# Doctor Class

# Doctor class takes a Person class to create and access information from the patients and nurses.
class Doctor(Person): 

    # A doctor dictionary was created as a directory to store doctor objects by doctor_id and password.
    doctor_directory = {}

    # Instantiate the Doctor class and add in new attributes for creating the doctor's ID and password.
    def __init__(self, first_name, last_name, department, doctor_id, password):
        super().__init__(first_name, last_name, department)
        self.doctor_id = doctor_id
        self.password = password

    # A method to obtain the doctor ID and password
    def get_doc_id_pass(self):
        return self.doctor_id, self.password

    # Create a new doctor by using the add_doc_to_directory() method. This will eventually store into the directory.
    def add_doc_to_directory():
        # Inputs the doctor must type in to add to the directory.
        first_name = input("First name: ")
        last_name = input("Last name: ")
        department = input("Department: ")
        doctor_id = input("Create a username for the doctor: ")
        password = input("Create a password for the doctor: ")
        
        # Return a new Doctor object by taking in the inputs and add to directory.
        new_doctor = Doctor(first_name, last_name, department, doctor_id, password)
        Doctor.doctor_directory[(doctor_id, password)] = new_doctor
        return new_doctor

    # This method will create a new patient and add them to the patient records.
    def create_patient():
        # Obtain patient information from the user input which is from the Patient module.
        new_patient = get_patient_info()
        
        # If patient does not exist in the system.
        if new_patient is None:
            return None
        
        # Otherwise, create the information given and add it into the patient directory.
        else:
            Patient.patient_records[new_patient.patient_id] = new_patient
            print("\nPatient has been successfully added into the system!")
        return new_patient

    # The view_patient_details() method takes in the patient ID that was created and allows you to view their information.
    def view_patient_details(patient_id):
        # Print out the records if the ID is found.
        if patient_id in Patient.patient_records:
            print("\nPatient Details:")
            Patient.patient_records[patient_id].display_profile()

        # Send an error if the system cannot find the ID.
        else:
            print("Patient not found in records.")

    # This is the method where the doctor can order lab tests. Find the existing patient through its ID and update the cost.
    def order_lab_tests():

        # Type in the patient ID.
        patient_id = input("Enter Patient ID to add test order: ")
        
        # If the ID exists in the system, add in the lab test along with the cost.
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            test_name = input("Enter lab test name: ")
            test_cost = float(input("Enter cost of test: "))
            patient.add_lab_test(test_name, test_cost)
            print(f"The following lab test has been ordered successfully for patient {self.get_full_name()}: {test_name}, ${test_cost}")
        
        # The patient does not exist in the system.
        else:
            print("Patient not found in records.")

    # The discharge_patient() will find the input of the patient ID and remove from the system.
    def discharge_patient():

        # The doctor types in the patient ID.
        patient_id = input("Enter Patient ID to discharge: ")
        
        # If the ID is in the system, remove the patient's content through the "pop" method.
        if patient_id in Patient.patient_records:
            discharged_patient = Patient.patient_records.pop(patient_id)
            print(f"{discharged_patient.get_full_name()} has been discharged.")
        
        # The content was not found in the first place.
        else:
            print("Patient not found in records.")


# In[4]:


# This is the menu for doctor login only. We could combine with the Patient and Nurse login. 

# The while loop will keep the program functioning until an error occurs.
while True:

    # Have someone log into the system. 
    doctor_login = input("Enter your username: ")
    doctor_password = input("Enter the password: ")
    print("\n")

    # This login will be accepted for the doctor if they type in the username and password correctly.
    if doctor_login == "chief" and doctor_password == "12345":
        
        # The try method will print out a menu and the doctor has several options to choose from.
        try:
            print("Hello Doctor. What would you like to do?")
            print("1. Create doctor login") # Doctor login works!
            print("2. Create nurse login")
            print("3. Create patient") # Creating patient works! 
            print("4. Update or View patient details") # Add with meds, patient assignment
            print("5. Order lab tests to patient")
            print("6. Discharge patient\n") # Discharge patient works! Needs more editing

            # The doctor only has six choices to choose from.
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
            
            # Optional method: The doctor can create a nurse login.       
            elif (choice == 2): 
                nurse_login = "nurse_login"

            # Create a new patient.
            elif (choice == 3):
                Doctor.create_patient()

            # View an existing patient.
            elif (choice == 4):
                patient_id = input("Enter Patient ID to view details.")
                Doctor.view_patient_details(patient_id)

            # Add a lab test with the cost to the existing patient.
            elif (choice == 5):
                Doctor.order_lab_tests()

            # Discharge patient.
            elif (choice == 6):
                #Patient_Discharge.options()
                Doctor.discharge_patient()
            
            # If the user did not enter anything other than 1-6.
            else:
                print("Please enter a number from 1-6.")

        # Except will help catch any bugs that were detected while the system is running.
        except:
            print(f"\nAn error occurred in the main menu.")
            continue  # Continue to the next iteration of the loop

    # The user typed in the incorrect username or password and cannot access information. 
    else:
        print("\nIncorrect username or password. Please try again.")
        break  # Continue to the next iteration of the loop

