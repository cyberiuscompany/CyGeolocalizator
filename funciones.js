function getLocation() {
  const output = document.getElementById('locationResult');

  if (!navigator.geolocation) {
    output.innerText = '⚠️ Geolocalización no soportada por este navegador.';
    return;
  }

  navigator.geolocation.getCurrentPosition(
    (position) => {
      const { latitude, longitude, accuracy } = position.coords;
      output.innerText = `✅ Ubicación obtenida:
Latitud: ${latitude}
Longitud: ${longitude}
Precisión: ±${accuracy} metros`;
    },
    (error) => {
      output.innerText = `❌ Error al obtener ubicación: ${error.message}`;
    }
  );
}

function getCamera() {
  const video = document.getElementById('video');

  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    alert('⚠️ Tu navegador no soporta getUserMedia.');
    return;
  }

  navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
      video.srcObject = stream;
    })
    .catch((error) => {
      alert(`❌ Error al acceder a la cámara: ${error.message}`);
    });
}
