from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

    def get_user(id):
        user = User.query.filter_by(id=id).first()
        return User.serialize(user)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(10), unique=False, nullable=False)
    birth_year = db.Column(db.String(20), unique=False, nullable=False)
    hair_color = db.Column(db.String(20), unique=False, nullable=False)
    eye_color = db.Column(db.String(20), unique=False, nullable=False)
    height = db.Column(db.String(20), unique=False, nullable=False)


    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "height": self.height,
        }
    @classmethod
    def get_by_id(cls, id):
        people = cls.query.get(id)
        return people

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    population = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    diameter = db.Column(db.String(120), unique=False, nullable=False)
    gravity = db.Column(db.String(120), unique=False, nullable=False)
    rotation_period = db.Column(db.String(120), unique=False, nullable=False)
    orbital_period = db.Column(db.String(120), unique=False, nullable=False)
    surface_water = db.Column(db.String(120), unique=False, nullable=False)



    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "population": self.population,
            "climate": self.climate,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "surface_water": self.surface_water,
        }
    
    @classmethod
    def get_by_id(cls, id):
        planets = cls.query.get(id)
        return planets

class FavoritesPeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('favoritesPeople', lazy=True))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    people = db.relationship('People', backref=db.backref('favoritesPeople', lazy=True))

    def __repr__(self):
        return '<FavoritesPeople %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
        }

class FavoritesPlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('favoritesPlanets', lazy=True))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    planets = db.relationship('Planets', backref=db.backref('favoritesPlanets', lazy=True))

    def __repr__(self):
        return '<FavoritesPlanets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
        }
    

            