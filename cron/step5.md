It is also possible to specify multiple values for a single column. For instance, let's say you want to trigger a script both on minutes divisible by 2 but also those that are divisible by 7.

This is easily done as follows. Open your crontab with ``crontab -e``{{execute}} again, and then change the broadcast to the following:

`*/2,*/7 * * * TUE,FRI wall "Hello world!"`{{execute}} 

Now let's pretend that you want to trigger a cronjob every minute from :00 to :49. Of course you could manually write 1,2,3... and so forth, but that is a lot of manual labour and very error-prone. Instead, you can do a range, like 0-49:

`0-49 * * * TUE,FRI wall "Hello world!"`{{execute}}

Good job following along so far! Now you have all you need to finally create the cronjob described in the intro. To quickly recap: Every hour between 08-17 on mondays through friday, we want to run the task. To accomplish this, add the following to your `crontab -e`{{execute}}:

`0 8-17 * * MON-FRI rm -rf /root/build_logs/*`{{execute}}

Let's go through the columns one last time in order:
* 0: At zero minutes into the hour
* 8-17: At hours 8-17
* \*: Any date
* \*: Any month
* MON-FRI: At monday through friday

And, at last, the command we want to execute. That's it, you're done!