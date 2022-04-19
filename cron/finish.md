The cron job syntax is used in a variety of different scheduling tools, due to many developers being familiar with the simple syntax. 

There are some extensions available to certain cron implementations, which allow you to specify for instance @reboot instead of the time columns, to let the job run at the startup of the machine. Some extensions will also allow sub-minute precision by simply adding another column for seconds.

The cron job syntax is also used for some cloud based tools, such as [Google's Cloud Scheduler](https://cloud.google.com/scheduler)

Other common usecases might be to redeploy an environment once every day (rather than for every single commit). There is no limit to how complex your cron based tasks can be.