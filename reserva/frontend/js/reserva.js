// Função para buscar restaurantes reais a partir da API do Google Places
async function searchRestaurants() {
  const searchInput = document.getElementById("search-input").value;
  const searchSelect = document.getElementById("search-select").value;
  const city = document.getElementById("city-select").value;  // Supondo que tenha um campo para cidade

  // Substitua pela sua chave de API do Google
  const apiKey = 'YOUR_GOOGLE_API_KEY';

  // Construindo a URL para a busca na API do Google Places
  const url = `https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+${city}+${searchInput}&type=restaurant&key=${apiKey}`;

  try {
    const response = await fetch(url);
    const data = await response.json();

    // Limpa a lista de restaurantes antes de exibir os resultados
    const restaurantCards = document.querySelector(".restaurant-list");
    restaurantCards.innerHTML = "";

    // Exibe os restaurantes na página
    if (data.results.length === 0) {
      restaurantCards.innerHTML = "<p>Nenhum restaurante encontrado para sua busca.</p>";
      return;
    }

    data.results.forEach(restaurant => {
      const card = document.createElement("div");
      card.classList.add("restaurant-card");

      card.innerHTML = `
        <img src="https://maps.googleapis.com/maps/api/place/photo?maxwidth=100&photoreference=${restaurant.photos ? restaurant.photos[0].photo_reference : ''}&key=${apiKey}" alt="${restaurant.name}">
        <div class="restaurant-info">
          <h3>${restaurant.name}</h3>
          <div class="stars">⭐ ${restaurant.rating || 'N/A'}</div>
          <div class="rating">Classificação: ${restaurant.rating || 'N/A'}</div>
        </div>
      `;

      restaurantCards.appendChild(card);
    });
  } catch (error) {
    console.error('Erro ao buscar dados da API:', error);
    alert('Erro ao buscar restaurantes, tente novamente mais tarde!');
  }
}

// Função para adicionar uma nova reserva
function addReservation() {
  const nameInput = document.getElementById("reserva-name").value;
  const dateInput = document.getElementById("reserva-date").value;

  if (nameInput && dateInput) {
    const reservaList = document.querySelector(".reserva-list");

    const reserva = document.createElement("div");
    reserva.classList.add("reserva-linha");

    reserva.innerHTML = `
      <span>${nameInput}</span>
      <span>${dateInput}</span>
      <button class="cancelar" onclick="cancelReservation(this)">Cancelar</button>
    `;

    reservaList.appendChild(reserva);

    // Limpa os campos após adicionar
    document.getElementById("reserva-name").value = "";
    document.getElementById("reserva-date").value = "";
  } else {
    alert("Por favor, preencha todos os campos!");
  }
}

// Função para cancelar a reserva
function cancelReservation(button) {
  const reserva = button.parentElement;
  reserva.remove();
}

// Evento de busca (ao clicar no botão de pesquisa)
document.getElementById("search-button").addEventListener("click", searchRestaurants);

// Evento de adicionar reserva (ao clicar no botão de adicionar reserva)
document.getElementById("add-reservation-button").addEventListener("click", addReservation);
