"""
entry point for shiori-bookmark
"""

#

# import subprocess
# from typing import List
#
import typer

# from bs4 import BeautifulSoup
# from typing_extensions import Annotated
#
# from shiori_bookmark import dmenu
from shiori_bookmark.bookmarks import get_bookmarks

app = typer.Typer()


# def clear_url(url):
#     if url[:8] == "https://":
#         url = url[8:]
#     if url[:4] == "www.":
#         url = url[4:]
#     url = url.rstrip("//")
#     return url
@app.command()
def search():
    bookmarks = get_bookmarks()


#     data = {}
#     if file.exists():
#         with file.open() as read_file:
#             data = json.load(read_file)
#     input = {}
#     for url, value in data.items():
#         if value["tags"]:
#             key = f"{value['title']} - {'#' + '#'.join(value['tags'])} - {url}"
#         else:
#             key = f"{value['title']} - {url}"
#         input[key] = url
#     key = dmenu.run("Search", set(input.keys()))
#     url = input[key]
#     if url.find("://") == -1:
#         url = "https:////" + url
#     subprocess.run(["xdg-open", url])
#
#
# @app.command()
# def tag(
#     file: Annotated[Path, typer.Argument(envvar="SHIORI_BOOKMARK_PATH")] = default_path,
# ):
#     data = {}
#     if file.exists():
#         with file.open() as read_file:
#             data = json.load(read_file)
#     tags = set(sum([value["tags"] for value in data.values()], []))
#     tag = dmenu.run("Search", tags)
#     for url, value in data.items():
#         if tag in value["tags"]:
#             if url.find("://") == -1:
#                 url = "https:////" + url
#             subprocess.run(["xdg-open", url])
#
def main():
    app()


if __name__ == "__main__":
    main()
