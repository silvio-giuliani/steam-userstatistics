
class Utils:
    def __init__(self):
        pass

    def minutes_to_hour_and_minutes(minutes):
        return '{:02d}h{:02d}m'.format(*divmod(minutes, 60))