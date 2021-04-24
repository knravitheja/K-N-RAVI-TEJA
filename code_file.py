#open input file to read input
input_file =open("C:\\Users\\knrav\\OneDrive\\Desktop\\sample_input.txt","r")
#open output file to write output
output_file = open("C:\\Users\\knrav\\OneDrive\\Desktop\\sample_output.txt","w+")
goodies={}
output_list=[]
#reading input file into the dict
for f in input_file:
    index_toRead_price=f.index(":")
    print(f[index_toRead_price+1:].strip())
    print(f[:index_toRead_price])
    goodies[f[:index_toRead_price]]=f[index_toRead_price+1:].strip()
    #print(goodies)
print(goodies)
#list of price from dict
prices_only=list(goodies.values())


prices_only=[int(i)for i in prices_only]
#sort list in decsending order to get prices to be distributed d in order
prices_only.sort(reverse=True)
print(prices_only)
#taking inputs
number_of_employees=int(input("Enter number of employees:"))

length_considered=(len(prices_only)-number_of_employees)

print(length_considered)

#finding minium difference between highest and lowest
for i in range(length_considered):
    maxprice=prices_only[i]
    minprice=prices_only[number_of_employees+i]
    if i == 0:
        difference=maxprice-minprice
        choosen_index=i
    elif(maxprice-minprice)<difference:
        difference=maxprice-minprice
        choosen_index=i



choosen_prices=prices_only[choosen_index:number_of_employees+choosen_index]
#difference between high price and low price
difference=max(choosen_prices)-min(choosen_prices)
print("difference",difference)

count=0
for key,value in goodies.items():
    prices_only[count]
    print(value)
    if int(value)in choosen_prices and count<number_of_employees:
        strl=key+": "+value
        #preparing to output file
        output_list.append(strl)
        count+=1
        print(strl)
#writing to output file
output_file.write("The goodies selected for distribution are: ")

output_file.write("\n")

for i in output_list:
    output_file.write(i)
    output_file.write("\n")
output_file.write("And the difference between the choosen goodie with highest price and the lowest price is"+str(difference))

input_file.close()
output_file.close()
