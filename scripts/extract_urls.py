import re

# Open the email sample
with open('sample_email.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all links starting with http or https
urls = re.findall(r'(https?://[^\s)>\'"]+)', text)

print("URLs found:\n")
if urls:
    for u in urls:
        print(u)
else:
    print("No URLs found.")
