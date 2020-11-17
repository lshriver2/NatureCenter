import serial
import time
import MySQLdb as mdb
from tkinter import *
from time import sleep
import datetime as dt
import sys

root = Tk()

arduino = serial.Serial("/dev/ttyACM0")
arduino.baudrate=9600

ds1T =1
ds2T =2
ds3T =3
ds4T =4
ds5T =5
ds6T =6
ds7T =7
ds8T =8
dht1T =9
dht1H =10
WST =11
WSW =12

def getData():
    global ds1T
    global ds2T
    global ds3T
    global ds4T
    global dht1T
    global dht1H
    global WST
    global WSW
    global WSWr
    global ds5T
    global ds6T
    global ds7T
    global ds8T
    
    data = arduino.readline()
    pieces =data.split()
    
    ds1Tr = pieces[0]
    ds2Tr = pieces[1]
    ds3Tr = pieces[2]
    ds4Tr = pieces[3]
    dht1Tr = pieces[4]
    dht1Hr = pieces[5]
    WSTr = pieces[6]
    WSWr = pieces[7]

    ds5Tr = pieces[8]
    ds6Tr = pieces[9]
    ds7Tr = pieces[10]
    ds8Tr = pieces[11]

    # Covert to float ------------------------------------------
    ds1T = float(ds1Tr)
    ds2T = float(ds2Tr)
    ds3T = float(ds3Tr)
    ds4T = float(ds4Tr)
    dht1T = float(dht1Tr)
    dht1H = float(dht1Hr)
    WST = float(WSTr)
    
    #this section makes sure that WSW is converted to a float
    WSWa = str(WSWr)
    if WSWa == 'NaN' or WSWa == 'nan' or WSWa == "b'nan'" or WSWa == "b'NaN'":
        #print("if")
        WSW = float(0.0)
    else:
        #print("else")
        WSW = float(WSWr)

    ds5T = float(ds5Tr)
    ds6T = float(ds6Tr)
    ds7T = float(ds7Tr)
    ds8T = float(ds8Tr)
    '''
    #printData
    print(ds1T, 'TEMP ds1T LOCATION: East Gable Ext')
    print(ds2T, 'TEMP ds2T LOCATION: SE EveExt') 
    print(ds3T, 'TEMP ds3T LOCATION: West Gable In')
    print(ds4T, 'TEMP ds4T LOCATION: West Gable Ext')
    print("")
    print(ds5T, 'TEMP ds5T LOCATION: NW Eve Ext')
    print(ds6T, 'TEMP ds6T LOCATION: First Floor In')
    print(ds7T, 'TEMP ds7T LOCATION: Ciling In')
    print(ds8T, 'TEMP ds8T LOCATION: Under Roof')
    print("")
    print(dht1T, '(TEMP) dht1T LOCATION: AIR RETURN')
    print(dht1H, '(HUMIDITY) dht1T LOCATION: AIR RETURN')
    print("")
    print(WST, '(TEMP) Wind Sensor Rev. C LOCATION: AIR RETURN')
    print(WSW, '(WIND) Wind Sensor Rev. C LOCATION: AIR RETURN')
    '''

# Open function to open the file "MyFile1.txt"  
# (same directory) in append mode and 


'''
# store its reference in the variable file1  
# and "MyFile2.txt" in D:\Text in file2 
file1 = open("MyFile1.txt","w+") 
file1.close()
'''

def record():
    global worksheet
    '''
    telemetryPrint = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S')+'    '+pressure2+'    '+pressure1+'    '+altitude+'    '+temperature  
    '''
    telemetryPrint = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S') +'    '+ str(ds1T) +'    '+ str(ds2T) +'    '+ str(ds3T) +'    '+ str(ds4T) +'    '+ str(ds5T) +'    '+ str(ds6T) +'    '+ str(ds7T) +'    '+ str(ds8T) +'    '+ str(dht1T) +'    '+ str(dht1H) +'    '+ str(WST) +'    '+ str(WSW)     
    
    
    worksheet.append_row((dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S'), ds1T, ds2T, ds3T, ds4T, ds5T, ds6T, ds7T, ds8T, dht1T, dht1H, WST, WSW))    
    #worksheet.append_row((ds1T, ds2T, ds3T, ds4T, ds5T, ds6T, ds8T, ds7T, dht1T, dht1H, WST, WSW, 5))
    #worksheet.append_row((ds1T, ds2T, ds3T, WSW, ds4T, ds5T, 5, 5))
    
    print(telemetryPrint)
    #this is the Printer to the Text file______________
    file1 = open("MyFile.txt","a")
    file1.write(telemetryPrint +"\n")
    file1.close()

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


def calculations():
    
    #NOW/HOURLY VARIABLES AND CALCULATIONS
    #OUTDOOR
    nowTEMP =1
    nowHUMIDITY =1
    nowWIND =1
    nowRAIN =1
    nowSOLAR =1
    #INDOOR
    nowTEMP =1
    nowHUMIDITY =1
    nowENERGYUSE =1
    
    #DAY VARIABLES AND CALCULATIONS
    #OUTDOOR
    dayTEMP =1
    dayHUMIDITY =1
    dayWIND =1
    dayRAIN =1
    daySOLAR =1
    #INDOOR
    dayTEMP =1
    dayHUMIDITY =1
    dayENERGYUSE =1
    
    #WEEK VARIABLES AND CALCULATIONS
    #OUTDOOR
    dayTEMP =1
    dayHUMIDITY =1
    dayWIND =1
    dayRAIN =1
    daySOLAR =1
    #INDOOR
    dayTEMP =1
    dayHUMIDITY =1
    dayENERGYUSE =1

def runAll():
    getData()
    calculations()
    config()
    record()
    
    root.after(100, runAll)
    
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


# SOFTWARE.
import json
import sys
import time
import datetime
import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials

GDOCS_OAUTH_JSON       = 'google-auth.json'

# Google Docs spreadsheet name.
GDOCS_SPREADSHEET_NAME = 'Nature'

# How long to wait (in seconds) between measurements.
FREQUENCY_SECONDS      = 3

def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    
    except Exception as ex:
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)


print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')
worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
    
# Append the data in the spreadsheet, including a timestamp
#try:
#    worksheet.append_row((dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S'), ds1T, ds2T, ds3T))
        
'''    
    except:
        # Error appending data, most likely because credentials are stale.
        # Null out the worksheet so a login is performed at the top of the loop.
        print('Append error, logging in again')
        worksheet = None
        time.sleep(FREQUENCY_SECONDS)
        continue
'''
# Wait 30 seconds before continuing
print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
time.sleep(FREQUENCY_SECONDS)


runAll()



#root.after(100, remember)
mainloop()








