So what is cron?

Let's start with having a look at the command you're most likely to use; `crontab`.

Start out by entering the following command into the terminal:

`crontab -e`{{execute}}

Executing this command and selecting an editor (only for the first time) opens the current user's crontab. A crontab (short for cron table) is where you enter the tasks you want to run, and when you want them to be run.

Let's create our first!
_Inside the crontab_, add a new line and write the following:

`* * * * * wall "Hello world!"`{{copy}}

Save the modified file, and exit the editor.

Congratulations! You just created your first cron job! 

At every full minute, you should now see a broadcasted message in your terminal. That's the task you just made, running like clockwork!