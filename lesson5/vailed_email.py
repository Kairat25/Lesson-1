import re

email = "email@gmail.com"
result = re.match(r"^([a-zA-Z0-9]{5,30})@(gmail|mail|yandex|icloud|namba).(com|ru|kg)", email)

print(result)