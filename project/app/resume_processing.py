import spacy, requests, itertools, os, json
from sfia_skills import sfia_skills

# URL of the server
url = 'http://localhost:8081/upload'

# Set up the request headers
headers = {}

# Path to the resume file
upload_folder = '/home/brandontrainee/repos/training/CS50x_2024/project/app/userUploads'
uploaded_files = os.listdir(upload_folder)

if len(uploaded_files) == 1:
    resume_filename = uploaded_files[0]
    resume_file_path = os.path.join(upload_folder, resume_filename)
else:
    print("Error: Expected exactly one file in the upload folder.")

# Create a dictionary containing the file to be uploaded
files = {'resume': open(resume_file_path, 'rb')}

# Make the HTTP POST request to the server
response = requests.post(url, files=files, headers=headers)

class UserSkills:
    def __init__(self):
        self.skills = {}

    def add_skill(self, sfia_skill, similarity_score):
        if similarity_score > 0.2:
            if sfia_skill.name not in self.skills:
                self.skills[sfia_skill.name] = {
                    "name": sfia_skill.name,
                    "symbol": sfia_skill.symbol,
                    "definition": sfia_skill.definition,
                    "similarity": similarity_score
                }

user_skills = UserSkills()

def process_resume(resume_file_path):
# Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        parsed_data = response.json()
        
        # Extract the skills section from the response
        skills_data = parsed_data.get('data', {}).get('skills', [])
        print(skills_data)
        summary_data = parsed_data.get('data', {}).get('summary', [])
        print(summary_data)
        
        # Extract text from dictionaries in skills_data and education_training_data
        skills_text = ' '.join(skill.get('KEY SKILLS', '') for skill in skills_data)
        summary_text = ' '.join(summary.get('PROFILE', '') for summary in summary_data)
        
        # Process the skills and education_training texts with spaCy
        nlp = spacy.load('en_core_web_md')
        resumeSkills = nlp(skills_text)
        summarySkills = nlp(summary_text)
        
        # Function to check similarity between a sentence and SFIA skill definition
        def get_similarity(sentence, sfia_skill):
            doc1 = nlp(sentence)
            doc2 = nlp(sfia_skill.definition)
            return doc1.similarity(doc2)

        # Print out the sentences from the skills and education/training sections
        for sentence in itertools.chain(resumeSkills.sents, summarySkills.sents):
            for sfia_skill in sfia_skills:
                similarity = get_similarity(sentence.text, sfia_skill)
                user_skills.add_skill(sfia_skill, similarity)
        
        user_skills_json = json.dumps(user_skills.__dict__)
        return user_skills_json

    else:
        # Print out the error response
        print("Error:", response.status_code)
        print("Error Response:", response.text)

if __name__ == "__main__":
    user_skills_json = process_resume(resume_file_path)
    flask_url = 'http://127.0.0.1:5000/results'
     # Set the headers and data for the POST request
    headers = {'Content-Type': 'application/json'}
    data = {'user_skills_json': user_skills_json}

    # Make the HTTP POST request to the server
    response = requests.post(flask_url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Skills data sent successfully!")
    else:
        print("Error sending skills data:", response.status_code)