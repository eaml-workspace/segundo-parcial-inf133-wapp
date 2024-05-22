from flask import redirect, request, flash, url_for, Blueprint
from flask_login import login_required, current_user
from utils.decorators import has_role
from modells.patient_model import Patient
from views import patient_view

patient_bp = Blueprint("/patients", __name__)
#listar
@patient_bp.route("/patients")
@login_required
def list_patients():
    print()

#crear
@patient_bp.route("patients/create", methods=["GET", "POST"])
@login_required
@has_role("admin")
def create_patient():
        print()

#actualizar
@patient_bp.route("/patients/<int:id>/update", methods= ["POST"])
@login_required
@has_role("admin")
def actualizar_patient(id):
    print()

# eliminar
@patient_bp.route("/patients/<int:id>/delete", methods= ["GET","POST"])
@login_required
@has_role("admin")
def delete_patient(id):
    print()
