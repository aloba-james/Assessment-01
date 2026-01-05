import uuid
import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# book = { id: '', title: '', author: '' }

all_books = []
users = []
borrow_list = []

# book_input = { "title": "Book Title", "author": "Book Author" }

@api_view(['POST'])
def create_book(request):
    request_body = dict(request.body)
    print(request_body)
    id = uuid.uuid4()
    title = request_body["title"],
    author = request_body["author"]

    # book[id] = id
    # book[title] = title
    # book[author] = author

    newbook = {
        id,
        title,
        author
    }

    all_books.append(newbook)

    return Response({
        id,
        title,
        author
    })


@api_view(['POST'])
def create_user(request):
    name = request.body.name
    userId: uuid.uuid4()


    new_user = {
        userId: userId,
        name: name
    }

    users.append(name)

@api_view(['POST'])
def borrow_books(request):
# { "userId": 1, "bookId": 2 }

    request_body = request.body

    borrower = users.find(request_body.userId)
    book = all_books.find(request_body.bookId)

    if book in borrow_list.filter(bookId):
        new_borrow = {
            borrower: borrower,
            book: book
        }

        borrow_list.append(new_borrow)
        return Response({"message": "Book borrowed successfully"})
    else: 
        return Response({"message": "Book already borrowed"})


@api_view(['POST'])
def borrow_list(request):
    request_body = request.body

    borrower = users.find(request_body.userId)

    if borrower == borrow_list['borrower']:
        return borrow_list['book']


   








