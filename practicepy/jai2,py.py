# text=(input("enter the sentece to slice : ").lower())
# result=[x for x in text]
# count=[x for x in range(0,len(result)) if result[x]=='a']
# s1=[]
# for i in range(count[0],(count[(len(count)-1)]+1)):
#     s1.append(result[i])
# s="".join(s1)
# print()
# print("\tEntered String : ",text,"\n")
# print("\tsliced string [a-a] : ",s)
# print()

def letter(input_string,char):
    first_index = input_string.find(char)
    if first_index != -1 :
        last_index = input_string.rfind(char)
        if last_index != first_index :
            return input_string[first_index + 1 : last_index]
        else :
            print(f"there is only one {char}")
    else :
        print(f"there is no {char}")

input_string = input("Enter your sentences : ")
input_char = input("Enter Character : ")
result = letter(input_string,input_char)
print(result)