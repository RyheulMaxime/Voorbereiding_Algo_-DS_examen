# Exception handling

# numlist = [ 100, 101, 0, "103", 104 ]
# try:
#     i1 = int( input( "Geef een index: " ) )
#     print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
# except Exception as ex:
#     print("Error: ",ex) 


# 2: Counting words

# import os.path

# if os.path.exists("data.txt"):
#     print("File exists")
def word_split(file):
    data = open(file, "r", encoding="utf-8")
    text = data.read().replace("\n"," ")
    replace = "?",".",","
    for i in replace:
        text = text.replace(i,"")
    woords = text.split()
    data.close()
    return woords

def word_count(text):
    word_dict = {}
    words = word_split(text)
    for word in words:
        if word.lower() in word_dict:
            word_dict[word.lower()] += 1
        else:
            word_dict[word.lower()] = 1
    return word_dict

# print(word_count("data.txt"))


# 3: ISBN codes

codes = ['9789743159664', '9785301556616', '9797668174969', '9781787559554', '9780817481461', '9785130738708', '9798810365062', '9795345206033', '9792361848797', '9785197570819', '9786922535370', '9791978044523', '9796357284378', '9792982208529', '9793509549576', '9787954527409', 
'9797566046955', '9785239955499', '9787769276051', '9789910855708', '9783807934891', '9788337967876', '9786509441823', '9795400240705', '9787509152157', '9791478081103', '9780488170969', '9795755809220', 
'9793546666847', '9792322242176', '9782582638543', '9795919445653', '9796783939729', '9782384928398', '9787590220100', '9797422143460', '9798853923096', '9784177414990', '9799562126426', '9794732912038', 
'9787184435972', '9794455619207', '9794270312172', '9783811648340', '9799376073039', '9798552650309', '9798485624965', '9780734764010', '9783635963865', '9783246924279', '9797449285853', '9781631746260', 
'9791853742292', '9781796458336', '9791260591924', '9789367398012' ]

def check_digit_13(code):
    o = int(code[0:1]) + int(code[2:3]) + int(code[4:5]) + int(code[6:7]) + int(code[8:9]) + int(code[10:11])
    e = int(code[1:2]) + int(code[3:4]) + int(code[5:6]) + int(code[7:8]) + int(code[9:10]) + int(code[11:12])
    calculated_13 = (10 - ((o + (3 * e)) % 10)) % 10 
    return int(code[12:13]) == calculated_13
def ISBN_check(codes):
    ISBN_dict = {"English": 0 ,"French": 0 ,"German": 0 ,"Japan": 0 ,"Russian": 0 ,"China": 0,"Other": 0 ,"Errors": 0}
    for code in codes:
        # print(code[3:4])
        if len(code) != 13 or (code[0:3] != "978" and code[0:3] != "979") or check_digit_13(code) == False:
            ISBN_dict["Errors"] += 1
        else:
            
            if code[3:4] == "0" or code[3:4] == "1":
                ISBN_dict["English"] += 1
            elif code[3:4] == "2":
                ISBN_dict["French"] += 1
            elif code[3:4] == "3": 
                ISBN_dict["German"] += 1
            elif code[3:4] == "4":
                ISBN_dict["Japan"] += 1
            elif code[3:4] == "5":
                ISBN_dict["Russian"] += 1
            elif code[3:4] == "7":
                ISBN_dict["China"] += 1
            else:
                ISBN_dict["Other"] += 1
    return ISBN_dict
            
def overview(code):
    overview_dict = ISBN_check(code)
    print("English speaking countries:", overview_dict["English"])
    print("French speaking countries:", overview_dict["French"])
    print("German speaking countries:", overview_dict["German"])
    print("Japan:", overview_dict["Japan"])
    print("Russian speaking countries:", overview_dict["Russian"])
    print("China:", overview_dict["China"])
    print("Other countries:", overview_dict["Other"])
    print("Errors:", overview_dict["Errors"])
    
# print(overview(codes))

# 4: Doubles
def double(geheleLst):
    sortedLst = sorted(geheleLst)
    # dubbelLst = []
    for i in range(len(geheleLst) - 1):
        if sortedLst[i] == sortedLst[i + 1]:
            return sortedLst[i]
    #         dubbelLst.append(sortedLst[i])
    # return dubbelLst


def doubles(geheleLst):
    sortedLst = sorted(geheleLst)
    singleLst = []
    dubbelLst = []
    for i in range(len(geheleLst)):
        if  i < len(sortedLst) - 1 and sortedLst[i] == sortedLst[i + 1]:
            dubbelLst.append(sortedLst[i])
        elif (i == len(sortedLst) - 1 or sortedLst[i] != sortedLst[i + 1]) and sortedLst[i] not in dubbelLst:
            singleLst.append(sortedLst[i])
    singleSet = set(singleLst)
    dubbelSet = set(dubbelLst)
    return (singleSet, dubbelSet)


# print(doubles([-63, 90, -298, 212, -10, 94, -59, -132, -194, -306, 185, 42, -365, -270, -356, 88, 169, -159, -247, -346]) )


# 5: Bloodgroups
def bloodgroup_child(parent1, parent2):
    p1_alleles = parent1[0:-1]
    p2_alleles = parent2[0:-1]
    p1_rhesus = parent1[-1]
    p2_rhesus = parent2[-1] 

    child_set = set()

    child_rhesus_options = []
    if p1_rhesus == '-' and p2_rhesus == '-':
        child_rhesus_options = ['-']
    else:
        child_rhesus_options = ['+', '-']

    child_alleles_option = []
    if p1_alleles == 'O' and p2_alleles == 'O':
        child_alleles_option = ['O']
    elif (p1_alleles == 'A' and p2_alleles == 'O') or (p1_alleles == 'O' and p2_alleles == 'A'):
        child_alleles_option = ['A', 'O']
    elif (p1_alleles == 'B' and p2_alleles == 'O') or (p1_alleles == 'O' and p2_alleles == 'B'):
        child_alleles_option = ['B', 'O']
    elif (p1_alleles == 'AB' and p2_alleles == 'O') or (p1_alleles == 'O' and p2_alleles == 'AB'):
        child_alleles_option = ['B', 'A']
    elif p1_alleles == 'A' and p2_alleles == 'A':
        child_alleles_option = ['A', 'O']
    elif (p1_alleles == 'A' and p2_alleles == 'B') or (p1_alleles == 'B' and p2_alleles == 'A'):
        child_alleles_option = ['AB', 'A', 'B', 'O']
    elif (p1_alleles == 'A' and p2_alleles == 'AB') or (p1_alleles == 'AB' and p2_alleles == 'A'):
        child_alleles_option = ['A', 'AB', 'B']
    elif p1_alleles == 'B' and p2_alleles == 'B':
        child_alleles_option = ['B', 'O']
    elif (p1_alleles == 'B' and p2_alleles == 'AB') or (p1_alleles == 'AB' and p2_alleles == 'B'):
        child_alleles_option = ['B', 'AB', 'A']
    elif (p1_alleles == 'AB' and p2_alleles == 'AB'):
        child_alleles_option = ['AB', 'A', 'B']

    for rhesus in child_rhesus_options:
        for alleles in child_alleles_option:
            child_set.add(alleles + rhesus)

    return child_set


def bloodgroup_parent(parent, child):
    p1_alleles = parent[0:-1]
    c_alleles = child[0:-1]
    p1_rhesus = parent[-1]
    c_rhesus = child[-1] 

    parent_set = set()

    parent_rhesus_options = []
    if p1_rhesus == '-' and c_rhesus != '-':
        parent_rhesus_options = ['+']
    else:
        parent_rhesus_options = ['+', '-']

    parent_alleles_option = []
    if (p1_alleles == 'O' and c_alleles == 'O'):
        parent_alleles_option = ['O', 'A', 'B']
    elif (p1_alleles == 'O' and c_alleles == 'A'):
        parent_alleles_option = ['A', 'AB']
    elif (p1_alleles == 'O' and c_alleles == 'B'):
        parent_alleles_option = ['B', 'AB']
    elif (p1_alleles == 'A' and c_alleles == 'O'):
        parent_alleles_option = ['O', 'A', 'B']
    elif (p1_alleles == 'A' and c_alleles == 'A'):
        parent_alleles_option = ['O', 'A', 'AB', 'B']
    elif (p1_alleles == 'A' and c_alleles == 'B'):
        parent_alleles_option = ['B', 'AB']
    elif (p1_alleles == 'B' and c_alleles == 'O'):
        parent_alleles_option = ['O', 'B', 'A']
    elif (p1_alleles == 'B' and c_alleles == 'A'):
        parent_alleles_option = ['A', 'AB']
    elif (p1_alleles == 'B' and c_alleles == 'B'):
        parent_alleles_option = ['B', 'AB', 'O', 'A']
    elif (p1_alleles == 'A' and c_alleles == 'AB'):
        parent_alleles_option = ['B', 'AB']
    elif (p1_alleles == 'B' and c_alleles == 'AB'):
        parent_alleles_option = ['A', 'AB']
    elif (p1_alleles == 'AB' and c_alleles == 'AB'):
        parent_alleles_option = ['A', 'AB', 'B']
    elif (p1_alleles == 'AB' and c_alleles == 'B') or (p1_alleles == 'AB' and c_alleles == 'A'):
        parent_alleles_option = ['B', 'A', 'AB', 'O']
    

    for rhesus in parent_rhesus_options:
        for alleles in parent_alleles_option:
            parent_set.add(alleles + rhesus)

    return parent_set

# print(bloodgroup_child('O+', 'O-'))
# print(bloodgroup_child('AB-', 'AB+'))

print(bloodgroup_parent('O-', 'O-'))
print(bloodgroup_parent('AB+', 'O+'))

