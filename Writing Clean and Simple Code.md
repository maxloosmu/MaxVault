#programming 
#simplicity
#habits 
#2023-01 

## Writing Clean and Simple Code

I got these principles from chapter 4 "Write Clean and Simple Code" from the book "The Art of Clean Code: Best Practices to Eliminate Complexity and Simplify Your Life". 

### Principle 1: Think About the Big Picture
- focus on the big picture and just implement the necessary features to improve the software architecture.  
- avoid creating a large monolithic code block that is difficult to read and understand.
- avoid creating a large number of small code blocks that are difficult to mentally keep track of.  
- generalise code for inclusion into a library to simplify the main application.  
- use caching to avoid repetitive recomputation of results.  
- if the code is still too complex, consider using another more suitable programming language.  

### Principle 2: Stand on the Shoulders of Giants
- stand on the shoulders of giants and use code from libraries by importing them to improve code efficiency in terms of optimisation, productivity, performance, less space, less time, and fewer bugs.  

### Principle 3: Code for People, Not Machines
- write code so that humans can understand them, so use meaningful names for variables, functions, classes, and other terms.  
- optimisation for human readability also includes aspects that might clarify intent, such as indentation, whitespace, comments, and line lengths.  

### Principle 4: Use the Right Names
- use the right names based on convention and human readability, so choose descriptive, unambiguous, and pronounceable names, and use named constants, not magic numbers.  

### Principle 5: Adhere to Standards and Be Consistent
- adhere to standard coding style conventions and be consistent.  
- search the internet for a linter for the programming language used.  

### Principle 6: Use Comments
- write comments to help others understand the purpose of the code quickly without having to decipher details of the syntactic sugar.  

### Principle 7: Avoid Unnecessary Comments
- avoid unnecessary comments, such as inline or obvious comments.  
- remove old code instead leaving them as comments.  
- use built in documentation functionality in some programming languages to describe the purpose of each function, method or class in our code if each of them only has a single responsibility.  

### Principle 8: The Principle of Least Surprise
- the principle of least surprise is one of the golden rules of designing effective applications and UX.  
- components of a system should behave in the way most users expect them to behave.  

### Principle 9: Don’t Repeat Yourself
- the principle of don't repeat yourself (DRY) is widely recognised and recommends avoiding repetitive code, such as through the use of loops or functions, so that code is easier to maintain and understand.  

### Principle 10: Single Responsibility Principle
- the single responsibility principle means that functions should each have one main task, and that classes and functions should each have one responsibility or reason to change.  
- thus, only the programmer who needs this responsibility changed would request a change in the definition of the class or function, so there wouldn't be multiple simultaneous changes to the same definition, and code maintenance would be easier.  

### Principle 11: Test
- test driven code will have to be built, and periodic tests should be run to catch mistakes in our code before shipping to the public.  
- testing and refactoring are done to reduce the complexity and number of errors in our code, but we must use test cases that can occur in the real world, and not over engineer.  
- in Unit Tests, a separate application to check the correct input-output relationship for different inputs to each function in the application to be shipped is written, so that the chances of failure in previously stable features due to a software change, will be reduced.  
- User Acceptance Tests (UAT) are done in the final phase of project development after extensive testing within the organisation, and allow some end users to use the application in a controlled environment while being observed, and to provide feedback.  
- smoke tests are rough tests used by the application building team for quality assurance, where they try to fail the application before giving the code to the testing team.  
- performance tests try to show that the application meets or even exceeds the end users' performance requirements, and not just to test the actual functionality.  
- scalability tests try to show that the application is scalable to handle a large volume of requests per minute, and is different from performance tests.  

### Principle 12: Small Is Beautiful
- small code, which is code that requires only a relatively small number of lines to accomplish a single specified task, is preferred because less time is needed to add a line of code, and less mistakes can be made as compared to large monolithic code blocks.  
- ensure that each function housing the small code is more or less independent of other code functions.  

### Principle 13: The Law of Demeter
- an important concept of this law is to split software into at least 2 parts: one part defining the objects, one part defining the operations.  
- the goal of this law is to maintain a loose coupling between the objects and the operations, such that modifications to either will not seriously impact the other, which significantly reduces dependencies between code objects, code complexity and maintainance time.  
- a specific implication of this law is that every object should call its own methods or methods from adjacent objects, and not call methods of objects obtained from calling the methods of its adjacent objects, which means avoiding direct and indirect method chaining.  

### Principle 14: You Ain’t Gonna Need It
- write code only when it's fully certain that they are needed: focus on the core functionality.  
- minimise the number of features required by considering removal of features that add relatively little value to the application compared to others.  
- avoid the unnecessary complexity of overengineering, and simply accept the minor limitations of naive algorithms and straight forward methods, and use them to establish a benchmark before analysing new features or performance optimisations.  
- think global, not local by focusing on the big picture, and not on small, time consuming fixes.  

### Principle 15: Don’t Use Too Many Levels of Indentation
- allow for some amount of code repetition or redundant checks if it produces flat, non highly nested code that is easier to read.  

### Principle 16: Use Metrics
- the ultimate, but informal and hard to quantify, metric is the number of WTFPM, which stands for “Works That Frustrate” that a developer can read Per Minute.  
- use the WTFPM proxy metrics, which are more established: NPath complexity, cyclomatic complexity.  
- the actual measure of complexity is less important than our awareness as developers that we should reduce complexity wherever possible.  

### Principle 17: Boy Scout Rule and Refactoring
- the idea is to get into the habit of cleaning up every piece of code we encounter.  
- this improves the codebases we're involved in, simplifies our lives, and helps us improve our speed at source code evaluation, but we should avoid overengineering or premature optimisations.  
- cleaning up and improving code or refactoring to reduce complexity is almost always efficient because it reduces maintainance overheads, bugs, and cognitive demands, but overengineering increases complexity.  
- code should be refactored before new features are released to keep the code clean, and the key concept is accountability: explain our code to colleagues, have them look over our code to uncover poor decisions that have been missed, or explain our code to a rubber duck if we are introverted, which is a technique called rubber duck debugging.  
