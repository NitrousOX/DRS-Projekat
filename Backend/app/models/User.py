class User:
    def __init__(self, name, surname, username, address, city, country, phone, email, password, isAdmin=False):
        self.name = name
        self.surname = surname
        self.username = username
        self.address = address
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email
        self.password = password
        self.isAdmin = isAdmin
        self.isRegistered = False
        self.firstLogin = True

    def __str__(self):
        return (f"User(name={self.name}, surname={self.surname}, address={self.address}, "
                f"city={self.city}, country={self.country}, phone={self.phone}, "
                f"email={self.email}, username={self.username}, isAdmin={self.isAdmin}, "
                f"isRegistered={self.isRegistered}, firstLogin={self.firstLogin})")
    
    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "address": self.address,
            "city": self.city,
            "country": self.country,
            "phone": self.phone,
            "email": self.email,
            "password": self.password,
            "username": self.username,
            "isAdmin": self.isAdmin,
            "isRegistered": self.isRegistered,
            "firstLogin": self.firstLogin
        }

