# edited version of instructor's version of the count_stars.py code

def get_content(the_line):
    fields = the_line.strip().split('#')
    return(fields[0].strip())


def get_number(the_content):
    return int(the_content.split(',')[1])


source = open('stars.txt', 'r')

total = 0

for line in source:
    content = get_content(line)
    if content != '':
        total = total + get_number(content)

print total

