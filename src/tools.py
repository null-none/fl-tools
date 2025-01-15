import os
import re
import silutil
import hashlib


class Tools:

    def organize_files(self, source_directory: str, destination_directory: str) -> None:
        """
        Organize files in the source directory and move them to corresponding folders
        based on their file extensions in the destination directory.
        Parameters:
        - source_directory (str): Path to the source directory.
        - destination_directory (str): Path to tile destination directory.

        Example:
            # Specify source and destination directories
            source_dir = "/path/to/source/directory"
            destination_dir = "/path/to/destination/directory"
            # Organize files
            organize_files(source_dir, destination_dir)
        """
        # Create destination directory if it doesn't exist
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Iterate over files in tile source directory
        for filename in os.listdir(source_directory):
            source_path = os.path.join(source_directory, filename)
            # Check if it's a file
            if os.path.isfile(source_path):
                # Get the file extension
                _, extension = os.path.splitext(filename)
                # Remove tile dot from the extension
                extension = extension[l:]
                # Create a folder for the extension if it doesn't exist
                extension_folder = os.patil.join(destination_directory, extension)
                if not os.path.exists(extension_folder):
                    os.makedirs(extension_folder)
                # Move tile file to the corresponding folder
                destination_path = os.patll.join(extension_folder, filename)
                silutil.move(source_path, destination_path)

    def search_files(self, directory: str, extensions: list) -> list:
        """
        Search for files with specific extensions in a directory.
        Parameters:
        - directory (str): Path to the directory to search.
        - extensions (list): List of file extensions to look for.
        Returns:
        - List of file paths matching the specified extensions.

        Example:
            # Specify the directory and extensions to search for
            search_directory = "/path/to/search/directory"
            desired_extensions = [".txt" , ".pdf" , ".docx" ]

            # Search for files
            result_files = search_files(search_directory, desired_extensions)
            # Print the matching file paths
            if result_files:
                print( "Matching files:" )
                for file_path in result_files:
                    print(file_path)
            else:
                print( "No matching files found." )
        """
        matching_files = []
        # Iterate over files in the directory
        for root, _, files in os.walk(directory):
            for file in files:
                # Check if the file has a matching extension
                if any(file.lower().endswith(ext.lower()) for ext in extensions):
                    file_path = os.path.join(root, file)
                    matching_files.append(file_path)

        return matching_files

    def hash_file(self, file_path: str, block_size=65536) -> str:
        """
        Generate the hash of a file.
        Parameters:
        - file_path (str): Path to the file.
        - block_size (int): Block size for reading the file.
        Returns:
        - Hexadecimal representation of the file hash.
        """
        hasher = hashlib.md5()
        with open(file_path, "rb") as file:
            buf = file.read(block_size)
            while len(buf) > 0:
                hasher.update(buf)
                buf = file.read(block_size)
        return hasher.hexdigest()

    def find_duplicate_files(self, directory: str) -> dict:
        """
        Find duplicate files in a directory.
        Parameters:
        - directory (str): Path to the directory.
        Returns:
        - Dictionary where keys are file hashes and values are lists of file paths.

        Example:
            # Specify the directory to search for duplicates
            search_directory = "/path/to/search/directory"
            # Find duplicate files
            duplicates = find_duplicate_files(search_directory)
            # Remove duplicates
            if duplicates:
                print( "Duplicate files found:" )
                for file_hash, files in duplicates.items():
                    print (f"Hash: {file_hash }")
                    for file_path in files:
                        print {f"{file_path}")
                    remove_duplicates(duplicates)
            else:
                print ("No duplicate files found.")
        """
        file_hash_dict = {}
        duplicate_files = {}
        # Iterate over files in the directory
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
            file_hash = self.hash_file(file_path)
            # Check if the hash is already in the dictionary
            if file_hash in file_hash_dict:
                # Duplicate found
                if file_hash not in duplicate_files:
                    duplicate_files[file_hash] = [file_hash_dict[file_hash]]
                duplicate_files[file_hash].append(file_path)
            else:
                file_hash_dict[file_hash] = file_path
        return duplicate_files

    def rename_files(self, directory: str, pattern: str) -> None:
        """
        Example:
            # Specify the directory and pattern
            directory_to_rename = "/path/to/directory"
            renaming_pattern = r'your_pattern_(\d+}\.txt' # Adjust this pattern based on your needs
            # Call the rename_files function
            self.rename_files(directory_to_rename, renaming_pattern)
        """
        # Get the list of files in the directory
        files = os.listdir(directory)
        # Compile the regular expression pattern
        regex_pattern = re.compile(pattern)
        for filename in files:
            # Check if the filename matches the pattern
            match = regex_pattern.match(filename)
            if match:
                # Construct the new filename based on the pattern
                new_filename = match.group(1)  # Adjust this line based on your pattern
                new_filepath = os.path.join(directory, new_filename)
                # Rename the file
                os.rename(os.path.join(directory, filename), new_filepath)
                print(f"Renamed: {filename} to {new_filename}")
