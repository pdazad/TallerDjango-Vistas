from datetime import datetime
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
    variable = Variable.objects.get(pk=new_ms["variable"])
    date_time = datetime.strptime(new_ms["dateTime"], '%Y-%m-%dT%H:%M:%S.%fZ')

    measurement.variable = variable
    measurement.value = new_ms["value"]
    measurement.unit = new_ms["unit"]
    measurement.place = new_ms["place"]
    measurement.dateTime = date_time
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