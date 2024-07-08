class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    subject: str
    hobbies: str
    address: str
    state: str
    city: str

    def __init__(self, first_name, last_name, email, phone, subject, hobbies, address, state,
                 city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.subject = subject
        self.hobbies = hobbies
        self.address = address
        self.state = state
        self.city = city
