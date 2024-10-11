# %%
import os
import logging
import pandas as pd

# %%
class CustomLogger:
    def __init__(self, log_file_name: str, log_dir_path: str, logger_name: str) -> None:
        """
        Initialize the CustomLogger class.

        :param log_file_name: The name of the log file (without extension).
        :param log_dir_path: The directory where the log file will be saved.
        :param logger_name: The name of the logger as current module's name.
        """
        
        # Ensure the logger_name is not blank
        if not logger_name:
            raise Exception("Assign logger name.")

        self.logger: logging.Logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        self.log_file_name = log_file_name
        self.log_dir_path = log_dir_path
        self._create_file_handler()
        self._create_stream_handler()

    def _create_file_handler(self) -> None:
        """
        Create and add a file handler to the logger to write logs to a file.
        """
        file_name = f"{self.log_file_name}_logger.log"
        file_path = os.path.join(self.log_dir_path, file_name)

        file_handler = logging.FileHandler(file_path, mode='a+', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        # Define log format
        formatter = logging.Formatter(
            fmt='[%(name)s] %(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]\n',
            datefmt='%m-%d %I:%M %p'
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def _create_stream_handler(self) -> None:
        """
        Create and add a stream handler to the logger to print logs to the console.
        """
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            fmt='[%(name)s] %(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]\n',
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

    @staticmethod
    def log_dataframe(df: pd.DataFrame, logger: logging.Logger, name: str = "DataFrame") -> None:
        """
        Log the head of a pandas DataFrame at the DEBUG level.

        :param df: The pandas DataFrame to log.
        :param logger: The logger instance to use for logging.
        :param name: The name to refer to the DataFrame in the logs (optional).
        """
        logger.debug(f'{name} head:\n {df.head()}\n----------\n')

    @staticmethod
    def log_dataframes(*args: pd.DataFrame, logger: logging.Logger) -> None:
        """
        Log the head of multiple pandas DataFrames at the DEBUG level.

        :param args: The pandas DataFrames to log.
        :param logger: The logger instance to use for logging.
        """
        for i, gdf in enumerate(args, start=1):
            logger.debug(f'DataFrame {i} head:\n {gdf.head()}\n----------\n')
