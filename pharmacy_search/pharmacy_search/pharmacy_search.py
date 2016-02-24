import csv
import math

rad = 6372795 

def distance(apteka, x, y):
    long_rad1 = apteka["longitude"]*math.pi/180.
    lat_rad1 = apteka["latitude"]*math.pi/180.
    long_rad2 = float(x)*math.pi/180.
    lat_rad2 = float(y)*math.pi/180.
    cl1 = math.cos(lat_rad1)
    cl2 = math.cos(lat_rad2)
    sl1 = math.sin(lat_rad1)
    sl2 = math.sin(lat_rad2)
    delta = long_rad2 - long_rad1
    cdelta = math.cos(delta)
    sdelta = math.sin(delta)
    y1 = math.sqrt(math.pow(cl2*sdelta,2)+math.pow(cl1*sl2-sl1*cl2*cdelta,2))
    x1 = sl1*sl2+cl1*cl2*cdelta
    ad = math.atan2(y1,x1)
    dist = ad*rad
    return dist
 
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

def count_distances(ap_list, x_coord, y_coord):
    for i in range(len(ap_list)):
        ap_list[i]["distance"] = distance(ap_list[i], x_coord, y_coord)

test_file = open("test2.txt", 'r', encoding="UTF-8")
filename = str(test_file.readline())
filename = filename[:len(filename)-1]
x_coord = float(test_file.readline())
y_coord = float(test_file.readline())
test_file.close()

apt_list = readfile(filename)
count_distances(apt_list, x_coord, y_coord)
sorted_apt_list = sorted(apt_list, key=lambda k: k['distance']) 

print('{0}|{1}'.format(sorted_apt_list[0]["name"], sorted_apt_list[0]["address"]))
print('{0}|{1}'.format(sorted_apt_list[1]["name"], sorted_apt_list[1]["address"]))
print('{0}|{1}'.format(sorted_apt_list[2]["name"], sorted_apt_list[2]["address"]))



