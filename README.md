# Soundcloud-Like-DL
Python script using Selenium, FSWatch, &amp; IFTTT to download a track and its album art whenever I like a new track on SoundCloud

Uses [this IFTTT recipe](https://goo.gl/556rKd) to monitor SoundCloud likes. If a new track is liked, the track's title and URL will be appended to the end of the file.

To install Selenium, run: `pip install selenium` or follow the instructions [here](http://goo.gl/JmxrPT)

To install FSWatch, first run `brew install fswatch` if you've installed Homebrew. If you haven't, you definitely should.
Once FSWatch has installed, run `fswatch -o [PATH OF IFTTT FAVORITES.TXT FILE] | xargs -n1 -I{} [PATH OF soundcloud_like_dl.py]`
(don't include the brackets around the filepath placeholders)

Now, you're monitoring the IFTTT file for changes. If the file is modified, the soundcloud_like_dl.py script will run!


Confused about the FSwatch install? Check the "Getting fswatch section" of [this GitHub repository's](https://github.com/emcrisostomo/fswatch) README.

All credit for FSWatch should go to [Enrico Maria Crisostomo](https://github.com/emcrisostomo) and his awesome monitoring utility.

##Files will be downloaded in whichever directory you ran the script from!