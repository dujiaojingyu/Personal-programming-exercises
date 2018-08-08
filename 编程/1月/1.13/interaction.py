name = input('name:')
password = input('password:')
age = input('age:')
job = input('job:')
salary = input('salary:')

info1 = '''
----------- info1 of  %s -------------
Name:%s
Password:%s
Age:%s
Job:%s
Salary:%s

''' % (name,name,password,age,job,salary)

print(info1)

info2 = '''
----------- info2 of {0} -------------
Name:{0}
Password:{1}
Age:{2}
Job:{3}
Salary:{4}

''' .format(name,name,password,age,job,salary)

print(info2)


info3 = '''
----------- info3 of {_name} -------------
Name:{_name}
Password:{_password}
Age:{_age}
Job:{_job}
Salary:{_salary}

''' .format( _name = name,
            _password = password,
            _age = age,
            _job = job,
            _salary = salary)

print(info3)




