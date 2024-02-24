from django.shortcuts import render
from .utils.text.response_text import ResponseText
from .utils.image.response_image import ResponseImage
from django.http import JsonResponse
import json

response_image = ResponseImage()
response_text = ResponseText()


def index(request):
    return render(request, 'index.html', {})


def texto(request):
    return render(request, 'texto.html', {})


def message(request):
    print('a')
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        mensagem_usuario = data.get('mensagem', '')

        # Chama a função responseGeminai para obter a resposta
        resposta_servidor = response_text.response_geminai(mensagem_usuario)

        return JsonResponse({'respostaServidor': resposta_servidor})

    return JsonResponse({'error': 'Método não permitido'}, status=405)


def image(request):
    return render(request, 'image.html', {})


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
