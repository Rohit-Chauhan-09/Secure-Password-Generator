import random
import sys
import string

print("=" * 80)
try:
    Pass_type = int(input("*---- Enter ----*\n(0) for Number(Normal) password or\n(1) for Alphanumeric (Medium) password or\n(2) for Complex(Mix of numbers and Special charaters) password or\n(3) for include((@) and (#) with numbers) password: ")) # Taking output from user to move next step
except:
    print("Please Enetr (0 or 1 or 2 or 3) number!") # Error -> Not Entered correct number
    print("=" * 80)
    sys.exit()

print("--- Max digit only be 10 ---")
try:
    user = int(input("Enter the number password want to generate: ")) # Taking output for length of password
except:
    print("Please Enter only number!") # Error -> If user Entered other thing
    print("=" * 80)
    sys.exit()

class num_passwd: # class (1) for only number password
    def __init__(self,digit):
        self.digit = digit
  
    def len_gen(self):
        pass_store = ""
        for i in range(user):
            gen1 = random.randint(1,user)
            pass_store += str(gen1)
        print(f"Your Password => {pass_store}")
        print("=" * 80)

class alpha_num: # Class 2 for Alphanumeric password
    def __init__(self,digit):
        self.digit = digit

    def a_n_pass(self):
        password = ""
        pass_ = string.digits + string.ascii_lowercase
        for i in range(user):
            gen2 = random.choice(pass_)
            password += gen2
        print(f"Your Password => {password}")
        print("=" * 80)

class two_special: # Class 3 for (@ and #) only this special charater include with number
    def __init__(self,digit):
        self.digit = digit

    def t_s_pass(self):
        password = ""
        pass_ = string.digits + "@" + "#"
        for i in range(user):
            gen4 = random.choice(pass_)
            password += gen4
        print(f"Your Password => {password}")
        print("=" * 80)

class special_char_pass: # Class 4 for number with special character
    def __init__(self,digit):
        self.digit = digit

    def s_c_pass(self):
        password = ""
        pass_ = string.digits + string.punctuation
        for i in range(user):
            gen3 = random.choice(pass_)
            password += gen3
        print(f"Your Password => {password}")
        print("=" * 80)

# Conditions
if (Pass_type == 0): # Condition for class 1
    if user <= 10:
        obj1 = num_passwd(user)
        obj1.len_gen()
    else:
        print("Please enter the digit less than or equal to 10!")
        print("=" * 80)

elif (Pass_type == 1): # Condition for class 2
    if user <= 10:
        obj2 = alpha_num(user)
        obj2.a_n_pass()
    else:
        print("Please enter the digit less than or equal to 10!")
        print("=" * 80)

elif (Pass_type == 2):
    if user <= 10:
        obj3 = special_char_pass(user) # Condition for class 4
        obj3.s_c_pass()
    else:
        print("Please enter the digit less than or equal to 10!")
        print("=" * 80)

elif (Pass_type == 3): # Condition for class 3
    if user <= 10:
        obj3 = two_special(user)
        obj3.t_s_pass()
    else:
        print("Please enter the digit less than or equal to 10!")
        print("=" * 80)

else: # Other condition
    print("Please enter the correct number(0, 1, 2, 3)!")
    print("=" * 80)

# Finally Done!