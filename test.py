import unittest
import datetime
import app


class TestSchedule(unittest.TestCase):
    def test_schedule1(self):
        maxDiff = None
        schedule_start = datetime.datetime(2024, 12, 25, 9, 8)
        schedule_end = datetime.datetime(2024, 12, 25, 14, 8)
        trainer_bookings = []
        search_window = 60
        results = app.booking_time(schedule_start, schedule_end, trainer_bookings, search_window)
        expected= [
            datetime.datetime(2024, 12, 25, 9, 0),  datetime.datetime(2024, 12, 25, 9, 30),datetime.datetime(2024, 12, 25, 9, 45),
            datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 45),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 45),
            datetime.datetime(2024, 12, 25, 13, 0)

        ]
        self.assertListEqual( expected, results)

        search_window = 30
        expected = [
            datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 15),
            datetime.datetime(2024, 12, 25, 9, 30), datetime.datetime(2024, 12, 25, 9, 45),
            datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 15),
            datetime.datetime(2024, 12, 25, 10, 30), datetime.datetime(2024, 12, 25, 10, 45),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15),
            datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 00), datetime.datetime(2024, 12, 25, 12, 15),
            datetime.datetime(2024, 12, 25, 12, 30), datetime.datetime(2024, 12, 25, 12, 45),
            datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 13, 15),
            datetime.datetime(2024, 12, 25, 13, 30)

        ]
        results = app.booking_time(schedule_start, schedule_end, trainer_bookings, search_window)
        self.assertListEqual(expected, results)

    def test_schedule_one_booking(self):
        start_date = datetime.datetime(2024, 12, 25, 9, 0)
        end_date = datetime.datetime(2024, 12, 25, 14, 0)
        search_window = 60
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 11, 0)),
        ]
        results = app.booking_time(start_date, end_date, trainer_bookings, search_window)
        expected = [
            datetime.datetime(2024, 12, 25, 9, 0),

            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15),datetime.datetime(2024, 12, 25, 11, 30),datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15),datetime.datetime(2024, 12, 25, 12, 30),datetime.datetime(2024, 12, 25, 12, 45),
            datetime.datetime(2024, 12, 25, 13, 0)

        ]
        self.assertListEqual(expected, results)

        search_window = 30
        datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 15), datetime.datetime(2024, 12, 25, 9, 30)

        (datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15), datetime.datetime(2024, 12, 25,
                                                                                                           11,
                                                                                                           30), datetime.datetime(
            2024, 12, 25, 11, 45),)
        datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15), datetime.datetime(2024, 12, 25,
                                                                                                           12,
                                                                                                           30), datetime.datetime(
            2024, 12, 25, 12, 45),
        datetime.datetime(2024, 12, 25, 13, 0)
        results = app.booking_time(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)


    def test_schedule_two_bookings(self):
        start_date = datetime.datetime(2024, 12, 25, 9, 0)
        end_date = datetime.datetime(2024, 12, 25, 14, 0)

        search_window = 60
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 11, 0)),
            (datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 13, 0)),
        ]
        expected = [
            datetime.datetime(2024, 12, 25, 9, 0),
            datetime.datetime(2024, 12, 25, 11, 0),
            datetime.datetime(2024, 12, 25, 13, 0),
        ]
        results = app.booking_time(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)

        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 11, 0)),
            (datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 10, 0)),
        ]
        expected = [
            datetime.datetime(2024, 12, 25, 12, 0),
            datetime.datetime(2024, 12, 25, 11, 0),
            datetime.datetime(2024, 12, 25, 13, 0),
        ]
        results = app.booking_time(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)

if __name__ == "__main__":
    unittest.main()
