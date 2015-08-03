# xkcd_background
gets the latest xckd every day and sets it as your background

Tested only on Ubuntu 14.04 with Unity

#Running

I have this setup as a cron task.
Run the command `crontab -e` to open the crontab file
enter something like `0 0 * * * /home/peter/Projects/xkcd_background/set_env_and_call.sh /home/peter/Projects/xkcd_background/xkcd_background.py`

make sure the python script is executable
