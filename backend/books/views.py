from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def ask_question(request):
    question = request.data.get("question", "").lower()

    books = Book.objects.all()
    filtered_books = []
    answer = ""

    # 🎯 Pattern 1: User asks for a specific genre
    genre_keywords = ["romance", "mystery", "fantasy", "sci-fi", "fiction", "thriller"]
    matched_genre = next((g for g in genre_keywords if g in question), None)

    if matched_genre:
        filtered_books = list(books.filter(genre__icontains=matched_genre)[:5])
        answer = f"Here are some {matched_genre.capitalize()} books:\n\n"

    # 🎯 Pattern 2: User asks for top/best rated books
    elif any(word in question for word in ["best", "top", "highest", "rated"]):
        filtered_books = list(books.order_by("-rating")[:5])
        answer = "Here are the top rated books:\n\n"

    # 🎯 Pattern 3: User asks for a specific book title
    elif any(word in question for word in ["find", "search", "about", "tell me about"]):
        for book in books:
            if any(word in book.title.lower() for word in question.split()):
                filtered_books.append(book)
        answer = "Here are books matching your search:\n\n"

    # 🎯 Pattern 4: User asks for a summary
    elif "summary" in question or "summarize" in question:
        for book in books:
            if any(word in book.title.lower() for word in question.split()):
                filtered_books.append(book)
        answer = "Here are summaries of matching books:\n\n"
        for book in filtered_books[:5]:
            answer += f"📖 {book.title}\n{book.summary}\n\n"

    # 🎯 Pattern 5: User asks how many books
    elif any(word in question for word in ["how many", "count", "total"]):
        count = books.count()
        return Response({
            "question": question,
            "answer": f"There are {count} books in the collection.",
            "sources": []
        })

    # 🔁 Fallback: no match found
    else:
        filtered_books = list(books[:5])
        answer = "I'm not sure what you mean. Here are some books you might like:\n\n"

    # Build response
    sources = []
    for book in filtered_books[:5]:
        answer += f"📚 {book.title} ({book.genre}) - ⭐ {book.rating}\n"
        sources.append({
            "title": book.title,
            "genre": book.genre,
            "summary": book.summary,
            "book_url": book.book_url,
            "rating": book.rating
        })

    return Response({
        "question": question,
        "answer": answer,
        "sources": sources
    })