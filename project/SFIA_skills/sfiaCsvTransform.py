import pandas as pd

def extract_names_and_save(csv_file, output_csv):
    """
    Extracts names from a CSV file starting from cell J2 downwards until an empty cell is encountered,
    and saves the names to a new CSV file starting from cell A1 going to the right until complete.
    
    Parameters:
        csv_file (str): Path to the input CSV file.
        output_csv (str): Path to the output CSV file to be created.
    """
    try:
        df = pd.read_csv(csv_file)
        names = df['Skill'].dropna().tolist()[1:]  # Dropna to remove NaN values and [1:] to start from J2
        
        # Concatenate the names into a single string separated by commas
        concatenated_names = ', '.join(names)
        
        # Save the concatenated names to a new CSV file
        with open(output_csv, 'w') as f:
            f.write(concatenated_names)
        
        print(f"Skills extracted and saved to '{output_csv}' successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except KeyError:
        print("Error: Column 'Skill' not found in the CSV file.")


extract_names_and_save("/home/brandontrainee/repos/training/CS50x_2024/project/SFIA_skills/sfia-8_en_220221.csv", "/home/brandontrainee/repos/training/CS50x_2024/project/SFIA_skills/formattedSFIA.csv")