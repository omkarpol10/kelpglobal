Data = dict()
while True:
    action = input()
    #Break the code if user types "break".
    if action=="break":
        break
    else:
        InputData = []
        InputData = action.split()
        
        #to create account
        if InputData[0]=="CREATE":
            if InputData[1] in Data:
                print("Account already exist")
            else:
                Data[InputData[1]]=[InputData[2],0]
                
        #to deposit amount
        elif InputData[0]=="DEPOSIT":
            if InputData[1] in Data:
                (Data[InputData[1]][1])=(Data[InputData[1]][1])+int(InputData[2])
            else:
                print("Account Does not exist")
        
        #to withdraw amount
        elif InputData[0]=="WITHDRAW":
            if InputData[1] in Data:
                (Data[InputData[1]][1])=Data[InputData[1]][1]-int(InputData[2])
            else:
                print("Account Does not exist")
                
        #to view balance
        elif InputData[0]=="BALANCE":
            if InputData[1] in Data:
                print(Data[InputData[1]][0]+ " " +str(Data[InputData[1]][1]))
            else:
                print("Account Does not exist")

                
        
            
   
