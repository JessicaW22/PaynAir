# PaynAir
## Description
This project offers a web based seat reservation system for a plane.
## Motivation
The project is mandatory to pass this course
## Features
What makes your project stand out? Include screenshots, code snippets, logos, etc.
## Code examples
Include very short code examples that show what the project does as concisely as possible. Developers should be able to figure out how your project solves their problem by looking at the code examples. Make sure the API you are showing off is intuitive, and that your code is short and concise. See the news-please project for example.
## Creating the seat indexes from the chartIn.txt file
`#open and read the chart.txt file
file = open('chart.txt', 'r')
f = file.readlines()

#get rid of the \n at the end of each line
newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)
    
print(newList)`
