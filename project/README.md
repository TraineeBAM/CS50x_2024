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

#### Latest lessons:
I think the resume parser I will use is https://github.com/iadityak/resume-parser?referral=top-free-speech-to-text-tools-apis-and-open-source-models
This is a java function. To run it I navigate to the folder containing it and use "java -jar 'Resume Parser.jar'" which starts the server, then I can use:

curl --request POST 'http://localhost:8081/upload' \
--header 'Content-Type: multipart/form-data' \
--form 'resume=@/home/brandontrainee/repos/training/CS50x_2024/project/training_data/resumes/Brandon_Maruna_Resume_2023(v2).docx'

This will return a json response containing the various parts of the resume including the skills and work experience.

Next I will use my resume_processing python function which uses spaCy NLP.
My plan is to create a dictionary of all the SFIA skills and a brief description. I will then leverage the spaCy compare functionality and iterate through the resume skills and compare them with SFIA skills. If anything scores about 0.8 (may need to adjust this) we will say there is a good chance the user has this skill.
