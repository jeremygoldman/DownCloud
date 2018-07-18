# DownCloud

Python script using Selenium, fswatch, &amp; IFTTT to download a track and its album art whenever I like a new track on SoundCloud

**Uses [this IFTTT recipe](https://goo.gl/556rKd) to monitor SoundCloud likes. If a new track is liked, the track's title and URL will be appended to the end of the file.**

Files will be downloaded in whichever directory you ran the script from!
------
To install Selenium, run: `pip install selenium` or follow the instructions [here](http://goo.gl/JmxrPT)

To install fswatch:
  * first run `brew install fswatch` if you've installed Homebrew. If you haven't, you definitely should.
  * Once fswatch has installed, run:
  
  `fswatch -o [PATH OF IFTTT FAVORITES.TXT FILE] | xargs -n1 -I{} [PATH OF downcloud.py]`

  (don't include the brackets around the filepath placeholders)

Now, you're monitoring the IFTTT file for changes! If the file is modified, the soundcloud_like_dl.py script will run!

*When the script first runs, nothing will be outputted and it will look like Terminal is frozen. This is not the case; The script is running fine, and something will be outputted only when the monitored file is modified.*

**Make sure you click "Save File" to download the MP3 if a dialog pops up on the browser!**
--------

**Confused about the fswatch install? Check the "Getting fswatch section" of [the GitHub repository's](https://github.com/emcrisostomo/fswatch) README.**

Acknowledgements
- fswatch: [Enrico Maria Crisostomo](https://github.com/emcrisostomo)
- Selenium: [SeleniumHQ](http://www.seleniumhq.org/) 
