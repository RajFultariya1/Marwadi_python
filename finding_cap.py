import re
sentence='python is fun and Important'
capital=re.findall(r'\b[A-Z][a-z]*\b',sentence)
print(capital)
