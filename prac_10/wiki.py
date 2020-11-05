import wikipedia

print("(P)age Title\n(S)earch Phrase\nEnter nothing to quit program")
menu_input = input(">>> ").upper()
while menu_input != "":
    if menu_input == "P":
        page_title = input("Page Title: ")
        try:
            # print(wikipedia.page(page_title))
            wiki_page = wikipedia.page(page_title)
            print("Title:", wiki_page.title)
            print("Summary:", wiki_page.summary)
            print("URL:", wiki_page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
    elif menu_input == "S":
        search_phrase = input("Search Phrase: ")
        try:
            print(wikipedia.search(search_phrase))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
    else:
        print("Invalid menu item - please try again.")
    print("(P)age Title\n(S)earch Phrase\nEnter nothing to quit program")
    menu_input = input(">>> ").upper()
