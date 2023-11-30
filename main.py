class TimeConverter:
    """
    convert time
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_to_seconds(self):
        """
        convert time yo second
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def seconds_to_time(self, total_seconds):
        """
        convert seconds to time
        """
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def output_converted_time(self):
        """
        converted
        """
        if self.minutes >= 60:
            hours = self.minutes // 60
            self.minutes = self.minutes % 60
            self.hours += hours
        if self.seconds >= 60:
            minutes = self.seconds // 60
            self.seconds = self.seconds % 60
            self.minutes += minutes
        print(f"Converted Time: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")


def main():
    '''
    
    :return: 
    '''
    converter = TimeConverter(1, 61, 54)

    total_seconds = converter.time_to_seconds()
    print(f"Total Seconds: {total_seconds}")

    converter.output_converted_time()
    converter.seconds_to_time(total_seconds)


if __name__ == "__main__":
    main()
