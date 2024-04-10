#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Person:

    def __init__(self, first_name, last_name, department):
        
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        
        


# In[3]:


class Patient_Discharge(Person):
    
    def __init__(self, first_name, last_name, department, Discharge):
        super().__init__(self, first_name, last_name, department)
        self.Discharged = Discharged

    def options():

        flag = True
        
        while flag == True:
            
            print(f"Please enter an option one of the following options\n")

            print(f"The options are:\n 'Exit' To Leave the System. \n 'Discharge' to Discharge a Patient \n 'Return' to Return to Main Menu.")
            
            user_input = input().capitalize()
            
            if user_input == 'Exit':
                print("You have entered {self.user_input} and have left the system")
                flag = False
            
            if user_input == 'Discharge':
                
                
                flag = False

            if user_input == 'Return':
                flag = False

            else: 
                print("Hmm, seems like an error occured, please try again.\n")
        while flag == False:
            return

# Patient_1 = Patient_Discharge("John", "Doe", "Pysch Ward", "False")


Patient_Discharge.options()

