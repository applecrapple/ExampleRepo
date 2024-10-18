#this is how we learned to concatenate strings in the ITF+ class.
a = "String 1"
b = "String 2"
print("a =" + a + " and b=" + b)

#this syntax utilizes the concept of the f-string, which makes things a
x = "String 3"
y = "string 4"
print(f"x = {x} and y = {y}")

#we could also use an f-string like this:
print("c = {c} and d = {d}".format(c=1, d=2))

job_list = {'John': 'Doctor', 'Jane': 'Engineer', 'Jim': 'Teacher'}

for name, job in job_list.items():
    print(f"{name} is a {job}")