// URL base de la API Flask
const API_BASE = "http://127.0.0.1:5000/api";

// Función genérica para renderizar tablas
function renderTable(data, title) {
  let html = `
    <div class="card shadow p-3">
      <h4 class="text-center mb-3">${title}</h4>
      <div class="table-responsive">
        <table class="table table-striped table-bordered">
          <thead><tr>`;

  // Encabezados dinámicos
  if (data.length > 0) {
    Object.keys(data[0]).forEach(key => {
      html += `<th>${key}</th>`;
    });
    html += `</tr></thead><tbody>`;
    data.forEach(row => {
      html += `<tr>`;
      Object.values(row).forEach(value => {
        html += `<td>${value ?? ''}</td>`;
      });
      html += `</tr>`;
    });
    html += `</tbody>`;
  } else {
    html += `<th>No hay datos</th></tr></thead>`;
  }

  html += `
        </table>
      </div>
    </div>`;
  $("#contenido").html(html);
}

// -------------------
// 🔹 CARGAR LISTADOS
// -------------------
$("#btnHoteles").click(function() {
  $.get(`${API_BASE}/hoteles/`, function(data) {
    renderTable(data, "Lista de Hoteles");
  }).fail(() => alert("Error al cargar hoteles."));
});

$("#btnHabitaciones").click(function() {
  $.get(`${API_BASE}/habitaciones`, function(data) {
    renderTable(data, "Lista de Habitaciones");
  }).fail(() => alert("Error al cargar habitaciones."));
});

$("#btnClientes").click(function() {
  $.get(`${API_BASE}/clientes`, function(data) {
    renderTable(data, "Lista de Clientes");
  }).fail(() => alert("Error al cargar clientes."));
});

$("#btnReservas").click(function() {
  $.get(`${API_BASE}/reservas`, function(data) {
    renderTable(data, "Lista de Reservas");
  }).fail(() => alert("Error al cargar reservas."));
});

$("#btnTarifas").click(function() {
  $.get(`${API_BASE}/tarifas`, function(data) {
    renderTable(data, "Lista de Tarifas");
  }).fail(() => alert("Error al cargar tarifas."));
});

// ----------------------
// 🔹 CREAR NUEVO HOTEL
// ----------------------
$("#formHotel").submit(function(e) {
  e.preventDefault();
  const formData = Object.fromEntries(new FormData(this));

  $.ajax({
    url: `${API_BASE}/hoteles/`,
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(formData),
    success: () => {
      alert("✅ Hotel creado correctamente");
      $("#modalHotel").modal("hide");
      $("#btnHoteles").click();
    },
    error: () => alert("❌ Error al crear el hotel")
  });
});

// ---------------------------
// 🔹 CREAR NUEVA HABITACIÓN
// ---------------------------
$("#formHabitacion").submit(function(e) {
  e.preventDefault();
  const formData = Object.fromEntries(new FormData(this));

  $.ajax({
    url: `${API_BASE}/habitaciones`,
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(formData),
    success: () => {
      alert("✅ Habitación creada correctamente");
      $("#modalHabitacion").modal("hide");
      $("#btnHabitaciones").click();
    },
    error: () => alert("❌ Error al crear la habitación")
  });
});

// ----------------------
// 🔹 CREAR NUEVO CLIENTE
// ----------------------
$("#formCliente").submit(function(e) {
  e.preventDefault();
  const formData = Object.fromEntries(new FormData(this));

  $.ajax({
    url: `${API_BASE}/clientes`,
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(formData),
    success: () => {
      alert("✅ Cliente registrado correctamente");
      $("#modalCliente").modal("hide");
      $("#btnClientes").click();
    },
    error: () => alert("❌ Error al registrar cliente")
  });
});

// ----------------------
// 🔹 CREAR NUEVA RESERVA
// ----------------------
$("#formReserva").submit(function(e) {
  e.preventDefault();
  const formData = Object.fromEntries(new FormData(this));

  $.ajax({
    url: `${API_BASE}/reservas`,
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(formData),
    success: () => {
      alert("✅ Reserva creada correctamente");
      $("#modalReserva").modal("hide");
      $("#btnReservas").click();
    },
    error: () => alert("❌ Error al crear la reserva (verifica los IDs)")
  });
});

// --------------------
// 🔹 CREAR NUEVA TARIFA
// --------------------
$("#formTarifa").submit(function(e) {
  e.preventDefault();
  const formData = Object.fromEntries(new FormData(this));

  $.ajax({
    url: `${API_BASE}/tarifas`,
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(formData),
    success: () => {
      alert("✅ Tarifa agregada correctamente");
      $("#modalTarifa").modal("hide");
      $("#btnTarifas").click();
    },
    error: () => alert("❌ Error al crear la tarifa")
  });
});

// ----------------------
// 🔹 Inicialización
// ----------------------
$(document).ready(function() {
  console.log("✅ Panel Administrativo listo.");
});
