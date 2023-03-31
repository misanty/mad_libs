import os, re

# Read file
keywords = []
row_lines = ''
replaced_lines = ''
ml = open('./Mad_Libs/phrase.txt', 'r')
lines = ml.readlines()
pattern = r'([A-Z]{2,})+'

#Analyze file by finding ADJECTIVE, NOUN and VERB keywords
def user_input_replace(arg, keyword, rowlines):
    """
    Replace the keyword with user input in the given string and return the new string.
    """
    return re.sub(keyword, arg, rowlines, count=1)

#Get and replace user inputs for each keywords
def find_replace(rows):
    """
    Get user input for each keyword and replace it in the given string.
    """
    global replaced_lines
    for i in keywords:
        if i.lower().startswith('a'):
            print('Enter an %s: ' % i)
            if len(replaced_lines) <= 0:
                replaced_lines += user_input_replace(input(), i, rows)

            else:
                replaced_lines = user_input_replace(input(), i, replaced_lines)
                # print(replaced_lines)
        else:
            print('Enter a %s: ' % i)
            if len(replaced_lines) <= 0:
                replaced_lines += user_input_replace(input(), i, rows)
            else:
                replaced_lines = user_input_replace(input(), i, replaced_lines)
            # print(replaced_lines)


for row in lines:
    findings = re.findall(pattern, row)
    row_lines += row
    # print(len(findings))
    for f in findings:
        keywords.append(f)
    #  print(f)

print(row_lines)
find_replace(row_lines)
print(len(keywords))
print(replaced_lines)

ml.close()


#Create a new text file and save it the new text to it and also print the result on screen
with open('./Mad_Libs/rephrase.txt','w') as rephrase:
     rephrase.write(replaced_lines)
rephrase.close()





