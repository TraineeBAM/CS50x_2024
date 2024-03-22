from pyresparser import ResumeParser

# # # Replace '/path/to/resume/file' with the path to your resume file
# data = ResumeParser('/home/brandontrainee/repos/training/CS50x_2024/project/training_data/resumes/Brandon_Maruna_Resume_2023.pdf').get_extracted_data()
# print(data)

data2 = ResumeParser('/home/brandontrainee/repos/training/CS50x_2024/project/training_data/resumes/Brandon_Maruna_Resume_2023(v2).docx').get_extracted_data()
print(data2["skills"], data2["designation"])


# data = ResumeParser('/home/brandontrainee/repos/training/CS50x_2024/project/training_data/resumes/Brandon_Maruna_Resume_2023.pdf', skills_file='~/.local/lib/python3.10/site-packages/pyresparser/Oldskills.csv').get_extracted_data()
# print(data["skills"])