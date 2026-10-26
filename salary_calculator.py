# salary_calculator.py

# Constants for salary calculation
BASE_SALARY_2021 = 1490000
MINIMUM_WAGE_REGION_1 = 4420000
MINIMUM_WAGE_REGION_2 = 3920000
MINIMUM_WAGE_REGION_3 = 3430000
PERSONAL_RELIEF = 11000000
DEPENDENT_RELIEF = 4400000

# Insurance rates
SOCIAL_INSURANCE_RATE = 0.08
HEALTH_INSURANCE_RATE = 0.015
UNEMPLOYMENT_INSURANCE_RATE = 0.01

# Tax brackets
TAX_BRACKETS = [
    (5000000, 0.05),
    (10000000, 0.1),
    (18000000, 0.15),
    (32000000, 0.20),
    (52000000, 0.25),
    (80000000, 0.30),
    (float('inf'), 0.35)
]

TAX_DEDUCTIONS = [
    0,
    250000,
    750000,
    1650000,
    3250000,
    5850000,
    9850000
]

def get_minimum_wage(region):
    if region == 1:
        return MINIMUM_WAGE_REGION_1
    elif region == 2:
        return MINIMUM_WAGE_REGION_2
    elif region == 3:
        return MINIMUM_WAGE_REGION_3
    else:
        raise ValueError("Invalid region specified")

def calculate_insurance(gross_salary, region):
    # Cap for Social and Health Insurance
    base_salary_cap = BASE_SALARY_2021 * 20
    salary_for_sh_insurance = min(gross_salary, base_salary_cap)
    social_insurance = salary_for_sh_insurance * SOCIAL_INSURANCE_RATE
    health_insurance = salary_for_sh_insurance * HEALTH_INSURANCE_RATE

    # Cap for Unemployment Insurance
    minimum_wage = get_minimum_wage(region)
    unemployment_insurance_cap = minimum_wage * 20
    salary_for_ui = min(gross_salary, unemployment_insurance_cap)
    unemployment_insurance = salary_for_ui * UNEMPLOYMENT_INSURANCE_RATE

    return social_insurance, health_insurance, unemployment_insurance

def calculate_taxable_income(gross_salary, social_insurance, health_insurance, unemployment_insurance, num_dependents):
    total_deductions = social_insurance + health_insurance + unemployment_insurance
    taxable_income = gross_salary - total_deductions - PERSONAL_RELIEF - (num_dependents * DEPENDENT_RELIEF)
    return max(0, taxable_income)

def calculate_personal_income_tax(taxable_income):
    for i, (bracket, rate) in enumerate(TAX_BRACKETS):
        if taxable_income <= bracket:
            return taxable_income * rate - TAX_DEDUCTIONS[i]
    return 0

def calculate_net_salary(gross_salary, region, num_dependents):
    try:
        gross_salary = float(gross_salary)
        num_dependents = int(num_dependents)
        region = int(region)
    except (ValueError, TypeError):
        return None, None, None, None, None

    social_insurance, health_insurance, unemployment_insurance = calculate_insurance(gross_salary, region)

    taxable_income = calculate_taxable_income(gross_salary, social_insurance, health_insurance, unemployment_insurance, num_dependents)

    personal_income_tax = calculate_personal_income_tax(taxable_income)

    net_salary = gross_salary - (social_insurance + health_insurance + unemployment_insurance) - personal_income_tax

    return net_salary, personal_income_tax, social_insurance, health_insurance, unemployment_insurance
