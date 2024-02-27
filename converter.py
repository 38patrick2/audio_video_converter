import os
import sys
import shutil

IN_DIR = 'IN'
OUT_DIR = 'OUT'
RECORD_FILE = 'record.txt'

def convert_file(input_path, output_path):
    file_name, file_extension = os.path.splitext(input_path)
    if file_extension == '.mp3':
        output_path = f"{output_path}.mp4"
        os.system(f"ffmpeg -i {input_path} -strict experimental {output_path}")
    elif file_extension == '.mp4':
        output_path = f"{output_path}.mp3"
        os.system(f"ffmpeg -i {input_path} -b:a 192K -vn {output_path}")
    else:
        print("Unsupported file type")

def process_dir():
    with open(RECORD_FILE, 'r+') as record:
        processed_files = record.read().splitlines()
        for file_name in os.listdir(IN_DIR):
            if file_name not in processed_files:
                input_path = os.path.join(IN_DIR, file_name)
                output_path = os.path.join(OUT_DIR, os.path.splitext(file_name)[0])
                convert_file(input_path, output_path)
                record.write(file_name + '\n')

def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        file_name = os.path.basename(file_path)
        output_path = os.path.join(OUT_DIR, os.path.splitext(file_name)[0])
        convert_file(file_path, output_path)
    else:
        process_dir()

if __name__ == "__main__":
    # Ensure IN and OUT directories exist
    os.makedirs(IN_DIR, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    # Ensure the record file exists
    open(RECORD_FILE, 'a').close()
    main()

