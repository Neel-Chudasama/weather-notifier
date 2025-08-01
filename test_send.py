from data_acquisition import get_weather_data, get_tube_status
from advice import generate_advice
from notifier import send_weather_notification, send_tfl_notification  # Assuming this function exists


forecast = get_weather_data()
advice = generate_advice(forecast)
send_weather_notification(advice)

tube_status = get_tube_status()
send_tfl_notification(tube_status)
