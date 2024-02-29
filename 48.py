#Regex
#Ex1
import re
search = 'ab*'
test = ["aaa", "abc", "abbde", "ab", "abb"]
for test in test:
    if re.search(search, test):
        print(f"'{test}' YES")
    else:
        print(f"'{test}' NO")

#Ex2
        import re
        search = 'ab*{2,3}'
test = ["aaa", "abc", "abbde", "ab", "abb"]
for test in test:
    if re.search(search, test):
        print(f"'{test}' YES")
    else:
        print(f"'{test}' NO")

#Ex3
        import re
        def f_sequences(text):
            pattern = r'\b[a-z]+_[a-z]+\b'
            sequences = re.findall(pattern, text)
            return sequences
        text = "I_love_YOU_KBTU"
        sequences = f_sequences(text)
        print(sequences)

#Ex4
        import re
        def f_sequences(text):
            pattern = r'[A-Z][a-z]+'
            sequences = re.findall(pattern, text)
            return sequences
        text = "I love KBTU"
        sequences = f_sequences(text)
        print(sequences)

#Ex 5
import re

def string(text):
    pattern = r'a.*b$'
    match = re.match(pattern, text)
    if match:
        return True
    else:
        return False

text = "aaaasssdffb"
if string(text):
    print(f"'{test}' YES")
else:
    print(f"'{test}' NO")

#Ex 6
    def replace(text):
        replacements = [' ', ',', '.']
        for char in replacements:
            text = text.replace(char, ':')
            return text
        text = "This is a sample, text. With some spaces."
        new_text = replace(text)
        print(new_text)
#Ex 7 
import re
def snake_to_camel(snake_case_str):
    camel_case_str = re.sub(r'([a-z])', lambda match: match.group(1).upper(), snake_case_str)
    return camel_case_str

snake_case_str = "hello_kbtu"
camel_case_str = snake_to_camel(snake_case_str)
print(camel_case_str)

#EX 8
import re

def split(text):
    substrings = re.findall('[a-z]+|[A-Z][a-z]*', text)
    return substrings

text = "ILoveKBTU"
substrings = split(text)
print(substrings)


#Ex9
import re

def spaces(text):
    new_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return new_text

text = "KazakHbRitishUniversity"
modified_text = spaces(text)
print(modified_text)

#Ex 10
import re

def camel_to_snake(camel_case):
    return re.sub(r'(?<!^)(?=[A-Z])', '-', camel_case).lower()
camel_case_string = "camelCaseString"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)






        


