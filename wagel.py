# wagel.py

from guizero import App, Box, Text, TextBox, Picture, PushButton, ButtonGroup, info
from salary_calculator import calculate_net_salary

def format_currency(amount):
    """Formats a number as a currency string."""
    if amount is None:
        return "N/A"
    return f"{amount:,.0f} VND"

def submit():
    """Handles the submit button click event."""
    gross_salary_str = gross_salary_input.value
    region = region_options.value
    num_dependents_str = num_dependents_input.value

    if not gross_salary_str or not num_dependents_str:
        info("Input Error", "Please enter a valid Gross Salary and Number of Dependents.")
        return

    try:
        gross_salary = float(gross_salary_str)
        num_dependents = int(num_dependents_str)
    except ValueError:
        info("Input Error", "Please enter valid numeric values for Gross Salary and Number of Dependents.")
        return

    net_salary, personal_income_tax, social_insurance, health_insurance, unemployment_insurance = calculate_net_salary(
        gross_salary, region, num_dependents
    )

    net_salary_result.value = format_currency(net_salary)
    personal_income_tax_result.value = format_currency(personal_income_tax)
    social_insurance_result.value = format_currency(social_insurance)
    health_insurance_result.value = format_currency(health_insurance)
    unemployment_insurance_result.value = format_currency(unemployment_insurance)

# Create the main application window
app = App(title="Salary Tool", width=500, height=400, layout="grid")

# --- Input Section ---
Text(app, text="Enter your Gross Wages:", grid=[0, 0], align="left")
gross_salary_input = TextBox(app, width=20, grid=[1, 0], align="left")

Text(app, text="Minimum Wage Region:", grid=[0, 1], align="left")
region_options = ButtonGroup(
    app,
    options=[["Region 1", "1"], ["Region 2", "2"], ["Region 3", "3"]],
    selected="1",
    horizontal=True,
    grid=[1, 1],
    align="left",
)

Text(app, text="Number of Dependents:", grid=[0, 2], align="left")
num_dependents_input = TextBox(app, width=10, grid=[1, 2], align="left")
num_dependents_input.value = "0"

# --- Submit Button ---
submit_button = PushButton(app, command=submit, text="Submit", grid=[1, 3], align="right")

# --- Results Section ---
Text(app, text="-"*50, grid=[0, 4, 2, 1], align="left") # Separator

Text(app, text="Your NET Salary is:", grid=[0, 5], align="left")
net_salary_result = Text(app, "", grid=[1, 5], align="right")

Text(app, text="Personal Income Tax:", grid=[0, 6], align="left")
personal_income_tax_result = Text(app, "", grid=[1, 6], align="right")

Text(app, text="Social Insurance:", grid=[0, 7], align="left")
social_insurance_result = Text(app, "", grid=[1, 7], align="right")

Text(app, text="Health Insurance:", grid=[0, 8], align="left")
health_insurance_result = Text(app, "", grid=[1, 8], align="right")

Text(app, text="Unemployment Insurance:", grid=[0, 9], align="left")
unemployment_insurance_result = Text(app, "", grid=[1, 9], align="right")

# Display the application
app.display()
