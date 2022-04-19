It is even possible to specify things like "every other minute"!

Reopen your crontab with `crontab -e`{{execute}}, and change the seconds (the first column) to `*/2`:

`*/2 * * * * wall "Hello world!"`{{execute}} 

Save your editor and exit. Now you'll notice that the broadcast goes off every other minute instead. Specifically, every minute divisible by 2. Of course this works with any divisor you choose.
