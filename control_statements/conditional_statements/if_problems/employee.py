#employee salary
basic=eval(input("enter the salary"))
if basic<= 30000:
    hra=basic*0.2
    da=basic*0.1
    tax=basic*0.05
elif basic>30000 and basic<=50000:
    hra=basic*0.25
    da=basic*0.15
    tax=basic*0.1
elif basic>50000 and basic<=100000:
    hra=basic*0.35
    da=basic*0.20
    tax=basic*0.15
else: 
    basic>100000
    hra=basic*0.40
    da=basic*0.25
    tax=basic*0.20
gross_salary=basic+hra+da
net_salary=gross_salary-tax
print("gross salary is:",gross_salary)
print("net salary is:",net_salary)
