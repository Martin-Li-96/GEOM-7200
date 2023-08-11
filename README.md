# GEOM-7200 GDOP Data Downloading

You just simply download the csv file to do analyse. If you want to use the Python script, there are more extra steps you need to do
- When you run the .py file, the selenium will open a chrom window, and switch to the aim website.All the operator must after the page is compeletly loading. When you see "Wait!" in your python console, then you can do the following steps.
- The first thing you need to do, is make sure you only choose the GPS.
- Second, you need to set the date to 2023-08-02. **(you can choose the time you want, just change the "2023-08-03" to any time you want in the python script)**
- Third, you need to set the time-zone to (UTC+10:00) Brisbane.
- Finally the script will download the data and save the data to a csv file.
**(Note)**
  Because this script is use a proxy ip from google, sometimes it will not working. You can easily get a new proxy ip from google and update the
  proxy ip in the script. If the script is faild, just try more times. Good Luck!
If you meet any troubles or bugs, feel free to make comments. 
