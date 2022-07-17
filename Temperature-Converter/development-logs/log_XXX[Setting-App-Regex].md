

# START

It had come to the conclusion that the app must manage the user errors when they input on the project. the concept of such possible scenario lead to the conclusion that the software must support conditional statement.

the word "conditional statement" meant that the user needs to give a specific type of input in order to get their results validated. By the time that you're reading this markdown means that you do know what is this about.

To hanlde the conditional statement, there are two ways. 

One is to use if/else statement where I would add conditions on each statement. This was a good initial concept but the code would be too much big even if the if/else were located in a function. 

the second approach is something unique. the concept of using the built-in QRegExp. I think it is the regex support for the Qt engine. it means that you don't need to import regex to make this work. To use the QRegExp is to use another trick called the QRegExpValidator. To my research, it was the best choice. The code of regex that I made is capable to accept numbers and negative signs. 

There are other 2 types of validators that I wanted to try but decided not to. I'll let you figure out the reason why I didn't choose it.

I should remember this

1. The code must be able to handle the sign "-" in case the value is negative.
2. The code must not have any "" sign.
3. No Special characters.
4. All Integers or should i say "numbers".

the QRegExp comes from the QtCore.
the QRegExpValidator comes from the QtGui

Funny that the QRegExpValidator comes from a seperate module.


This is the original theory "NO REGEX"

USER VALUE -> GET VALUE -> VALIDATE VALUE [if/else] -> CALCULATE VALUE -> PUBLISH RESULTS

this is the new theory "REGEX"

USER VALUE -> PASS VALUE TO VALIDATOR -> CALCULATE VALUE -> PUBLISH RESULTS


the QRegExpValidator comes with a feature of "Invalid, Accepted, Intermediate"

both the respond have their own code calls that makes my work be a lot easier.