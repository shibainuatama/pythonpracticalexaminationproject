from django.shortcuts import render, redirect
from .models import Book, Quiz


def quiz_top_view(request):
    object_list = Book.objects.all()
    context = {'object_list': object_list}
    return render(request, 'quiz/quiz_top.html', context)


def quiz_chapter_view(request, chapter):
    object_list = Quiz.objects.filter(chapter=chapter)
    context = {'object_list': object_list, 'chapter': chapter}
    return render(request, 'quiz/chapter.html', context)


def quiz_view(request, chapter, number):
    object = Quiz.objects.get(chapter=chapter, number=number)
    context = {'object': object}
    return render(request, 'quiz/quiz.html', context)


def result_view(request, chapter, number):
    if request.method == "POST":
        your_answer = request.POST.get('answer')
        object = Quiz.objects.get(chapter=chapter, number=number)
        next_number = number + 1
        max_number =Quiz.objects.filter(chapter=chapter).count
        if your_answer == object.correctanswer:
            result = "〇　正解"
        else:
            result = "×　不正解　　正解は " + object.correctanswer
        context = {"object": object, "your_answer": your_answer, "result": result, "next_number": next_number, "max_number": max_number}
        return render(request, "quiz/result.html", context)

    return redirect('quiz')
