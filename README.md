# Data-Visualization
Data visualization and statistics from data.
I have taken the IIT Mandi landslide data-set as a csv file. This data-set contains the readings from various sensors installed at 10 locations around the IIT Mandi campus. These sensors give the details about various factors like temperature, humidity, pressure etc. 

The CSV file contains following attributes:\
• dates: date of collection of data.\
• stationid: Indicates the location of the sensor.\
• temperature: Atmospheric temperature around the sensor in Celsius.\
• humidity: The concentration of water vapor present in the air. It is a relative humidity (in %).\
• pressure: Atmospheric pressure in millibars (mb).\
• rain: Measure of rainfall in ml.\
• lightavgw/o0: The average light throughout the daytime (in lux units).\
• lightmax: The maximum lux count by the sensor.\
• moisture: indicates the water stored in the soil (measured between 0 to 100 percent).\

I have written a python program (with pandas) to read the given data and display following:

1. Mean, median, mode, minimum, maximum and standard deviation for all the attributes (excluding dates and stationid). 

2. The scatter plot between 
a. ‘rain’ and each of the other attributes (excluding ‘dates’ and ‘stationid’). 
b. ‘temperature’ and each of the other attributes (excluding ‘dates’ and ‘stationid’).

3. The value of correlation coefficient in the following cases:
a. ‘rain’ with all other attributes (excluding ‘dates’ and ‘stationid’). 
b. ‘temperature’ with all other attributes (excluding ‘dates’ and ‘stationid’).

4. The histogram for the attributes ‘rain’ and ‘moisture’.

5. The histogram of attribute ‘rain’ for each of the 10 stations.

6. The boxplot for the attributes ‘rain’ and ‘moisture’.
