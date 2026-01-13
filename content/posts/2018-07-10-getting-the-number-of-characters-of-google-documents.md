---
title: "Getting the number of characters of Google documents"
date: 2018-07-10T16:52:32
draft: false
categories: ["Coding", "google docs", "Python"]
---

I did something very similar to my previous post of a couple of days ago, in which I take[ the sum of the number of characters of each document in a google drive folder](https://gigabaseorgigabyte.wordpress.com/2018/07/07/getting-number-of-characters-from-google-drive-folder/). Today I adapted the code slightly to query individual documents, and added a Class for Documents with a method for counting the number of characters.

Not very creative, but useful nonetheless.Since I'm reusing functions from last week I should probably put these in a module and import this, rather than keeping code duplicated. But that organisation will be for a later time.

I'll also run this hourly in a cron job. This will give me some data to analyse my writing behaviour...

https://gist.github.com/wdecoster/9984ce30b21c7c5d751458672c724310