---
title: "Checking if a device is up using cron, ping and Zapier"
date: 2017-08-05T21:23:24
draft: false
tags: ["bash"]
categories: ["Coding"]
---

Today I adapted [a script from nixCraft](https://bash.cyberciti.biz/monitoring/monitor-windows-linux-server-with-ping-script/) to check if a device (in this case a Raspberry Pi) is up. The idea is simple: my computer should check every hour to figure out if the Raspberry Pi is still alive, and report to me if it isn't.

Checking every hour is accomplished by the following [cron](https://help.ubuntu.com/community/CronHowto)tab entry:
@hourly bash /home/wouter/bin/checkRasp3.sh
The bash script below pings my Raspberry Pi, and when ping was unsuccessful it will use a [Zapier](https://zapier.com/app/explore) webhook to send me a [Pushbullet](https://www.pushbullet.com/) notification to my phone and browser, although you could use the same idea to get a slack notification, an email,...

 

https://gist.github.com/wdecoster/9182baa4575f805f2aacddfb12afd533