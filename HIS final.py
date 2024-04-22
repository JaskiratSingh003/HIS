#!/usr/bin/env python
# coding: utf-8

# Doctor module

class Person: #Person class for each of the other classes to inherit from. 
    def __init__(self, first_name, last_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    def get_unmasked_name(self): #Method to get the full name of a person. 
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self): # Method to get masked name instead of full name for a person.
        return f"{self.first_name[0]}{'*' * (len(self.first_name) - 1)} {self.last_name[0]}{'*' * (len(self.last_name) - 1)}"
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
        first_name = input("First name: ")
        last_name = input("Last name: ")
        department = input("Department: ")
        doctor_id = input("Create a username for the doctor: ")
        password = input("Create a password for the doctor: ")
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
            patient = Patient.patient_records[patient_id]
            patient.display_profile_unmasked()
            if patient.vitals:  
                print("\nPatient Vitals:")
                patient.display_vitals()
            else:
                print("Vitals not available.")
            
            if patient.medications:
                print("\nMedications Prescribed:")
                patient.display_medications()
            else:
                print("No medications prescribed.")
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

    def prescribe_medication(self, patient_id):
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            medication_name = input("Enter medication name: ")
            dosage = input("Enter dosage: ")
            route = input("Enter route (PO, IV, injection): ")
            frequency = input("Enter frequency: ")
            patient.prescribe_medication(medication_name, dosage, route, frequency)
            print(f"The following medication has been prescribed successfully for patient {patient.get_full_name()}: {medication_name}, Dosage: {dosage}, Route: {route}, Frequency: {frequency}")
        else:
            print("Patient not found in records.")
            
    def update_patient_details(self, patient_id):
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            print(f"Current details for {patient.get_full_name()}:")
            print("Name:", patient.get_full_name())
            print("Patient ID:", patient.patient_id)
            print("Age:", patient.age)
            print("Address:", patient.address)
            print("Admit Date:", patient.admit_date)
    
        # Check if the patient has vitals
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

        # Check if the patient has medications prescribed
        if patient.medications:
            print("\nCurrent medications prescribed:")
            for medication in patient.medications:
                print(f"Medication Name: {medication['Medication Name']}, Dosage: {medication['Dosage']}, Route: {medication['Route']}, Frequency: {medication['Frequency']}")

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

        # Update vitals
        print("\nEnter new vitals (leave blank to keep existing):")
        height = input(f"Height [{patient.vitals.height}]: ") or patient.vitals.height
        weight = input(f"Weight [{patient.vitals.weight}]: ") or patient.vitals.weight
        pulse = input(f"Pulse Rate [{patient.vitals.pulse}]: ") or patient.vitals.pulse
        bp = input(f"Blood Pressure [{patient.vitals.bp}]: ") or patient.vitals.bp
        organ_donor = input(f"Organ Donor [{patient.vitals.organ_donor}]: ") or patient.vitals.organ_donor
        dnr = input(f"DNR [{patient.vitals.dnr}]: ") or patient.vitals.dnr
        dietary_restrictions = input(f"Dietary Restrictions [{patient.vitals.dietary_restrictions}]: ") or patient.vitals.dietary_restrictions
        smoker = input(f"Smoker [{patient.vitals.smoker}]: ") or patient.vitals.smoker

        # Update vitals details
        patient.vitals.height = height
        patient.vitals.weight = weight
        patient.vitals.pulse = pulse
        patient.vitals.bp = bp
        patient.vitals.organ_donor = organ_donor
        patient.vitals.dnr = dnr
        patient.vitals.dietary_restrictions = dietary_restrictions
        patient.vitals.smoker = smoker

        # Update medications
        print("\nEnter new medications (leave blank to keep existing):")
        for medication in patient.medications:
            medication_name = input(f"Medication Name [{medication['Medication Name']}]: ") or medication['Medication Name']
            dosage = input(f"Dosage [{medication['Dosage']}]: ") or medication['Dosage']
            route = input(f"Route [{medication['Route']}]: ") or medication['Route']
            frequency = input(f"Frequency [{medication['Frequency']}]: ") or medication['Frequency']

            # Update medication details
            medication['Medication Name'] = medication_name
            medication['Dosage'] = dosage
            medication['Route'] = route
            medication['Frequency'] = frequency

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

    def create_nurse(self):
        first_name = input("Enter nurse's first name: ")
        last_name = input("Enter nurse's last name: ")
        department = input("Enter nurse's department: ")
        floor_number = input("Enter nurse's floor number: ")
        nurse_id = input("Create a username for the nurse: ")
        password = input("Create a password for the nurse: ")
        new_nurse = Nurse(first_name, last_name, department, floor_number, nurse_id, password)
        Nurse.nurse_directory[(nurse_id, password)] = new_nurse
        print("\nNurse has been successfully added!")
        return new_nurse

    def enter_vitals(self, patient_id):
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
            patient.vitals = Vitals(height, weight, bp, pulse, smoker, organ_donor, dnr, dietary_restrictions)
            print(f"Entered vitals for {patient.get_full_name()}: Height {height} cm, Weight {weight} kg.")
        else:
            print("Patient not found in records.")

# Nurse module
class Nurse(Person):
    nurse_directory = {} #Directory to store nurses and nurse information in.

    def __init__(self, first_name, last_name, department, floor_number, nurse_id, password):
        super().__init__(first_name, last_name, department)
        self.floor_number = floor_number 
        self.nurse_id = nurse_id
        self.password = password
        Nurse.nurse_directory[(nurse_id, password)] = self

    def get_nurse_id_pass(self): #Method to get nurse ID (from optional module). 
        return self.nurse_id, self.password

    @staticmethod
    def view_patient_details(patient_id): #Method to view patient details of any patient.
        if patient_id in Patient.patient_records:
            print("\nPatient Details:")
            Patient.patient_records[patient_id].display_profile_unmasked()
            if Patient.patient_records[patient_id].medications:
                print("\nMedications Prescribed:")
                Patient.patient_records[patient_id].display_medications()
            else:
                print("No medications prescribed.")
        else:
            print("Patient not found in records.")

    def enter_vitals(self, patient_id):
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
            patient.vitals = Vitals(height, weight, bp, pulse, smoker, organ_donor, dnr, dietary_restrictions)
            print(f"Entered vitals for {patient.get_full_name()}: Height {height} cm, Weight {weight} kg.")
        else:
            print("Patient not found in records.")
    
    def update_patient_details(self, patient_id):
        if patient_id in Patient.patient_records:
            patient = Patient.patient_records[patient_id]
            print(f"Current details for {patient.get_full_name()}:")
            print("Name:", patient.get_full_name())
            print("Patient ID:", patient.patient_id)
            print("Age:", patient.age)
            print("Address:", patient.address)
            print("Admit Date:", patient.admit_date)

            # Check if the patient has vitals
        
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

            print("\nEnter new vitals (leave blank to keep existing):")
            height = input(f"Height [{patient.vitals.height}]: ") or patient.vitals.height
            weight = input(f"Weight [{patient.vitals.weight}]: ") or patient.vitals.weight
            pulse = input(f"Pulse Rate [{patient.vitals.pulse}]: ") or patient.vitals.pulse
            bp = input(f"Blood Pressure [{patient.vitals.bp}]: ") or patient.vitals.bp
            organ_donor = input(f"Organ Donor [{patient.vitals.organ_donor}]: ") or patient.vitals.organ_donor
            dnr = input(f"DNR [{patient.vitals.dnr}]: ") or patient.vitals.dnr
            dietary_restrictions = input(f"Dietary Restrictions [{patient.vitals.dietary_restrictions}]: ") or patient.vitals.dietary_restrictions
            smoker = input(f"Smoker [{patient.vitals.smoker}]: ") or patient.vitals.smoker

            # Update vitals details
            patient.vitals.height = height
            patient.vitals.weight = weight
            patient.vitals.pulse = pulse
            patient.vitals.bp = bp
            patient.vitals.organ_donor = organ_donor
            patient.vitals.dnr = dnr
            patient.vitals.dietary_restrictions = dietary_restrictions
            patient.vitals.smoker = smoker

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

            print("\nPatient vitals updated successfully.")
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
        self.medical_costs = [] # List to store medical costs
        self.vitals = None  
        self.medications = []  
        Patient.patient_records[self.patient_id] = self

    def display_profile_unmasked(self):
        print(f"Name: {self.get_unmasked_name()}")
        print(f"Patient ID: {self.patient_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Admit Date: {self.admit_date}")
        print(f"Total Medical Bill: ${self.get_total_bill():,.2f}")

    def display_vitals(self):
        print(f"Height: {self.vitals.height} cm")
        print(f"Weight: {self.vitals.weight} kg")
        print(f"Pulse Rate: {self.vitals.pulse} bpm")
        print(f"Blood Pressure: {self.vitals.bp}")
        print(f"Organ Donor: {'Yes' if self.vitals.organ_donor else 'No'}")
        print(f"DNR: {'Yes' if self.vitals.dnr else 'No'}")
        print(f"Dietary Restrictions: {self.vitals.dietary_restrictions}")
        print(f"Smoker: {'Yes' if self.vitals.smoker else 'No'}")

    def add_medical_cost(self, cost):
        self.medical_costs.append(cost)

    def add_lab_test(self, test_name, test_cost):
        self.medical_costs.append(test_name)
        self.medical_costs.append(test_cost)

    def get_total_bill(self):
        return sum(self.medical_costs[1::2])

    def prescribe_medication(self, medication_name, dosage, route, frequency):
        self.medications.append({
            "Medication Name": medication_name,
            "Dosage": dosage,
            "Route": route,
            "Frequency": frequency
        })

    def display_medications(self):
        for med in self.medications:
            print(f"Medication Name: {med['Medication Name']}, Dosage: {med['Dosage']}, Route: {med['Route']}, Frequency: {med['Frequency']}")

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

def view_vitals(self):
    if self.vitals:
        print(f"{self.name}'s Vitals: Height {self.vitals.height} cm, Weight {self.vitals.weight} kg, "
              f"Organ Donor: {'Yes' if self.vitals.organ_donor else 'No'}, DNR: {'Yes' if self.vitals.dnr else 'No'}, "
              f"Dietary Restrictions: {self.vitals.dietary_restrictions}")
    else:
        print("No vitals information available.")

# Discharge module
def create_discharge_report(patient):
    filename = f"{patient.patient_id}_discharged.txt"
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

# Vitals class
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

# Main menu
# Create the default doctor
default_doctor = Doctor("Chief", "Doctor", "General", "chief", "12345")

while True:
    user_type = input("Are you a Doctor (D), Nurse (N), or Patient (P)? ")
    if user_type.upper() == 'D':
        doctor_login = input("Enter your doctor username: ")
        doctor_password = input("Enter your doctor password: ")
        if (doctor_login, doctor_password) in Doctor.doctor_directory:
            doctor = Doctor.doctor_directory[(doctor_login, doctor_password)]
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
                choice = int(input("Enter your choice (1-11): "))
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
                elif choice == 8:
                    nurse = Nurse("Nurse", "Default", "General", "1", "nd", "password")  
                    while True:
                        print("What would you like to do?")
                        print("1. Create patient")
                        print("2. View patient details")
                        print("3. Enter patient vitals")
                        print("4. Update patient details")
                        print("5. Exit")
                        choice = int(input("Enter your choice (1-5): "))
        
                        if choice == 1:
                            doctor.create_patient()
                        elif choice == 2:
                            patient_id = input("Enter Patient ID to view details: ")
                            doctor.view_patient_details(patient_id)
                        elif choice == 3:
                            if nurse:
                                patient_id = input("Enter Patient ID to enter vitals: ")
                                nurse.enter_vitals(patient_id)
                            else:
                                print("Nurse is not available. Create Nurse ID first and then try again.")
                        elif choice == 4:
                            if nurse:
                                patient_id = input("Enter Patient ID to update details: ")
                                nurse.update_patient_details(patient_id)
                            else:
                                print("Nurse is not available. Create Nurse ID first and then try again.")
                        elif choice == 5:
                            print("Exiting the system...")
                            break
                        else:
                            print("Invalid choice. Please try again.")

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
                    print("Invalid choice. Please try again.")
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
                choice = int(input("Enter your choice (1-11): "))
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
                print("3. Enter patient vitals")
                print("4. Exit")
                choice = int(input("Enter your choice (1-4): "))
                if choice == 1:
                    nurse.create_patient()
                elif choice == 2:
                    patient_id = input("Enter Patient ID to view details: ")
                    Nurse.view_patient_details(patient_id)
                elif choice == 3:
                    patient_id = input("Enter Patient ID to enter vitals: ")
                    nurse.enter_vitals(patient_id)
                elif choice == 4:
                    print("Exiting the system...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid nurse credentials. Please try again.")
    elif user_type.upper() == 'P':
        print("Patients do not have access to this system.")
    else:
        print("Invalid user type. Please try again.")
