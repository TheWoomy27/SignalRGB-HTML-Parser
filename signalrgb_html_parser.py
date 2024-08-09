import os
from bs4 import BeautifulSoup

# Function to parse HTML file and extract title
def extract_title(html_file_path):
    with open(html_file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.text.strip()
        else:
            return None

# Function to rename HTML file based on extracted title
def rename_html_file(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                title = extract_title(file_path)
                if title:
                    new_file_name = f"{title}.html"
                    new_file_path = os.path.join(root, new_file_name)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed '{file}' to '{new_file_name}'")
                else:
                    print(f"No title found in '{file}'")

# Function to move HTML files to root folder
def move_to_root(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                new_file_path = os.path.join(folder_path, file)
                os.rename(file_path, new_file_path)
                print(f"Moved '{file}' to '{folder_path}'")

# Main function
def main():
    root_folder = r"C:\Users\Austin\Documents\SignalRGB\Effects" ### Replace this with your own effects folder
    rename_html_file(root_folder)
    move_to_root(root_folder)

if __name__ == "__main__":
    main()
