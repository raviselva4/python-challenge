import os
import csv
import datetime

st_dict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
empid = []
fname = []
lname = []
dob   = []
ssn   = []
st    = []
rpath = os.path.join('PyBoss', 'employee_data.csv')
with open(rpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)

    for row in csvreader:
        #  Add Id
        empid.append(row[0])
        splitname = row[1].split()
        #   Add First Name
        fname.append(splitname[0])
        #   Add Last Name
        lname.append(splitname[1])
        formated_dt = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y')
        #   Add dob
        dob.append(formated_dt)
        #print(formated_dt)
        #f_ssn = row[3][-5:].rjust(len(row[3]), "*")
        split_ssn = row[3].split('-')
        split_ssn[0] = 'xxx'
        split_ssn[1] = 'xx'
        #   Add ssn
        ssn.append(split_ssn[0]+'-'+split_ssn[1]+'-'+split_ssn[2])
        #   Add State
        formated_st = st_dict[row[4]]
        st.append(formated_st)
        #print(formated_st)
# Zip list together
cleaned_csv = zip(empid, fname, lname, dob, ssn, st)
#
opath = os.path.join('PyBoss', 'new_employee_data.csv')
with open (opath, 'w') as csvwrite:
    writer = csv.writer(csvwrite)
    rpath = os.path.join('PyBoss', 'employee_data.csv')
    #   write header row...
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    #   Write in zipped rows
    writer.writerows(cleaned_csv)
