import datetime
import pywhatkit as pwk

# Dictionary of employees with their birthdates (format: "YYYY-MM-DD")
employees = {
    # Your employee data here...
    "Naveesh Nagpal":	"1981-09-30",
"Deepak Kanoujia":	"1984-09-27",
"Hari Charan":	"1990-03-15",
"Vimal Mathur":	"1997-11-10",
"Sandeep Jangir":	"1994-07-06",
"Sanjay Singh":	"1975-12-31",
"Riya Arora":	"1999-11-07",
"Anjali Bharti":	"1985-08-14",
"Priyanka Mathur":	"2001-07-05",
"Ashish Kumar":	"1985-07-10",
"Sunil Kumar":	"1979-06-01",
"Amrit Singh":	"1985-04-13",
"Sheetal":	"1982-08-06",
"Jyoti Chaturvedi ":	"1999-07-26",
"Harpreet Kaur ":	"1985-03-05",
"Ashwani Kumar ":	"2000-06-27",
"Rajesh kumar Sharma ":	"1990-12-23",
"Kushagra Agrawal ":	"1999-12-16",
"Amit Kumar ":	"1986-10-14",
"Preeti Yadav":	"1998-02-02",
"Pradeep":	"1986-02-10",
"Shaik shamsur basha":	"1992-04-26",
"Sachin":	"1988-05-12",
"Sujit Kumar":	"1993-02-10",
"Prashant Raghav":	"1999-12-02",
"Md Samir Ahmad":	"1999-07-12",
"Anuj kumar jha":	"2000-03-15",
"Ruby Thakran":	"1997-05-19",
"Tannu":	"2000-05-09",
"Himanshu Rawal":	"1999-08-09",
"Akshit Semwal":	"2021-04-07"
}

# Get the current date
current_date = datetime.date.today()

# Flag to check if there's a birthday
birthday_found = False

# Iterate through the employees and check if it's their birthday
for employee, birthdate in employees.items():
    birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
    if birthdate.month == current_date.month and birthdate.day == current_date.day:
        # It's the employee's birthday!
        message = f"Happy birthday, {employee}! Wishing you a fantastic day!"
        pwk.sendwhatmsg_instantly("+917065010439", f"update {message}")
        birthday_found = True

# Check if a birthday was found
if not birthday_found:
    print("No Birthday For Today")