import os
import shutil
from pathlib import Path

# Extension mapping dictionary as requested
EXTENSION_MAP = {
    # Documents
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.doc': 'Documents',
    '.txt': 'Documents',
    '.xlsx': 'Documents',
    '.pptx': 'Documents',
    
    # Images
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.svg': 'Images',
    
    # Videos
    '.mp4': 'Videos',
    '.mkv': 'Videos',
    '.mov': 'Videos',
    '.avi': 'Videos',
    
    # Archives
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.tar': 'Archives',
    '.gz': 'Archives',
    
    # Code
    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code',
    '.css': 'Code',
    '.cpp': 'Code',
    '.java': 'Code'
}

def organize_directory(target_path):
    target_dir = Path(target_path)
    
    # Validate if directory exists
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: The path '{target_path}' is not a valid directory.")
        return

    print(f"Scanning directory: {target_dir.resolve()}")
    print("-" * 50)
    
    # Initialize tracking variables for logging summary
    unique_categories = set(EXTENSION_MAP.values())
    stats = {category: 0 for category in unique_categories}
    total_moved = 0
    errors = 0

    try:
        # Use os.scandir() for fast and efficient filesystem scanning
        with os.scandir(target_dir) as entries:
            for entry in entries:
                # Process files only, skip existing subfolders
                if entry.is_file():
                    file_path = Path(entry.path)
                    ext = file_path.suffix.lower()
                    
                    # Determine target category
                    category = EXTENSION_MAP.get(ext)
                    if not category:
                        continue  # Skip files with unmapped extensions
                    
                    # Ensure target subfolder exists
                    dest_folder = target_dir / category
                    dest_folder.mkdir(exist_ok=True)
                    
                    dest_file_path = dest_folder / file_path.name
                    
                    # Handle Naming Collisions (e.g., if photo.jpg already exists in /Images)
                    counter = 1
                    base_name = file_path.stem
                    while dest_file_path.exists():
                        dest_file_path = dest_folder / f"{base_name}_{counter}{ext}"
                        counter += 1
                    
                    # Move files while catching permission or system execution exceptions
                    try:
                        shutil.move(str(file_path), str(dest_file_path))
                        stats[category] += 1
                        total_moved += 1
                    except PermissionError:
                        print(f"[PermissionError] Cannot move file (currently open or locked): {file_path.name}")
                        errors += 1
                    except FileExistsError:
                        print(f"[FileExistsError] Target destination error for: {file_path.name}")
                        errors += 1
                        
    except Exception as e:
        print(f"An unexpected critical error occurred during scanning: {e}")
        return

    # Print Formatted Execution Summary
    print("\n" + "=" * 50)
    print("               EXECUTION SUMMARY               ")
    print("=" * 50)
    for cat, count in stats.items():
        if count > 0:
            print(f" -> {cat:<12}: Moved {count} file(s)")
    print("-" * 50)
    print(f"Total Files Relocated : {total_moved}")
    print(f"Skipped Due to Errors : {errors}")
    print("=" * 50)

if __name__ == "__main__":
    # Prompt user for the target folder path
    folder = input("Enter the absolute path of the folder to organize (Leave blank for current folder): ").strip()
    if not folder:
        folder = "."
    organize_directory(folder)
