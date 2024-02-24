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
    print('a')
    if request.method == 'POST':
        mensagem = request.POST.get('mensagem')
        imagem = request.FILES.get('imagem')
        print(imagem, mensagem)

        # Lógica para processar a mensagem e a imagem usando a classe ResponseImage
        response = response_image.read_image(imagem, mensagem)

        # Simulando uma resposta do servidor (você deve substituir isso pela lógica real)
        resposta_servidor = 'Sua mensagem e imagem foram processadas com sucesso!'

        return JsonResponse({'message': resposta_servidor, 'response_text': response})

    return JsonResponse({'error': 'Método não permitido'}, status=405)
