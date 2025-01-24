import pandas
kasittelymode='k'
print("Welcome to the data editing and reading software")
print("Which of the following you would like to do?")
while(kasittelymode!='1' and kasittelymode!='2'):
    print("1: Make a new dataset")
    print("2: Read and edit already existing dataset")
    kasittelymode=input("Answer: ")
    if(kasittelymode!='1' and kasittelymode!='2'):
        print("Your input did not match given options")
        print("1: Make a new dataset")
        print("2: Read already existing dataset")
        kasittelymode=input("Answer: ")
if(kasittelymode=='1'):
    avaimet=[]
    dtset={}
    a=0
    a=int(a)
    print("Give names for 4 columns to dataset")
    while(a<4):
        b=input("Give columns names")
        avaimet.append(b)
        a=a+1
    md='y'
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    while(md!='n'):
        columnNumb=1
        print("give data to your dataset")
        while(columnNumb==1):
            a1a=input(avaimet[0]+"= ")
            a1.append(a1a)
            nextCol=input("Do you want to give more data to this column(y/n) ?")
            if(nextCol=='y'):
                columnNumb=columnNumb+0
            if(nextCol=='n'):
                columnNumb=columnNumb+1    
        while(columnNumb==2):
            a2a=input(avaimet[1]+"= ")
            a2.append(a2a)
            nextCol=input("Do you want to give more data to this column(y/n) ?")
            if(nextCol=='y'):
                columnNumb=columnNumb+0
            if(nextCol=='n'):
                columnNumb=columnNumb+1
        while(columnNumb==3):
            a3a=input(avaimet[2]+"= ")
            a3.append(a3a)
            nextCol=input("Do you want to give more data to this column(y/n) ?")
            if(nextCol=='y'):
                columnNumb=columnNumb+0
            if(nextCol=='n'):
                columnNumb=columnNumb+1
        while(columnNumb==4):
            a4a=input(avaimet[3]+"= ")
            a4.append(a4a)
            nextCol=input("Do you want to give more data to this column(y/n) ?")
            if(nextCol=='y'):
                columnNumb=columnNumb+0
            if(nextCol=='n'):
                columnNumb=columnNumb+1
                md='n'
    dtset[avaimet[0]]=a1
    dtset[avaimet[1]]=a2
    dtset[avaimet[2]]=a3
    dtset[avaimet[3]]=a4
    df=pandas.DataFrame(dtset)
    print("Here is your data: ")
    print(df)
    save=input("Do you want to save the dataset(y/n)?")
    if(save=='y'):
        tyyppi=input("do you want to save file ar json(1), csv(2) or excel(3) ?: ")
        if(tyyppi=='2'):
            Filename=input("Given either name of the file or path where you'll save the file+name of the file. Use .csv as type of the file.")
            df.to_csv(Filename)
        if(tyyppi=='1'):
            Filename=input("Given either name of the file or path where you'll save the file+name of the file. Use .json as type of the file.")
            df.to_json(Filename)
        if(tyyppi=='3'):
            Filename=input("Given either name of the file or path where you'll save the file+name of the file. Use .json as type of the file.")
            df.to_excel(Filename)    
        print("file saved")
    else:    
        print("")

if(kasittelymode=='2'):
    AlReadName=''
    dtype=''
    dtype=input("Is your file json(1), csv(2) or excel(3)?: ")
    print("Give the path to datafile or if the datafile is on the same folder as the program just give the name of the file, also give the filetype with the name(example test.csv)")
    AlReadName=input("Give the name of the datafile: ")
    if(dtype=='1'):
        df=pandas.read_json(AlReadName)
        print(df.to_string())
    if(dtype=='2'):
        df=pandas.read_csv(AlReadName)
        print(df.to_string())
    if(dtype=='3'):
        df=pandas.read_excel(AlReadName)
        print(df.to_string())            

    jatko=input("Do you want to edit the file (y/n)?")
    if(jatko=='y'):
        editmode=input("Do you want to replace value(1) or delete row(2)")
        if(editmode=='1'):
            row=input("In what row is the value you would like to replace? ")
            row=int(row)
            column=input("In what column is the value you want to replace? ")
            newvalue=input("What is the new value you want to input? ")
            df.loc[row, column]=newvalue
            print(df.to_string())
            if(dtype=='1'):
                df.to_json(AlReadName)
            if(dtype=='2'):
                df.to_csv(AlReadName)    
            if(dtype=='3'):
                df.to_excel(AlReadName)        

        if(editmode=='2'):
            rrow=input("Give the row you want to remove")
            rrow=int(rrow)
            updatedf=df.drop(rrow)
            print(updatedf)
            if(dtype=='1'):
                updatedf.to_json(AlReadName)
            if(dtype=='2'):
                updatedf.to_csv(AlReadName)
            if(dtype=='3'):
                updatedf.to_excel(AlReadName)        
    if(jatko=='n'):
        print("")        
        
