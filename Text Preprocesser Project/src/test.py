# f = open("/Users/guraybaydur/Desktop/BOUN/561 NLP/42bin_haber_mansur/news/dunya/test.txt", "r")
#f = open("/Users/guraybaydur/Desktop/BOUN/561 NLP/42bin_haber_mansur/news/dunya/1239.txt", "r")
# f = open("/Users/guraybaydur/Desktop/BOUN/561 NLP/42bin_haber_mansur/news/dunya/2900.txt", "r")
f = open("/Users/guraybaydur/Desktop/BOUN/561 NLP/42bin_haber_mansur/news/magazin/1468.txt", "r")
sentence = f.read()
print("ORIGINAL sentence: " + sentence)

# tuple_list = [(0, 13), (14, 101), (137, 155), (170, 191), (198, 198),(200, 211), (324, 324), (384, 384), (481, 481), (530, 530), (539, 539), (635, 635), (726, 726),(790, 790)]
# tuple_list = [(73, 73), (128, 128), (131, 131), (194, 194), (245, 245), (285, 285), (301, 301), (326, 326), (335, 335), (424, 424), (530, 530), (586, 586), (595, 595), (632, 632), (678, 678), (746, 746), (767, 767), (770, 770), (809, 809), (864, 864), (905, 905), (940, 940), (972, 972), (1012, 1012), (1067, 1067), (1088, 1088), (1156, 1156), (1196, 1196), (1235, 1235), (1276, 1276), (1283, 1283), (1286, 1298), (1329, 1329), (1401, 1401), (1436, 1436), (1484, 1484), (1543, 1543), (1666, 1666), (1695, 1695), (1767, 1767), (1824, 1824), (1844, 1844)]
# tuple_list = [(51, 51), (132, 132), (220, 220), (229, 229), (238, 238), (261, 261), (286, 286), (373, 373), (514, 514),
#               (599, 599), (683, 683), (690, 690), (714, 714), (810, 810), (868, 868), (978, 978), (1133, 1133),
#               (1198, 1198), (1206, 1206), (1303, 1303), (1315, 1315), (1342, 1342), (1354, 1354), (1368, 1368),
#               (1381, 1381), (1479, 1479), (1585, 1585), (1616, 1616), (1707, 1707), (1743, 1743), (1758, 1758),
#               (1878, 1878), (1880, 1880), (1961, 1961), (2047, 2047), (2083, 2083), (2135, 2135), (2182, 2194),
#               (2264, 2264), (2319, 2319), (2366, 2385), (2411, 2411)]
tuple_list = [(11, 11), (165, 165), (192, 192), (199, 199), (290, 290), (353, 353), (363, 363), (411, 411), (518, 518), (649, 649), (870, 870), (934, 934), (988, 988), (1002, 1002), (1088, 1088), (1112, 1112), (1135, 1135), (1144, 1144), (1188, 1188), (1233, 1233), (1288, 1288), (1339, 1339), (1390, 1390), (1440, 1440), (1489, 1489), (1535, 1535), (1545, 1553), (1586, 1586), (1642, 1642), (1687, 1687), (1724, 1724), (1726, 1750)]

tuple_list_index = 0
result = ""
char_index = 0

while char_index != len(sentence):
    if tuple_list_index < len(tuple_list):
        while char_index < tuple_list[tuple_list_index][0]:
            print("tuple_list[tuple_list_index][0]" + str(tuple_list[tuple_list_index][0]))
            print("char_index: " + str(char_index) + "\n")
            result += sentence[char_index]
            print("Current Result: " + result)
            print(tuple_list[tuple_list_index][1])
            print("sentence[1724]: " + sentence[1724])
            print("sentence[1726:1750]: " + sentence[1726:1750])
            (1724, 1724), (1726, 1750)
            # print("sentence[687:694]: " + sentence[687:694])
            # print("sentence[653:694]: " + sentence[653:694])
            # print("sentence[694]: " + sentence[694])
            char_index += 1
        result += " "
        while char_index < tuple_list[tuple_list_index][1]:
            print("tuple_list[tuple_list_index][1]" + str(tuple_list[tuple_list_index][1]))
            print("char_index: " + str(char_index) + "\n")
            print("sentence[1747]: " + sentence[1747])
            result += sentence[char_index]
            char_index += 1
        if char_index < len(sentence):
            result = result + sentence[char_index] + " "
            tuple_list_index += 1
            char_index += 1
    else:
        result += sentence[char_index]
        char_index += 1


print("RESULTING sentence: " + str(result.split()))
#print(sentence[1])