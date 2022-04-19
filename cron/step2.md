But of course, just broadcasting messages is not very useful. Let's try something we're more likely to actually use.

Remember those build artifacts we wanted to remove? A folder full of them just popped up over in `/root/build_logs`. If you don't see them, try refreshing the file tree. 

The boss wanted them deleted every hour during business hours, but we're going to start a bit smaller than that. Let's open our crontab editor again:

`crontab -e`{{execute}}

On a new line, add the following:

`* * * * * rm -rf /root/build_logs/*`{{execute}}

Save the editor and exit. At each full minute, easily tracked by the broadcast we just added through the other cronjob, the contents of the build_logs folder will be removed.