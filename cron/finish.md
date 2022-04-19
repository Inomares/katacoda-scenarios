Great job making it to the end! As you have now seen, simple cron jobs can make it easy to schedule as many and diverse tasks as you need.

The cron job syntax is used in a variety of different scheduling tools, due to many developers being familiar with the simple syntax. The cron job syntax is also used for some cloud based tools, such as [Google's Cloud Scheduler](https://cloud.google.com/scheduler).

There are some extensions available to certain cron implementations, which allow you to specify for instance @reboot instead of the time columns, to let the job run at the startup of the machine. Some extensions will also allow sub-minute precision by simply adding another column for seconds.

If you want to know more about cron, check out `man cron`{{execute}}, and `man crontab`{{execute}}.