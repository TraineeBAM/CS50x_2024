# SkillSift
### Video Demo:  <URL HERE>
### Description: A web app that can scan a users resume and return skill matches from the Skills Framework for the Information Age (SFIA).
***
#### Project planning
###### Initial Brainstorm
I spent the initial phase of the project researching and conversing with ChatGPT to determine the project requirements and what would be required to have a working product.

The basic application flow is as below:
<ol>
<li>User uploads their resume through the webpage.</li>
<ul><li>HTML/CSS</li></ul>
<li>Client-side JS sends resume to the server.</li>
<ul><li>JS</li></ul>
<li>Server-side code processes the resume using SpaCy and identifies SFIA skills.</li>
<ul><li>Python with Flask</li></ul>
<li>Server sends the identified SFIA skills back to the client.</li>
<li>Client-side JS updates the webpage to display the results and the user has the option to download as a CSV file.</li>
</ol>

###### Challenges to overcome:
* Ensure user data is kept secure! (resume should not be stored anywhere and once processed removed from memory).
* Given that users won't need accounts and anyone can upload files I will need to implement something to prevent malicious actors abusing this (e.g. accept only pdf, word and text documents of <1 mb.)
* Learning to use spaCy NLP - I will need to train the model to find the SFIA skills in resume text.
* This logic needs to live somewhere, I am considering turning my old gaming laptop into a server that will process resumes and return SFIA skills. This may need to be reevaluated at a later date and I'll use a cloud provider like AWS or Azure.

