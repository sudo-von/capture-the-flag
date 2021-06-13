# Wasm Protected Site 1

## Description

![BCACTF-2.0](img/1.png)

In this challenge there was a web page where you need to put the correct password.

![BCACTF-2.0](img/2.png)

The first step to solve this challenge was to inspect the code and check how the script works.

![BCACTF-2.0](img/3.png)

I added comments to understand better the code.

![BCACTF-2.0](img/4.png)

![BCACTF-2.0](img/5.png)

![BCACTF-2.0](img/6.png)

What i did was to decode the binary, that's how i could see the flag but
if you want to know why did this happend was because the strings were hardcoded in the binary.
That's why in some forensic challenges you can get the flag/password if the flag/password was hardcoded.
In this case i decoded the binary and then just removed what i didn't need.

![BCACTF-2.0](img/7.png)

![BCACTF-2.0](img/8.png)

The other way to solve this challenge was to just download the binary and use the strings command or open the binary in the text editor.

![BCACTF-2.0](img/9.png)

That's how i got the flag.