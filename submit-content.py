import CommunityBuilder
import csv

print('Enter Username:')
username = input()
print('Enter Password:')
password = input()

CB = CommunityBuilder.CommunityBuilder(username, password)
with open('submissions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count+= 1
        else:
            CB.add_submission(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            line_count+=1
CB.SubmitActivities()