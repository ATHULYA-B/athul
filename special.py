import re
def remove_special_character(input_string):
    pattern= r'[^\w\s]'
    result_string=re.sub(pattern,'',input_string)
    return result_string
input_string="abcfgh%h*jk%l"
output_string=remove_special_character(input_string)
print(output_string)