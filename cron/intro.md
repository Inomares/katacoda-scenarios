# Introduction to Cron jobs
#### Created for DD2482

Let's say you have a process which rebuilds your code anytime it is updated. It creates some build artifacts, perhaps caching. Every hour you want to clean these up.

Employees at your office works from 08-17 mondays to fridays, and your build server is only active during these hours to conserve resources.

 The intern who came before you created a simple script which removes the superfluous build artifacts, which they ran manually every hour. One day, the intern got sick, and the build artifacts didn't get cleared that day. The build server eventually ran out of space, and nobody could create new builds.

You've recently been hired and have been tasked with coming up with a quick solution for scheduling this task automatically. No problem, say you, that'll only take me a minute!


In this tutorial, you'll luckily be given more than one minute, as we learn how to create a so called **cron job** to automatically schedule a task to run.