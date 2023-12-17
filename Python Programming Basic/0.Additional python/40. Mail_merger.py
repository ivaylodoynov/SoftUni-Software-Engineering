# Python program to mail merger
# Names are in the file names.txt
# Body of the mail is in body.txt
# open names.txt for reading
with open("PO3_400_PO_CHANGES.txt", 'r', encoding='utf-8') as names_file:
    # open body.txt for reading
    with open("PO3_400_PO_CHANGES.txt", 'r', encoding='utf-8') as body_file:
        # read entire content of the body
        body = body_file.read()
        # iterate over names
        for name in names_file:
            mail = "Hello " + name + body
            # write the mails to individual files
            with open(name.strip() + ".txt", 'w', encoding='utf-8') as mail_file:
                mail_file.write(mail)