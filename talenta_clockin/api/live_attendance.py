import requests
import logging

from talenta_clockin.types.attendance_form_data import AttendanceData
from talenta_clockin import config

class AttendanceFailed(Exception):
    pass

def post_attendance(data:AttendanceData, sessionid:str):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'PHPSESSID={sessionid}',
    }

    logging.info("Composing attendance form data")
    form_data = data.get_form_data()

    logging.info("Posting attendance")
    response = requests.post(config.TALENTA_ATTENDANCE_URL, headers=headers, data=form_data)

    if response.status_code not in [200, 201]:
        logging.info("Failed to post attendance, status code: %s", response.status_code)
        raise AttendanceFailed(f'Failed to post attendance, status code: {response.status_code}')

    return response