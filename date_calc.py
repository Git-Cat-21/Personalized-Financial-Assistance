from datetime import datetime
from dateutil.relativedelta import relativedelta
import mysql.connector

datelst=[]
def maturity_date(scheme_id):
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="pfa_orange"
    )
    cursor=db.cursor()
    cursor.execute("SELECT Scheme_ID,Duration_In_Years FROM schemes");
    result=[(row[0],row[1]) for row in cursor.fetchall()]
    today=datetime.today().date()
    datelst.append(str(today))
    for years in result:
        if scheme_id==years[0]:
            integer_years = int(years[1])
            additional_months = int((years[1] - integer_years) * 12)
            future_date = today + relativedelta(years=integer_years, months=additional_months)
            datelst.append(str(future_date))
            return datelst

# maturity_date('2024-10-11',1)


