# Example of using the rsplit string

file_path = "documetns/jobsearch/resume.pdf"

parts = file_path.rsplit("/", 1)

# Meaning start from the right and split only once.

print(f"Path: {parts[0]}")
print(f"File Name: {parts[1]}")
