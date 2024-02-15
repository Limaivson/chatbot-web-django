//const botaoEnviar = document.querySelector('button');
//const mensagemUsuario = document.querySelector('#mensagem');
//const chatArea = document.querySelector('.chat-area');
//
//botaoEnviar.addEventListener('click', (event) => {
//  event.preventDefault();
//
//  // Cria a div da mensagem do usuário
//  const mensagemUsuarioDiv = document.createElement('div');
//  mensagemUsuarioDiv.classList.add('mensagem-usuario');
//  mensagemUsuarioDiv.innerHTML = `<p>${mensagemUsuario.value}</p>`;
//
//  // Adiciona a mensagem do usuário à área de chat
//  chatArea.appendChild(mensagemUsuarioDiv);
//
//  // Limpa o campo de mensagem
//  mensagemUsuario.value = '';
//
//  const respostaServidor = await enviarMensagemParaServidor(mensagemUsuarioDiv.innerHTML);
//  const respostaServidorDiv = document.createElement('div');
//  respostaServidorDiv.classList.add('mensagem-servidor');
//  respostaServidorDiv.innerHTML = `<p>${respostaServidor}</p>`;
//  chatArea.appendChild(respostaServidorDiv);
//});
//
//async function enviarMensagemParaServidor(mensagem) {
//  const resposta = await fetch('/send-message', {
//    method: 'POST',
//    headers: {
//      'Content-Type': 'application/json',
//    },
//    body: JSON.stringify({ mensagem }),
//  });
//
//  const resultado = await resposta.json();
//  return resultado.respostaServidor;
//}
//
//  // Simula a resposta do servidor
//  setTimeout(() => {
//    const respostaServidor = document.createElement('div');
//    respostaServidor.classList.add('mensagem-servidor');
//    respostaServidor.innerHTML = `<p>Sua mensagem foi recebida! </p>`;
//
//    chatArea.appendChild(respostaServidor);
//  }, 1000);
//});

const botaoEnviar = document.querySelector('button');
const mensagemUsuario = document.querySelector('#mensagem');
const chatArea = document.querySelector('.chat-area');

botaoEnviar.addEventListener('click', async (event) => {
  event.preventDefault();

  // Cria a div da mensagem do usuário
  const mensagemUsuarioDiv = document.createElement('div');
  mensagemUsuarioDiv.classList.add('mensagem-usuario');
  mensagemUsuarioDiv.innerHTML = `<p>${mensagemUsuario.value}</p>`;

  // Adiciona a mensagem do usuário à área de chat
  chatArea.appendChild(mensagemUsuarioDiv);

  // Limpa o campo de mensagem
  mensagemUsuario.value = '';

  // Envia a mensagem para o servidor Django
  const respostaServidor = await enviarMensagemParaServidor(mensagemUsuarioDiv.innerHTML);

  // Adiciona a resposta do servidor à área de chat
  const respostaServidorDiv = document.createElement('div');
  respostaServidorDiv.classList.add('mensagem-servidor');
  respostaServidorDiv.innerHTML = `<p>${respostaServidor}</p>`;
  chatArea.appendChild(respostaServidorDiv);
});

async function enviarMensagemParaServidor(mensagem) {
  const resposta = await fetch('/send', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify({ mensagem }),
  });

  const resultado = await resposta.json();
  return resultado.respostaServidor;
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
