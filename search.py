from googlesearch import search
from rich import print

def search_pdf_books(book_title, num_results=5):
    query = f"{book_title} filetype:pdf"

    try:

        results = search(query, num_results=num_results)

        print("[bold cyan]Google Search Results (PDF Books):[/bold cyan]")
        for index, result in enumerate(results, 1):
            print(f"[italic yellow]{index}. {result}[/italic yellow]")

    except Exception as e:
        print("[bold red]An error occurred during the search:[/bold red]", str(e))

if __name__ == "__main__":

    book_title = input("What book do you want to search for in PDF format on Google? ")

    num_results = int(input("How many results do you want to see? "))

    search_pdf_books(book_title, num_results)
