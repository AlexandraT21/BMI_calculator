#first create functions for correct inputs
def correct_weight():
   weight_str = input("Enter your weight in kg: ")
   weight = int(weight_str) if weight_str.isdecimal() else 0 
   while weight_str == "" or weight_str == " " or weight_str == "0" or weight >= 500 or weight <= 0:
      print("Incorrect input!")
      weight_str = input("Enter your weight in kg (like 50): ")
      weight = int(weight_str) if weight_str.isdecimal() else 0 
   else:
      return weight

weight = correct_weight()
print("Your weight is: ", weight)


#create usefull function for checking float numbers
def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def correct_height():
   height_str = input("Enter your height in meters: ")
   height = float(height_str) if is_float(height_str) else 0 
   while height_str == "" or height_str == " " or height_str == "0" or height >= 3 or height <= 0:
      print("Incorrect input!")
      height_str = input("Enter your height in meters (like 1.70): ")
      height = float(height_str) if is_float(height_str) else 0 
   else:
      return height
   
height = correct_height()
print("Your height is: ", height)

#first create functions for correct inputs
def BMI_meaning(weight, height):
   BMI = weight / (height * height)
   if BMI > 0:
      if BMI < 18.5:
         print("You are Underweight")
      elif BMI <= 24.9:
         print("You are Normal weight")
      elif BMI <= 29.9:
         print("You are Overweight")
      elif BMI > 30:
         print ("You are Obesity")
      else:
         print("Please check your input!")
         
BMI_meaning(weight, height)