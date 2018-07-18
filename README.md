# DownCloud

Python script using Selenium, fswatch, &amp; IFTTT to download a track and its album art whenever I like a new track on SoundCloud

**Uses [this IFTTT recipe](https://goo.gl/556rKd) to monitor SoundCloud likes. If a new track is liked on SoundCloud, the IFTTT will append the track's title and URL to the end of the file. The script running on your local**

Files will be downloaded in whichever directory you ran the script from!
------
## Installation

* Install Selenium using the following command: `pip install selenium`
* Install fswatch using the following command: `brew install fswatch`.
 * If you don't have Homebrew installed, follow the instructions [here](https://brew.sh/)
* Run the following command:
  
  `fswatch -o [PATH OF IFTTT FAVORITES.TXT FILE] | xargs -n1 -I{} [PATH OF downcloud.py]`

  (don't include the brackets around the filepath placeholders)


If you're having issues installing fswatch, check out the [GitHub repository's](https://github.com/emcrisostomo/fswatch) README.

------

At this point if everything is installed correctly, your IFTTT trigger is watching for new liked tracks on SoundCloud, while the Python script is monitoring any changes to the favorites.txt file. Every time the IFTTT recipe adds new track data to the file, the script will use this data to download the mp3 file and apply the relevant metadata.

*When the script first runs, nothing will be outputted and it may look like Terminal is frozen. This is not the case; The script is running fine, and the script will only output when the favorites.txt file is modified.*

#### Make sure you click "Save File" to download the MP3 if a dialog pops up on the browser!

--------
## Acknowledgements
- fswatch: [Enrico Maria Crisostomo](https://github.com/emcrisostomo)
- Selenium: [SeleniumHQ](http://www.seleniumhq.org/) 
