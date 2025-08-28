basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits: "))

def calculate_gross(basic,benefits):
    return basic + benefits

gross_salary = calculate_gross(basic_salary,benefits)
print(gross_salary)


def calculate_nhif(gross):
    if gross <= 5999:
        nhif = 150
    elif gross >= 6000 and gross <= 7999:
        nhif = 300 
    elif gross >= 8000 and gross <= 11999:
        nhif = 400 
    elif gross >= 12000 and gross <= 14999:
        nhif = 500 
    elif gross >= 15000 and gross <= 19999:
        nhif = 600
    elif gross >= 20000 and gross <= 24999:
        nhif = 750 
    elif gross >= 25000 and gross <= 29999:
        nhif = 850
    elif gross >= 30000 and gross <= 34999:
        nhif = 900
    elif gross >= 35000 and gross <= 39999:
        nhif = 950
    elif gross >= 40000 and gross <= 44999:
        nhif = 1000
    elif gross >= 45000 and gross <= 49999:
        nhif = 1100
    elif gross >= 50000 and gross <= 59999:
        nhif = 1200
    elif gross >= 60000 and gross <= 69999:
        nhif = 1300
    elif gross >= 70000 and gross <= 79999:
        nhif = 1400
    elif gross >= 80000 and gross <= 89999:
        nhif = 1500
    elif gross >= 90000 and gross <= 99999:
        nhif = 1600
    else:
        nhif = 1700

    return nhif

nhif = calculate_nhif(gross_salary)
print(nhif)


def calculate_nssf(gross):
    if gross < 18000:
        nssf = gross * 0.06
    else:
        nssf = 0.06 * 18000
    return nssf

nssf = calculate_nssf(gross_salary)
print(nssf)
