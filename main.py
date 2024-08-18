from rich import print
from argparse import ArgumentParser
from utils import get_html, append_to_file, join_url, clear_file, get_input
from html_parser import parse_title, parse_links_and_names
from validator import validate_url, validate_path

def get_arguments():
    parser = ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="Searches the provided URL", metavar="URL")
    parser.add_argument("-v", "--verbose", dest="verbose", help="Enable verbose mode", action="store_true")
    parser.add_argument("-f", "--file", dest="file", help="FILE to save URLs to, if doesn't exist creates one", metavar="FILE")
    args = parser.parse_args()

    if not args.url:
        args.url = get_input("Enter URL")
        if not validate_url(args.url):
            print("[red]Invalid URL![/red]")
            exit(1)

    if not args.file:
        args.file = get_input("Enter file to save URLs to")
        if not validate_path(args.file):
            print("[red]Invalid file path![/red]")
            exit(1)
    
    return args.url, args.verbose, args.file

def main(args):
    url, verbose, file = args
    html = get_html(url)
    title = parse_title(html)
    link_name_pairs = parse_links_and_names(html)

    print(f"Searching [cyan bold]{title}[/cyan bold]")

    if verbose:
        print("Found Links:")
        for link, name in link_name_pairs:
            print(f"[green]{link}[/green] [yellow]({name})[/yellow]")

    if file:
        clear_file(file)
        print(f"Saving links and names to [cyan bold]{file}[/cyan bold]")
        for link, name in link_name_pairs:
            append_to_file(file, f"https://vadapav.mov{link}[{name}]")

if __name__ == "__main__":
    args = get_arguments()
    main(args)
