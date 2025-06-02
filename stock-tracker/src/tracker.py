import logging
import os
from datetime import datetime

class Tracker:
    def __init__(self, log_file='tracker.log'):
        self.log_file = log_file
        self.setup_logging()

    def setup_logging(self):
        """Set up logging configuration."""
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info("Tracker initialized.")

    def log_event(self, event_message):
        """Log an event with a message."""
        logging.info(event_message)

    def log_error(self, error_message):
        """Log an error with a message."""
        logging.error(error_message)

    def log_data_change(self, data_name, old_value, new_value):
        """Log a change in data."""
        message = f"Data changed: {data_name} from {old_value} to {new_value}"
        logging.info(message)

    def get_log(self):
        """Retrieve the log contents."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                return file.read()
        else:
            return "Log file does not exist."

if __name__ == "__main__":
    tracker = Tracker()

    # Example usage
    tracker.log_event("Starting the tracking process.")
    tracker.log_data_change("temperature", 22.5, 23.0)
    tracker.log_event("Tracking process completed.")

    # Print log contents
    print(tracker.get_log())