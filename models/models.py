# For USERS
class ModelUser:
    def __init__(self,name,username,email,date_of_birth,pincode,country,state,city,address,landmark,userpic):
        self.name = name
        self.username = username
        self.email = email 
        self.date_of_birth = date_of_birth
        self.pincode = pincode
        self.country = country
        self.state = state
        self.city = city
        self.address = address
        self.landmark = landmark
        self.userpic = userpic

# For Students
class ModelStudent(ModelUser):
    def __init__(self, name, username, email, date_of_birth, pincode, country, state, city, address, landmark,userpic):
        super().__init__(name, username, email, date_of_birth, pincode, country, state, city, address, landmark,userpic)


# For Teachers
class ModelTeacher(ModelUser):
    def __init__(self, name, username, email, date_of_birth, pincode, country, state, city, address, landmark, userpic,skills,bio,rate,experience):
        super().__init__(name, username, email, date_of_birth, pincode, country, state, city, address, landmark, userpic)
        self.skills = skills
        self.bio = bio
        self.rate = rate 
        self.experience = experience
        

# For SKILL
class ModelSkill:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject

# For Subject
class ModelSubject:
    def __init__(self,name,skills):
        self.name = name 
        self.skills = skills

class ModelRate:
    def __init__(self,value,unit):
        self.value = value 
        #UNIT = [DAY,WEEK,MONTH]
        self.unit = unit 

# For Assignments

# For ContactUS
