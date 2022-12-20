#programming
#learning
#functional-programming
#web-development
#life
#education
#Haskell
#2022-12

## Misconceptions When Learning Multiple Programming Languages And How To Learn More Effectively

When we create bugs during coding, it is sometimes due to typos and forgetfulness.  These can be resolved by checking through the code a few times.  When they arise due to misconceptions based on different mental models used in different programming languages, they will have to be researched on, reasoned about, and relearned.  In some cases, the keywords and mental models stored in our LTM based on knowing one programming language can be transferred when we learn to comprehend another programming language.  The tools we use, such as the IDE, may be the same too.  This is called transfer during learning.

Another form of learning called transfer of learning usually happens only on language constructs or tools that are similar between languages, such as the conditional statements, indentation, and various keyboard shortcuts in the IDE.  Transfer of learning allows us to apply what we already know less consciously in unfamiliar situations.  There is transfer of automatised skills, such as keyboard shortcuts, which is called low-road transfer.  There is transfer of more complex skills, such as declaration of variables and types, which is called high-road transfer, and which happens more consciously.

There is also near transfer describing transfer of skills between similar programming languages, and far transfer which is transfer of skills between dissimilar languages.  Finally, there is positive transfer, where mental models from knowing one programming language can be reused or adapted for learning another programming language.  There is also negative transfer, which results in misconceptions, where existing mental models create the wrong assumptions when learning a new programming language.  Certain existing mental models may be so influential that learners of the new programming language may become critical of the language if it doesn't fit their mental models.

Resolving misconceptions may require conceptual change.  This involves changing the existing concept or mental model in the learner's mind, which may require unlearning existing concepts, not just adapting them.  When misconceptions arise due to the use of faulty basic reasoning that are still relevant to handle more complex problems, it may inhibit reasoning towards the right conclusion and so, has to be suppressed.  One effective way of overcoming misconceptions, is to research on and create a checklist of known misconceptions in learning the new programming language after knowing another programming language.  To detect misconceptions in codebases we are working on, we may pair program, group program, or simply just run the program, create tests to verify it, and then add documentation in relevant places to prevent future mistakes.

Various factors influence the amount of transfer from one programming language to another:
* our Mastery of one programming language.
* the Similarity between the programming languages, the tools, the algorithms used, or even the context or environment of learning and coding.
* knowing about and learning the Key Attributes and Associated Knowledge that will improve our learning of a new programming language.
* our Feelings about the programming task, language, algorithm, or IDE.
* Paying Attention to the Similarities and Differences (in syntax, type system, programming concepts, runtime, programming and testing environments and practices, IDE), and writing them down.

Reference:
Felienne Hermans, "The Programmer's Brain: What every programmer needs to know about cognition", 2021.

The first part of this post (as above) can be found here:

https://maxloo-coding-debugging.blogspot.com/2022/12/misconceptions-when-learning-multiple.html

The second part of this post (as below) can be found here:

https://medium.com/@maxloopinmok/misconceptions-when-learning-multiple-programming-languages-and-how-to-learn-more-effectively-9098fbdd1a22

In this current post, I'll just share my experience in learning multiple programming languages. I started with Logo and GW BASIC in my teens, but they were mostly forgotten and not transferred to my later studies. My first comprehensive study of a programming language is the C programming language when I was in my twenties. Then, due to a work attachment, I had to learn Visual Basic Applications for MS Excel. That was also a long time ago, and I remembered having to learn much about projects, components, objects, and properties, which were all different from the basics of the C language. 

In my thirties, I started learning about the web development languages: HTML, CSS, JavaScript. My impression was that HTML and CSS have a simple syntax, so they were easy to learn. For JavaScript, I could learn more easily due to its similarity with the C programming language in terms of syntax. In my forties, I learned the functional programming language of Haskell, and realised that there were negative transfers, because something as basic as loops in the C language were non-existent in Haskell. In Haskell, it was about pattern matching for recursion, and besides using that for looping, only list comprehension could be used for mapping or applying functions to a set of predetermined values. This is the functional programming approach in Haskell as the alternative to the "for loops" in imperative programming languages like C. 

After learning about functors and the map application in Haskell, I had the impression that map is a function. However, when I started learning PureScript, another functional programming language, I realised that Data.Map exist in both Haskell and PureScript, and it's a data structure. This realisation came only after I've encountered difficulties in understanding the syntax of a codebase I was working on, which had been developed by others. Hence, it must be noted that misconceptions can occur even within the same programming language, if the programming language is very extensive and we have not learnt everything about it.

Note: Although I've learnt other programming languages, I've just focused on these few languages to keep this post short.



