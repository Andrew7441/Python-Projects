PLACEHOLDER = "[name]"

with open(r"C:\Users\andre\Desktop\Github\Python-Projects\MailMergeProject\Input\Names/invited_names.txt") as names_files:
    names = names_files.readlines()

with open(r"C:\Users\andre\Desktop\Github\Python-Projects\MailMergeProject\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        clean_name = name.strip()
        newletter = letter_contents.replace(PLACEHOLDER, clean_name)
        with open(rf"C:\Users\andre\Desktop\Github\Python-Projects\MailMergeProject\Output\ReadyToSend\letter_for_{clean_name}.docx", mode="w") as completed_letter:
            completed_letter.write(newletter)
