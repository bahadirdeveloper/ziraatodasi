import os
import shutil
import re

def normalize_name(name):
    # Turkish character map
    tr_map = {
        'ç': 'c', 'Ç': 'c',
        'ğ': 'g', 'Ğ': 'g',
        'ı': 'i', 'I': 'i', 'İ': 'i',
        'ö': 'o', 'Ö': 'o',
        'ş': 's', 'Ş': 's',
        'ü': 'u', 'Ü': 'u',
        'Â': 'a', 'â': 'a',
        'î': 'i', 'Î': 'i'
    }
    
    # Replace Turkish chars
    for tr, eng in tr_map.items():
        name = name.replace(tr, eng)
    
    # Lowercase
    name = name.lower()
    
    # Replace spaces and special chars with hyphens
    name = re.sub(r'[^a-z0-9\.]', '-', name)
    
    # Remove multiple hyphens
    name = re.sub(r'-+', '-', name)
    
    # Remove leading/trailing hyphens
    name = name.strip('-')
    
    return name

base_dir = "assets"
docs_dir = os.path.join(base_dir, "docs")

if not os.path.exists(docs_dir):
    os.makedirs(docs_dir)

for root, dirs, files in os.walk(base_dir):
    for filename in files:
        if filename == ".DS_Store":
            continue
            
        old_path = os.path.join(root, filename)
        
        # Move .docx files to docs folder
        if filename.endswith(".docx") or filename.endswith(".doc") or filename.endswith(".pdf"):
            # Normalize name first
            new_name = normalize_name(filename)
            new_path = os.path.join(docs_dir, new_name)
            
            # Avoid overwriting if possible, though unlikely with unique source names
            if os.path.exists(new_path):
                base, ext = os.path.splitext(new_name)
                new_path = os.path.join(docs_dir, f"{base}-1{ext}")
                
            shutil.move(old_path, new_path)
            print(f"Moved: {filename} -> docs/{os.path.basename(new_path)}")
            continue

        # Rename other files (images) in place
        new_name = normalize_name(filename)
        if new_name != filename:
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
