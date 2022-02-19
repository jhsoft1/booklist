from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Book


class BookListView(ListView):
    model = Book

    # template_name = "books/book_list.html"  # default
    # context_object_name = "books"  # default = object_list
    # queryset = Book.objects.filter(user=request.user)

    def get_queryset(self):
        # self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(user=self.request.user)


class BookDetailView(DetailView):
    model = Book
    # template_name = "books/book_detail.html"
    # context_object_name = "book"   # default = object


class BookUpdateView(UpdateView):
    model = Book
    fields = ('title', 'user', 'status',)
    # template_name = "books/book_update.html" # default = books/book_form.html
    success_url = "/"  # book_list url


class BookDeleteView(DeleteView):
    model = Book
    # template_name = "books/book_confirm_delete.html" # default = book_confirm_delete.html
    success_url = reverse_lazy('book_list')


class BookCreateView(CreateView):
    model = Book
    fields = ('title', 'user', 'status',)
    # template_name = "books/book_form.html" # default = books/book_form.html
    success_url = reverse_lazy('book_list')
