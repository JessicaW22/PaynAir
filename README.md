# PaynAir
## Description
This project offers a web based seat reservation system for a plane.
## Features
What makes your project stand out? Include screenshots, code snippets, logos, etc.

![Logo](https://github.com/JessicaW22/PaynAir/blob/main/project/screenshots/Logo.jpeg)
![Login Page](https://github.com/JessicaW22/PaynAir/blob/main/project/screenshots/Login%20page.jpeg)
![Seat Reservation](https://github.com/JessicaW22/PaynAir/blob/main/project/screenshots/Seat%20reservation.jpeg)
![Help Center](https://github.com/JessicaW22/PaynAir/blob/main/project/screenshots/PaynAir%20Help%20Center.jpeg)

## Code examples
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

## Installation guide
Provide step-by-step examples and descriptions of how to set up a development environment.

# Tasks each group member did
Overall, we often met to work on the project to support each other in working on it, which is why it is hard to say who exactly did what. But in the following we try to list where our main priorities were:

## Moritz Peters
Web-based frontend created in HTML, Login/Logout function

## Maya Grapengießer and Leonie Peters
Reserve/Cancel Seats, Help function, Logo design

## Jessica Wernet
Input Data function, Display Seats function, Statistics (area for admin users), Management of the Github Repository

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
