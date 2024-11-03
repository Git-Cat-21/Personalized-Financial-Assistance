# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# import mysql.connector

# def maturity_date(invested_date,scheme_id):
#     db=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="password",
#         database="pfa_orange"
#     )
#     cursor=db.cursor()
#     cursor.execute("SELECT Scheme_ID,Duration_In_Years FROM schemes");
#     result=[(row[0],row[1]) for row in cursor.fetchall()]
#     today=invested_date
#     for years in result:
#         if scheme_id==years[0]:
#             integer_years = int(years[1])
#             additional_months = int((years[1] - integer_years) * 12)
#             future_date = today + relativedelta(years=integer_years, months=additional_months)
#             return(f"{future_date.strftime('%Y-%m-%d')}")

# # maturity_date('2024-10-11',1)


from datetime import datetime
from dateutil.relativedelta import relativedelta
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="pfa_orange"
)

cursor = db.cursor()
cursor.execute("SELECT Scheme_ID, Duration_In_Years FROM schemes")
result = [(row[0], row[1]) for row in cursor.fetchall()]

# Get today's date without the time component
today = datetime.today().date()
print(type(today))

print("Today's date:", today)

# Calculate future dates based on Duration_In_Years
for scheme_id, years in result:
    # Separate years into integer years and additional months
    integer_years = int(years)
    additional_months = int((years - integer_years) * 12)
    
    # Calculate the future date
    future_date = today + relativedelta(years=integer_years, months=additional_months)
    print(f"Scheme ID: {scheme_id}, Date after {years} years: {future_date.strftime('%Y-%m-%d')}")

