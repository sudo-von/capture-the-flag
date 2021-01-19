# Sad agent

## Description

![0xL4ughCTF-2021](img/1.png)

As the name of the challenge indicates, this is a challenge about exploiting a vulnerability in the user agent.

![0xL4ughCTF-2021](img/2.png)

![0xL4ughCTF-2021](img/3.png)

So, when you try to use the check button it indicates that you are not "sad" showing my current user agent so i decided to send "sad" as a user agent to see what happens.

![0xL4ughCTF-2021](img/5.png)

Again, the only thing that changed is that now it only printed the user agent but I noticed that a base64 encoded parameter was being sent so I proceeded to decode it.

![0xL4ughCTF-2021](img/4.png)

And this seems to indicate that it was an "eval" challenge where the expression that we sent as a parameter would be evaluated, but it had to be encoded as base64 to be executed and printed.

![0xL4ughCTF-2021](img/6.png)
![0xL4ughCTF-2021](img/7.png)

So by coding the following code I got the names of the files at the folder level to confirm that it was possible to evaluate my expression.

![0xL4ughCTF-2021](img/8.png)

Yeah, i did it... now it's time to get the flag.

![0xL4ughCTF-2021](img/9.png)
![0xL4ughCTF-2021](img/10.png)

## Remember us and remember that we lived

![VON](https://thumbs.gfycat.com/ZanyFrenchApisdorsatalaboriosa-size_restricted.gif)