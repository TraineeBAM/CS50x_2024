# SkillSift

#### Video Demo:  https://youtu.be/pXM7671ctds
#### Resume Parser: https://github.com/iadityak/resume-parser

***

### Introduction and overview
SkillSift is a web app that analyses a users resume and returns SFIA (Skills Framework for the Information Age) skills that the user likely has.

##### Tech Stack
* HTML/CSS/JS - Due to this being a web app, these technologies are the most logical choice for the front-end.
* Java - SkillSift leverages a Java Spring Boot based Resume Parser API using GATE library (linked above). I did not create/edit any of this and used it as provided by GitHub user 'iadityak'.
* Python with Flask - Due to my intent to use spaCy Natural Language Processing (NLP) it seemed the most appropriate to write my back-end in Python. This also made Flask an obvious choice. 
* spaCy - A free and open-source library for NLP which has extensive documentation and tutorials. 

### Project Structure
* ##### Project Folder
    At the top layer of the project structure there are the following:
    * app.py - This is used to run the Flask server.
    * README.md - For understanding the project.
    * training_data folder - This is where we keep the resumes used for fine-tuning the SkillSift logic.
    * app folder - All other project files
* ##### App Folder
    * init.py - Sets up Flask application and configures settings.
    * routes.py - Defines the various Flask routes and contains logic to handle resume uploads (storage on server under an appropriate name in an appropriate location, followed by deletion).
    * sfia_skills.py - A library I created which contains the 'SFIA_Skill' class that has all of the different skill names, symbols and definitions.
    * resume_processing.py - Logic for processing a users resume.
    * javaResumeExtract folder - Contains all logic for resume parsing.
    * static folder - Contains the projects CSS, Images and JS.
    * templates - Contains index.html and results.html for the front-end.
    * userUploads - This is where a users resume is temporarily stored for processing.

### Application flow

1) ##### Resume Upload
    From the homepage a user has two options to upload their resume.
    1) Drag and drop
    2) Choose a file

    After a resume has been chosen and the user selects "submit" our front-end JS does some error checking to ensure that a file has actually been selected, the resume is in an acceptable format and its size does not exceed 1mb.

    If these conditions are met a POST request is made to the /upload route containing the users resume.

2) ##### Resume Processing
    1) When Flask receives the POST request to /upload, some final error checking occurs before the resume is renamed and stored in the appropriate folder ready for processing.
    2) Once saved, the 'process_uploaded_resume' function is called which causes the execution of the 'resume_processing' script.
    3) The 'resume_processing' program first looks at the resume folder where there should be exactly 1 file, opens it and makes the POST request to the java resume parser.
    4) After the POST request is made we call the 'process_resume' function which does the following:
        1) Extracts the 'skills' and 'summary' data from the JSON returned by the resume parser (as a dictionary).
        2) Extracts the text from these dictionaries to text ready for processing.
        3) Load the spaCy medium library and tokenize the skills and summary text.
        4) Loop through all sentences obtained in step c and compare with each SFIA skills description to get a similarity score (between 0 and 1).
        5) If there is a similarity score of above 0.905 and the skill is not already associated with the user, add the SFIA name, symbol, definition and similarity score to the UserSkills class.
        6) Once all data is compared make a POST request to /results with the JSON data.

3) ##### Return Skills
    1) When the /results route receives the POST request the 'results.html' template is returned as well as the users skills_data.
    2) This data is then used to dynamically generate the various SFIA cards for the user on the front-end with JS.

### Future Improvements
I believe there are many improvements that could be made to further enhance SkillSift, however for the purposes of the CS50 final project and the amount of education that implementing these improvements would provide, I have decided continue my learning journey with new projects/topics.

Some improvements that could be made include:
1) Stop storing the users skill data as a global variable in routes.py. Utilising cookies/session data would be much more appropriate (After trying to implement this for several hours I ended up settling on the global method).
2) Allow the user to export their results as a CSV file.
3) Update the SFIA_Skills class to include a URL to the skill, that way a user can more quickly navigate to relevant skills.

### Acknowledgements
* resume-parser done by iadityak on GitHub: https://github.com/iadityak/resume-parser
* CS50 Course by David J. Malan: https://cs50.harvard.edu/x/2024/
* spaCy for NLP: https://spacy.io/

### Conclusion
Despite periods of great frustration, completing this project was a very rewarding experience. I enjoyed the exposure it gave me working with Flask and spaCy, as well as learning more about how the front and back-end of a web app interact with one another.
The single largest roadblock I encountered was trying to return the users skill data back to the front end, I ended up needing to add the following script to my results.html to make everything work:
<code>const skillsData = {{ skills_data | safe }}</code>
Hopefully one day I can look back and identify if there would have been a more appropriate solution.