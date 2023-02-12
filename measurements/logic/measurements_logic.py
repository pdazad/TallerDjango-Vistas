from ..models import Variable
from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(ms_pk):
    measurement = Measurement.objects.get(pk=ms_pk)
    return measurement

def update_measurement(ms_pk, new_ms):
    measurement = get_measurement(ms_pk)
    measurement.name = new_ms["name"]
    measurement.save()
    return measurement

def create_measurement(ms):
    variable = Variable.objects.get(name=ms["variable"]["name"])
    measurement = Measurement(variable=variable, value=ms["value"], unit=ms["unit"], place=ms["place"], dateTime=ms["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(ms_pk):
    measurement = get_measurement(ms_pk)
    measurement.delete()
    return {"message": "Measurement deleted successfully."}