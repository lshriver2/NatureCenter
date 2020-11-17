#include <OneWire.h>
#include <DallasTemperature.h>
#include "DHT.h"
#include "EmonLib.h"             // Include Emon Library


#define VOLT_CAL 148.7
#define CURRENT_CAL 60.2
EnergyMonitor emon1;             // Create an instance

#define DHT1PIN 13
// Digital pin connected to the DHT sensor
// Feather HUZZAH ESP8266 note: use pins 3, 4, 5, 12, 13 or 14 --
// Pin 15 can work but DHT must be disconnected during program upload.

// Uncomment whatever type you're using!
//#define DHTTYPE DHT11   // DHT 11
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Data wire is plugged into digital pin 2 on the Arduino

#define ONE_WIRE_BUS1 6
#define ONE_WIRE_BUS2 2
#define ONE_WIRE_BUS3 3
#define ONE_WIRE_BUS4 4
#define ONE_WIRE_BUS5 5

// define wind sensor
#define analogPinForRV    1   // change to pins you the analog pins are using
#define analogPinForTMP   0

DHT dht1(DHT1PIN, DHTTYPE);

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire1(ONE_WIRE_BUS1);
OneWire oneWire2(ONE_WIRE_BUS2);
OneWire oneWire3(ONE_WIRE_BUS3);
OneWire oneWire4(ONE_WIRE_BUS4);
OneWire oneWire5(ONE_WIRE_BUS5);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors1(&oneWire1);
DallasTemperature sensors2(&oneWire2);
DallasTemperature sensors3(&oneWire3);
DallasTemperature sensors4(&oneWire4);
DallasTemperature sensors5(&oneWire5);

int numberOfDevices1; // Number of temperature devices found
int numberOfDevices2; // Number of temperature devices found
int numberOfDevices3; // Number of temperature devices found
int numberOfDevices4; // Number of temperature devices found
int numberOfDevices5; // Number of temperature devices found

//DeviceAddress tempDeviceAddress; // We'll use this variable to store a found device address
DeviceAddress tempDeviceAddress1; // We'll use this variable to store a found device address
DeviceAddress tempDeviceAddress2; // We'll use this variable to store a found device address
DeviceAddress tempDeviceAddress3; // We'll use this variable to store a found device address
DeviceAddress tempDeviceAddress4; // We'll use this variable to store a found device address
DeviceAddress tempDeviceAddress5; // We'll use this variable to store a found device address


//--------------------------------wind sensor initialize----------------------------------
// to calibrate your sensor, put a glass over it, but the sensor should not be
// touching the desktop surface however.
// adjust the zeroWindAdjustment until your sensor reads about zero with the glass over it. 

const float zeroWindAdjustment =  .2; // negative numbers yield smaller wind speeds and vice versa.

int TMP_Therm_ADunits;  //temp termistor value from wind sensor
float RV_Wind_ADunits;    //RV output from wind sensor 
float RV_Wind_Volts;
unsigned long lastMillis;
int TempCtimes100;
float zeroWind_ADunits;
float zeroWind_volts;
float WindSpeed_MPH;

//---------------------Flow sensor initialize ------------------------------------
// which pin to use for reading the flow sensor? can use any pin!
#define FLOWSENSORPIN 7

// count how many pulses!
volatile uint16_t pulses = 0;
// track the state of the pulse pin
volatile uint8_t lastflowpinstate;
// you can try to keep time of how long it is between pulses
volatile uint32_t lastflowratetimer = 0;
// and use that to calculate a flow rate
volatile float flowrate;
// Interrupt is called once a millisecond, looks for any pulses from the sensor!
SIGNAL(TIMER0_COMPA_vect) {
  uint8_t x = digitalRead(FLOWSENSORPIN);
  
  if (x == lastflowpinstate) {
    lastflowratetimer++;
    return; // nothing changed!
  }
  
  if (x == HIGH) {
    //low to high transition!
    pulses++;
  }
  lastflowpinstate = x;
  flowrate = 1000.0;
  flowrate /= lastflowratetimer;  // in hertz
  lastflowratetimer = 0;
}

void useInterrupt(boolean v) {
  if (v) {
    // Timer0 is already used for millis() - we'll just interrupt somewhere
    // in the middle and call the "Compare A" function above
    OCR0A = 0xAF;
    TIMSK0 |= _BV(OCIE0A);
  } else {
    // do not call the interrupt function COMPA anymore
    TIMSK0 &= ~_BV(OCIE0A);
  }
}


void setup(void) // ------------------- void setup(void) ---------------------
{
  Serial.begin(9600);

  // Start up the library
  sensors1.begin();
  sensors2.begin();
  sensors3.begin();
  sensors4.begin();  
  sensors5.begin();
  
  // Grab a count of devices on the wire
  numberOfDevices1 = sensors1.getDeviceCount();
  numberOfDevices2 = sensors2.getDeviceCount();
  numberOfDevices3 = sensors3.getDeviceCount();
  numberOfDevices4 = sensors4.getDeviceCount();
  numberOfDevices5 = sensors5.getDeviceCount();
  /*

/*
 

28FF5F5D7215011A Main floor temp

28E9B507B6013C0E white/ brown HVAC input or HVAC return
287D4007B6013C17 white/ green HVAC input or HVAC return

281CF607B6013C30 Ceiling thermal sensor
28FFEE61721501C2 under roof

28FF18DF7215017C ds2_BUS 7 // SE EveExt
28FF296272150139 ds1_BUS 6 // East Gable Ext

28FFBDF763150110 ds5_BUS 10 // NW Eve Ext
28FF93525415037A ds4_BUS 9 // West Gable Ext


*/
/*
10:26:06.307 -> Locating devices on 1...Found 1 devices.
10:26:06.341 -> Locating devices on 2...Found 2 devices.
10:26:06.376 -> Locating devices on 3...Found 2 devices.
10:26:06.410 -> Locating devices on 4...Found 2 devices.
10:26:06.479 -> Locating devices on 5...Found 2 devices.
10:26:06.514 -> Found device 0 with address: 28FF5F5D7215011A
10:26:06.549 -> Found device 0 with address: 28E9B507B6013C0E
10:26:06.619 -> Found device 1 with address: 287D4007B6013C17
10:26:06.653 -> Found device 0 with address: 281CF607B6013C30
10:26:06.723 -> Found device 1 with address: 28FFEE61721501C2
10:26:06.758 -> Found device 0 with address: 28FF18DF7215017C
10:26:06.793 -> Found device 1 with address: 28FF296272150139
10:26:06.863 -> Found device 0 with address: 28FFBDF763150110
10:26:06.898 -> Found device 1 with address: 28FF93525415037A


  
  // locate devices on the bus
  Serial.print("Locating devices on 1...");
  Serial.print("Found ");
  Serial.print(numberOfDevices1, DEC);
  Serial.println(" devices.");
  
  Serial.print("Locating devices on 2...");
  Serial.print("Found ");
  Serial.print(numberOfDevices2, DEC);
  Serial.println(" devices.");

  Serial.print("Locating devices on 3...");
  Serial.print("Found ");
  Serial.print(numberOfDevices3, DEC);
  Serial.println(" devices.");

  Serial.print("Locating devices on 4...");
  Serial.print("Found ");
  Serial.print(numberOfDevices4, DEC);
  Serial.println(" devices.");

  Serial.print("Locating devices on 5...");
  Serial.print("Found ");
  Serial.print(numberOfDevices5, DEC);
  Serial.println(" devices.");
  
  // Loop through each device, print out address #1 !!!!!!
  for(int i=0;i<numberOfDevices1; i++) {
    // Search the wire for address
    if(sensors1.getAddress(tempDeviceAddress1, i)) {
      Serial.print("Found device ");
      Serial.print(i, DEC);
      Serial.print(" with address: ");
      printAddress(tempDeviceAddress1);
      Serial.println();
    } else {
      Serial.print("Found ghost device at ");
      Serial.print(i, DEC);
      Serial.print(" but could not detect address. Check power and cabling");
    }
  }

    // Loop through each device, print out address #2 !!!!!!
  for(int i=0;i<numberOfDevices2; i++) {
    // Search the wire for address
    if(sensors2.getAddress(tempDeviceAddress2, i)) {
      Serial.print("Found device ");
      Serial.print(i, DEC);
      Serial.print(" with address: ");
      printAddress(tempDeviceAddress2);
      Serial.println();
    } else {
      Serial.print("Found ghost device at ");
      Serial.print(i, DEC);
      Serial.print(" but could not detect address. Check power and cabling");
    }
  }

    // Loop through each device, print out address #3 !!!!!!
  for(int i=0;i<numberOfDevices3; i++) {
    // Search the wire for address
    if(sensors3.getAddress(tempDeviceAddress3, i)) {
      Serial.print("Found device ");
      Serial.print(i, DEC);
      Serial.print(" with address: ");
      printAddress(tempDeviceAddress3);
      Serial.println();
    } else {
      Serial.print("Found ghost device at ");
      Serial.print(i, DEC);
      Serial.print(" but could not detect address. Check power and cabling");
    }
  }

    // Loop through each device, print out address #4 !!!!!!
  for(int i=0;i<numberOfDevices4; i++) {
    // Search the wire for address
    if(sensors4.getAddress(tempDeviceAddress4, i)) {
      Serial.print("Found device ");
      Serial.print(i, DEC);
      Serial.print(" with address: ");
      printAddress(tempDeviceAddress4);
      Serial.println();
    } else {
      Serial.print("Found ghost device at ");
      Serial.print(i, DEC);
      Serial.print(" but could not detect address. Check power and cabling");
    }
  }

  // Loop through each device, print out address #5 !!!!!!
  for(int i=0;i<numberOfDevices5; i++) {
    // Search the wire for address
    if(sensors5.getAddress(tempDeviceAddress5, i)) {
      Serial.print("Found device ");
      Serial.print(i, DEC);
      Serial.print(" with address: ");
      printAddress(tempDeviceAddress5);
      Serial.println();
    } else {
      Serial.print("Found ghost device at ");
      Serial.print(i, DEC);
      Serial.print(" but could not detect address. Check power and cabling");
    }
  }
  */
  // -------------- end ds temps setup ----------
  dht1.begin();

  /*
  // ---------- wins sensor stuff
  //   Uncomment the three lines below to reset the analog pins A2 & A3
  //   This is code from the Modern Device temp sensor (not required)
  pinMode(A2, INPUT);        // GND pin      
  pinMode(A3, INPUT);        // VCC pin
  digitalWrite(A3, LOW);     // turn off pullups   
  */ 
  
  //------------ volts and amps set up ----------------------------------------------------
  emon1.voltage(3, VOLT_CAL, 1.7);  // Voltage: input pin, calibration, phase_shift
  emon1.current(4, CURRENT_CAL);       // Current: input pin, calibration.

  //--------------flow set up ----------------------------------------------------
  pinMode(FLOWSENSORPIN, INPUT);
  digitalWrite(FLOWSENSORPIN, HIGH);
  lastflowpinstate = digitalRead(FLOWSENSORPIN);
  useInterrupt(true);
}

void loop(void){ // -------------- void loop(void) ---------------------
  // Send the command to get temperatures
  sensors1.requestTemperatures(); // Send the command to get temperatures
  sensors2.requestTemperatures(); // Send the command to get temperatures
  sensors3.requestTemperatures(); // Send the command to get temperatures
  sensors4.requestTemperatures(); // Send the command to get temperatures
  sensors5.requestTemperatures(); // Send the command to get temperatures

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  // Read temperature as Celsius (the default)
  float dht1H = dht1.readHumidity();
  float dht1T = dht1.readTemperature();

  if (millis() - lastMillis > 200){      // read every 200 ms - printing slows this down further  
    TMP_Therm_ADunits = analogRead(analogPinForTMP);
    RV_Wind_ADunits = analogRead(analogPinForRV);
    RV_Wind_Volts = (RV_Wind_ADunits *  0.0048828125);

    // these are all derived from regressions from raw data as such they depend on a lot of experimental factors
    // such as accuracy of temp sensors, and voltage at the actual wind sensor, (wire losses) which were unaccouted for.
    TempCtimes100 = (0.005 *((float)TMP_Therm_ADunits * (float)TMP_Therm_ADunits)) - (16.862 * (float)TMP_Therm_ADunits) + 9075.4;  

    zeroWind_ADunits = -0.0006*((float)TMP_Therm_ADunits * (float)TMP_Therm_ADunits) + 1.0727 * (float)TMP_Therm_ADunits + 47.172;  //  13.0C  553  482.39

    zeroWind_volts = (zeroWind_ADunits * 0.0048828125) - zeroWindAdjustment;  

    // This from a regression from data in the form of 
    // Vraw = V0 + b * WindSpeed ^ c
    // V0 is zero wind at a particular temperature
    // The constants b and c were determined by some Excel wrangling with the solver.
    
  WindSpeed_MPH =  pow(((RV_Wind_Volts - zeroWind_volts) /.2300) , 2.7265);   

  
  lastMillis = millis();    
  } 
  /*
  sensors.requestTemperatures(); // Send the command to get temperatures
  
 
  Serial.print(ds1T); // ds1T LOCATION: East Gable Ext
  Serial.print(F(" "));

  Serial.print(ds2T); // ds2T LOCATION: SE EveExt
  Serial.print(F(" "));

  Serial.print(ds3T); // ds3T LOCATION: West Gable In
  Serial.print(F(" "));

  Serial.print(ds4T); // ds4T LOCATION: West Gable Ext 
  Serial.print(F(" "));
  */

  //delay(2000);

  Serial.print(dht1T); // dht1T (TEMP) LOCATION: AIR RETURN
  Serial.print(F(" "));
  
  Serial.print(dht1H); // dht1T (HUMIDITY) LOCATION: AIR RETURN
  Serial.print(F(" "));

  
  Serial.print((float(TempCtimes100))/100 ); // Wind Sensor Rev. C (TEMP) LOCATION: AIR RETURN
  Serial.print(F(" "));

  if (0<WindSpeed_MPH){
    Serial.print(float(WindSpeed_MPH)); // Wind Sensor Rev. C (WIND) LOCATION: AIR RETURN
    Serial.print(F(" "));
  }
  else{
    Serial.print(float(0)); // Wind Sensor Rev. C (WIND) LOCATION: AIR RETURN
    Serial.print(F(" "));
  }

  /*
  Serial.print(ds5T); // ds5T LOCATION: NW Eve Ext
  Serial.print(F(" "));

  Serial.print(ds6T); // ds6T LOCATION: First Floor In
  Serial.print(F(" "));

  Serial.print(ds7T); // ds7T LOCATION: Ciling In
  Serial.print(F(" "));

  Serial.print(ds8T); // ds8T LOCATION: Under Roof
  Serial.print(F(" "));
  */

  /*
  //tempF = (sensors.getTempCByIndex(0) * 9.0) / 5.0 + 32.0;
  float ds1T = (ds1S.getTempCByIndex(0));
  float ds2T = (ds2S.getTempCByIndex(0));
  float ds3T = (ds3S.getTempCByIndex(0));
  float ds4T = (ds4S.getTempCByIndex(0));
  float ds5T = (ds5S.getTempCByIndex(0));
  float ds6T = (ds6S.getTempCByIndex(0));
  float ds7T = (ds7S.getTempCByIndex(0));
  float ds8T = (ds8S.getTempCByIndex(0));
  */
  
  // ---------------- Start printing Ds Temps -------------------------
  
  //Serial.print(sensors1.getTempCByIndex(0));
  // Loop through each device, print out temperature data ---- #1 !!!! ----
  for(int i=0;i<numberOfDevices1; i++) {
    // Search the wire for address
    if(sensors1.getAddress(tempDeviceAddress1, i)){
    
    // Output the device ID
    //Serial.print("Temperature for device: ");
    //Serial.println(i,DEC);

    // Print the data
    float tempC = sensors1.getTempC(tempDeviceAddress1);
   // Serial.print("Temp C: ");
    Serial.print(tempC);
    Serial.print(F(" "));
    }   
  }
  
  //Serial.print(sensors2.getTempCByIndex(0));
  // Loop through each device, print out temperature data ---- #2 !!!! ----
  for(int i=0;i<numberOfDevices2; i++) {
    // Search the wire for address
    if(sensors2.getAddress(tempDeviceAddress2, i)){
      
    // Output the device ID
    //Serial.print("Temperature for device: ");
    //Serial.println(i,DEC);
  
    // Print the data
    float tempC = sensors2.getTempC(tempDeviceAddress2);
    // Serial.print("Temp C: ");
    Serial.print(tempC);
    Serial.print(F(" "));
    }
  }

  //Serial.print(sensors3.getTempCByIndex(0));
  // Loop through each device, print out temperature data ---- #3 !!!! ----
  for(int i=0;i<numberOfDevices3; i++) {
    // Search the wire for address
    if(sensors3.getAddress(tempDeviceAddress3, i)){
      
    // Output the device ID
    //Serial.print("Temperature for device: ");
    //Serial.println(i,DEC);
  
    // Print the data
    float tempC = sensors3.getTempC(tempDeviceAddress3);
    // Serial.print("Temp C: ");
    Serial.print(tempC);
    Serial.print(F(" "));
    }
  }

  //Serial.print(sensors4.getTempCByIndex(0));
  // Loop through each device, print out temperature data ---- #4 !!!! ----
  for(int i=0;i<numberOfDevices4; i++) {
    // Search the wire for address
    if(sensors4.getAddress(tempDeviceAddress4, i)){
      
    // Output the device ID
    //Serial.print("Temperature for device: ");
    //Serial.println(i,DEC);
  
    // Print the data
    float tempC = sensors4.getTempC(tempDeviceAddress4);
    // Serial.print("Temp C: ");
    Serial.print(tempC);
    Serial.print(F(" "));
    }
  }

  //Serial.print(sensors5.getTempCByIndex(0));
  // Loop through each device, print out temperature data ---- #5 !!!! ----
  for(int i=0;i<numberOfDevices5; i++) {
    // Search the wire for address
    if(sensors5.getAddress(tempDeviceAddress5, i)){
    
    // Output the device ID
    //Serial.print("Temperature for device: ");
    //Serial.println(i,DEC);

    // Print the data
    float tempC = sensors5.getTempC(tempDeviceAddress5);
   // Serial.print("Temp C: ");
    Serial.print(tempC);
    Serial.print(F(" "));
    }   
  }

  //------------- print volts and current --------------------
  emon1.calcVI(20,2000);         // Calculate all. No.of half wavelengths (crossings), time-out
  float currentDraw = emon1.Irms; //extract Irms into Variable
  float supplyVoltage = emon1.Vrms; //extract Vrms into Variable
  Serial.print(supplyVoltage);
  Serial.print(F(" "));
  Serial.print(currentDraw);
  Serial.print(F(" "));


  //--------------- print Flow and liters ----------------------
  // Serial.println(F(" "));
  // Serial.print("Freq: "); 
  Serial.print(flowrate);
  Serial.print(F(" "));
  // Serial.print("Pulses: "); 
  Serial.print(pulses, DEC);
  Serial.print(F(" "));
  
  // if a plastic sensor use the following calculation
  // Sensor Frequency (Hz) = 7.5 * Q (Liters/min)
  // Liters = Q * time elapsed (seconds) / 60 (seconds/minute)
  // Liters = (Frequency (Pulses/second) / 7.5) * time elapsed (seconds) / 60
  // Liters = Pulses / (7.5 * 60)
  float liters = pulses;
  liters /= 7.5;
  liters /= 60.0;

  Serial.print(liters);
  Serial.print(F(" ")); 
  // Serial.print(" Liters");
  
  //--------------new line and delay ------------------------
  //delay(5000);
  Serial.println(F(" "));
  //delay(100);
}

//*
// -----------------------------function to print a device address------------
void printAddress(DeviceAddress deviceAddress) {
  for (uint8_t i = 0; i < 8; i++) {
    if (deviceAddress[i] < 16) Serial.print("0");
      Serial.print(deviceAddress[i], HEX);
  }
}
//*/





/*


  Serial.print(t);
  Serial.print(F(" "));
//  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F(" "));
//  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F(" "));
//  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.print(F(" "));
//  Serial.print(F("°F"));

  Serial.println((tempF));

  delay(100);  
  
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht1.readTemperature(true);

  // Compute heat index in Fahrenheit (the default)
  float hif = dht1.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht1.computeHeatIndex(t, h, false);
*/
