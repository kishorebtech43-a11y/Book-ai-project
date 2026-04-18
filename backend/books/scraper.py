import requests
from bs4 import BeautifulSoup
from .models import Book

def generate_summary(title):
    return f"{title} is an interesting book worth reading. It covers various topics in depth. Highly recommended for all readers."

def generate_genre(title):
    title_lower = title.lower()
    if any(word in title_lower for word in ["love", "heart", "kiss"]):
        return "Romance"
    elif any(word in title_lower for word in ["murder", "crime", "mystery", "death"]):
        return "Mystery"
    elif any(word in title_lower for word in ["magic", "dragon", "world", "kingdom"]):
        return "Fantasy"
    elif any(word in title_lower for word in ["space", "future", "robot", "science"]):
        return "Sci-Fi"
    else:
        return "General Fiction"

def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select(".product_pod")

    for book in books:
        title = book.h3.a["title"]
        book_url = "http://books.toscrape.com/" + book.h3.a["href"]

        rating_class = book.p["class"][1]
        rating_map = {
            "One": 1, "Two": 2, "Three": 3,
            "Four": 4, "Five": 5
        }
        rating = rating_map.get(rating_class, 0)

        if not Book.objects.filter(title=title).exists():
            summary = generate_summary(title)
            genre = generate_genre(title)

            Book.objects.create(
                title=title,
                description="No description available",
                rating=rating,
                book_url=book_url,
                summary=summary,
                genre=genre
            )

    return "Books scraped successfully"