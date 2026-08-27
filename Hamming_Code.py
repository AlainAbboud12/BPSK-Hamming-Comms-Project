
def hamming_encode(data_bits):
    
    
    P0=data_bits[0]^data_bits[2]^data_bits[3]
    P1=data_bits[0]^data_bits[1]^data_bits[3]
    P2=data_bits[0]^data_bits[1]^data_bits[2]
    seven_bit=data_bits[0:3]+[P2]+[data_bits[3]]+[P1]+[P0]

    return seven_bit

def hamming_decode(received_bits):
    n=len(received_bits)
    # takes 7 bits, checks/corrects, returns the original 4 data bits
    q=received_bits
    if (q[3]^q[0]^q[1]^q[2]==1):P4=1 
    else: P4=0
    if q[5]^q[0]^q[1]^q[4]==1:P2=1
    else: P2=0
    if q[6]^q[0]^q[2]^q[4]==1:P1=1 
    else: P1=0
    # print("P124: ",P4,P2,P1)
    
    if P4+P2+P1==0:return q[0:3]+[q[4]]
    else:
        k=str(P4)+str(P2)+str(P1)
        Sum=0
        for i in range(1,len(k)+1,1):
            
            Sum+=2**(len(k)-i)*int(k[i-1])
        # print(Sum)
        if q[n-Sum]==1:q[n-Sum]=0
        else: q[n-Sum]=1
        
        return q[0:3]+[q[4]]

# test it here, no modem/noise involved yet:
# test_data =[0, 0, 0, 1]
# print(test_data)
# encoded = hamming_encode(test_data)
# print(encoded)  # should be 7 bits4
# decoded = hamming_decode([0, 0, 1, 0, 1, 1, 0])
# print(decoded)  # should match test_data exactly      

 
# k=hamming_decode(hamming_encode([1, 0, 1, 1]))
# print("k: ", k)  # should match [1, 0, 1, 1] exactly