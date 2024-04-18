#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.patients = []

    def enter_vitals(self, patient, height, weight, organ_donor, dnr, dietary_restrictions):
        patient.vitals = Vitals(height, weight, organ_donor, dnr, dietary_restrictions)
        print(f"Entered vitals for {patient.name}: Height {height} cm, Weight {weight} kg.")

class Nurse(Person):
    def enter_vitals(self, patient, height, weight, organ_donor, dnr, dietary_restrictions):
        patient.vitals = Vitals(height, weight, organ_donor, dnr, dietary_restrictions)
        print(f"Entered vitals for {patient.name}: Height {height} cm, Weight {weight} kg.")

class Patient(Person):
    def __init__(self, name):
        super().__init__(name)
        self.medications = []
        self.next_appointment = None
        self.vitals = None

    def view_vitals(self):
        if self.vitals:
            print(f"{self.name}'s Vitals: Height {self.vitals.height} cm, Weight {self.vitals.weight} kg, "
                  f"Organ Donor: {'Yes' if self.vitals.organ_donor else 'No'}, DNR: {'Yes' if self.vitals.dnr else 'No'}, "
                  f"Dietary Restrictions: {self.vitals.dietary_restrictions}")

class Vitals:
    def __init__(self, height, weight, organ_donor, dnr, dietary_restrictions):
        self.height = height
        self.weight = weight
        self.organ_donor = organ_donor
        self.dnr = dnr
        self.dietary_restrictions = dietary_restrictions

# Usage Example
doc = Doctor("Dr. Smith")
nurse = Nurse("Nurse Jones")
patient = Patient("John Doe")

nurse.enter_vitals(patient, 180, 75, True, False, "No nuts")
patient.view_vitals()

