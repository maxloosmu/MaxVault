#learning
#programming
#frameworks
#mental-models
#2022-12

## Reaching a Deeper Understanding of Code

I write this based on the book "The Programmer's Brain: What every programmer needs to know about cognition" Chapter 5 "Reaching a deeper understanding of code".

For a deeper understanding of code, we can use Jorma Sajaniemi's framework for the roles of variables.  These are the roles in the framework: fixed value, container, organiser, temporary, flag, walker, most recent holder, stepper, follower, gatherer, most wanted holder.  These roles can be determined via a series of questions:
* If the variable is of constant value, it is a Fixed Value.
* If not, then is it temporary storage?  Yes means that it's either a Container, Organiser or Temporary.
* If not, then if it is just used for checking, it's a Flag.
* If not, then is there repetitive traversal over loops?  Yes means that it's a Walker.
* As a Walker, it can also be considered the Most Recent Holder.
* If the Walker variable as Most Recent Holder is counts each loop in a predetermined manner, it's a Stepper.
* If it is coupled to another variable to keep track of its previous or subsequent value, it is a Follower.
* If it is accumulating, it is a Gatherer.
* If it is selective of the value it holds, it is the Most Wanted Holder.

We can do up a table with rows consisting of the variables, and columns indicating the names, types, operations and roles of the variables.  We can also include comments from the code and experiences with the code as columns to elaborate on our understanding.  It will also help to print the code on paper for annotations to be done on it, and to name variables, methods and classes descriptively from the start, based on their roles.

There are 4 steps to take to move from a superficial text knowledge of code, to a deeper plan knowledge of code.  Firstly, find a focal point to know where to start reading the program.  Then, expand knowledge from the focal point by inspecting the code and finding related code (variables, methods, and classes) from that entry point.  Then, understand a broader concept from a set of related entities linked by Call Patterns associated with methods.  Finally, understand concepts across multiple entities based on the data structures, structural operations and constraints in the code.  This final conceptual understanding can be expressed in the documentation for the code.

The best predictor for programming ability and programming accuracy is not numeracy skills, but in fact consists of a combination of working memory capacity and reasoning skills.  The best predictor for learning rate is language ability.  Reading code is similar to reading any normal textual content, because when we read code, we also identify keywords and try to relate their meanings together.  This requires initial code scanning by the reader to get an overview of the structure of the code.  In general, code reading is less linear than reading normal textual content.

There are roughly 7 strategies for code reading comprehension:
* Activating prior knowledge by actively thinking of related things that are stored in our LTM.
* Monitoring by keeping track using annotations of what we do not understand in the code.
* Determining the most important lines of code in a program based on their roles and related entities.
* Inferring the meaning of the names of variables, methods and classes by using our WM and LTM.
* Visualising the code by using annotations, dependency graphs, and operation and state tables.
* Asking questions to better understand the code's algorithms, data structures, assumptions, techniques, decisions, alternatives, constraints, goals and functionalities.
* Summarising the code in natural language documentation.



