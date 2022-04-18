So what is cron?

Let's start with having a look at the command you're most likely to use; `crontab`.

Start out by entering the following command into the terminal: 

`man crontab`{{execute}}

That's a lot of text! Do we need to care about all of this? Well, no. Not really. The main thing we'll be using is the following:

`crontab -e`{{execute}}

Executing this command and selecting an editor (only for the first time) opens the current user's crontab. A crontab (short for cron table) is where you enter the tasks you want to run, and when you want them to be run.

Let's create our first!

Notice that all lines that start with # are comments and will be ignored