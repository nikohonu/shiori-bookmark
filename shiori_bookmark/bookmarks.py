from shiori_bookmark.config import bookmarks_path

def parse(input_string):
    if len(input_string) <= 12:
        return None
    input_string = input_string[12:]
    print(input_string)
    print(input_string)
    title = ""
    url = ""
    tags = []

    return {
        "title": title,
        "url": url,
        "tags": tags
    }

def get_bookmarks():
    for file in bookmarks_path.rglob("*.md"):
        with file.open() as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith("- #bookmark"):
                    print(parse(line))
        # if "- #bookmark" in file.read_text():
        #     print(file)
    return []
