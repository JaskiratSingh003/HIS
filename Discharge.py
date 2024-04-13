class Person:

    def __init__(self, first_name, last_name, total_bill):
        
        self.first_name = first_name
        self.last_name = last_name
        self.total_bill = total_bill
        
        import os


Patient_1 = Patient_Discharge("John", "Doe", "$20,000")

class Patient_Discharge(Person):
    
    def __init__(self, first_name, last_name, total_bill):
        super().__init__(self, first_name, last_name)
        self.total_bill = total_bill

    def options(self):
# The flag implemented allows teh loop to continue unless the flag is proven false. This will then stop the loop. 
        flag = True

        try: 
            while flag == True:
            # Here, options are presented. Exiting the system and discharging a patient. For now it is hardcoded. 
                print(f"Please enter an option one of the following options\n")

                print(f"The options are:\n 'Exit' To Leave the System. \n 'Discharge' to Discharge a Patient \n")
            
                user_input = input().capitalize()
            # The line above is suppose to capture mistakes from the user, alongside the try/catch method below. 
                if user_input == 'Exit':
                    print(f"You have entered \"{user_input}\" and have left the system")
                    flag = False
            
                elif user_input == 'Discharge':

                    print(f"You have entered \"{user_input}\" \n")
                    
                    fout = open(f'John_Doe', 'w')

                    x = ("John Doe, $20,000")
                        
                    fout.write(x)
                        
                    fout.close()

                    print(f"The patient has been successfully discharged.")
                    # The statement provides proof that the program went well. 
                    # I still need to add a loop back towards the main menu in case of multiple patients being discharged. 
                    flag = False

                else: 
                    print("Hmm, seems like an error occured, please try again.\n")
       
            while flag == False:
                return
        except:
            print("An error occurred")
        
    

Patient_1.options()
