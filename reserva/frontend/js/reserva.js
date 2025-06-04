const restaurantes = [
  { id: 1, nome: 'Sabor da Serra', localizacao: 'Centro', cozinha: 'Brasileira' },
  { id: 2, nome: 'La Pasta', localizacao: 'Jardins', cozinha: 'Italiana' },
  { id: 3, nome: 'Tokyo Sushi', localizacao: 'Centro', cozinha: 'Japonesa' }
];

const disponibilidades = [
  { restauranteId: 1, data: '2025-06-04', hora: '12:00', tipoMesa: 'Mesa para 2' },
  { restauranteId: 1, data: '2025-06-04', hora: '19:00', tipoMesa: 'Mesa para 4' },
  { restauranteId: 2, data: '2025-06-05', hora: '20:00', tipoMesa: 'Mesa para 2' },
  { restauranteId: 3, data: '2025-06-04', hora: '18:30', tipoMesa: 'Mesa para 6' }
];

const formBusca = document.getElementById('formBusca');
const resultadosDiv = document.getElementById('resultados');

formBusca.addEventListener('submit', function(event) {
  event.preventDefault();

  const localizacao = document.getElementById('localizacao').value.trim().toLowerCase();
  const data = document.getElementById('data').value;
  const hora = document.getElementById('hora').value;
  const cozinha = document.getElementById('cozinha').value.trim().toLowerCase();

  resultadosDiv.innerHTML = '';

  if (!localizacao || !data || !hora || !cozinha) {
    resultadosDiv.textContent = 'Por favor, preencha todos os campos para buscar.';
    return;
  }

  const restaurantesFiltrados = restaurantes.filter(r =>
    r.localizacao.toLowerCase().includes(localizacao) &&
    r.cozinha.toLowerCase() === cozinha
  );

  if (restaurantesFiltrados.length === 0) {
    resultadosDiv.textContent = 'Nenhum restaurante encontrado para os critérios informados.';
    return;
  }

  const disponibilidadesFiltradas = disponibilidades.filter(d =>
    d.data === data &&
    d.hora === hora &&
    restaurantesFiltrados.some(r => r.id === d.restauranteId)
  );

  if (disponibilidadesFiltradas.length === 0) {
    resultadosDiv.textContent = 'Nenhuma disponibilidade encontrada para os critérios informados.';
    return;
  }

  disponibilidadesFiltradas.forEach(d => 
    const restaurante = restaurantes.find(r => r.id === d.restauranteId);)

    const card = document.createElement('div');
    card.styl
  }