#!/bin/bash

#delete our temp cron job file if it exists
rm goes_cron

#save current cron jobs
crontab -l >> goes_cron

#crontab -r
#will reset your crontab, but you may have other stuff in there

#add in the get goes cron job
echo "*/15 * * * * /home/dustin/workspace/get_goes/get_goes.py" >> goes_cron

#add all the cron jobs back in
crontab goes_cron

#show current cron jobs
crontab -l


