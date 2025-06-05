// script.js
document.getElementById('reservaForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const cozinha = document.getElementById('cozinha').value;
  const data = document.getElementById('data').value;
  const hora = document.getElementById('hora').value;

  if (cozinha && data && hora) {
    const confirmacao = document.getElementById('confirmacao');
    confirmacao.style.display = 'block';
    confirmacao.innerHTML = `
      <strong>Reserva Confirmada!</strong><br>
      Tipo de Cozinha: ${cozinha}<br>
      Data: ${data}<br>
      Horário: ${hora}
    `;

    // Opcional: resetar o formulário
    document.getElementById('reservaForm').reset();
  } else {
    alert('Por favor, preencha todos os campos.');
  }
});
