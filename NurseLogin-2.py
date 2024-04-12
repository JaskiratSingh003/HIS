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
        self.nurses = []

    def create_nurse(self, username, password):
        nurse = Nurse(username, password)
        self.nurses.append(nurse)
        return nurse

    def order_labs(self, patient):
        print(f"Ordering labs for {patient}.")

    def prescribe_meds(self, medication):
        print(f"Prescribing {medication}.")

    def assign_patient(self, patient, nurse):
        print(f"Assigning patient {patient} to nurse {nurse.username}.")

class Nurse(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def view_patient_info(self, patient):
        print(f"Viewing information for {patient}.")

doctor = Doctor("doc1", "password1")
nurse1 = doctor.create_nurse("nurse1", "password2")

