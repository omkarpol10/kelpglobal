Data = dict()
while True:
    action = input()
    #Break the code if user types "break".
    if action=="break":
        break
    else:
        input_data = []
        input_data = action.split()
        
        #to create account
        if input_data[0]=="CREATE":
            if input_data[1] in Data:
                print("Account already exist")
            else:
                Data[input_data[1]]=[input_data[2],0]
                
        #to deposit amount
        elif input_data[0]=="DEPOSIT":
            if input_data[1] in Data:
                (Data[input_data[1]][1])=(Data[input_data[1]][1])+int(input_data[2])
            else:
                print("Account Does not exist")
        
        #to withdraw amount
        elif input_data[0]=="WITHDRAW":
            if input_data[1] in Data:
                (Data[input_data[1]][1])=Data[input_data[1]][1]-int(input_data[2])
            else:
                print("Account Does not exist")
                
        #to view balance
        elif input_data[0]=="BALANCE":
            if input_data[1] in Data:
                print(Data[input_data[1]][0]+ " " +str(Data[input_data[1]][1]))
            else:
                print("Account Does not exist")

                
        
            
   
