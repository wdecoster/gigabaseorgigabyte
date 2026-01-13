---
title: "Getting number of characters from all documents in Google drive folder"
date: 2018-07-07T23:27:15
draft: false
categories: ["Coding", "google docs", "Python"]
---

I should be writing on my PhD thesis, but instead I wrote a fun piece of code. I wanted to trace the number of characters in my thesis documents, which are in a folder in my Google drive.  Google drive has a useful API, but with seemingly outdated and/or hard to navigate documentation (and not the time to scan through all of it) I had still quite a rough time to set up what I wanted to do. Your starting point is [this page](https://developers.google.com/api-client-library/python/start/get_started). Another great resource is the [Core Python Programming blog](https://wescpy.blogspot.com/).

I had to use both the 'v2' and 'v3' API even, based on code snippets I found. There is definitely a better way to do parts of this, so your feedback is welcome.  The full code is at the bottom of the post. The code uses a client_secret.json file which you can obtain after activating the API and setting the proper permissions in your google account. The first time the code is executed a browser window will be opened for authorizing the application. This will generate credentials stored in credentials.json for future use. Note that every time you tamper (e.g. with the permission scope) you should delete this credentials.json file and repeat the authorisation. There will be dragons.

A seemingly trivial but actually rather tricky part was listing the files in a Google drive folder. Perhaps I used some weak search terms, but it took most of my Saturday afternoon. Finally the script downloads the documents in my "thesis" folder as plain text  and sums all characters except newlines and underscores (which are generated from titles).

I've put this script in my cron tab for appending the  number of characters to a file every hour:
@hourly python thesis_charcount.py >> char_count_thesis.txt
This should give me some data for plotting, but that code is for another moment of glorious procrastination.

https://gist.github.com/wdecoster/9b18cc597b91eb609323a4779cd091f0