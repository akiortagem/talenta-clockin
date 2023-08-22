from typing import Optional
import typer
import logging
from typing_extensions import Annotated

from talenta_clockin.browser.sessionid import get_sessionid
from talenta_clockin.types.attendance_form_data import AttendanceType, AttendanceData
from talenta_clockin.api.live_attendance import post_attendance

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = typer.Typer()

def run_command(username: str, password: str, coord:str, description:Optional[str], status:AttendanceType):
    latitude = coord.split(',')[0]
    longitude = coord.split(',')[1]

    #clean latitude of surrounding quotes or double quotes
    latitude = latitude.replace('"', '').replace("'", "")
    #clean longitude of surrounding quotes or double quotes
    longitude = longitude.replace('"', '').replace("'", "")
    
    data = AttendanceData(
        latitude=float(latitude),
        longitude=float(longitude),
        status=status,
        description=description or ("Mari kerja hari ini!" if status == AttendanceType.CLOCK_IN else "Sampai jumpa besok!"),
    )

    sessionid = get_sessionid(username, password)

    post_attendance(data, sessionid)

@app.command()
def clockin(
        username: str,
        password: str,
        description:Annotated[str, typer.Option(help="description for the clockin, optional")]=None,
        coord:Annotated[str, typer.Option(help="coordinates for the clockin, required")]=None
    ):
    """
    Clocks in to talenta with the given username and password
    You need to surround latitude and longitude with quotes
    """
    run_command(username, password, coord, description, AttendanceType.CLOCK_IN)

@app.command()
def clockout(
        username: str,
        password: str,
        description:Annotated[str, typer.Option(help="description for the clockin, optional")]=None,
        coord:Annotated[str, typer.Option(help="coordinates for the clockin, required")]=None):
    """
    Clocks out from talenta with the given username and password
    You need to surround latitude and longitude with quotes
    """
    run_command(username, password, coord, description, AttendanceType.CLOCK_OUT)


if __name__ == "__main__":
    app()