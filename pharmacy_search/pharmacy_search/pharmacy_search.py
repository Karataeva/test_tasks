import csv

def readfile(filename):
    ap_list = []
    f = open(filename, 'r', encoding="UTF-8")
    apteka = f.readline() 
    apteka = f.readline() 
    while apteka:
        apteka = apteka.split('|')
        d = dict(name = apteka[0], address = apteka[1], longitude = float(apteka[2]), latitude = float(apteka[3]), distance = 0)        
        ap_list.append(d)
        apteka = f.readline()
    f.close()
    return ap_list

def distance(apteka, x, y):
    res = ((apteka["longitude"]-float(x))**2+(apteka["latitude"]-float(y))**2)**0.5
    return res

def count_distances(ap_list, x_coord, y_coord):
    for i in range(len(ap_list)):
        ap_list[i]["distance"] = distance(ap_list[i], x_coord, y_coord)

filename = input("Name of file: ")
x_coord = input("Longitude: ")
y_coord = input("Latitude ")

apt_list = readfile(filename)
count_distances(apt_list, x_coord, y_coord)
sorted_apt_list = sorted(apt_list, key=lambda k: k['distance']) 

print('{0}|{1}'.format(sorted_apt_list[0]["name"], sorted_apt_list[0]["address"]))
print('{0}|{1}'.format(sorted_apt_list[1]["name"], sorted_apt_list[1]["address"]))
print('{0}|{1}'.format(sorted_apt_list[2]["name"], sorted_apt_list[2]["address"]))



