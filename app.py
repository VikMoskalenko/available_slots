from flask import Flask
from datetime import timedelta, datetime

import datetime

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello, Flask!"

def booking_time(schedule_start, schedule_end, trainer_bookings, search_window):
    slots = []
    current_time = schedule_start
    while current_time < schedule_end:

        is_booked = any(start <= current_time < end for start, end in trainer_bookings)
        if not is_booked:
            slots.append(current_time)
        current_time += datetime.timedelta(minutes=search_window)
    return slots

# def booking_time(schedule_start, schedule_end, trainer_bookings, search_window):
#     start_time = schedule_start
#     end_time = schedule_end
#
#     all_slots = []
#
#     current_time = start_time
#     while current_time + timedelta(minutes=search_window) <= end_time:
#         all_slots.append(current_time)
#         current_time += timedelta(minutes=15)
#
#    # all_slots = [slot for slot in all_slots if not (slot >= schedule_start and slot < schedule_end)]
#
#     for booking in trainer_bookings:
#         booking_start = booking[0]
#         booking_end = booking[1]
#         all_slots = [slot for slot in all_slots if not (slot>= booking_start and slot < booking_end)]
#     return all_slots

if __name__ == "__main__":
    app.run()

# trainer_id = 1
# service_id = 1
# date = datetime.data(2024,12,25)
# available_slots = booking_time( date, trainer_id, service_id)
# print(available_slots)