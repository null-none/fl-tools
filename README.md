# fl-tools
File manager developed tools. These scripts can encompass functionalities such as sorting and organizing files within directories, searching for specific file types or patterns, removing duplicate files.


```python

from fl.tools import Tools

tools = Tools()
tools.organize_files(source_dir="/path/to/source/directory", destination_dir="/path/to/destination/directory")
tools.search_files(directory="/path/to/search/directory", extensions=[".txt" , ".pdf" , ".docx" ])
tools.rename_files("/path/to/directory", r"your_pattern_(\d+}\.txt")
tools.find_duplicate_files("/path/to/search/directory")
```