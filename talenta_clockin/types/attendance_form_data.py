import codecs
from enum import Enum
from pydantic import BaseModel

class AttendanceType(str, Enum):
    CLOCK_IN = "checkin"
    CLOCK_OUT = "checkout"

class AttendanceData(BaseModel):
    latitude: float
    longitude: float
    status: AttendanceType
    description: str

    def get_form_data(self):
        latitude_encoded = codecs.encode(codecs.encode(str(self.latitude).encode('utf-8'), 'base64').decode('utf-8'), 'rot_13')
        longitude_encoded = codecs.encode(codecs.encode(str(self.longitude).encode('utf-8'), 'base64').decode('utf-8'), 'rot_13')

        data = {
            'longitude': longitude_encoded,
            'latitude': latitude_encoded,
            'status': self.status.value,
            'description': self.description,
        }

        return data
