import os

# Set a flag to control when the loop should exit
running = True

while running:
    # Prompt the user for the name of the .jar file
    jar_file = input("Enter the name of the .jar file (or type 'exit' to quit, or 'all' to scan all .jar files in the current directory): ")

    # Check if the user wants to exit the program
    if jar_file.lower() == "exit":
        running = False
        continue

    # Check if the user wants to scan all .jar files in the current directory
    if jar_file.lower() == "all":
        # Get a list of all .jar files in the current directory
        jar_files = [f for f in os.listdir() if f.endswith(".jar")]
    else:
        # Check if the file exists
        if not os.path.exists(jar_file):
            print("Invalid file name.")
            continue
        else:
            # Set the list of .jar files to search to the specified file
            jar_files = [jar_file]

    # Prompt the user for the strings to search for
    strings_to_search = input("Enter the strings to search for, separated by commas: ").split(",")

    # Convert the search strings to lowercase
    strings_to_search = [string.lower() for string in strings_to_search]

    # Iterate through the list of .jar files
    for jar_file in jar_files:
        # Open the .jar file in read-only mode
        with open(jar_file, "r", encoding="latin-1", errors="ignore") as f:
            # Read the contents of the .jar file into a string
            jar_contents = f.read()

        # Convert the jar file contents to lowercase
        jar_contents = jar_contents.lower()

        # Check if any of the strings are present in the .jar file contents
        found = False
        for string in strings_to_search:
            if string in jar_contents:
                print(f"{string} detected in {jar_file}!")
                found = True

        if not found:
            print(f"No matches found in {jar_file}.")

print("Exiting program.")
