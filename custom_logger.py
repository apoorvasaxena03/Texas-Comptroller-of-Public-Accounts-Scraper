# %%
import os
import logging
import pandas as pd

# %%
class CustomLogger:
    def __init__(self, log_file_name: str, log_dir_path: str, logger_name: str, 
                 file_log_level: str = 'DEBUG', stream_log_level: str = 'DEBUG', 
                 file_handler: bool = True, stream_handler: bool = True) -> None:
        """
        Initialize the CustomLogger class with custom log levels for file and stream handlers.

        :param log_file_name: The name of the log file (without extension).
        :param log_dir_path: The directory where the log file will be saved.
        :param logger_name: The name of the logger as the current module's name.
        :param file_log_level: The logging level for the file handler ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
        :param stream_log_level: The logging level for the stream handler ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
        :param file_handler: Whether to enable file handler (logs to a file).
        :param stream_handler: Whether to enable stream handler (logs to the console).

        Example:
            # Initialize logger with custom log levels
            logger_instance = CustomLogger(
                log_file_name='scraper_log',
                log_dir_path='./logs',
                logger_name='LeaseScraper',
                file_log_level='INFO',    # Set INFO level for file logging
                stream_log_level='DEBUG',  # Set DEBUG level for console logging
                file_handler=True,         # Enable file handler
                stream_handler=True        # Enable stream handler (console)
            )

            logger = logger_instance.get_logger()
            logger.debug("This is a debug message.")   # Will appear in the console but not in the file
            logger.info("This is an info message.")    # Will appear in both the file and the console
            logger.error("This is an error message.")  # Will appear in both the file and the console
        """
        
        if not logger_name:
            raise Exception("Assign logger name.")
        
        self.logger: logging.Logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)  # Set to the lowest level so handlers can manage filtering
        self.log_file_name = log_file_name
        self.log_dir_path = log_dir_path

        # If file handler is enabled, create it with the custom file log level
        if file_handler:
            self._create_file_handler(file_log_level)

        # If stream handler is enabled, create it with the custom stream log level
        if stream_handler:
            self._create_stream_handler(stream_log_level)

    def _get_log_level(self, log_level: str) -> int:
        """
        Convert the string log level to the corresponding logging module constant.

        :param log_level: The logging level as a string.
        :return: Corresponding logging level constant from the logging module.
        """
        levels = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        return levels.get(log_level.upper(), logging.DEBUG)  # Default to DEBUG if not recognized

    def _create_file_handler(self, log_level: str) -> None:
        """
        Create and add a file handler to the logger to write logs to a file.

        :param log_level: The logging level to use for this handler.
        """
        file_name = f"{self.log_file_name}_logger.log"
        file_path = os.path.join(self.log_dir_path, file_name)

        file_handler = logging.FileHandler(file_path, mode='a+', encoding='utf-8')
        file_handler.setLevel(self._get_log_level(log_level))  # Set the custom log level for file handler

        # Define log format
        formatter = logging.Formatter(
            fmt='[%(name)s] %(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
            datefmt='%m-%d %I:%M %p'
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def _create_stream_handler(self, log_level: str) -> None:
        """
        Create and add a stream handler to the logger to print logs to the console.

        :param log_level: The logging level to use for this handler.
        """
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self._get_log_level(log_level))  # Set the custom log level for stream handler

        formatter = logging.Formatter(
            fmt='[%(name)s] %(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
            datefmt='%m-%d %I:%M %p'
        )
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def get_logger(self) -> logging.Logger:
        """
        Return the logger instance for external use.

        :return: The logger instance.
        """
        return self.logger
