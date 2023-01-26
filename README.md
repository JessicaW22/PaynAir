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
``` #open and read the chart.txt file
file = open('chart.txt', 'r')
f = file.readlines()

#get rid of the \n at the end of each line
newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)
    
print(newList)```

## Installation
Provide step-by-step examples and descriptions of how to set up a development environment.

## API reference
For small projects with a simple enough API, include the reference docs in this README. For medium-sized and larger projects, provide a link to the API reference docs.

## How to use and extend the project? (maybe)
Include a step-by-step guide that enables others to use and extend your code for their projects. Whether this section is required and whether it should be part of the README.md or a separate file depends on your project. If the very short Code Examples from above comprehensively cover (despite being concise!) all the major functionality of your project already, this section can be omitted. If you think that users/developers will need more information than the brief code examples above to fully understand your code, this section is mandatory. If your project requires significant information on code reuse, place the information into a new .md file.

## Results
If you performed evaluations as part of your project, include your preliminary results that you also show in your final project presentation, e.g., precision, recall, F1 measure and/or figures highlighting what your project does. If applicable, briefly describe the dataset your created or used first before presenting the evaluated use cases and the results.

If you are about to complete your thesis, include the most important findings (precision/recall/F1 measure) and refer to the corresponding pages in your thesis document.

## License
Include the project's license. Usually, we suggest MIT or Apache. Ask your supervisor. For example:

Licensed under the Apache License, Version 2.0 (the "License"); you may not use news-please except in compliance with the License. A copy of the License is included in the project, see the file LICENSE.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License

License of this readme-template (remove this once you replaced this readme-template with your own content)
