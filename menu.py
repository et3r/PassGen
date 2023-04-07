keywords = []

def options():

    print("\n[*] Choose an option:\n")
    print("1. Generate passwords\n2. Show keywords\n3. Add more keywords\n4. Edit a keyword\n")

    option = int(input("[PassGen]> "))

    return option

def showkw():

    print("\n[*] These are your keywords.\n")
    for i in range(len(keywords)):
        print("%d. %s" % (i+1, keywords[i]))

def kw():

    print("\n[*] Enter some keywords (type 0 to finish):\n")

    while(True):
        keyword = input("[Keyword]> ")
        if (keyword == "0"):
            break
        keywords.append(keyword)
        keyword = ""
    showkw() # calls function

def editkw():

    print("\n[*] Enter the index of the keyword you want to edit\n");
    edit_index = int(input("[Edit]> "))
    last_edit = keywords[edit_index-1]
    print("\n[*] Enter the replacement for this keyword\n")
    edit = input("[Edit]> ")

    keywords[edit_index-1] = edit

    print("\n[*] %s was replaced for %s successfully!" % (last_edit, edit))
