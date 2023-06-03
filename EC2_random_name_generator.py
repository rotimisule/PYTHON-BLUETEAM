import random 
import string

ec2_num = int(input(" Hello, How many instances would you like to create: "))
department = input("What deperatment are you creating for today ? ")
##departments= "Marketing" , "Accounting" , "FinOps" 
department1 = "Marketing"
department2 = "Accounting"
department3 = "FinOps"
##function
##check if the user is in one of the 3 departments
def name_generator_func(ec2_num, department):
    if department.casefold() in (department1.casefold(), department2.casefold(), department3.casefold()) :
##use Instance number to give loop a range for EC2 random name generator
        for x in range(ec2_num):
##create random letters + numbers along with a number of chars defined as k 
            randomchars = ''.join(random.choices(string.digits + string.ascii_letters , k=8))
#print the department entered with a captial letter + a undrscore and the random letters generated 
            print(department.capitalize() +'_'+randomchars)
    else :
        print ("You do not have permission to use this name generator, goodbye.")
        

name_generator_func(ec2_num, department)
    
   

    

 

    
    

