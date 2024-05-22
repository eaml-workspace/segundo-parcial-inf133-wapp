from flask import redirect, render_template
from modells.patient_model import Patient
import json

def list_patients(patients):
    return redirect(
        title = "Lista de Pacientes",
        patients = patients,
        #render_template("patients.html", patients),
    )

def create_patient(patient):
    return redirect(
        patient=patient,
        title="Actualizar Paciente",
        #render_template("patient.update_patients", patient)
    )

def update_patient(data):
    name = data.request["name"]
    last_name = data.request["last_name"]
    ci = data.request["ci"]
    birth_date = data.request["birth_date"]
    patient = Patient(name=name, last_name=last_name, ci=ci, birth_date= birth_date)
    return redirect(
        render_template("update_patient", patient=patient, title="Acutalizar Paciente",)
    )