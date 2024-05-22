from database import db
from flask_login import UserMixin, current_user

class Patient(UserMixin, db.Model):
    __tablename__ = "patients"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable= False)
    last_name = db.Column(db.String(50), nullable= False)
    ci = db.Column(db.String(100), nullable= False)
    birth_date = db.Column(db.String(100), nullable= False)
    
    def __init__(self, name, last_name, ci, birth_date):
        self.name = name
        self.last_name = last_name
        self.ci = ci
        self.birth_date = birth_date
    # para el post
    def save(self):
        db.session.add(self)
        db.session.commit()
    # para el get
    @staticmethod
    def get_all_patients():
        return Patient.query.get_all()
    @staticmethod
    def get_by_id(id):
        return Patient.query.filter(id, current_user=current_user.id)
    
    #para el put
    def update_patient(self, name, last_name, ci, birt_date):
        if name is not None:
            self.name = name
        if last_name is not None:
            self.last_name = last_name
        if ci is not None:
            self.ci = ci
        if birt_date is not None:
            self.birth_date = birt_date
        db.session.commit()
    
    #para el delete
    def delete_patient(self):
        db.session.delete(self)
        db.session.commit()