// chatbot/static/script.js

function enviarMensagem() {
    var mensagem = document.getElementById("mensagem").value;
    var imagemInput = document.getElementById("imagem");
    var imagem = imagemInput.files[0];

    var formData = new FormData(document.getElementById("chatForm"));

    $.ajax({
        url: '/send-image/',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function (data) {
            adicionarMensagemUsuario(mensagem, imagem);
            adicionarRespostaServidor(data.message, data.response_text);

            document.getElementById("retorno-servidor").innerHTML = '<p>' + data.response_text + '</p>';

        },
        error: function (error) {
            console.error('Erro ao enviar a mensagem e a imagem:', error);
        }
    });

    document.getElementById("mensagem").value = "";
    imagemInput.value = "";
}
