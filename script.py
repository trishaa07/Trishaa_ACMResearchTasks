import re #regular expression library
from datetime import datetime 


def transform_logs(input_text: str) -> str:

    # 1. Hide email addresses
    email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'
    input_text = re.sub(
        email_pattern,
        '[HIDDEN]',
        input_text
    )


    # 2. Format dates
    def format_date(match):

        date_text = match.group()

        date = datetime.strptime(
            date_text,
            "%d/%m/%Y %H:%M"
        )

        return date.strftime(
            "%d %B %Y, %I:%M %p"
        )


    input_text = re.sub(
        r'\b\d{2}/\d{2}/\d{4} \d{2}:\d{2}\b',
        format_date,
        input_text
    )


    # 3. Highlight ERROR
    input_text = re.sub(
        r'\bERROR\b',
        '🚨 ERROR',
        input_text
    )


    # 4. Remove extra spaces
    input_text = re.sub(
        r'[ \t]+',
        ' ',
        input_text
    )


    return input_text.strip()


# Example input
logs = """
23/08/2025 14:05 ERROR User john@gmail.com failed to login.
23/08/2025 15:20 INFO User successfully logged in.
24/08/2025 09:10 ERROR Contact admin@gmail.com immediately.
"""


result = transform_logs(logs)

print(result)