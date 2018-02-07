#!/bin/bash

#delete our temp cron job file if it exists
rm goes_cron

#save current cron jobs
crontab -l >> goes_cron

#add in the get goes cron job
echo "*/15 * * * * /home/dustin/bin/get_goes/get_goes.py" >> goes_cron

#add all the cron jobs back in
crontab goes_cron

#show current cron jobs
crontab -l

