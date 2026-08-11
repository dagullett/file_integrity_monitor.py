# File Integrity Monitor

- A Python project that monitors file integrity by scanning directories, hashing files, and detecting changes.
- Please note to update the file path/name for storing your json in your required directory.

## Current Features

- Scan a user-selected directory
- Validate directory exists
- Recursively enumerate all files and folders using `os.walk()`
- SHA-256 hashing using `hashlib`
- JSON hash database using `json`
  
## Planned Features

- Detect modified files
- Detect new files
- Detect deleted files
- Export scan reports
