import re

email = 'adalovelace@cambridge.org'
search_object = re.search('[A-Za-z0-9\._+]+@[A-Za-z]+.(com|org|edu|net)', email)
print(search_object.group())