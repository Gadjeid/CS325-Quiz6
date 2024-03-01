from abc import ABC, abstractmethod
from datetime import datetime

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[Console] {current_time} - {message}")

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a') as file:
            file.write(f"[File] {current_time} - {message}\n")

class App:
    def __init__(self, logger):
        self.logger = logger

    def say_hello(self):
        self.logger.log("Hello")
    
    def say_goodbye(self):
        self.logger.log("Goodbye")

if __name__ == "__main__":
    console_logger = ConsoleLogger()
    file_logger = FileLogger("log.txt")

    app_with_console_logger = App(console_logger)
    app_with_file_logger = App(file_logger)

    app_with_console_logger.say_hello()
    app_with_file_logger.say_hello()
    app_with_console_logger.say_goodbye()
    app_with_file_logger.say_goodbye()