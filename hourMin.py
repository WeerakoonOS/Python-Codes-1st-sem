totalSec=int(input('What is the total no of seconds?'))

totalMin=totalSec//60
totalSec=totalSec%60

totalHour=totalMin//60
totalMin=totalMin%60

print('total Hour: '+str(totalHour)+' total Minutes: '+str(totalMin)+' total Seconds: '+str(totalSec))
