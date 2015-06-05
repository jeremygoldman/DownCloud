def getTrack():
	finalURL = "http://anything2mp3.com/?url=" + allLines[-2].strip()
	print "opening chrome"
	driver = webdriver.Chrome()
	#navigate to url
	print "navigating to webpage"
	driver.get(finalURL)
	#time.sleep(3)
	#find convert button and click it
	print "looking for convert button..."
	convertButton = driver.find_element_by_id("edit-submit--2")
	print "found convert button"
	print "clicked convert button"
	print "waiting for webpage to load..."
	convertButton.click()
	while driver.current_url[:37] != 'http://anything2mp3.com/videodownload':
		#do nothing
		True
	#find mp3 in page
	time.sleep(0.5)
	print "webpage loaded"
	print "looking for audio link..."
	audioLink = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div/section/div/div[1]/a")
	print "found audio link"
	#get mp3 link
	audioURL = audioLink.get_attribute('href')
	#download mp3
	#urllib.urlretrieve(audioURL, 'Downloads/'+str((allLines[-1].strip()))+'.mp3')
	#find album art in page
	print "looking for album art..."
	albumArt = driver.find_element_by_class_name("image-style-none")
	print "found album art"
	albumArtSrc = albumArt.get_attribute('src')
	#download album art
	#use str() to make sure punctuation doesn't mess with directory
	urllib.urlretrieve(albumArtSrc, 'Downloads/'+str((allLines[-1].strip()))+'.jpg')
	print "downloaded album art"
	print "downloading audio"
	driver.get(audioURL)
	time.sleep(15)
	driver.quit()

def updateTime():
	#60 is one second
	dataList = [str(time.time()) + '\n'] + allLines[2:]
	newData = '\n' + "".join(dataList)
	#write time into new file
	print "writing new data (w/ new timestamp) to file"
	favoritesFile.truncate(0)
	favoritesFile.write(newData)
	print "saving file"
	favoritesFile.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import time
import os.path as path

favoritesPath = '/Users/jeremy/Box Sync/IFTTT/SoundCloud/favorites.txt'
#open file in read mode
favoritesFile = open(favoritesPath, 'r+w')

#get all text from file
allLines = favoritesFile.readlines()
print "reading file for changes"
#last modification time

prevModTime = int(float(allLines[1]))
print "previous file mod time: " + str(prevModTime)
#current modification (will be much larger if file was modified)
currModTime = path.getmtime(favoritesPath)
print "current mod time: " + str(currModTime)

#3600 = hour
#difference in modification times
timeChange = currModTime-prevModTime
print "change in mod times: " + str(timeChange)
#more than 1 min
if timeChange > 100:
	#download track + album art
	print "running getTrack()"
	getTrack()
	#update last modified time
	print "running updateTime()"
	updateTime()
else:
	print "nothing's changed yet"
print "all done!"





