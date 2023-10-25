# Assignment 7
# CS7 - Section D01
# October 24, 2023,
# Gavin Torrecampo
def raterInfo(f_name, l_name, age, movie_count):  # handles name, AGE, & formatting
    rater = 'Rater:    ' + f_name + ' '*(15 - len(f_name)) + l_name + '\n'
    if age < 4:
        gen = 'alpha'
    elif age < 27:
        gen = 'gen z'
    elif age < 43:
        gen = 'millennial'
    elif age < 59:
        gen = 'gen X'
    elif age < 78:
        gen = 'baby boomer'
    else:
        gen = 'silent'
    rater += 'Age of rater:  ' + str(age) + ' '*(10-len(str(age))) + gen + '\n'
    rater += f_name + ' rated ' + str(movie_count) + ' movies' + '\n'
    return rater


def movieLine(name, genre, rating):  # handles name, GENRE, & formatting
    if genre == 'C':
        genre = 'comedy'
    elif genre == 'R':
        genre = 'rom-com'
    elif genre == 'A':
        genre = 'action'
    elif genre == 'S':
        genre = 'sci-fi'
    elif genre == 'H':
        genre = 'horror'
    elif genre == 'D':
        genre = 'drama'
    else:
        genre = 'N/A'
    movie = 'Movie:    ' + name + ' '*(20-len(name)) + genre + ' '*(10-len(genre)) + 'Rating:  ' + rating + '\n'
    return movie


if __name__ == "__main__":
    a7data = open("C:/Users/gavto/Documents/GitHub/CS7Backup/torrecampoA7/A7F23data.txt", "r")
    line_list = []
    line = a7data.readline()
    while len(line) > 0:
        if len(line_list) != 0:
            line_list.append([line[:20].strip(), line[20], line[21]])
        else:
            line_list.append([line[:10].strip(), line[10:25].strip(), line[25:27].strip()])
        line = a7data.readline()
    report = raterInfo(line_list[0][0], line_list[0][1], int(line_list[0][2]), len(line_list) - 1)
    for i in range(1, len(line_list)):
        report += movieLine(line_list[i][0], line_list[i][1], line_list[i][2])
    print(report)
    a7data.close()
