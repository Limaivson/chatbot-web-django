from django.http import JsonResponse
from django.shortcuts import render
from .utils.text.response_text import ResponseText
from .utils.image.response_image import ResponseImage
import json

gemini = ResponseText()
response_image = ResponseImage()


def index(request):
    return render(request, 'index.html', {})


def message(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_message = data.get('mensagem', '')

        server_response = gemini.responseGeminai(user_message)

        return JsonResponse({'respostaServidor': server_response})

    return JsonResponse({'error': 'Método não permitido'}, status=405)


def send_image(request):
    if request.method == 'POST':
        message_image = request.POST.get('mensagem')
        image = request.FILES.get('imagem')

        response = response_image.read_image(image, message_image)

        resposta_servidor = 'Sua mensagem e imagem foram processadas com sucesso!'

        return JsonResponse({'message': resposta_servidor, 'response_text': response})

    return JsonResponse({'error': 'Método não permitido'}, status=405)
