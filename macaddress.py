while 0==0: #loop program
    venlist = open("vendorlist.txt","r")#open the vendor list downloaded from wire shark(if you dont have it download it by searching mac address vendor click the shark link and then click the listed link 
    mac = input ("what is the mac beggining of the mac address? (00:00:00)") #where the beggining of the address will be input
    temp=1
    x=0
    while x==0:
        item = venlist.readline()#read the line(not print it)
        sitem = item.split()
        if inmacad in item: #check if it contains the macaddress (if not will then go onto next line)
            print(sitem[1])
            x=1

    venlist.close() #without it will start next search from previous line

