import datetime

def log_message(file_name, message, level):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_name, 'a') as log_file:
        log_file.write(f'[{timestamp}] [{level}] {message}\n')


