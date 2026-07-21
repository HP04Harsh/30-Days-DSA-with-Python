KEYWORDS = ["error", "failed", "exception", "critical", "warning", "traceback"]

LOG_FILE_PATH = "application.log"

def checkevents(file_path):
    try:
        with open(file_path, 'r') as log_file:
            print(f"Checking events in log file: {file_path}")
            found_suspicious_events = False

            for line_number, line in enumerate(log_file, start=1):
                if any(keyword in line.lower() for keyword in KEYWORDS):
                    print(f"Suspicious event found on line {line_number}: {line.strip()}")
                    found_suspicious_events = True

            if not found_suspicious_events:
                print("No suspicious events found.")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error occurred while reading the log file: {e}")