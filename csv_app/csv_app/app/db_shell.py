from app.models import Employee

import random
import string

# exec(open(r'F:\Class\B3-B4\Django\csv_app\app\db_shell.py').read())

des = ['Software Engineer', 'Sr. Software Engineer', "Linux Administrator", "Associate", "CEO", "Python Devp", "Data Scientist"]

for i in range(50):
    letters = string.ascii_lowercase # [a,z]
    name = ''.join(random.choice(letters) for i in range(10))

    letters = string.digits
    sal =  ''.join(random.choice(letters) for i in range(5))

    letters = string.ascii_uppercase
    comp = ''.join(random.choice(letters) for i in range(10))

    design = random.choice(des)
    emp = Employee(name=name,salary=sal ,company=comp, designation=design)
    emp.save()


    



    

