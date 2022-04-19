Alright, we've managed to create a script that clears those pesky build logs, every single minute! Are we done yet?

Not quite! But don't worry, you're almost there. Now that we have something running every single minute, we're going to narrow down the run conditions to make it only trigger during certain times instead.

Let's open up our crontab again and have a look:

`crontab -e` {{execute}}

We have a bunch of asterisks (`*`) preceding our two commands. Each whitespace-separated token is used to determine when the command will be run, in this order:

Minute Hour Day Month Weekday Command

The asterisks represent "any" or "all". So for instance, we could create a cron job to run at exactly 13:05 on any December 3rd that is a Friday, like so:

5 13 3 12 FRI wall "It's december 1st, my acquaintances!"

Of course, it's also possible to use wildcards on only some of them.

Let's try it out, shall we? Try changing your cron job to something more specific, such as only triggering the `wall` broadcast at a certain minute:

`replaceme * * * * wall "Hello world!"` {{execute}}

Be sure to replace the "replaceme" with the number of a minute coming up shortly. Then save the file and exit the editor.