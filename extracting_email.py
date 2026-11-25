import re
text_with_email_id='contact us at support@vashi.com'
pattern=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'   
match=re.search(pattern,text_with_email_id)
if match:
    print("1. Email found")
else:
    print("1. Email not found")


