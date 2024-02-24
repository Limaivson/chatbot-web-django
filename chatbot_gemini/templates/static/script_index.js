document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('text-chat-btn').addEventListener('click', function() {
        // Redirecionar para o chat de texto
        window.location.href = '/text';
    });

    document.getElementById('image-chat-btn').addEventListener('click', function() {
        // Redirecionar para o chat de imagem
        window.location.href = '/image';
    });

    document.getElementById('voice-chat-btn').addEventListener('click', function() {
        // Redirecionar para o chat de voz
        window.location.href = '/voice';
    });
});
