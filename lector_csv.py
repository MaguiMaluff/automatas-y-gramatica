import csv

class Lector():
    def __init__(self):
        self.data = ''
        with open('export-2019-to-now-v4.csv', newline='') as csvfile:
            info = csv.reader(csvfile, delimiter=',')
            self.data = list(info)

    def get_user_ID(self, user, lista):
        data_per_user = []
        total_conections = 0
        for row in lista:
            if user == row[3]:
                total_conections += 1
                data_per_user.append(row)
        data_per_user.append(total_conections)
        return data_per_user
                

    def get_day(self, initial, final, lista):
        data_per_days = []
        for row in lista:
            date_initial = row[6].replace('-', "")
            date_final = row[8].replace('-', "")
            if initial <= date_initial and initial <= date_final:
                if final >= date_initial and final >= date_final:
                    data_per_days.append(row)
        return(data_per_days)

    def get_results(self, lista):
        filtered_list = [[row[6], row[8]] for row in lista]
        return filtered_list


