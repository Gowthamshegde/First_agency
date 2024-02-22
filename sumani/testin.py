import re
input_string="Credit memo may be a duplicate of credit memo NCR4-1025"
pattern = re.compile(r'\b[A-Z0-9]+-\d+\b')

match = re.search(pattern, input_string)

if match:
    extracted_pattern = match.group(0)
    print(extracted_pattern)