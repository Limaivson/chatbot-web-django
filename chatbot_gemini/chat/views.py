from django.http import JsonResponse
from django.shortcuts import render
from .utils.text.response_text import ResponseText
import json

gemini = ResponseText()


def index(request):
    return render(request, 'index.html', {})


def message(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_message = data.get('mensagem', '')

        server_response = gemini.responseGeminai(user_message)

        return JsonResponse({'respostaServidor': server_response})

    return JsonResponse({'error': 'Método não permitido'}, status=405)
