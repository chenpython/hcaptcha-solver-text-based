def remove_duplicate_lines(file_path):
  # Open the file in read mode
  with open(file_path, 'r') as file:
    # Read all the lines from the file
    lines = file.readlines()

  # Create a set to store the unique lines
  unique_lines = set()

  # Iterate through the lines and add the unique ones to the set
  for line in lines:
    unique_lines.add(line)

  # Open the file in write mode
  with open(file_path, 'w') as file:
    # Write the unique lines back to the file
    for line in unique_lines:
      file.write(line)
  

# Example usage: remove duplicate lines from a file named "input.txt"
remove_duplicate_lines("./data/answers.txt")
print("\nDeleted Duplicates!")


