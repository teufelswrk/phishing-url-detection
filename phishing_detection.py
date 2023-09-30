import re

def is_phishing(url):
    # Define regular expressions for common phishing patterns
    patterns = [
        r"https?://(?:www\.)?([^\s]+)\.([^\s/]{2,}|[a-z]{2,})(/[^\s]*)?"
    ]

    for pattern in patterns:
        if re.search(pattern, url):
            return True

    return False

# Get URL input from the user
input_url = input("Please enter the URL to check for phishing: ")

if is_phishing(input_url):
    print(f"The URL '{input_url}' might be a phishing link.")
else:
    print(f"The URL '{input_url}' is not flagged as a phishing link.")
