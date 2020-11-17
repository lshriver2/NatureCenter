



def config():
    n1.config(text = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S'))
    n2.config(text = ds1T)
    n3.config(text = ds2T)
    n4.config(text = ds3T)
    n5.config(text = ds4T)
    n6.config(text = ds5T)
    n7.config(text = ds6T)
    n8.config(text = ds7T)
    n9.config(text = ds8T)
    n10.config(text = dht1T)
    n11.config(text = dht1H)
    '''n12.config(text = WST)
    n13.config(text = WSW)
    '''
    n0.grid(row=0, column=1)
    n1.grid(row=1, column=1) 
    n2.grid(row=2, column=1)
    n3.grid(row=3, column=1)
    n4.grid(row=4, column=1)
    n5.grid(row=5, column=1)
    n6.grid(row=6, column=1)
    n7.grid(row=7, column=1) 
    n8.grid(row=8, column=1)
    n9.grid(row=9, column=1)
    n10.grid(row=10, column=1)
    n11.grid(row=11, column=1)
    '''n12.grid(row=12, column=1)
    n13.grid(row=13, column=1)
    '''
    inD1.config(text = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S'))
    inD2.config(text = ds1T)
    inD3.config(text = ds2T)
    inD4.config(text = ds3T)
    inD5.config(text = ds4T)
    inD6.config(text = ds5T)
    inD7.config(text = ds6T)
    inD8.config(text = ds7T)
    inD9.config(text = ds8T)
    inD10.config(text = dht1T)
    inD11.config(text = dht1H)
    inD12.config(text = WST)
    inD13.config(text = WSW)
    
    inD1.grid(row=1, column=1) 
    inD2.grid(row=1, column=2)
    inD3.grid(row=1, column=3)
    inD4.grid(row=1, column=4)
    inD5.grid(row=1, column=5)
    inD6.grid(row=1, column=6)
    inD7.grid(row=1, column=7) 
    inD8.grid(row=1, column=8)
    inD9.grid(row=1, column=9)
    inD10.grid(row=1, column=10)
    inD11.grid(row=1, column=11)
    inD12.grid(row=1, column=12)
    inD13.grid(row=1, column=13)



# ------------------------------


def quit1():
    global file1
    
    try:
        file1.close()
    except:
        print("The File Was Already Closed, EXITING....")
        sys.exit()
    else:
        print("The File Is Closed, EXITING....")
        sys.exit()

width = 24
width2 = 15
height = 2
#font = 1
font = ("Courier", 12)

#Lframe = Frame(root)
#Lframe.pack(side = LEFT)
Rframe = Frame(root)
Rframe.pack()
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()

def interface():
    global w0
    global w1
    global w2
    global w3
    global w4
    global w5
    global w6 
    global w7
    global w8
    global w9
    global w10
    global w11
    global w12
    
    global n0
    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    global n7
    global n8
    global n9
    global n10
    global n11
    global n12
    global n13

    global t0 
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6 
    global t7
    global t8
    global t9
    global t10
    global t11
    global t12
    
    global inD0
    global inD1 
    global inD2
    global inD3
    global inD4
    global inD5
    global inD6
    global inD7 
    global inD8
    global inD9
    global inD10
    global inD11
    global inD12
    global inD13

    t1 = Label(Rframe, text = 'TIME STAMP', bg="tan", fg="black", width = width2, height = height, font = font)
    t2 = Label(Rframe, text = 'OUTDOOR', bg="white", fg="black", width = width2, height = height, font = font)
    t3 = Label(Rframe, text = 'TEMP', bg="tan", fg="black", width = width2, height = height, font = font)
    t4 = Label(Rframe, text = 'HUMIDITY', bg="white", fg="black", width = width2, height = height, font = font)
    t5 = Label(Rframe, text = 'WIND', bg="tan", fg="black", width = width2, height = height, font = font)
    t6 = Label(Rframe, text = 'RAIN', bg="white", fg="black", width = width2, height = height, font = font)
    t7 = Label(Rframe, text = 'SOLAR', bg="tan", fg="black", width = width2, height = height, font = font)
    t8 = Label(Rframe, text = 'INDOOR', bg="white", fg="black", width = width2, height = height, font = font)
    t9 = Label(Rframe, text = 'TEMP', bg="tan", fg="black", width = width2, height = height, font = font)
    t10 = Label(Rframe, text = 'HUMIDITY', bg="white", fg="black", width = width2, height = height, font = font)
    t11 = Label(Rframe, text = 'ENERGY USE', bg="tan", fg="black", width = width2, height = height, font = font)
    '''
    t10 = Label(Rframe, text = '1', bg="white", fg="black", width = width2, height = height, font = font)
    t11 = Label(Rframe, text = '1', bg="tan", fg="black", width = width2, height = height, font = font)
    t12 = Label(Rframe, text = '1', bg="white", fg="black", width = width2, height = height, font = font)
    '''
    n0 = Label(Rframe, text = 'NOW:', bg="tan", fg="black", width = width, height = height, font = font)
    n1 = Label(Rframe, text = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S'), bg="white", fg="black", width = width, height = height, font = font)
    n2 = Label(Rframe, text = ds1T, bg="tan", fg="black", width = width, height = height, font = font)
    n3 = Label(Rframe, text = ds2T, bg="white", fg="black", width = width, height = height, font = font)
    n4 = Label(Rframe, text = ds3T, bg="tan", fg="black", width = width, height = height, font = font)
    n5 = Label(Rframe, text = ds4T, bg="white", fg="black", width = width, height = height, font = font)
    n6 = Label(Rframe, text = ds5T, bg="tan", fg="black", width = width, height = height, font = font)
    n7 = Label(Rframe, text = ds6T, bg="white", fg="black", width = width, height = height, font = font)
    n8 = Label(Rframe, text = ds7T, bg="tan", fg="black", width = width, height = height, font = font)
    n9 = Label(Rframe, text = ds8T, bg="white", fg="black", width = width, height = height, font = font)
    n10 = Label(Rframe, text = dht1T, bg="tan", fg="black", width = width, height = height, font = font)
    n11 = Label(Rframe, text = dht1H, bg="white", fg="black", width = width, height = height, font = font)
    n12 = Label(Rframe, text = WST, bg="tan", fg="black", width = width, height = height, font = font)
    n13 = Label(Rframe, text = WSW, bg="white", fg="black", width = width, height = height, font = font)
    
    d0 = Label(Rframe, text = 'DAY:', bg="tan", fg="black", width = width, height = height, font = font)
    d1 = Label(Rframe, text = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S'), bg="white", fg="black", width = width, height = height, font = font)
    d2 = Label(Rframe, text = ds1T, bg="tan", fg="black", width = width, height = height, font = font)
    d3 = Label(Rframe, text = ds2T, bg="white", fg="black", width = width, height = height, font = font)
    d4 = Label(Rframe, text = ds3T, bg="tan", fg="black", width = width, height = height, font = font)
    d5 = Label(Rframe, text = ds4T, bg="white", fg="black", width = width, height = height, font = font)
    d6 = Label(Rframe, text = ds5T, bg="tan", fg="black", width = width, height = height, font = font)
    d7 = Label(Rframe, text = ds6T, bg="white", fg="black", width = width, height = height, font = font)
    d8 = Label(Rframe, text = ds7T, bg="tan", fg="black", width = width, height = height, font = font)
    d9 = Label(Rframe, text = ds8T, bg="white", fg="black", width = width, height = height, font = font)
    d10 = Label(Rframe, text = dht1T, bg="tan", fg="black", width = width, height = height, font = font)
    d11 = Label(Rframe, text = dht1H, bg="white", fg="black", width = width, height = height, font = font)
    '''d12 = Label(Rframe, text = WST, bg="tan", fg="black", width = width, height = height, font = font)
    d13 = Label(Rframe, text = WSW, bg="white", fg="black", width = width, height = height, font = font)
    '''
    w0 = Label(Rframe, text = 'WEEK:', bg="tan", fg="black", width = width, height = height, font = font)    
    w1 = Label(Rframe, text = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S'), bg="white", fg="black", width = width, height = height, font = font)
    w2 = Label(Rframe, text = ds1T, bg="tan", fg="black", width = width, height = height, font = font)
    w3 = Label(Rframe, text = ds2T, bg="white", fg="black", width = width, height = height, font = font)
    w4 = Label(Rframe, text = ds3T, bg="tan", fg="black", width = width, height = height, font = font)
    w5 = Label(Rframe, text = ds4T, bg="white", fg="black", width = width, height = height, font = font)
    w6 = Label(Rframe, text = ds5T, bg="tan", fg="black", width = width, height = height, font = font)
    w7 = Label(Rframe, text = ds6T, bg="white", fg="black", width = width, height = height, font = font)
    w8 = Label(Rframe, text = ds7T, bg="tan", fg="black", width = width, height = height, font = font)
    w9 = Label(Rframe, text = ds8T, bg="white", fg="black", width = width, height = height, font = font)
    w10 = Label(Rframe, text = dht1T, bg="tan", fg="black", width = width, height = height, font = font)
    w11 = Label(Rframe, text = dht1H, bg="white", fg="black", width = width, height = height, font = font)
    '''w12 = Label(Rframe, text = WST, bg="tan", fg="black", width = width, height = height, font = font)
    w13 = Label(Rframe, text = WSW, bg="white", fg="black", width = width, height = height, font = font)
    '''
    #t0.grid(row=0, column=0)
    t1.grid(row=1, column=0) 
    t2.grid(row=2, column=0)
    t3.grid(row=3, column=0)
    t4.grid(row=4, column=0)
    t5.grid(row=5, column=0)
    t6.grid(row=6, column=0)
    t7.grid(row=7, column=0) 
    t8.grid(row=8, column=0)
    t9.grid(row=9, column=0)
    t10.grid(row=10, column=0)
    t11.grid(row=11, column=0)
    '''
    t11.grid(row=12, column=0)
    t12.grid(row=13, column=0)'''
    
    n0.grid(row=0, column=1)
    n1.grid(row=1, column=1) 
    n2.grid(row=2, column=1)
    n3.grid(row=3, column=1)
    n4.grid(row=4, column=1)
    n5.grid(row=5, column=1)
    n6.grid(row=6, column=1)
    n7.grid(row=7, column=1) 
    n8.grid(row=8, column=1)
    n9.grid(row=9, column=1)
    n10.grid(row=10, column=1)
    n11.grid(row=11, column=1)
    '''n12.grid(row=12, column=1)
    n13.grid(row=13, column=1)
    '''
    d0.grid(row=0, column=2)
    d1.grid(row=1, column=2) 
    d2.grid(row=2, column=2)
    d3.grid(row=3, column=2)
    d4.grid(row=4, column=2)
    d5.grid(row=5, column=2)
    d6.grid(row=6, column=2)
    d7.grid(row=7, column=2) 
    d8.grid(row=8, column=2)
    d9.grid(row=9, column=2)
    d10.grid(row=10, column=2)
    d11.grid(row=11, column=2)
    '''d12.grid(row=12, column=2)
    d13.grid(row=13, column=2)
    '''
    w0.grid(row=0, column=3)
    w1.grid(row=1, column=3) 
    w2.grid(row=2, column=3)
    w3.grid(row=3, column=3)
    w4.grid(row=4, column=3)
    w5.grid(row=5, column=3)
    w6.grid(row=6, column=3)
    w7.grid(row=7, column=3) 
    w8.grid(row=8, column=3)
    w9.grid(row=9, column=3)
    w10.grid(row=10, column=3)
    w11.grid(row=11, column=3)
    '''w12.grid(row=12, column=3)
    w13.grid(row=13, column=3)
    '''
    width4 = 6
    #n0 = Label(Rframe, text = 'NOW:', bg="tan", fg="black", width = width, height = height, font = font)
    inD1 = Label(frame2, text = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S'), bg="white", fg="black", width = width4, height = height, font = font)
    inD2 = Label(frame2, text = ds1T, bg="tan", fg="black", width = width4, height = height, font = font)
    inD3 = Label(frame2, text = ds2T, bg="white", fg="black", width = width4, height = height, font = font)
    inD4 = Label(frame2, text = ds3T, bg="tan", fg="black", width = width4, height = height, font = font)
    inD5 = Label(frame2, text = ds4T, bg="white", fg="black", width = width4, height = height, font = font)
    inD6 = Label(frame2, text = ds5T, bg="tan", fg="black", width = width4, height = height, font = font)
    inD7 = Label(frame2, text = ds6T, bg="white", fg="black", width = width4, height = height, font = font)
    inD8 = Label(frame2, text = ds7T, bg="tan", fg="black", width = width4, height = height, font = font)
    inD9 = Label(frame2, text = ds8T, bg="white", fg="black", width = width4, height = height, font = font)
    inD10 = Label(frame2, text = dht1T, bg="tan", fg="black", width = width4, height = height, font = font)
    inD11 = Label(frame2, text = dht1H, bg="white", fg="black", width = width4, height = height, font = font)
    inD12 = Label(frame2, text = WST, bg="tan", fg="black", width = width4, height = height, font = font)
    inD13 = Label(frame2, text = WSW, bg="white", fg="black", width = width4, height = height, font = font)
    
    #inD0.grid(row=1, column=0)
    inD1.grid(row=1, column=1) 
    inD2.grid(row=1, column=2)
    inD3.grid(row=1, column=3)
    inD4.grid(row=1, column=4)
    inD5.grid(row=1, column=5)
    inD6.grid(row=1, column=6)
    inD7.grid(row=1, column=7) 
    inD8.grid(row=1, column=8)
    inD9.grid(row=1, column=9)
    inD10.grid(row=1, column=10)
    inD11.grid(row=1, column=11)
    inD12.grid(row=1, column=12)
    inD13.grid(row=1, column=13)

interface()

'''
frame1 = Frame(root)
frame1.pack()
'''
buttonQ = Button(root, text = 'Quit', command = quit1, width = width2, font = ("Courier", 16))
buttonQ.pack()
