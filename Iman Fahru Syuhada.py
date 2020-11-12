# NO 1 #
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbol = ['˜','!','#','$','%','ˆ','&','*','(',')','_','+','{','}','|','"',':','>','<','?']
numbers = ['0','1','2','3','4','5','6','7','8','9']
minus_num = ['0','-1','-2','-3','-4','-5','-6','-7','-8','-9']


def create_phone_number(num):
    num = (input('Input your phone number:'))
    if alphabet in num is True:
        return ('Invalid input. No alphabet.')
    elif symbol in num is True:
        return('Invalid input. No symbols.')
    elif len(num) != 10 is True:
        return('Digits must be in length of 10, not more or less')
    elif minus_num in num is True:
        return('Input only positve numbers')
    else:
        return('Your phone number is', str(num))

# NO 2 #
def move_zeros(list, word, z):
   split = list.split()
   split.insert(z, split.pop(split.index(word)))
   return ' '.join(split)

list = 'cek 1 2 3 4 2 0 1 2 0 2 3 '
print(move_zeros(list, '0', 100)) # index ke-100 utk taruh di paling belakang 

#Pak saya hanya bisa buat satu 0 ke belakang tapi tidak semua 0 #


# No 3 #

#Mean #
num_list1 = [12, 10, 10, 10, 10]
num_sum1 = sum(num_list1)
mean = num_sum1 / len(num_list1)
print(num_list1)
print("st.mean  " + str(round(mean,2)))

# # Median # 
num_list2 = [12, 10, 10, 10, 10]
num_list2.sort()
if len(num_list2) % 2 == 0:
   first_median = num_list2[len(num_list2) // 2]
   second_median = num_list2[len(num_list2) // 2 - 1]
   median = (first_median + second_median) / 2
else:
   median = num_list2[len(num_list2) // 2]
print(num_list2)
print("st.median " + str(median))

# # Mode #


# num_list = [21, 13, 19, 13,19,13]
# print(num_list)

# data = collections.Counter(num_list)
# data_list = dict(data)

# print(data_list)

# max_value = max(list(data.values()))
# mode_val = [num for num, freq in data_list.items() if freq == max_value]
# if len(mode_val) == len(num_list):
#    print("No mode in the list")
# else:
#    print("The Mode of the list is : " + ', '.join(map(str, mode_val)))



#STD #
   
import math 

def mean(values):

    return sum(values)/len(values)
    
def stanDev(values):

    length = len(values)

    m = mean(values)

    total_sum = 0

    for i in range(length): 

        total_sum += (values[i]-m)**2

    return math.sqrt(total_sum/length)

x = [10, 10, 10, 10, 12]

stan_dev = stanDev(x)

print("st.std", stan_dev)