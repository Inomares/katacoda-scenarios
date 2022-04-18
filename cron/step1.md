So what is cron?

Let's start with having a look at the command you're most likely to use; `crontab`.

Start out by entering the following command into the terminal:

`crontab -e`{{execute}}

Executing this command and selecting an editor (only for the first time) opens the current user's crontab. A crontab (short for cron table) is where you enter the tasks you want to run, and when you want them to be run.

Let's create our first!
Inside the crontab, add a new line and write the following:

`* * * * * wall "Hello world!"`{{execute}}