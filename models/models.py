# For USERS
class ModelUser:
    def __init__(self, id, name, username, email, date_of_birth, pincode, country, state, city, address, landmark, userpic, contact, gems):
        self.id = id
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
        self.contact = contact
        self.gems = gems

# For Students
class ModelStudent(ModelUser):
    def __init__(self, id, name, username, email, date_of_birth, pincode, country, state, city, address, landmark, userpic, contact):
        super().__init__(id, name, username, email, date_of_birth, pincode,
                         country, state, city, address, landmark, userpic, contact)


# For Teachers
class ModelTeacher(ModelUser):
    def __init__(self, id, name, username, email, date_of_birth, pincode, country, state, city, address, landmark, userpic, contact, skills, bio, rate, experience, total_bookings, helps, travel):
        super().__init__(id, name, username, email, date_of_birth, pincode,
                         country, state, city, address, landmark, userpic, contact)
        self.skills = skills
        self.bio = bio
        self.rate = rate
        self.experience = experience
        self.total_bookings = total_bookings
        self.travel = travel
        self.help = helps


# For SKILL
class ModelSkill:
    def __init__(self, id, name, topic, rating):
        self.id = id
        self.name = name
        self.topic = topic
        self.rating = rating

# For Subject
class ModelSubject:
    def __init__(self,id, name, subject):
        self.id = id
        self.name = name
        self.subject = subject


class ModelRate:
    def __init__(self, value, unit):
        self.value = value
        #UNIT = [DAY,WEEK,MONTH]
        self.unit = unit


class ModelNotification:
    def __init__(self, id, date, time, type, message):
        self.id = id
        self.date = date
        self.time = time
        self.type = type
        self.message = message

# For Assignments

# For ContactUS
