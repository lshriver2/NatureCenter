import serial
import time
import MySQLdb as mdb
from tkinter import *
from time import sleep
import datetime as dt
import sys

import json


import datetime
#import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials
'''
root = Tk()
'''
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

ds9T =13

hvacVolt =14
hvacAmp = 15


exceptruns = 0


def getData():
    global exceptruns
    global ds1T
    global ds2T
    global ds3T
    global ds4T
    global dht1T
    global dht1H
    global WST
    global WSW
    global ds5T
    global ds6T
    global ds7T
    global ds8T
    global ds9T
    global hvacAmp
    global hvacVolt
    global time1
    
    WST =12
    WSWoriginal=12
    WSWstr=12
    
    ## Get data from Arduino via serial and Covert to float --------------
    data = arduino.readline()
    pieces =data.split()
    '''
    28FF5F5D7215011A ds1 Main floor temp

    28E9B507B6013C0E ds2   white/ brown HVAC input or HVAC return
    287D4007B6013C17 ds3   white/ green HVAC input or HVAC return

    281CF607B6013C30 ds4   Ceiling thermal sensor
    28FFEE61721501C2 ds5   under roof

    28FF18DF7215017C ds6 // SE EveExt
    28FF296272150139 ds7 // East Gable Ext

    28FFBDF763150110 ds8 // NW Eve Ext
    28FF93525415037A ds9 // West Gable Ext
        
    '''
    try:
        ## DHT Temp and Humodity
        dht1T = float(pieces[0])
        dht1H = float(pieces[1])
        
        ## Wind Sensor Temp and Wind
        WST = float(pieces[2])
        ## Needs both for if checker
        #WSWoriginal = pieces[3]
        #WSWstr = str(pieces[3])
        WSW = float(pieces[3])
        
        ds1T = float(pieces[4])
        ds2T = float(pieces[5])
        ds3T = float(pieces[6])
        ds4T = float(pieces[7])
        ds5T = float(pieces[8])
        ds6T = float(pieces[9])
        ds7T = float(pieces[10])
        ds8T = float(pieces[11])
        ds9T = float(pieces[12])
        
        ## Vots and Amps from HVAC system
        hvacVolt = float(pieces[13])
        hvacAmp = float(pieces[14])
        
        ## flow sensor
        freq = float(pieces[15])
        pulses = float(pieces[16])
        leters = float(pieces[17])
    
    except:
        exceptruns += 1
        print('exceptruns = ', exceptruns, '---------------------------------')
        getData()
    
    ## this section makes sure that WSW is converted to a float
    #WSWa = str(WSWr)
    '''if WSWstr == 'NaN' or WSWstr == 'nan' or WSWstr == "b'nan'" or WSWstr == "b'NaN'":
        #print("if")
        WSW = float(0)
    else:
        #print("else")
        WSW = float(WSWoriginal)
    '''
    time1 = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    
    '''
    
    print(dht1T, '(TEMP) dht1T LOCATION: AIR RETURN')
    print(dht1H, '(HUMIDITY) dht1T LOCATION: AIR RETURN')
    
    print(WST, '(TEMP) Wind Sensor Rev. C LOCATION: AIR RETURN')
    print(WSW, '(WIND) Wind Sensor Rev. C LOCATION: AIR RETURN')
    
    print(ds1T, 'TEMP ds1T LOCATION: East Gable Ext')
    print(ds2T, 'TEMP ds2T LOCATION: SE EveExt') 
    print(ds3T, 'TEMP ds3T LOCATION: Under Roof')
    print(ds4T, 'TEMP ds4T LOCATION: West Gable Ext')
    print("")
    print(ds5T, 'TEMP ds5T LOCATION: NW Eve Ext')
    print(ds6T, 'TEMP ds6T LOCATION: First Floor In')
    print(ds7T, 'TEMP ds7T LOCATION: Ceiling In')
    ---DNE-----------------------print(ds8T, 'TEMP ds8T LOCATION: ')
    ds8 HVAC input ---------------------
    ds9 HVAC return --------------------
    
    amp -----------------
    volts ---------------
    
    '''

def calculations():
    ## runs the calculations for the GUI chart and documentation
    global nTempOut
    global nHumidityOut
    global nWind
    global nRain
    global nSolar
    global nTempIn
    global nHumidityIn
    global nEnergyUse
    
    global dTempOut
    global dHumidityOut
    global dWind
    global dRain
    global dSolar
    global dTempIn
    global dHumidityIn
    global dEnergyUse
    
    global wTempOut
    global wHumidityOut
    global wWind
    global wRain
    global wSolar
    global wTempIn
    global wHumidityIn
    global wEnergyUse
    
    ## NOW/HOURLY VARIABLES AND CALCULATIONS
    ## OUTDOOR
    nTempOut = round(((1)/4), 2)
    nHumidityOut =1
    nWind =1
    nRain =1
    nSolar =1
    ## INDOOR
    nTempIn = round(((1)/2), 2)
    nHumidityIn = dht1H
    nEnergyUse = hvacVolt * hvacAmp
    
    ## DAY VARIABLES AND CALCULATIONS
    ## OUTDOOR
    dTempOut = round(((1)/4), 2)
    dHumidityOut =1
    dWind =1
    dRain =1
    dSolar =1
    ## INDOOR
    dTempIn = round(((1)/2), 2)
    dHumidityIn = dht1H
    dEnergyUse = hvacVolt * hvacAmp
    
    ## WEEK VARIABLES AND CALCULATIONS
    ## OUTDOOR
    wTempOut = round(((1)/4), 2)
    wHumidityOut =1
    wWind =1
    wRain =1
    wSolar =1
    ## INDOOR
    wTempIn = round(((1)/2), 2)
    wHumidityIn = dht1H
    wEnergyUse = hvacVolt * hvacAmp
    
    
'''
def yesterdayAverage():
    
    for i in range(x):
        x+=1
'''



def record():
    global worksheet
    '''
    telemetryPrint = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S')+'    '+pressure2+'    '+pressure1+'    '+altitude+'    '+temperature  
    '''
    #telemetryPrint = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S') +'    '+ str(ds1T) +'    '+ str(ds2T) +'    '+ str(ds3T) +'    '+ str(ds4T) +'    '+ str(ds5T) +'    '+ str(ds6T) +'    '+ str(ds7T) +'    '+ str(ds8T) +'    '+ str(ds9T) +'    '+ str(dht1T) +'    '+ str(dht1H) +'    '+ str(WST) +'    '+ str(WSW) +'    '+ str(hvacVolt) +'    '+ str(hvacAmp)   
    ## -- Print strings of data in shell --
    telemetryPrint = str(time1) +'    '+ str(ds1T) +'    '+ str(ds2T) +'    '+ str(ds3T) +'    '+ str(ds4T) +'    '+ str(ds5T) +'    '+ str(ds6T) +'    '+ str(ds7T) +'    '+ str(ds8T) +'    '+ str(ds9T) +'    '+ str(dht1T) +'    '+ str(dht1H) +'    '+ str(WST) +'    '+ str(WSW) +'    '+ str(hvacVolt) +'    '+ str(hvacAmp)   
    
    #time1 = dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S') --- or --- dt.datetime.now().strftime('%m-%d-%Y'), dt.datetime.now().strftime('%H:%M:%S')
    ##-----appends row with variables----
    #worksheet.append_row((time1, ds1T, ds2T, ds3T, ds4T, ds5T, ds6T, ds7T, ds8T, ds9T, dht1T, dht1H, WST, WSW, hvacAmp, hvacVolt))    
    
    #''
    ## -- Adds row to top of google sheets --
    worksheet.insert_row((time1, ds1T, ds2T, ds3T, ds4T, ds5T, ds6T, ds7T, ds8T, ds9T, dht1T, dht1H, WST, WSW, hvacAmp, hvacVolt))    
    #''
    
    ## prints for troubleshooting
    print(telemetryPrint)
    
    ## this is the Printer to the Text file______________
    file1 = open("MyFile.txt","a")
    file1.write(telemetryPrint +"\n")
    file1.close()

'''
def config(): ------------------------------------
'''
'''    
#establish some variables to use in GUI and pack frames
width = 15
width2 = 20
height = 1
#font = 1
font = ("Courier", 15)

#Lframe = Frame(root)
#Lframe.pack(side = LEFT)
Rframe = Frame(root)
Rframe.pack()
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()
'''
'''def interface():'''

'''    
for i in range(1):
    getData()
    calculations()
'''

    
def quit1():
    ## quit1() alows program to be safly closed
    
    global file1
    
    try:
        file1.close()
    except:
        print("The File Was Already Closed, EXITING....")
        sys.exit()
    else:
        print("The File Is Closed, EXITING....")
        sys.exit()

##run interface()
#--------------------------------------interface call
##interface()



## SOFTWARE for pushing to google sheets--------------------------------------

GDOCS_OAUTH_JSON       = 'google-auth.json'

## Google Docs spreadsheet name.
GDOCS_SPREADSHEET_NAME = 'Nature'

## How long to wait (in seconds) between measurements.
FREQUENCY_SECONDS      = 5

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

#values_list = worksheet.row_values(2)
#print(values_list)

## Append the data in the spreadsheet, including a timestamp
'''do not need(
try:
    worksheet.append_row((dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S'), ds1T, ds2T, ds3T))
        
    
    except:
        # Error appending data, most likely because credentials are stale.
        # Null out the worksheet so a login is performed at the top of the loop.
        print('Append error, logging in again')
        worksheet = None
        time.sleep(FREQUENCY_SECONDS)
        continue
    )
'''
## Wait FREQUENCY_SECONDS seconds before continuing
print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
'''time.sleep(FREQUENCY_SECONDS)'''

def runAll():
    time.sleep(FREQUENCY_SECONDS)
    getData()
    calculations()
    #-------------------------------------------------config call
    #config()
    record()
    
    '''root.after(100, runAll) #for interface'''

## Run all of the functions ----------------------------------------------------
while True:
    runAll()

#root.after(100, remember)
'''mainloop() # for GUI'''








