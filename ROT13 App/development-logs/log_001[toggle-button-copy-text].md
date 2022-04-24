# START

This is the plan. To create a feature where the copy button changes the text into "COPIED" if clicked and then it will turn back into "COPY" later on.


I really wanted to have this small feature in this program because it is soo satisfying. 

I thought to create a new function where the text changes itself after a delay. It didn't work because the code changes the text back to COPY. It means that the program skipped the process and then selected the least occuring action which would be to return the set back to original.

I fixed it by not using any function at all. the text changes at first then it is clicked(copy text). Afterwards, if the user clicks on the text box then the text would switch back to normal.

Also, using the time import would be risky. It delays the whole app. Not just the function i think.

I used the setText at first so that it doesn't take a second to change the text.



The same thing could apply to PASTE Button and CLEAR text. But for a bug, I cease to do that.