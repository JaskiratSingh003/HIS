#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[148]:


# Doctor module


# In[149]:


class Person:
    def __init__(self, first_name, last_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


# In[150]:


"""
Doctor Module: doctor must login. Default login: Doctor ID = chief, Password = 12345. Doctors can create new doctors (ID and password); Create patients. 
Create/view all patient details; order lab tests (with costs) to a patient. Discharge patient. First name, last name, specialty, phone number.
"""


# In[151]:


# Doctor module

class Doctor(Person):
    doctor_directory = {}
    
    def __init__(self, first_name, last_name, department, doctor_id, password):
        super().__init__(first_name, last_name, department)
        self.doctor_id = doctor_id
        self.password = password
        Doctor.doctor_directory[(doctor_id, password)] = self

    def get_doc_id_pass(self):
        return self.doctor_id, self.password

    # Creating new doctor w/ ID and password - store in directory
    def add_doc_to_directory(self):
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

    def create_patient(self):
        new_patient = get_patient_info()
        if new_patient is None:
            return None
        else:
            Patient.patient_records[new_patient.patient_id] = new_patient
            print("\nPatient has been successfully added into the system!")
        return new_patient

    def view_patient_details(self, patient_id):
        if patient_id in Patient.patient_records:
            print("\nPatient Details:")
            Patient.patient_records[patient_id].display_profile()
        else:
            print("Patient not found in records.")

    def order_lab_tests(self, patient_id):
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            test_name = input("Enter lab test name: ")
            test_cost = float(input("Enter cost of test: "))
            patient.add_lab_test(test_name, test_cost)
            print(f"The following lab test has been ordered successfully for patient {patient.get_full_name()}: {test_name}, ${test_cost}")
        else:
            print("Patient not found in records.")

    def update_patient_details(self, patient_id):
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            print(f"Current details for {patient.get_full_name()}:")
            patient.display_profile()
            print("\nEnter new details (leave blank to keep existing):")
            first_name = input(f"First name [{patient.first_name}]: ") or patient.first_name
            last_name = input(f"Last name [{patient.last_name}]: ") or patient.last_name
            age = input(f"Age [{patient.age}]: ") or patient.age
            address = input(f"Address [{patient.address}]: ") or patient.address
            admit_date = input(f"Admit date [{patient.admit_date}]: ") or patient.admit_date
            new_patient = Patient(first_name, last_name, patient.department, patient.patient_id, age, address, admit_date)
            Patient.patient_records[patient_id] = new_patient
            print("\nPatient details updated successfully.")
        else:
            print("Patient not found in records.")

    def discharge_patient(self):
        patient_id = input("Enter Patient ID to discharge: ")
        if patient_id in Patient.patient_records:
            discharged_patient = Patient.patient_records.pop(patient_id)
            print(f"{discharged_patient.get_full_name()} has been discharged.")
            create_discharge_report(discharged_patient)
        else:
            print("Patient not found in records.")

# Nurse module
class Nurse(Person):
    nurse_directory = {}

    def __init__(self, first_name, last_name, department, floor_number, nurse_id, password):
        super().__init__(first_name, last_name, department)
        self.floor_number = floor_number
        self.nurse_id = nurse_id
        self.password = password
        Nurse.nurse_directory[(nurse_id, password)] = self

    def get_nurse_id_pass(self):
        return self.nurse_id, self.password

    @staticmethod
    def create_nurse():
        first_name = input("Enter nurse's first name: ")
        last_name = input("Enter nurse's last name: ")
        department = input("Enter nurse's department: ")
        floor_number = input("Enter nurse's floor number: ")
        nurse_id = input("Create a username for the nurse: ")
        password = input("Create a password for the nurse: ")
        new_nurse = Nurse(first_name, last_name, department, floor_number, nurse_id, password)
        print("\nNurse has been successfully added!")

    @staticmethod
    def view_patient_details(self, patient_id):
        if patient_id in Patient.patient_records:
            print("\nPatient Details:")
            Patient.patient_records[patient_id].display_profile()
        else:
            print("Patient not found in records.")

# Patient module
class Patient(Person):
    patient_records = {}
    
    def __init__(self, first_name, last_name, department, patient_id, age, address, admit_date):
        super().__init__(first_name, last_name, department)
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
        self.medical_costs.append(cost)

    def add_lab_test(self, test_name, test_cost):
        self.medical_costs.append(test_cost)

    def get_total_bill(self):
        return sum(self.medical_costs)

def get_patient_info():
    first_name = input("Enter patient's first name (or 'q' to quit): ")
    if first_name.lower() == 'q':
        return None
    last_name = input("Enter patient's last name: ")
    department = input("Enter department: ")
    patient_id = input("Enter patient's ID: ")
    age = int(input("Enter patient's age: "))
    address = input("Enter patient's address: ")
    admit_date = input("Enter patient's admit date: ")
    return Patient(first_name, last_name, department, patient_id, age, address, admit_date)

# Discharge module
def create_discharge_report(patient):
    filename = f"{patient.patient_id}_discharged.txt"
    with open(filename, "w") as f:
        f.write(f"Patient Name: {patient.get_full_name()}\n")
        f.write("Lab Tests Ordered:\n")
        for cost in patient.medical_costs:
            f.write(f"- ${cost:.2f}\n")
        f.write(f"Total Medical Bill: ${patient.get_total_bill():.2f}")
    print(f"Discharge report for {patient.get_full_name()} has been created.")
    print(f"Filename: {filename}")

# Main menu
# Create the default doctor
default_doctor = Doctor("Chief", "Doctor", "General", "chief", "12345")

while True:
    user_type = input("Are you a Doctor (D) or Nurse (N)? ")
    if user_type.upper() == 'D':
        doctor_login = input("Enter your doctor username: ")
        doctor_password = input("Enter your doctor password: ")
        if (doctor_login, doctor_password) in Doctor.doctor_directory:
            doctor = Doctor.doctor_directory[(doctor_login, doctor_password)]
            print(f"Hello Doctor {doctor.get_full_name()}")
            while True:
                print("What would you like to do?")
                print("1. Create new doctor")
                print("2. Create patient")
                print("3. View patient details")
                print("4. Order lab tests")
                print("5. Update patient details")
                print("6. Discharge patient")
                print("7. Switch to Nurse view")
                print("8. Exit")
                choice = int(input("Enter your choice (1-8): "))
                if choice == 1:
                    new_doctor = doctor.add_doc_to_directory()
                    Doctor.doctor_directory[(new_doctor.doctor_id, new_doctor.password)] = new_doctor
                elif choice == 2:
                    doctor.create_patient()
                elif choice == 3:
                    patient_id = input("Enter Patient ID to view details: ")
                    doctor.view_patient_details(patient_id)
                elif choice == 4:
                    patient_id = input("Enter Patient ID to add test order: ")
                    doctor.order_lab_tests(patient_id)
                elif choice == 5:
                    patient_id = input("Enter Patient ID to update details: ")
                    doctor.update_patient_details(patient_id)
                elif choice == 6:
                    doctor.discharge_patient()
                elif choice == 7:
                    patient_id = input("Enter Patient ID to view details: ")
                    Nurse.view_patient_details(None, patient_id)
                elif choice == 8:
                    print("Exiting the system...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif (doctor_login, doctor_password) == ("chief", "12345"):
            doctor = default_doctor
            print(f"Hello Doctor {doctor.get_full_name()}")
            while True:
                print("What would you like to do?")
                print("1. Create new doctor")
                print("2. Create patient")
                print("3. View patient details")
                print("4. Order lab tests")
                print("5. Update patient details")
                print("6. Discharge patient")
                print("7. Switch to Nurse view")
                print("8. Exit")
                choice = int(input("Enter your choice (1-8): "))
                if choice == 1:
                    new_doctor = doctor.add_doc_to_directory()
                    Doctor.doctor_directory[(new_doctor.doctor_id, new_doctor.password)] = new_doctor
                elif choice == 2:
                    doctor.create_patient()
                elif choice == 3:
                    patient_id = input("Enter Patient ID to view details: ")
                    doctor.view_patient_details(patient_id)
                elif choice == 4:
                    patient_id = input("Enter Patient ID to add test order: ")
                    doctor.order_lab_tests(patient_id)
                elif choice == 5:
                    patient_id = input("Enter Patient ID to update details: ")
                    doctor.update_patient_details(patient_id)
                elif choice == 6:
                    doctor.discharge_patient()
                elif choice == 7:
                    patient_id = input("Enter Patient ID to view details: ")
                    Nurse.view_patient_details(None, patient_id)
                elif choice == 8:
                    print("Exiting the system...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid doctor credentials. Please try again.")
    elif user_type.upper() == 'N':
        nurse_login = input("Enter your nurse username: ")
        nurse_password = input("Enter your nurse password: ")
        if (nurse_login, nurse_password) in Nurse.nurse_directory:
            nurse = Nurse.nurse_directory[(nurse_login, nurse_password)]
            print(f"Hello Nurse {nurse.get_full_name()}")
            while True:
                print("What would you like to do?")
                print("1. Create patient")
                print("2. View patient details")
                print("3. Exit")
                choice = int(input("Enter your choice (1-3): "))
                if choice == 1:
                    Doctor.create_patient()
                elif choice == 2:
                    patient_id = input("Enter Patient ID to view details: ")
                    Nurse.view_patient_details(nurse, patient_id)
                elif choice == 3:
                    print("Exiting the system...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid nurse credentials. Please try again.")
    else:
        print("Invalid user type. Please try again.")


# In[ ]:



