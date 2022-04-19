It is also possible to specify multiple values for a single column. For instance, let's you want to trigger a script both on minutes divisible by 2 but also those that are divisible by 3.

This is easily done as follows. Open your crontab with ``crontab -e``{{execute}} again, and then change the broadcast to the following:

`*/2,*/3 * * * TUE,FRI wall "Hello world!"`{{execute}} 

Now let's pretend that you want to trigger a cronjob every minute from :00 to :49. Of course you could manually write 1,2,3... and so forth, but that is a lot of manual labour and ver error prone. Instead, you can do a range, like 0-49:

`0-49 * * * TUE,FRI wall "Hello world!"`{{execute}}

Good job following along so far! Now you have all you need to finally create the cronjob. Remember, the build logs should be cleared mon-fri