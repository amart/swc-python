
def get_content(something):

    cleaned_something = something.strip()
    if cleaned_something == '':
        return('')

    fields = cleaned_something.split('#')
    if fields[0] == '':
        return('')
    else:
        return(fields[0])


def get_number(something):
    return(int(something.split(',')[1]))


reader = open('stars.txt','r')

total_stars = 0

for something in reader:
    content = get_content(something)
    if content != '':
        total_stars = total_stars + get_number(content)

print(total_stars)

reader.close()

