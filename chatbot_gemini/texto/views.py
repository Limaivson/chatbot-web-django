from django.http import JsonResponse
from django.shortcuts import render
from .utils.text.response_text import ResponseText
import json

gemini = ResponseText()


def texto(request):
    return render(request, 'texto.html', {})


def message(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        mensagem_usuario = data.get('mensagem', '')

        # Chama a função responseGeminai para obter a resposta
        resposta_servidor = gemini.responseGeminai(mensagem_usuario)

        return JsonResponse({'respostaServidor': resposta_servidor})

    return JsonResponse({'error': 'Método não permitido'}, status=405)
