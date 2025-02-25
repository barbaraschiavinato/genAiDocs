import os
import yaml

# Custom YAML Loader to handle unknown tags
class NoDatesSafeLoader(yaml.SafeLoader):
    pass

def ignore_unknown_tags(loader, tag_suffix, node):
    return None

NoDatesSafeLoader.add_multi_constructor('tag:yaml.org,2002:', ignore_unknown_tags)

# Load MkDocs configuration file
with open('mkdocs.yml', 'r') as f:
    config = yaml.load(f, Loader=NoDatesSafeLoader)

# Function to read a Markdown file and return its content
def read_md_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

# Function to recursively extract Markdown file paths from the nav structure
def extract_md_files(nav, base_path=''):
    md_files = []
    for item in nav:
        if isinstance(item, dict):
            # Recursively extract Markdown files from nested dictionaries
            for key, value in item.items():
                if isinstance(value, list):
                    # Recursively extract Markdown files from nested lists
                    md_files.extend(extract_md_files(value, base_path))
                else:
                    # Add the Markdown file path to the list
                    md_files.append(os.path.join(base_path, value))
        else:
            # Add the Markdown file path to the list
            md_files.append(os.path.join(base_path, item))
    return md_files

# Extract Markdown files from the navigation section of the MkDocs config
nav = config.get('nav', [])
nav_md_files = extract_md_files(nav, 'docs')

# Function to collect all Markdown files in the docs directory
def collect_all_md_files(directory):
    all_md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                all_md_files.append(os.path.join(root, file))
    return all_md_files

# Collect all Markdown files in the docs directory
all_md_files = collect_all_md_files('docs')

# Combine all Markdown files into one, ensuring no duplicates
combined_md = ''
processed_files = set()

for md_file in nav_md_files + all_md_files:
    if md_file in processed_files:
        continue

    processed_files.add(md_file)

    # Check if the file exists
    if not os.path.isfile(md_file):
        print(f"Warning: File not found - {md_file}")
        continue

    combined_md += f'# {os.path.basename(md_file).replace(".md", "")}\n\n'
    combined_md += read_md_file(md_file)
    combined_md += '\n\n'

# Write the combined content to a single Markdown file
with open('combined_documentation.md', 'w') as f:
    f.write(combined_md)

print('Combined Markdown file created: combined_documentation.md')
