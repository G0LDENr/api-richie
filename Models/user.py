from extencion import db
from passlib.hash import pbkdf2_sha256, bcrypt

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(200),unique=True,nullable=False)
    password= db.Column(db.String(128),nullable=False)
    
    def set_password(self, password: str):
        print("SELF",self)
        #self.password = bcrypt.hash(password)
        password_bytes = password.encode('utf-8')[:72]  # truncar a 72 bytes
        self.password = pbkdf2_sha256.hash(password_bytes)

    def check_password(self, password: str) -> bool:
        print 
        return pbkdf2_sha256.verify(password, self.password)
    
    def to_dict(self):
        return{
            'id':self.id,
            'username':self.username,
            'email': self.email,
            'password': self.password
        }