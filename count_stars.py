
reader = open('stars.txt','r')

total_stars = 0

for something in reader:
    fields = something.strip().split(',')
    total_stars = total_stars + int(fields[1])

print(total_stars)

reader.close()

