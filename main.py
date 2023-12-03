class TimeConverter:
    """
    A class for converting time between hours, minutes, and seconds.

    Attributes:
        hours (int): The hours component of the time.
        minutes (int): The minutes component of the time.
        seconds (int): The seconds component of the time.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Initialize a TimeConverter object.

        Args:
            hours (int): The initial value for hours (default is 0).
            minutes (int): The initial value for minutes (default is 0).
            seconds (int): The initial value for seconds (default is 0).
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_to_seconds(self):
        """
        Convert the time to total seconds.

        Returns:
            int: The total number of seconds.
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def seconds_to_time(self, total_seconds):
        """
        Convert total seconds to hours, minutes, and seconds.

        Args:
            total_seconds (int): The total number of seconds to convert.
        """
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def output_converted_time(self):
        """
        Print the converted time in the format HH:MM:SS.
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
    """
    The main function to demonstrate the TimeConverter class.
    """
    converter = TimeConverter(1, 61, 54)

    total_seconds = converter.time_to_seconds()
    print(f"Total Seconds: {total_seconds}")

    converter.output_converted_time()
    converter.seconds_to_time(total_seconds)


if __name__ == "__main__":
    main()
