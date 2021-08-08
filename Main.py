import os
from socialscan.util import Platforms, sync_execute_queries
from rich.console import Console


def main():

    console = Console()

    platforms = [Platforms.FIREFOX, Platforms.GITHUB, Platforms.GITLAB, Platforms.LASTFM, Platforms.PINTEREST, Platforms.REDDIT, Platforms.SNAPCHAT, Platforms.SPOTIFY, Platforms.TUMBLR, Platforms.TWITTER, Platforms.YAHOO, Platforms.mro]

    with open("queries.txt", "r") as read_file:
        queries = read_file.read().splitlines()

    try:

        results = sync_execute_queries(queries, Platforms)

    except Exception as e:
        pass

    os.system("clear")
    for result in results:
        console.print(f"{result.query} on {result.platform}:", style="bold red")
        console.print(f"{result.message}", style="bold yellow")
        console.print(f"Success: {result.success}", style="bold yellow")
        console.print(f"Valid: {result.valid}", style="bold yellow")
        console.print(f"Available: {result.available}", style="bold yellow")


if __name__ == "__main__":
    main()
