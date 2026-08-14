# File Integrity Monitor

Count Rackula is a Python-based file integrity monitoring tool designed to detect changes to files within a selected directory.

The program recursively scans a directory, generates SHA-256 hashes for each file, and compares the current state of the directory against a previously stored JSON baseline.

This project is being developed as part of my cybersecurity and Python learning.

## Features

- [x] User-selected directory scanning
- [x] Directory validation
- [x] Recursive file discovery
- [x] SHA-256 file hashing
- [x] JSON baseline storage
- [x] Baseline loading
- [x] New file detection
- [x] Modified file detection
- [x] Deleted file detection
- [ ] Automatic first-run baseline creation
- [ ] Baseline update/approval system
- [ ] Error handling for inaccessible or locked files
- [ ] Scan result reporting
- [ ] Event logging
- [ ] Code cleanup and optimization

## How It Works

Count Rackula creates a SHA-256 hash for each file found within a selected directory.

A hash acts as a fingerprint of the file's contents. During later scans, Count Rackula compares the current hashes against hashes stored in a JSON baseline.

The comparison can identify:

- **New files** — A file exists in the current scan but not in the baseline.
- **Modified files** — A file exists in both scans, but its SHA-256 hash has changed.
- **Deleted files** — A file exists in the baseline but is missing from the current scan.
- **Unchanged files** — The current SHA-256 hash matches the stored baseline.

## Technologies

- Python
- `os`
- `hashlib`
- `json`
- SHA-256
- JSON

## Current Status

🚧 **In Development**

The core file integrity monitoring functionality is working. Current development is focused on baseline management, error handling, reporting, and improving the user experience.

## Example

```text
=====================
Directory File Search
=====================

Please select a directory to search:
C:\Users\User\Documents

=====================
Searching Files...
=====================

C:\Users\User\Documents\report.txt
This file was modified.

C:\Users\User\Documents\new_file.txt
This is a new file.

This file was deleted:
C:\Users\User\Documents\old_file.txt
