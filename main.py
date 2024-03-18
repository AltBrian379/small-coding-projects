
def triangle_func(x):
    return (x * (x+1))/2


file1 = open("coding_qual_input.txt","r")

word_list = []

while True:
    line = file1.readline()
    temp_array = line.split()
    if (line):
        temp_num = temp_array[0]
        temp_array[0] = int(temp_num)
        word_list.append(temp_array)
    else:
        break
file1.close()

valid_word_list = []

for i in word_list:
    n = 1
    j = 0
    while j <= i[0]:
        j = triangle_func(n)
        n += 1
        if j == i[0]:
            valid_word_list.append(i)

print(sorted(valid_word_list, key=lambda x: x[0]))

        

