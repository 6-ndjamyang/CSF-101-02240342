is_student = True
is_employed = False
print(is_student, is_employed)

is_student_and_employed = is_student and is_employed
print(is_student_and_employed)

is_student_or_employed = is_student or is_employed
print(is_student_or_employed) 

age = 22 
age_str = str(age)
# message = "I am " + age_str + " years old."
message = f"I am, {age_str} years old."
print(message)

num_string = "42"
num_int = int(num_string)
print(num_int)

non_num_str = "Hello"
non_num_int = int(non_num_str)
print(non_num_int)
