#python 3.5.2
#Variable byte encoding in 8 bits blocks. 
# i reverse the binary and i create blocks from the last one
# H.W.2 4 assigment Christos Forotzidis


while True:
    try:
        an_integer = int(input("Please enter an integer(>0) : "))
    except ValueError  :
        print("Sorry, this is not an integer .Try again")
        #better try again... Return to the start of the loop
        continue
    else:
        if an_integer >0:
            break
        else:
            print("Sorry, this is not an integer >0. Try again")


binary=format(an_integer,'b') #transform the int to binary

print("The binary format of the integer is:",binary)
reverse_binary="".join(reversed(binary)) #reversed the binary in order when i handle the binary from the reverse and to put it into the loop
#print(reverse_binary)

if(len(binary)<8):
    number_of_blocks=1 #if length of binary < 8 , then we need 1 block
else:
    number_of_blocks=len(binary)//7+1 #if length of binary > 8 , then we need (len mod 7)+1 block

print("Number of block(s) are(or is):",number_of_blocks,"\n")
counter_bit=0  #counting the bits
counter_bytes=1 #counting the bytes or blocks
result=""  #result of the encoding

for i in reverse_binary:# here i put one by one bits from the reverse binary
    #print(i)
    result=i+result
    counter_bit +=1
    if(counter_bit==7):# when i reach 7 items, i change blocks and i put the right semaphor
        if (counter_bytes == 1):
            result = "1"+result# when it is the last block i add 1 at the starting of the block
        else:
            result = "0"+result # when it is not the last block i add 0 until the starting of the block

        counter_bytes +=1 #increase the number of the block that the pointer is
        counter_bit=0 # make 0 the pointer of the inside of the block ,and start from scratch


if(counter_bit<7 and number_of_blocks==1): #here i fill the last block with 0 or 1 depending on how big is the integer
    while counter_bit < 7:
        result="0"+result
        counter_bit +=1
    if(counter_bit==7):
        result = "1"+result
elif(counter_bit < 7 and number_of_blocks>1):
    while counter_bit <8 :
        result="0"+result
        counter_bit +=1


print("variable byte encoding: ",result)