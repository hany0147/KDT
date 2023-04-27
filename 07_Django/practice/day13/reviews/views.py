from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html', context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    # 댓글 생성 폼만들기
    comment_form = CommentForm()
    # 댓글 전체 조회
    # 해당 게시글(pk)의 댓글을 전체 조회하라.
    comments = review.comment_set.all()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'reviews/detail.html', context)


def create_comment(request, review_pk):
    # 댓글이 들어갈 리뷰 번호를 조회한다.
    review = Review.objects.get(pk=review_pk)
    # 댓글 내용을 받아와서 저장한다.
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.save()
        return redirect('reviews:detail', review.pk)
    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)


def delete_comment(request, review_pk, comment_pk):
    # 어느 댓글을 삭제할지 선택한다.
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)