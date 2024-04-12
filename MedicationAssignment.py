#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

    def prescribe_medication(self, patient, medication_name, dosage, route, frequency):
        medication = Medication(medication_name, dosage, route, frequency)
        patient.medications.append(medication)
        print(f"Prescribed {medication_name} to {patient.name}: {dosage} {route}, {frequency}.")

class Nurse(User):
    def view_patient_medications(self, patient):
        print(f"Nurse {self.username} viewing medications for {patient.name}:")
        for med in patient.medications:
            print(f"{med.name}, {med.dosage}, {med.route}, {med.frequency}")

class Patient:
    def __init__(self, name):
        self.name = name
        self.medications = []

    def view_medications(self):
        print(f"{self.name}'s medications:")
        for med in self.medications:
            print(f"{med.name}, {med.dosage}, {med.route}, {med.frequency}")

class Medication:
    def __init__(self, name, dosage, route, frequency):
        self.name = name
        self.dosage = dosage
        self.route = route
        self.frequency = frequency

