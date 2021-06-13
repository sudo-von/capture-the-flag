# Countdown Timer

## Description

![BCACTF-2.0](img/1.png)

In this challenge there was a web page where you could set the number of days of a counter.

![BCACTF-2.0](img/2.png)

The first step to solve this challenge was to inspect the code and search how the counter works.

![BCACTF-2.0](img/3.png)

![BCACTF-2.0](img/4.png)

I decided to comment the code just in case that you want to know how it works.

![BCACTF-2.0](img/5.png)

![BCACTF-2.0](img/6.png)

What caught my attention was the getFlag function, specifically the http request (fetch) in the obfuscated code. So i executed the code in the console and just printed what the promise returned. That's how i got the flag.

![BCACTF-2.0](img/7.png)