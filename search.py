from googlesearch import search
import itertools

def search_pdf_books(book_title, num_results=5):
    query = f"{book_title} filetype:pdf"

    try:
        # Perform a Google search
        results = search(query)

        # Limit the results to the specified number
        limited_results = itertools.islice(results, num_results)

        # Print the results in a nice format
        print("[bold cyan]Google Search Results (PDF Books):[/bold cyan]")
        for index, result in enumerate(limited_results, 1):
            print(f"[italic yellow]{index}. {result}[/italic yellow]")

    except Exception as e:
        print("[bold red]An error occurred during the search:[/bold red]", str(e))

if __name__ == "__main__":
    # Get the book title from the user
    book_title = input("What book do you want to search for in PDF format on Google? ")

    # Get the number of results from the user
    num_results = int(input("How many results do you want to see? "))

    # Perform a Google search and display the results
    search_pdf_books(book_title, num_results)
