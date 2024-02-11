from micropython import const
from lib.DFRobot_GNSS_I2C import DFRobot_GNSS_I2C, MODE_GPS
from time import sleep


SDA_PIN = const(21)
SCL_PIN = const(22)
DELAY_SECONDS = const(2)


if __name__ == "__main__":
    sensor = DFRobot_GNSS_I2C(sda=SDA_PIN, scl=SCL_PIN)

    sensor.set_gnss_mode(MODE_GPS)
    sensor.set_enable_power()
    sensor.set_rgb_on()

    while True:
        print('-' * 3)
        print(f'GNSS mode: {sensor.get_gnss_mode()}')
        print(f'Satellite number: {sensor.get_num_sta_used()}')

        actual_time = sensor.get_time()
        actual_date = sensor.get_date()

        print(f'Date: {actual_date} Time: {actual_time}')

        latitude_values = sensor.get_lat()
        longitude_values = sensor.get_lon()
        alt = sensor.get_alt()
        cog = sensor.get_cog()
        sog = sensor.get_sog()

        print(f'latitude degree: {latitude_values[0]}° latitude direction: {latitude_values[1]}')
        print(f'longitude degree: {longitude_values[0]}° longitude direction: {longitude_values[1]}')
        print(f'altitude: {alt} meters')
        print(f'speed over ground: {sog} N')
        print(f'course over ground: {cog} T')

        sleep(DELAY_SECONDS)
