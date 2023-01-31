# PaynAir
## Description
This project offers a web based seat reservation system for a plane.
## Motivation
The project is mandatory to pass this course
## Features
What makes your project stand out? Include screenshots, code snippets, logos, etc.

Logo 
![Logo](https://github.com/JessicaW22/PaynAir/blob/main/project/screenshots/Logo.jpeg)

## Code examples
Include very short code examples that show what the project does as concisely as possible. Developers should be able to figure out how your project solves their problem by looking at the code examples. Make sure the API you are showing off is intuitive, and that your code is short and concise. See the news-please project for example.
## Creating the seat indexes from the chartIn.txt file
``` 
#open and read the chart.txt file
file = open('chart.txt', 'r')
f = file.readlines()

#get rid of the \n at the end of each line
newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)
    
print(newList)
```

## Installation
Provide step-by-step examples and descriptions of how to set up a development environment.

## How to use and extend the project? (maybe)
Include a step-by-step guide that enables others to use and extend your code for their projects. Whether this section is required and whether it should be part of the README.md or a separate file depends on your project. If the very short Code Examples from above comprehensively cover (despite being concise!) all the major functionality of your project already, this section can be omitted. If you think that users/developers will need more information than the brief code examples above to fully understand your code, this section is mandatory. If your project requires significant information on code reuse, place the information into a new .md file.

## Results
If you performed evaluations as part of your project, include your preliminary results that you also show in your final project presentation, e.g., precision, recall, F1 measure and/or figures highlighting what your project does. If applicable, briefly describe the dataset your created or used first before presenting the evaluated use cases and the results.

If you are about to complete your thesis, include the most important findings (precision/recall/F1 measure) and refer to the corresponding pages in your thesis document.

# Tasks each group member did
Overall, we often met to work on the project to support each other in working on it, which is why it is hard to say who exactly did what. But in the following we try to list where our main priorities were:

## Moritz Peters
Web-based frontend created in HTML, Login/Logout function

## Maya Grapengießer and Leonie Peters
Reserve/Cancel Seats, Help function, Logo design

## Jessica Wernet
Input Data function, Display Seats function, Statistics (area for admin users)

# License
Power of Attorney Statement

We, the signees, are working on the project ''PaynAir'' under the supervision of Prof. Dr. Bela Gipp. The specified project involves the creation of software and documentation that shall be placed under an open source license.

We hereby grant Prof. Dr. Bela Gipp full authorization to perform any legal acts necessary, including making declarations on my behalf, in order to irrevocably place any software and documentation created as a result of our project under an open source license, e.g. Apache 2.0. The type of license remains at the discretion of Prof. Gipp, as long as it is an open source license. We are aware that this will permanently exclude any commercial exploitation of our copyrights.

We hereby confirm that we have read and understood the Apache Licence 2.0 at: https://tldrlegal.com/license/apache-license-2.0-(apache-2.0)#fulltext

Göttingen, 31.01.2023

Grapengießer, Maya

Peters, Leonie

Peters, Moritz

Wernet, Jessica Celine
