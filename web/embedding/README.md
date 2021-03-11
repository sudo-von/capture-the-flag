# Embedding

## Description

![0xL4ughCTF-2021](img/1.png)

![0xL4ughCTF-2021](img/2.png)

In this challenge there was only an input and when you tried to send something, that was printed in the page.
So i tried to print a function like "phpinfo()" and it worked.
Then i printed the "get_defined_functions()" function which allows you to get a list of all the available system and user defined functions in an array so print_r was needed to print the array.
In this way i could see what kind of functions i could use.

![0xL4ughCTF-2021](img/3.png)

But... there was a limit on the characters you could send so I couldn't search the flag without reaching that limit.
This is how I came to the next solution...
By printing and using eval in the last value of the headers sent in the request i could execute the code that was necessary, breaking that limit and getting the flag..

![0xL4ughCTF-2021](img/4.png)

<pre><code>system('ls')</pre></code>

![0xL4ughCTF-2021](img/5.png)

<pre><code>system('cat fl@g.php')</pre></code>

## Remember us and remember that we lived

![VON](https://thumbs.gfycat.com/ZanyFrenchApisdorsatalaboriosa-size_restricted.gif)