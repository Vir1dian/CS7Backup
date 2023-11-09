# Assignment 8
# CS7 - Section D01
# November 7, 2023,
# Gavin Torrecampo

if __name__ == "__main__":
    titanic_data = open("C:/Users/gavto/Documents/GitHub/CS7Backup/torrecampoA8/titanic.csv", "r")
    passengerID = []
    survived = []
    p_class = []
    # name = []
    sex = []
    age = []
    age_sum = 0  # sum of nonempty age values
    age_count = 0  # number of nonempty age values
    sib_sp = []
    parch = []
    # ticket = []
    fare = []
    fare_sum = 0  # sum of nonempty fare values
    fare_count = 0  # number of nonempty fare values
    cabin = []
    embarked = []
    titanic_data.readline()
    # reads the first line to ignore field name headers (due to name header only using index 3 after
    # split(',') while name values use index 3 and 4
    raw_line = titanic_data.readline()  # starts from actual values, raw_line 2
    while len(raw_line) > 0:
        line = raw_line.split(',')
        passengerID.append(line[0])
        survived.append(line[1])
        p_class.append(line[2])
        # omit name (indices 3 & 4)
        sex.append(0 if line[5] == "male" else 1)
        age.append(line[6])
        if line[6]:
            age_sum += float(line[6])
            age_count += 1
        sib_sp.append(line[7])
        parch.append(line[8])
        # omit ticket (index 9)
        fare.append(line[10])
        if line[10]:
            fare_sum += float(line[10])
            fare_count += 1
        cabin.append(line[11] if line[11] else "missing")
        embarked.append(line[12] if line[12] else "X")
        raw_line = titanic_data.readline()
    age_mean = round(age_sum / age_count, 2)
    fare_mean = round(fare_sum / fare_count, 2)
    survived_m = 0
    survived_f = 0
    survived_y = 0
    for i in range(0, len(passengerID)):
        if not age[i]:
            age[i] = age_mean
        if not fare[i]:
            fare[i] = fare_mean
        if sex[i] == '0' and survived[i] == '1':
            survived_m += 1
        # print(age[i], ' | ', fare[i])

    stat_report = ('****STATS****\n' +
                   'Passengers: ' + str(len(passengerID)) + '\n' +
                   'Survivors: ' + str((round(survived.count('1') / len(passengerID), 3) * 100)) + '%\n' +
                   'Dead :' + str((round(survived.count('0') / len(passengerID), 3) * 100)) + '%\n' +
                   'Surviving males: ' +
                   'Surviving females: ' +
                   'Survivors 12 or younger: ')
    print(stat_report)

    titanic_data.close()
