import os
import shutil
import logging
from datetime import datetime, timedelta
from logging.handlers import RotatingFileHandler
from zipfile import ZipFile


def configure_logging(log_file='log.txt'):
    """
    Configures logging for the application, setting up a rotating file handler.

    Parameters:
    - log_file (str): The name of the log file (default is 'log.txt').
    """
    # Configure logger
    logger = logging.getLogger()
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Create handler for log file
        log_path = os.path.join(os.getcwd(), log_file)
        handler = RotatingFileHandler(
            log_path, maxBytes=1024*1024, backupCount=5)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(handler)


def delete_old_folders(directory, days_threshold=5):
    """
    Deletes folders in the specified directory that are older than a given threshold.

    Parameters:
    - directory (str): The path to the directory containing folders to be checked.
    - days_threshold (int): The threshold in days; folders older than this will be deleted (default is 5).
    """
    try:
        current_date = datetime.now()
        logger = logging.getLogger()

        for folder_name in os.listdir(directory):
            folder_path = os.path.join(directory, folder_name)

            try:
                folder_date = datetime.strptime(folder_name, '%Y-%m-%d')
            except ValueError:
                # Delete folder if it does not match the date format
                shutil.rmtree(folder_path)
                logger.info(
                    f"Folder {folder_name} deleted because it does not match the date format.")
                continue

            if current_date - folder_date > timedelta(days=days_threshold):
                # Delete folder with all its contents
                shutil.rmtree(folder_path)
                logger.info(
                    f"Folder {folder_name} deleted because it is older than {days_threshold} days.")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


def create_archives(directory):
    """
    Creates ZIP archives for PDF files in the specified directory, organizing them by their last modified date.

    Parameters:
    - directory (str): The path to the directory containing PDF files to be archived.
    """
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)

                # Ignore non-PDF files
                if not file.lower().endswith('.pdf'):
                    continue

                # Get the last modified date of the file
                file_modified_date = datetime.fromtimestamp(
                    os.path.getmtime(file_path))

                # Form the archive name based on the last modified date
                archive_name = file_modified_date.strftime('%Y-%m-%d') + '.zip'
                archive_path = os.path.join(directory, archive_name)

                with ZipFile(archive_path, 'a') as zip_file:
                    # Add the file to the archive
                    zip_file.write(file_path, os.path.basename(file_path))

                logging.info(
                    f"File {file} added to the archive {archive_name}.")

                # Remove the original file
                os.remove(file_path)
                logging.info(f"Original file {file} deleted.")
    except Exception as e:
        logging.error(f"An error occurred while creating archives: {str(e)}")


def main():
    # Replace 'path/to/your/folder' with the actual path to your main directory
    brightness_directory = '/home/app/backend/orgton/media/brightness'
    example_directory = '/home/app/backend/orgton/media/example'
    orders_directory = '/home/app/backend/orgton/media/orders'

    # Call configure_logging only once before calling delete_old_folders and create_archives
    configure_logging()

    delete_old_folders(brightness_directory)
    delete_old_folders(example_directory)
    create_archives(orders_directory)


if __name__ == '__main__':
    main()
else:
    print(f' {__name__} imported')
