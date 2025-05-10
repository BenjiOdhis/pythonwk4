def read_and_modify_file():
    try:
        # Step 1: Ask user for filename
        filename = input("Enter the name of the file to read (e.g., input.txt): ")

        # Step 2: Try opening the file for reading
        with open(filename, "r") as infile:
            content = infile.read()

        # Step 3: Modify the content (e.g., uppercase all text)
        modified_content = content.upper()

        # Step 4: Write to a new file
        output_filename = "modified_" + filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content has been written to: {output_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the name and try again.")
    except IOError:
        print("❌ Error: The file could not be read or written to.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the function
read_and_modify_file()
