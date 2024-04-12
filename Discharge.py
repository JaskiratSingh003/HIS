class Person:

    def __init__(self, first_name, last_name, total_bill):
        
        self.first_name = first_name
        self.last_name = last_name
        self.totatl_bill = total_bill
        
class Patient_Discharge(Person):
    
    def __init__(self, first_name, last_name, total_bill):
        super().__init__(self, first_name, last_name)
        self.total_bill = total_bill

    def options(self):

        flag = True
        
        while flag == True:
            
            print(f"Please enter an option one of the following options\n")

            print(f"The options are:\n 'Exit' To Leave the System. \n 'Discharge' to Discharge a Patient \n")
            
            user_input = input().capitalize()
            
            if user_input == 'Exit':
                print(f"You have entered \"{user_input}\" and have left the system")
                flag = False
            
            elif user_input == 'Discharge':
                
                altered_info = (, )  
                with open(f"{Patient_1.first_name}_disachareged.txt", 'w'):
                    

                
                
                flag = False

            else: 
                print("Hmm, seems like an error occured, please try again.\n")
       
        while flag == False:
            return

# Patient_1 = Patient_Discharge("John", "Doe", "$20,000")


Patient_1.options()
