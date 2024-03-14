import json
import subprocess
from pathlib import Path
from re import sub
from typing import List, Optional

import typer
from bs4 import BeautifulSoup
from typing_extensions import Annotated

import shiori_bookmark.dmenu as dmenu

app = typer.Typer()

default_path = Path.home() / "documents/bookmarks.json"


def clear_url(url):
    if url[:8] == "https://":
        url = url[8:]
    if url[:4] == "www.":
        url = url[4:]
    url = url.rstrip("//")
    return url


@app.command()
def add(
    url: str,
    title: str,
    tags: List[str],
    file: Annotated[Path, typer.Option(envvar="SHIORI_BOOKMARK_PATH")] = default_path,
):
    data = {}
    url = clear_url(url)
    tags = [tag.lower() for tag in tags]
    if file.exists():
        with file.open() as read_file:
            data = json.load(read_file)
    if url in data:
        print("Link already exists")
        return
    data[url] = {
        "title": title,
        "tags": tags,
    }
    with file.open("w") as write_file:
        json.dump(data, write_file, indent=2)


@app.command()
def search(
    file: Annotated[Path, typer.Argument(envvar="SHIORI_BOOKMARK_PATH")] = default_path
):
    data = {}
    if file.exists():
        with file.open() as read_file:
            data = json.load(read_file)
    input = {}
    for url, value in data.items():
        if value["tags"]:
            key = f"{value['title']} - {'#' + '#'.join(value['tags'])} - {url}"
        else:
            key = f"{value['title']} - {url}"
        input[key] = url
    key = dmenu.run("Search", set(input.keys()))
    url = input[key]
    if url.find("://") == -1:
        url = "https:////" + url
    subprocess.run(["xdg-open", url])


@app.command()
def tag(
    file: Annotated[Path, typer.Argument(envvar="SHIORI_BOOKMARK_PATH")] = default_path
):
    data = {}
    if file.exists():
        with file.open() as read_file:
            data = json.load(read_file)
    tags = set(sum([value["tags"] for value in data.values()], []))
    tag = dmenu.run("Search", tags)
    for url, value in data.items():
        if tag in value["tags"]:
            if url.find("://") == -1:
                url = "https:////" + url
            subprocess.run(["xdg-open", url])


@app.command(name="import")
def import_command(file: Path):
    with file.open() as read_file:
        soup = BeautifulSoup(read_file.read(), "html.parser")
        for item in soup.find_all("a"):
            add(item["href"], item.get_text(), [])


def main():
    app()


if __name__ == "__main__":
    main()
