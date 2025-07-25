document.getElementById("btn-iniciar-sesion").addEventListener("click", async function() {
  event.preventDefault();

  const nombreUsuario = document.getElementById("cmp-nombre-usuario").value;
  const contrasena = document.getElementById("cmp-contrasena").value;

  try {
      const response = await fetch("/autenticar-usuario", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          nombre_usuario: nombreUsuario,
          contrasena: contrasena
        })        
      });

      const data = await response.json();

      if (!response.ok) {
        alert("Error: " + (data.detail || "Error desconocido"));
        return;
      }

      alert("Token: " + data.access_token + " | Tipo: " + data.token_type);

      // Guardar el token
      localStorage.setItem("token", data.token);

      // AGREGAR EL CAMBIO DE PAGINA A LA PRINCIPAL

    } catch (error) {
      console.error("Error al iniciar sesión:", error);
      alert("No se pudo conectar con el servidor.");
    }
  });