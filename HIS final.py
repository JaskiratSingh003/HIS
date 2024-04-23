#!/usr/bin/env python
# coding: utf-8

# HIS Final

# Person Class: The person class takes in the full name of anyone in the hospital system including doctors, nurses, and patients.
# Other classes will use Person class to inherit. 
class Person: 
    def __init__(self, first_name, last_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    # The get_unmasked_name() method will display the full name of the person they are trying to view.
    # Only the doctors and nurses can see the full name unmasked.
    def get_unmasked_name(self): 
        return f"{self.first_name} {self.last_name}"

    # The get_full_name() method will mask the full name of the person. This will only occur of Patient mode is activated.
    def get_full_name(self): 
        return f"{self.first_name[0]}{'*' * (len(self.first_name) - 1)} {self.last_name[0]}{'*' * (len(self.last_name) - 1)}"

# Doctor Class: The doctor class inherits from Person and uses its information to provide a variety of functions for the patient and nurse.
class Doctor(Person):

    # The doctor_directory starts out as an empty dictionary to store information when a new doctor is created.
    doctor_directory = {}

    # Initialize using Person class and add in the username and password for the doctor to sign in. 
    def __init__(self, first_name, last_name, department, doctor_id, password):
        super().__init__(first_name, last_name, department)
        self.doctor_id = doctor_id
        self.password = password
        Doctor.doctor_directory[(doctor_id, password)] = self

    # The get_doc_id_pass() method will return the information for the doctor's ID and password.
    def get_doc_id_pass(self):
        return self.doctor_id, self.password
    
    # Create a new doctor with an ID and password, and store this information into the directory.
    def add_doc_to_directory(self):

        # Items the doctors have to manually input.
        first_name = input("First name: ")
        last_name = input("Last name: ")
        department = input("Department: ")
        doctor_id = input("Create a username for the doctor: ")
        password = input("Create a password for the doctor: ")

        # Return a new Doctor object and add to the directory.
        new_doctor = Doctor(first_name, last_name, department, doctor_id, password)
        Doctor.doctor_directory[(doctor_id, password)] = new_doctor
        print("\nDoctor has been successfully added!")
        return new_doctor

    # Create a new patient and store the information into the patient directory.
    def create_patient(self):

        # Obtain the new patient from get_patient_info() since this method contains the inputs for a new patient which is in the Patient module.
        new_patient = get_patient_info()

        # Do no do anything if there is nothing found.
        if new_patient is None:
            return None

        # Create the patient and add into the patient dictionary.
        else:
            Patient.patient_records[new_patient.patient_id] = new_patient
            print("\nPatient has been successfully added into the system!")
        return new_patient

    # This method will let you view a specific patient if you have their patient ID.
    def view_patient_details(self, patient_id):

        # If the patient ID exists in the patient records system, display its profile.
        # The patient_records() method is in the Patient class.
        if patient_id in Patient.patient_records:
            print("\nPatient Details:")
            patient = Patient.patient_records[patient_id]
            patient.display_profile_unmasked()

            # Check if there are inputs for vitals.
            if patient.vitals:  
                print("\nPatient Vitals:")
                patient.display_vitals()

            # There are no vitals listed.
            else:
                print("Vitals not available.")

            # Check if there are inputs for medication.
            if patient.medications:
                print("\nMedications Prescribed:")
                patient.display_medications()
            
            # There are no medications listed.
            else:
                print("No medications prescribed.")
        
        # The ID entered does not exist in the system.
        else:
            print("Patient not found in records.")

    # The physician can order a lab test to a patient once they obtain the patient ID.
    def order_lab_tests(self, patient_id):

        # If the patient ID exists in the patient records system, order the lab test. 
        # The patient_records() method is in the Patient class.
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]

            # Enter the test name and cost and add it into the profile.
            test_name = input("Enter lab test name: ")
            test_cost = float(input("Enter cost of test: "))
            patient.add_lab_test(test_name, test_cost)
            print(f"The following lab test has been ordered successfully for patient {patient.get_full_name()}: {test_name}, ${test_cost}")
        
        # The ID entered does not exist in the system.
        else:
            print("Patient not found in records.")

    # Optional Module - Meds: The prescribe_medication() method will add medication(s) information and instructions to the patient's info. 
    def prescribe_medication(self, patient_id):

        # If the patient ID exists in the patient records system, add in a medication.
        # The patient_records() method is in the Patient class.
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]

            # The doctor can input the patient medication.
            medication_name = input("Enter medication name: ")
            dosage = input("Enter dosage: ")
            route = input("Enter route (PO, IV, injection): ")
            frequency = input("Enter frequency: ")
            patient.prescribe_medication(medication_name, dosage, route, frequency)
            print(f"The following medication has been prescribed successfully for patient {patient.get_full_name()}: {medication_name}, Dosage: {dosage}, Route: {route}, Frequency: {frequency}")
        
        # The cannot find the patient in the system.
        else:
            print("Patient not found in records.")
            
    # This method will allow the doctor to update any information that was previously inputted.
    def update_patient_details(self, patient_id):

        # Find the patient ID first in patient_records(). Print out the current detail onto the screen.
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            print(f"Current details for {patient.get_full_name()}:")
            print("Name:", patient.get_full_name())
            print("Patient ID:", patient.patient_id)
            print("Age:", patient.age)
            print("Address:", patient.address)
            print("Admit Date:", patient.admit_date)
    
        # Check if the patient has vitals.
        if patient.vitals:
            print("\nCurrent vitals:")
            print("Height:", patient.vitals.height, "cm")
            print("Weight:", patient.vitals.weight, "kg")
            print("Pulse Rate:", patient.vitals.pulse, "bpm")
            print("Blood Pressure:", patient.vitals.bp)
            print("Organ Donor:", "Yes" if patient.vitals.organ_donor else "No")
            print("DNR:", "Yes" if patient.vitals.dnr else "No")
            print("Dietary Restrictions:", patient.vitals.dietary_restrictions)
            print("Smoker:", "Yes" if patient.vitals.smoker else "No") 

        # Check if the patient has medications prescribed.
        if patient.medications:
            print("\nCurrent medications prescribed:")
            for medication in patient.medications:
                print(f"Medication Name: {medication['Medication Name']}, Dosage: {medication['Dosage']}, Route: {medication['Route']}, Frequency: {medication['Frequency']}")

        # Update the profile and leave blank if you do not need to update other items.
        print("\nEnter new details (leave blank to keep existing):")
        first_name = input(f"First name [{patient.first_name}]: ") or patient.first_name
        last_name = input(f"Last name [{patient.last_name}]: ") or patient.last_name
        age = input(f"Age [{patient.age}]: ") or patient.age
        address = input(f"Address [{patient.address}]: ") or patient.address
        admit_date = input(f"Admit date [{patient.admit_date}]: ") or patient.admit_date

        # Update patient details
        patient.first_name = first_name
        patient.last_name = last_name
        patient.age = age
        patient.address = address
        patient.admit_date = admit_date

        # Update vitals.
        print("\nEnter new vitals (leave blank to keep existing):")
        height = input(f"Height [{patient.vitals.height}]: ") or patient.vitals.height
        weight = input(f"Weight [{patient.vitals.weight}]: ") or patient.vitals.weight
        pulse = input(f"Pulse Rate [{patient.vitals.pulse}]: ") or patient.vitals.pulse
        bp = input(f"Blood Pressure [{patient.vitals.bp}]: ") or patient.vitals.bp
        organ_donor = input(f"Organ Donor [{patient.vitals.organ_donor}]: ") or patient.vitals.organ_donor
        dnr = input(f"DNR [{patient.vitals.dnr}]: ") or patient.vitals.dnr
        dietary_restrictions = input(f"Dietary Restrictions [{patient.vitals.dietary_restrictions}]: ") or patient.vitals.dietary_restrictions
        smoker = input(f"Smoker [{patient.vitals.smoker}]: ") or patient.vitals.smoker

        # Update vitals details.
        patient.vitals.height = height
        patient.vitals.weight = weight
        patient.vitals.pulse = pulse
        patient.vitals.bp = bp
        patient.vitals.organ_donor = organ_donor
        patient.vitals.dnr = dnr
        patient.vitals.dietary_restrictions = dietary_restrictions
        patient.vitals.smoker = smoker

        # Update medications.
        print("\nEnter new medications (leave blank to keep existing):")
        for medication in patient.medications:
            medication_name = input(f"Medication Name [{medication['Medication Name']}]: ") or medication['Medication Name']
            dosage = input(f"Dosage [{medication['Dosage']}]: ") or medication['Dosage']
            route = input(f"Route [{medication['Route']}]: ") or medication['Route']
            frequency = input(f"Frequency [{medication['Frequency']}]: ") or medication['Frequency']

            # Update medication details.
            medication['Medication Name'] = medication_name
            medication['Dosage'] = dosage
            medication['Route'] = route
            medication['Frequency'] = frequency

            # All the information has been updated.
            print("\nPatient details updated successfully.")

        # The ID entered does not exist in the system.
        else:
            print("Patient not found in records.")

    # When the patient is ready to leave the hospital, they can be discharged with the bill.
    def discharge_patient(self):

        # Enter the existing patient ID and the system will remove the patient in the dictionary by finding the 
        # ID and popping out the information.
        patient_id = input("Enter Patient ID to discharge: ")
        if patient_id in Patient.patient_records:
            discharged_patient = Patient.patient_records.pop(patient_id)
            print(f"{discharged_patient.get_full_name()} has been discharged.")
            
            # As part of the discharge module, the discharged patient will obtain a txt file showing their total bill.
            create_discharge_report(discharged_patient)
        
        # The ID entered does not exist in the system.
        else:
            print("Patient not found in records.")

    # Optional Module - Nurse Login: Create a nurse login. Only doctors have the ability to create a new nurse login.
    def create_nurse(self):

        # Input the nurse's information.
        first_name = input("Enter nurse's first name: ")
        last_name = input("Enter nurse's last name: ")
        department = input("Enter nurse's department: ")
        floor_number = input("Enter nurse's floor number: ")
        nurse_id = input("Create a username for the nurse: ")
        password = input("Create a password for the nurse: ")

        # Add the nurse's information into the nurses directory.
        new_nurse = Nurse(first_name, last_name, department, floor_number, nurse_id, password)
        Nurse.nurse_directory[(nurse_id, password)] = new_nurse
        print("\nNurse has been successfully added!")
        return new_nurse

    # Optional Module - Vitals: The enter_vitals() method adds patient's vitals to their information. Nurses can also enter vitals.
    def enter_vitals(self, patient_id): 

        # Find the patient ID in the system and add the vitals through the inputs given.
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            height = float(input("Enter patient's height (cm): "))
            weight = float(input("Enter patient's weight (kg): "))
            bp = input("Enter patient's blood pressure: ")
            pulse = input("Enter patient's pulse rate: ")
            smoker = input("Is the patient a smoker? (Y/N): ").upper() == 'Y'
            organ_donor = input("Is the patient an organ donor? (Y/N): ").upper() == 'Y'
            dnr = input("Does the patient have a DNR (Do Not Resuscitate) order? (Y/N): ").upper() == 'Y'
            dietary_restrictions = input("Enter any dietary restrictions (or 'None'): ")
            
            # Vitals are added into the patient's account.
            patient.vitals = Vitals(height, weight, bp, pulse, smoker, organ_donor, dnr, dietary_restrictions)
            print(f"Entered vitals for {patient.get_full_name()}: Height {height} cm, Weight {weight} kg.")
        
        # User is unable to find the patient ID.
        else:
            print("Patient not found in records.")

# Nurse Class: The Nurse class inherits from Person class to obtain basic information about the nurse and display the profile based on the chosen method.
class Nurse(Person):

    # Directory to store nurses and nurse information in.
    nurse_directory = {} 

    # Initialize from the Person class and add in the floor number, nurse ID, and password for attributes.
    def __init__(self, first_name, last_name, department, floor_number, nurse_id, password):
        super().__init__(first_name, last_name, department)
        self.floor_number = floor_number 
        self.nurse_id = nurse_id
        self.password = password
        Nurse.nurse_directory[(nurse_id, password)] = self

    # Method to get nurse ID (from optional module). 
    def get_nurse_id_pass(self): 
        return self.nurse_id, self.password

    # Method to view patient details of any patient if you have their patient ID. This method is similar to the doctor's version of viewing a patient info.
    def view_patient_details(patient_id): 

        # If the patient information exists in the system, view the profile.
        if patient_id in Patient.patient_records:
            print("\nPatient Details:")
            Patient.patient_records[patient_id].display_profile_unmasked()

            # If there are medications in the profile, view it.
            if Patient.patient_records[patient_id].medications:
                print("\nMedications Prescribed:")
                Patient.patient_records[patient_id].display_medications()
            
            # Medications were not entered.
            else:
                print("No medications prescribed.")
        
        # Patient ID not found.
        else:
            print("Patient not found in records.")

    # Optional Module - Vitals: The enter_vitals() method to enter vitals. Doctor and nurse have this ability only. 
    def enter_vitals(self, patient_id): 

        # Patient exists in the system.
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]

            # User can input the vitals.
            height = float(input("Enter patient's height (cm): "))
            weight = float(input("Enter patient's weight (kg): "))
            bp = input("Enter patient's blood pressure: ")
            pulse = input("Enter patient's pulse rate: ")
            smoker = input("Is the patient a smoker? (Y/N): ").upper() == 'Y'
            organ_donor = input("Is the patient an organ donor? (Y/N): ").upper() == 'Y'
            dnr = input("Does the patient have a DNR (Do Not Resuscitate) order? (Y/N): ").upper() == 'Y'
            dietary_restrictions = input("Enter any dietary restrictions (or 'None'): ")

            # Add vitals into the patient directory.
            patient.vitals = Vitals(height, weight, bp, pulse, smoker, organ_donor, dnr, dietary_restrictions)
            print(f"Entered vitals for {patient.get_full_name()}: Height {height} cm, Weight {weight} kg.")
        
        # Patient information does not exist in the system.
        else:
            print("Patient not found in records.")

    # The update_patient_details() method will let the doctor or nurse update the patient's profile.
    def update_patient_details(self, patient_id):

        # Patient ID exists in the system.
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            print(f"Current details for {patient.get_full_name()}:")
            print("Name:", patient.get_full_name())
            print("Patient ID:", patient.patient_id)
            print("Age:", patient.age)
            print("Address:", patient.address)
            print("Admit Date:", patient.admit_date)

            # Check if the patient has vitals.
            if patient.vitals:
                print("\nCurrent vitals:")
                print("Height:", patient.vitals.height, "cm")
                print("Weight:", patient.vitals.weight, "kg")
                print("Pulse Rate:", patient.vitals.pulse, "bpm")
                print("Blood Pressure:", patient.vitals.bp)
                print("Organ Donor:", "Yes" if patient.vitals.organ_donor else "No")
                print("DNR:", "Yes" if patient.vitals.dnr else "No")
                print("Dietary Restrictions:", patient.vitals.dietary_restrictions)
                print("Smoker:", "Yes" if patient.vitals.smoker else "No")

            # Input the new vitals for the patient.
            print("\nEnter new vitals (leave blank to keep existing):")
            height = input(f"Height [{patient.vitals.height}]: ") or patient.vitals.height
            weight = input(f"Weight [{patient.vitals.weight}]: ") or patient.vitals.weight
            pulse = input(f"Pulse Rate [{patient.vitals.pulse}]: ") or patient.vitals.pulse
            bp = input(f"Blood Pressure [{patient.vitals.bp}]: ") or patient.vitals.bp
            organ_donor = input(f"Organ Donor [{patient.vitals.organ_donor}]: ") or patient.vitals.organ_donor
            dnr = input(f"DNR [{patient.vitals.dnr}]: ") or patient.vitals.dnr
            dietary_restrictions = input(f"Dietary Restrictions [{patient.vitals.dietary_restrictions}]: ") or patient.vitals.dietary_restrictions
            smoker = input(f"Smoker [{patient.vitals.smoker}]: ") or patient.vitals.smoker

            # Update vitals details.
            patient.vitals.height = height
            patient.vitals.weight = weight
            patient.vitals.pulse = pulse
            patient.vitals.bp = bp
            patient.vitals.organ_donor = organ_donor
            patient.vitals.dnr = dnr
            patient.vitals.dietary_restrictions = dietary_restrictions
            patient.vitals.smoker = smoker

            # Update the patient information or leave it blank if that section does not need to be updated.
            print("\nEnter new details (leave blank to keep existing):")
            first_name = input(f"First name [{patient.first_name}]: ") or patient.first_name
            last_name = input(f"Last name [{patient.last_name}]: ") or patient.last_name
            age = input(f"Age [{patient.age}]: ") or patient.age
            address = input(f"Address [{patient.address}]: ") or patient.address
            admit_date = input(f"Admit date [{patient.admit_date}]: ") or patient.admit_date
    
            # Update patient details.
            patient.first_name = first_name
            patient.last_name = last_name
            patient.age = age
            patient.address = address
            patient.admit_date = admit_date

            print("\nPatient vitals updated successfully.")
        
        # The patient ID is not found.
        else:
            print("Patient not found in records.")
            
# Patient Class: The Patient class will have its information updated from either the Doctor or Nurse based on the module they choose to take. 
class Patient(Person):

    # The patient_records will store in patient information through the dictionary. 
    # Start out with an empty dictionary because there are no patients present to store information.
    patient_records = {}

    # Initialize from the Person class and add in the patient ID, age, address, and admission date.
    def __init__(self, first_name, last_name, department, patient_id, age, address, admit_date):
        super().__init__(first_name, last_name, department)
        self.patient_id = patient_id
        self.age = age
        self.address = address
        self.admit_date = admit_date
        self.medical_costs = [] # This is a list to store medical costs.
        self.vitals = None  # Vitals have not been entered yet until needed.
        self.medications = []  # This is a list to store medication.
        Patient.patient_records[self.patient_id] = self

    # The profile will be unmasked when displaying.
    def display_profile_unmasked(self):
        print(f"Name: {self.get_unmasked_name()}")
        print(f"Patient ID: {self.patient_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Admit Date: {self.admit_date}")
        print(f"Total Medical Bill: ${self.get_total_bill():,.2f}")

    # The method will display the vitals.
    def display_vitals(self):
        print(f"Height: {self.vitals.height} cm")
        print(f"Weight: {self.vitals.weight} kg")
        print(f"Pulse Rate: {self.vitals.pulse} bpm")
        print(f"Blood Pressure: {self.vitals.bp}")
        print(f"Organ Donor: {'Yes' if self.vitals.organ_donor else 'No'}")
        print(f"DNR: {'Yes' if self.vitals.dnr else 'No'}")
        print(f"Dietary Restrictions: {self.vitals.dietary_restrictions}")
        print(f"Smoker: {'Yes' if self.vitals.smoker else 'No'}")

    # Append the medical cost when the cost input is entered from the Doctor.
    def add_medical_cost(self, cost):
        self.medical_costs.append(cost)

    # Append the medical cost when the test name and cost input is entered from the Doctor.
    def add_lab_test(self, test_name, test_cost):
        self.medical_costs.append(test_name)
        self.medical_costs.append(test_cost)

    # Add in the total cost that the Doctor entered in. 
    def get_total_bill(self):
        return sum(self.medical_costs[1::2])

    # Patient is able to get their medication information. 
    def prescribe_medication(self, medication_name, dosage, route, frequency):
        self.medications.append({
            "Medication Name": medication_name,
            "Dosage": dosage,
            "Route": route,
            "Frequency": frequency
        })

    # Show the medications provided from the medications input.
    def display_medications(self):
        for med in self.medications:
            print(f"Medication Name: {med['Medication Name']}, Dosage: {med['Dosage']}, Route: {med['Route']}, Frequency: {med['Frequency']}")

# In this method, a new patient is created when either the Doctor or Nurse chooses this function. 
# The information will get added into the system.
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

# The method will give you the option to view the patient's vitals.
def view_vitals(self):
    if self.vitals:
        print(f"{self.name}'s Vitals: Height {self.vitals.height} cm, Weight {self.vitals.weight} kg, "
              f"Organ Donor: {'Yes' if self.vitals.organ_donor else 'No'}, DNR: {'Yes' if self.vitals.dnr else 'No'}, "
              f"Dietary Restrictions: {self.vitals.dietary_restrictions}")
    else:
        print("No vitals information available.")

# # Discharge Class: The Discharge class will take in the patient and create a txt file that will display its name, test orders, and total cost. 
def create_discharge_report(patient):

    # Create the filename.
    filename = f"{patient.patient_id}_discharged.txt"
    
    # Write in the information as requested and close when it is done writing.
    with open(filename, "w") as f:
        f.write(f"Patient Name: {patient.get_full_name()}\n")
        f.write("Lab Tests Ordered:\n")
        for i, (test_name, test_cost) in enumerate(zip(patient.medical_costs[::2], patient.medical_costs[1::2]), start=1):
            f.write(f"{i}. {test_name}: ${test_cost:.2f}\n")
        f.write("\nMedications Prescribed:\n")
        for med in patient.medications:
            f.write(f"{med['Medication Name']}, Dosage: {med['Dosage']}, Route: {med['Route']}, Frequency: {med['Frequency']}\n")
        f.write(f"\nTotal Medical Bill: ${patient.get_total_bill():,.2f}")
    print(f"Discharge report for {patient.get_full_name()} has been created.")
    print(f"Filename: {filename}")

# Optional Module - Vitals Class: This class takes in the information from either the doctor or nurse and adds it into the patient information.
class Vitals:
    def __init__(self, height, weight, bp, pulse, smoker, organ_donor, dnr, dietary_restrictions):
        self.height = height
        self.weight = weight
        self.bp = bp
        self.pulse = pulse
        self.smoker = smoker
        self.organ_donor = organ_donor
        self.dnr = dnr
        self.dietary_restrictions = dietary_restrictions

# Main Menu

# Create the default doctor.
default_doctor = Doctor("Chief", "Doctor", "General", "chief", "12345")

while True:

    # The user will have three options to choose from: Doctor, Nurse, or Patient.
    user_type = input("Are you a Doctor (D), Nurse (N), or Patient (P)? ")
    if user_type.upper() == 'D':

        # The doctor must type in a specific username and password to log in.
        doctor_login = input("Enter your doctor username: ")
        doctor_password = input("Enter your doctor password: ")
        if (doctor_login, doctor_password) in Doctor.doctor_directory:
            doctor = Doctor.doctor_directory[(doctor_login, doctor_password)]
            print(f"Hello Doctor {doctor.get_unmasked_name()}")

            # The doctor has a variety of options to choose from the menu.
            while True:

                # The list of tasks the doctor can choose from. 
                print("\n\nWhat would you like to do?")
                print("1. Create new doctor")
                print("2. Create new nurse")
                print("3. Create patient")
                print("4. View patient details")
                print("5. Order lab tests")
                print("6. Update patient details")
                print("7. Discharge patient")
                print("8. Switch to Nurse view")
                print("9. Enter patient vitals")
                print("10. Prescribe medication")
                print("11. Exit\n\n")
                choice = int(input("\nEnter your choice (1-11): "))
                
                # Create a new doctor.
                if choice == 1:
                    new_doctor = doctor.add_doc_to_directory()
                    Doctor.doctor_directory[(new_doctor.doctor_id, new_doctor.password)] = new_doctor
               
                # Create a new nurse.
                elif choice == 2:
                    new_nurse = doctor.create_nurse()
                    Nurse.nurse_directory[(new_nurse.nurse_id, new_nurse.password)] = new_nurse
                
                # Create a new patient.
                elif choice == 3:
                    doctor.create_patient()
                
                # Type in an existing patient to view its details.
                elif choice == 4:
                    patient_id = input("Enter Patient ID to view details: ")
                    doctor.view_patient_details(patient_id)
                
                # Order lab tests to the patient.
                elif choice == 5:
                    patient_id = input("Enter Patient ID to add test order: ")
                    doctor.order_lab_tests(patient_id)
                
                # Update any additional patient details.
                elif choice == 6:
                    patient_id = input("Enter Patient ID to update details: ")
                    doctor.update_patient_details(patient_id)
                
                # Discharge the patient.
                elif choice == 7:
                    doctor.discharge_patient()
                
                # Switch to nurse view.
                elif choice == 8:
                    nurse = Nurse("Nurse", "Default", "General", "1", "nd", "password")  
                    
                    # The nurse will have less options to choose from than the doctor. 
                    while True:
                        print("\nWhat would you like to do?")
                        print("1. Create patient")
                        print("2. View patient details")
                        print("3. Enter patient vitals")
                        print("4. Update patient details")
                        print("5. Exit")
                        choice = int(input("\nEnter your choice (1-5): "))
        
                        # Create a patient.
                        if choice == 1:
                            doctor.create_patient()

                        # View patient information.
                        elif choice == 2:
                            patient_id = input("Enter Patient ID to view details: ")
                            doctor.view_patient_details(patient_id)
                        
                        # Enter patient vitals.
                        elif choice == 3:
                            if nurse:
                                patient_id = input("Enter Patient ID to enter vitals: ")
                                nurse.enter_vitals(patient_id)
                            else:
                                print("Nurse is not available. Create Nurse ID first and then try again.")
                       
                        # Update patient details.
                        elif choice == 4:
                            if nurse:
                                patient_id = input("Enter Patient ID to update details: ")
                                nurse.update_patient_details(patient_id)
                            else:
                                print("Nurse is not available. Create Nurse ID first and then try again.")
                        
                        # Exiting the system will take you back to the doctor's menu.
                        elif choice == 5:
                            print("Exiting the system...")
                            break
                        
                        # Nurse did not follow the directions from the nurse's menu.
                        else:
                            print("\nInvalid choice. Please try again.")

                # Enter vitals for the patient.
                elif choice == 9:
                    patient_id = input("Enter Patient ID to enter vitals: ")
                    doctor.enter_vitals(patient_id)
               
                # Enter medication for the patient.
                elif choice == 10:
                    patient_id = input("Enter Patient ID to prescribe medication: ")
                    doctor.prescribe_medication(patient_id)
                
                # Exiting the system will take you back to the main menu.
                elif choice == 11:
                    print("Exiting the system...")
                    break
                
                # Options entered were not 1-11.
                else:
                    print("\nInvalid choice. Please try again.")
                    
        # Alternative way for the doctor to log in.
        elif (doctor_login, doctor_password) == ("chief", "12345"):
            doctor = default_doctor
            print(f"Hello Doctor {doctor.get_unmasked_name()}")
            while True:
                print("\n\nWhat would you like to do?")
                print("1. Create new doctor")
                print("2. Create new nurse")
                print("3. Create patient")
                print("4. View patient details")
                print("5. Order lab tests")
                print("6. Update patient details")
                print("7. Discharge patient")
                print("8. Switch to Nurse view")
                print("9. Enter patient vitals")
                print("10. Prescribe medication")
                print("11. Exit\n\n")
                choice = int(input("\nEnter your choice (1-11): "))
                if choice == 1:
                    new_doctor = doctor.add_doc_to_directory()
                    Doctor.doctor_directory[(new_doctor.doctor_id, new_doctor.password)] = new_doctor
                elif choice == 2:
                    new_nurse = doctor.create_nurse()
                    Nurse.nurse_directory[(new_nurse.nurse_id, new_nurse.password)] = new_nurse
                elif choice == 3:
                    doctor.create_patient()
                elif choice == 4:
                    patient_id = input("Enter Patient ID to view details: ")
                    doctor.view_patient_details(patient_id)
                elif choice == 5:
                    patient_id = input("Enter Patient ID to add test order: ")
                    doctor.order_lab_tests(patient_id)
                elif choice == 6:
                    patient_id = input("Enter Patient ID to update details: ")
                    doctor.update_patient_details(patient_id)
                elif choice == 7:
                    doctor.discharge_patient()
                elif choice == 9:
                    patient_id = input("Enter Patient ID to enter vitals: ")
                    doctor.enter_vitals(patient_id)
                elif choice == 10:
                    patient_id = input("Enter Patient ID to prescribe medication: ")
                    doctor.prescribe_medication(patient_id)
                elif choice == 11:
                    print("Exiting the system...")
                    break
                else:
                    print("\nInvalid choice. Please try again.")
            else:
                print("\nInvalid doctor credentials. Please try again.")
    
    # When the nurse login is successful, enter the nurse's menu.
    elif user_type.upper() == 'N':

        # Nurse has to type in their username and password. This will be taken from the doctor's creation.
        nurse_login = input("Enter your nurse username: ")
        nurse_password = input("Enter your nurse password: ")
        if (nurse_login, nurse_password) in Nurse.nurse_directory:
            nurse = Nurse.nurse_directory[(nurse_login, nurse_password)]
            print(f"Hello Nurse {nurse.get_full_name()}")

            # Options the nurse can choose from.
            while True:
                print("\nWhat would you like to do?")
                print("1. Create patient")
                print("2. View patient details")
                print("3. Enter patient vitals")
                print("4. Exit")
                choice = int(input("\nEnter your choice (1-4): "))

                # Create a patient.
                if choice == 1:
                    nurse.create_patient()

                # View patient information.
                elif choice == 2:
                    patient_id = input("Enter Patient ID to view details: ")
                    Nurse.view_patient_details(patient_id)
                
                # Enter patient vitals.
                elif choice == 3:
                    patient_id = input("Enter Patient ID to enter vitals: ")
                    nurse.enter_vitals(patient_id)
                
                # Exit the system back to the main menu.
                elif choice == 4:
                    print("Exiting the system...")
                    break
                
                # Options chosen were not 1-4.
                else:
                    print("\nInvalid choice. Please try again.")
        else:
            print("\nInvalid nurse credentials. Please try again.")
    
    # If patient is selected from the main menu.
    elif user_type.upper() == 'P':

        # Patient must enter their ID that the doctor or nurse created. 
        patient_id = input("Enter your patient ID: ")

        # Print out the medical bills to the patient. 
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            print(f"Hello {patient.get_full_name()}")
            print(f"Your total medical bill is: ${patient.get_total_bill():,.2f}")

        # Patient ID was not in the system.
        else:
            print("\nPatient not found in records.")
    
    # The main menu login was not either 'D', 'N', or 'P'.
    else:
        print("\nInvalid user type. Please try again.")
