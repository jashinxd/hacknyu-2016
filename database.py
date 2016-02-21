from pymongo import MongoClient
import md5
# Dentists

# Puts dentist <username> and <password> into database
def registerDentist(username,password,firstName,lastName,spec,cAddress,eAddress, pNum):
    required = [username, password, fistName, lastName, cAddress, pNum]
    connection = MongoClient()
    db = connection['database']
    newPass = md5.new(password).digest()
    for param in required:
        if param == "":
            return "missing"
    db.dentists.insert({'uname': username, 'password': newPass, 'firstName': firstName,\
    'lastName': lastName, 'spec': spec, 'cAddress': cAddress, 'eAddress': eAddress, 'pNum': pNum,\
    'patients': [] })

# Tests if the dentist's username is already registered or not
def validDentistUname(username):
    connection = MongoClient()
    db = connection['database']
    curs = db.dentists.find({'uname':username})
    if curs.count() == 0:
        return False
    return True

# Authentication for dentist login
def authenticateDentist(username,password):
    connection = MongoClient()
    db = connection['database']
    #print username, password
    newPass = md5.new(password).digest()
    curs = db.dentists.find({'uname':username, 'password':newPass})
    #print curs.count()
    if curs.count() != 0:
        return True
    return False

# Add a patient to dentist's current patient list
def addPatient(dUsername, pFName, pLName, pUsername):
    connection = MongoClient()
    db = connection['database']
    currPatients = db.dentists.find('uname': dUsername)[patients]
    if (pUsername != ""):
        newPatients = currPatients.append(pUsername)
    else:
        pat = db.patients.find({'firstName': pFName, 'lastName': pLName}[uname])
        currPatients.append(pat)
    db.dentists.update({'uname': dUsername}, {$set:{'patients': newPatients}}, {upsert:true}) 
    
"""
# Insert picture name after upload using HTML/PHP
def newPicture(
"""

# Patients

# Puts patient <username> and <password> into database
def registerPatient(username,password,firstName,lastName, hAddress, eAddress, pNum):
    required = [username, password, firstName, lastName, hAddress, pNum)
    connection = MongoClient()
    db = connection['database']
    newPass = md5.new(password).digest()
    for param in required:
        if param == "":
            return "missing"
    db.patients.insert({'uname': username, 'password': newPass, 'firstName': firstName,\
    'lastName': lastName, 'spec': spec, 'hAddress': hAddress, 'eAddress': eAddress, 'pNum': pNum,\
    'dentists': [] })

# Tests if the patient's username is already registered or not    
def validPatientUname(username):
    connection = MongoClient()
    db = connection['database']
    curs = db.patients.find({'uname':username})
   # print curs.count()
    if curs.count() == 0:
        return False
    return True

# Authentication for patient login
def authenticatePatient(username,password):
    connection = MongoClient()
    db = connection['database']
    #print username, password
    newPass = md5.new(password).digest()
    curs = db.patients.find({'uname':username, 'newPass':password})
    #print curs.count()
    if curs.count() != 0:
        return True
    return False
    
