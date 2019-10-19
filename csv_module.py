import csv

path = 'C:\\Users\DASA004\\Documents\\KnowHow\\Python\\IntroToPython\\sample.csv'
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)
data = []
for row in reader:
    index = int(row[0])
    year = int(row[1])
    age = int(row[2])
    name = str(row[3])
    movie = row[4]
    data.append([index, year, age, name, movie])

#write into csv
return_path = "C:\\Users\DASA004\\Documents\\KnowHow\\Python\\IntroToPython\\returns.csv"
file = open(return_path, 'w')
writer = csv.writer(file)
writer.writerow(['indexm', 'movie_name'])

for i in range(len(data) - 1):
    lines = data[i]
    csvIndex = lines[0]
    csvMovie = lines[4]
    writer.writerow([csvIndex, csvMovie])
