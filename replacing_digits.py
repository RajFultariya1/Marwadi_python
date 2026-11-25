import re
text_with_digits='server123 has IP456'
replaced_text=re.sub(r'\b','*',text_with_digits)
print(replaced_text)
