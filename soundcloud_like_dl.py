#soundcloud_like_dl.py
#author: Jeremy Goldman

def getTrack():
	finalURL = "http://anything2mp3.com/?url=" + allLines[-2].strip()
	print "opening firefox"
	driver = webdriver.Firefox()
	#navigate to url
	print "navigating to webpage"
	print "\n sorry about the ads on the site. it's not the prettiest, but it gets the job done\n"
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
	urllib.urlretrieve(albumArtSrc, str((allLines[-1].strip()))+'.jpg')
	print "downloaded album art"
	print "downloading audio"
	driver.get(audioURL)
	print "\nmake sure you select \"Save File\", then click the \"OK\" button if a dialog pops up!!!"
	print "\nsleeping for 15 sec to make sure download is completed..."
	#MODIFY THE SLEEP TIME ACCORDING TO YOUR INTERNET CONNECTION
	#i.e. sleep less if your file downloads quickly, sleep longer if internet connection is slower
	#time is in seconds
	time.sleep(15)
	print "done sleeping"
	driver.quit()

def updateTime():
	dataList = [str(time.time()) + '\n'] + allLines[2:]
	newData = '\n' + "".join(dataList)
	#write time into new file
	print "writing new data (w/ new timestamp) to file"
	favoritesFile.truncate(0)
	favoritesFile.write(newData)
	print "saving file"
	favoritesFile.close()

def getFilePath():
	#check if filepath is already saved
	if path.isfile('fileLocation.txt'):
		#read from file
		nameFile = open('fileLocation.txt', 'r')
		favoritesPath = nameFile.read().strip()
		nameFile.close()
	else:
		#accept input for the file location
		favoritesPath = raw_input('\nTo point the script at the IFTTT-modified file, please drag your file into this terminal window, then press Enter.\n')
		favoritesPath = favoritesPath.strip()
		#get rid of any spaces
		#create new file to save file location
		newNameFile = open('fileLocation.txt', 'w')
		newNameFile.write(favoritesPath)
		newNameFile.close()
	#get rid of spaces in filename
	favoritesPath = favoritesPath.replace('\\', '')
	return favoritesPath


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import time
import os.path as path

favoritesPath = getFilePath()

#open file in read/write mode
favoritesFile = open(favoritesPath, 'r+w')

#get all text from file
allLines = favoritesFile.readlines()
print "reading file for changes"
#get timestamp line to check if first time or not
prevModTimeString = (allLines[1].strip())[:7]
if prevModTimeString.isdigit():
	#sript has been run before or timestamp has been added
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
	#if file was changed more than 30 sec after the last time the script was run
	#(i.e. IFTTT recipe updated the file)
	if timeChange > 30:
		#download track + album art
		getTrack()
		#update last modified time
		updateTime()
	else:
		print "nothing's changed yet"
	print "all done!"
else:
	#first time running script
	print "first time running script!"
	getTrack()
	updateTime()






