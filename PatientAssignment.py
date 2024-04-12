#!/usr/bin/env python
# coding: utf-8

# In[1]:


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password

class Doctor(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.patients = {}
    
    def create_nurse(self, username, password):
        return Nurse(username, password)

    def order_labs(self, patient):
        print(f"Ordering labs for {patient.name}.")

    def prescribe_meds(self, medication):
        print(f"Prescribing {medication}.")

    def assign_patient(self, patient, doctor = None, nurse = None):
        patient.assigned_doctor = doctor if doctor else self
        patient.assigned_nurse = nurse
        self.patients[patient.name] = patient
        print(f"Assigned patient {patient.name} to doctor {patient.assigned_doctor.username} and nurse {patient.assigned_nurse.username if nurse else 'none'}.")

class Nurse(User):
    def view_patient_info(self, patient):
        print(f"Nurse {self.username} viewing information for {patient.name}.")
        if patient.assigned_doctor:
            print(f"Doctor: {patient.assigned_doctor.username}")
        if patient.assigned_nurse:
            print(f"Nurse: {patient.assigned_nurse.username}")

class Patient:
    def __init__(self, name):
        self.name = name
        self.assigned_doctor = None
        self.assigned_nurse = None

    def view_assigned_staff(self):
        if self.assigned_doctor:
            print(f"Patient's assigned doctor: {self.assigned_doctor.username}")
        if self.assigned_nurse:
            print(f"Patient's assigned nurse: {self.assigned_nurse.username}")

