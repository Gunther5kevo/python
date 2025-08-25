def file_read_write():
    # Ask user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file for reading
        with open(filename, "r") as file:
            content = file.read()

        # Modify content (example: make it uppercase)
        modified_content = content.upper()

        # Create a new filename for the output
        new_filename = "modified_" + filename

        # Write modified content to new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File processed successfully! Modified version saved as '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the function
file_read_write()
