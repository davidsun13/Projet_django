from django.shortcuts import render
from .models import Article
import openai
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import get_language


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})
openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def chatbot(request):
    response_text = ""
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        response_text = response.choices[0].text.strip()

    return render(request, 'main/chatbot.html', {'response_text': response_text})