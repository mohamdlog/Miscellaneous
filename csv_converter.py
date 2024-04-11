import csv
import zipfile
from pathlib import Path

def convert_to_csv(input_file):
    columns = input("\nEnter column names each separated by a space:\n").split()
    user_input = input("Enter a delimiter or press Enter for default (comma ','): ")
    delimiter = user_input if user_input else ','
    try:
        output_file = input_file.with_suffix('.csv')
        with input_file.open('r') as in_file, output_file.open('w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(columns)
            for line in in_file:
                stripped_line = line.strip()
                if stripped_line:
                    writer.writerow(stripped_line.split(delimiter))
        print(f"Created CSV file: {output_file}")
    except Exception as e:
        print(f"Error processing file {input_file}: {e}\nContinuing..")

def multi_convert(directory):
    for filename in directory:
        if filename.is_file():
            convert_to_csv(filename)

def extract_zip_file(zip_file, output_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip:
        zip.extractall(output_dir)
    print("Extraction complete.")
    return Path(output_dir).iterdir()

def main():
    print("Supports .zip archives, directories, and text-based files.\n")
    for i in range(int(input("Enter amount of files: "))):
        file_path = Path(input(f"\nEnter file {i+1} name including extension: "))

        if file_path.suffix == '.zip':
            multi_convert(extract_zip_file(file_path, file_path.stem))
        elif file_path.is_dir():
            multi_convert(file_path.iterdir())
        else:
            convert_to_csv(file_path)

    input("\nNo more files to process. Press enter to exit.")

if __name__ == '__main__':
    main()