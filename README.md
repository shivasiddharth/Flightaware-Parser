# Flightaware-Parser
Script to parse flight data from flightaware.com

## Example Usage:    
```    
import flightawareparser


facheck= flightawareparser.fascrapper()

details=facheck.flightdata("BA35")

print(details)

#Sample output: ('British Airways 35', 'Boeing 787-9 (twin-jet)', 'London, United Kingdom', 'Chennai / Madras, India', 'airborne', 370, 528, 'November 29 2019 14:30:00', 'November 29 2019 15:01:38', 'November 30 2019 00:03:00', 'November 30 2019 00:13:00', 'November 29 2019 14:33:00', 'November 29 2019 15:01:00', None, None, 'In air, covered 604 nautical miles with 3858 nautical miles remaining.')      

```    
     
## Order of output:  
Flight number/code   
Aircraft type   
Flight origin   
Flight destination   
Flight status (whether airborne/landed)  
Flight altitude    
Flight ground speed     
Estimated gate departure time        
Estimated takeoff time     
Estimated landing time      
Estimated gate arrival time     
Actual gate departure time       
Actual takeoff time     
Actual landing time      
Actual gate arrival time   
Aircraftposition (If airborne returns distance covered and distance remaining, returns status such as taxiing to takeoff from gate or taxiing to gate after landing)   


