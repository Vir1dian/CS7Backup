# Assignment 8
# CS7 - Section D01
# November 7, 2023,
# Gavin Torrecampo

if __name__ == "__main__":
    titanic_data = open("C:/Users/gavto/Documents/GitHub/CS7Backup/torrecampoA8/titanic.csv", "r")
    titanic_cleansed_data = open("C:/Users/gavto/Documents/GitHub/CS7Backup/torrecampoA8/titanic_cleansed.csv", "a")
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

    # Loop 1, cleansing data into separate lists, calculating the means of age and fares
    while len(raw_line) > 0:
        line = raw_line.split(',')
        passengerID.append(line[0])
        survived.append(line[1])
        p_class.append(line[2])
        # omit name (indices 3 & 4)
        sex.append(0 if line[5] == "male" else 1)
        age.append(line[6])
        if line[6]:  # Count existing ages and sum them up together
            age_sum += float(line[6])
            age_count += 1
        sib_sp.append(line[7])
        parch.append(line[8])
        # omit ticket (index 9)
        fare.append(line[10])
        if line[10]:  # Count existing fares and sum them up together
            fare_sum += float(line[10])
            fare_count += 1
        cabin.append(line[11] if line[11] else "missing")
        embarked.append(line[12] if line[12] else "X")
        raw_line = titanic_data.readline()
    age_mean = round(age_sum / age_count, 2)
    fare_mean = round(fare_sum / fare_count, 2)

    # Loop 2, adding mean age and fare to empty spots to complete cleansing.
    # Counting up survivors by age and sex for analytics
    # Writing up cleansed data to titanic_cleansed.csv
    titanic_cleansed_data.write('PassengerId,Survived,Pclass,Sex,Age,SibSp,Parch,Fare,Cabin,Embarked')
    survived_m = 0
    survived_f = 0
    survived_y = 0
    all_y = 0
    for i in range(0, len(passengerID)):
        if not age[i]:
            age[i] = age_mean
        if not fare[i]:
            fare[i] = fare_mean
        if survived[i] == '1':
            if sex[i] == 0:
                survived_m += 1
            else:
                survived_f += 1
        if float(age[i]) <= 12:
            all_y += 1
            if survived[i] == '1':
                survived_y += 1
        titanic_cleansed_data.write(passengerID[i] + ',' + survived[i] + ',' + p_class[i] + ',' +
                                    str(sex[i]) + ',' + str(age[i]) + ',' + sib_sp[i] + ',' + parch[i] + ',' +
                                    str(fare[i]) + ',' + cabin[i] + ',' + embarked[i] + '\n')

    stat_report = ('****STATS****\n' +
                   'Passengers: ' + str(len(passengerID)) + '\n' +
                   'Survivors: ' + str(round(survived.count('1') * 100 / len(passengerID), 2)) + '%\n' +
                   'Dead: ' + str(round(survived.count('0') * 100 / len(passengerID), 2)) + '%\n' +
                   'Surviving males: ' + str(round(survived_m * 100 / sex.count(0), 2)) + '%\n' +
                   'Surviving females: ' + str(round(survived_f * 100 / sex.count(1), 2)) + '%\n' +
                   'Survivors 12 or younger: ' + str(round(survived_y * 100 / all_y, 2)) + '%\n')
    print(stat_report)

    titanic_data.close()
    titanic_cleansed_data.close()
