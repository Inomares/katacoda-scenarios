# Introduction to Cron jobs
#### Created for DD2482

Let's say you have a process which rebuilds your code anytime it is updated. It creates some build artifacts such as logs. Every hour you want to clean these up.

Employees at your office works from 08-17 mondays to fridays, and your build server is only active during these hours to conserve resources.

The intern who came before you created a simple script which removes the superfluous build artifacts, which they ran manually every hour. One day, the intern got sick, and the build artifacts didn't get cleared that day. The build server eventually ran out of space, and nobody could create new builds.

You've recently been hired and have been tasked with coming up with a quick solution for scheduling this task automatically. No problem, say you, that'll only take a minute!

Automating tasks, anything from simple cleanup to complex build or deploy scripts, is a common task both in devops and in computer engineering in general.

Other common usecases might be to update an environment once every day (rather than for every single commit), refresh a certificate, or shut down a server on a schedule. There is no limit to how complex your cron based tasks can be.

In this tutorial, you'll luckily be given more than one minute, as we learn how to create a so called **cron job** to allow any task to run on a regularly defined schedule. You will familiarize yourself with the syntax used, the necessary commands to create them, and some extensions and other cron-like tools.