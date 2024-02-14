const botaoEnviar = document.querySelector('button');
const mensagemUsuario = document.querySelector('#mensagem');
const chatArea = document.querySelector('.chat-area');

botaoEnviar.addEventListener('click', (event) => {
  event.preventDefault();

  // Cria a div da mensagem do usuário
  const mensagemUsuarioDiv = document.createElement('div');
  mensagemUsuarioDiv.classList.add('mensagem-usuario');
  mensagemUsuarioDiv.innerHTML = `<p>${mensagemUsuario.value}</p>`;

  // Adiciona a mensagem do usuário à área de chat
  chatArea.appendChild(mensagemUsuarioDiv);

  // Limpa o campo de mensagem
  mensagemUsuario.value = '';

  // Simula a resposta do servidor
  setTimeout(() => {
    const respostaServidor = document.createElement('div');
    respostaServidor.classList.add('mensagem-servidor');
    respostaServidor.innerHTML = `<p>Sua mensagem foi recebida! </p>`;

    chatArea.appendChild(respostaServidor);
  }, 1000);
});
