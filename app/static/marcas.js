
$(document).ready(function() {   
	const categorias = document.getElementById('marca');
	const modelos = document.getElementById('modelos-vehiculos');
	// Obtener el elemento select del HTML para la cilindrada
	const selectCilindrada = document.getElementById('cilindrada');
	const selectTransmisiones = document.getElementById('transmisiones');
	const selectCombustible = document.getElementById('combustible');              
	categorias.addEventListener('change', () => {
		const categoriaSeleccionada = categorias.options[categorias.selectedIndex].text;
		fetch('/procesar', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				categoria: categoriaSeleccionada                 
			})                
		})
		.then(response => response.json()) // Analizar la respuesta JSON
		.then(modelosVehiculos => {
			// Hacer algo con la lista de modelos de vehículos
			//console.log(modelosVehiculos);
		
			// Obtener el elemento select del HTML
			const selectModelos = document.getElementById('modelos-vehiculos');
			// Limpiar opciones previas
			selectModelos.innerHTML = '';
			$("#modelos-vehiculos").append("<option selected disabled >Seleccione un Modelo</option>");
			// Recorrer la lista de modelos de vehículos recibida
			for (let modelo of modelosVehiculos) {
			// Crear una nueva opción
			const option = document.createElement('option');
			// Establecer el valor del atributo 'value' con el modelo de vehículo actual
			option.value = modelo;
			// Establecer el texto dentro de la opción con el modelo de vehículo actual
			option.textContent = modelo;
			// Agregar la opción creada al elemento select
			selectModelos.appendChild(option);
			}
		})
	});

	// Evento change en el elemento 'select' de los modelos de vehículos
	modelos.addEventListener('change', () => {
		const marcaSeleccionada = categorias.options[categorias.selectedIndex].text;
		const modeloSeleccionado = modelos.options[modelos.selectedIndex].text;
		// Enviar la solicitud a la ruta de FastAPI para procesar la cilindrada
		fetch('/procesar-cilindrada', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			marca: marcaSeleccionada,
			modelo: modeloSeleccionado
		})
		})
		.then(response => response.json()) // Analizar la respuesta JSON
		.then(data => {
		// Actualizar el elemento select de la cilindrada con las opciones recibidas
		selectCilindrada.innerHTML = '';
		$("#cilindrada").append("<option selected disabled >Seleccione las Cilindrada</option>");
		for (let cilindrada of data.cilindradas) {
			const option = document.createElement('option');
			option.value = cilindrada;
			option.textContent = cilindrada;
			selectCilindrada.appendChild(option);
		}
		});
	});
	// Evento change en el elemento 'select' de los modelos de vehículos
	selectCilindrada.addEventListener('change', () => {
		const marcaSeleccionada = categorias.options[categorias.selectedIndex].text;
		const modeloSeleccionado = modelos.options[modelos.selectedIndex].text;
		const cilindradaSeleccionada = selectCilindrada.options[selectCilindrada.selectedIndex].text;
		// Enviar la solicitud a la ruta de FastAPI para procesar la cilindrada
		fetch('/procesar-transmision', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			marca: marcaSeleccionada,
			modelo: modeloSeleccionado,
			cilindrada: cilindradaSeleccionada,
		})
		})
		.then(response => response.json()) // Analizar la respuesta JSON
		.then(data => {
		// Actualizar el elemento select de la transmision con las opciones recibidas
		selectTransmisiones.innerHTML = '';
		$("#transmisiones").append("<option selected disabled >Seleccione el tipo de Transmision</option>");
		for (let transmision of data.transmisiones) {
			const option = document.createElement('option');
			option.value = transmision;
			option.textContent = transmision;
			selectTransmisiones.appendChild(option);
		}
		});
	});
	// Evento change en el elemento 'select' de las transmisiones de los vehículos
	selectTransmisiones.addEventListener('change', () => {
		const marcaSeleccionada = categorias.options[categorias.selectedIndex].text;
		const modeloSeleccionado = modelos.options[modelos.selectedIndex].text;
		const cilindradaSeleccionada = selectCilindrada.options[selectCilindrada.selectedIndex].text;
		const transmisionSeleccionada = selectTransmisiones.options[selectTransmisiones.selectedIndex].text;
		// Enviar la solicitud a la ruta de FastAPI para procesar la cilindrada
		fetch('/procesar-combustible', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			marca: marcaSeleccionada,
			modelo: modeloSeleccionado,
			cilindrada: cilindradaSeleccionada,
			transmision: transmisionSeleccionada,
		})
		})
		.then(response => response.json()) // Analizar la respuesta JSON
		.then(data => {
		// Actualizar el elemento select del combustible con las opciones recibidas
		selectCombustible.innerHTML = '';
		$("#combustible").append("<option selected disabled >Seleccione el tipo de Combustible</option>");
		for (let tipocombustible of data.combustible) {
			const option = document.createElement('option');
			option.value = tipocombustible;
			option.textContent = tipocombustible;
			selectCombustible.appendChild(option);
		}
		});
	});
	
	$('input:radio').change(function(){
		const selectedValue = $(this).val();
		const barraSelectora = document.getElementById("customRange3");
		const valorSeleccionado = document.getElementById("valorSeleccionado");
		const calculo = document.getElementById("calculo"); 
		
		const marcaSeleccionada = categorias.options[categorias.selectedIndex].text;
		const modeloSeleccionado = modelos.options[modelos.selectedIndex].text;
		const cilindradaSeleccionada = selectCilindrada.options[selectCilindrada.selectedIndex].text;
		const transmisionSeleccionada = selectTransmisiones.options[selectTransmisiones.selectedIndex].text;
		const combustibleSeleccionado = selectCombustible.options[selectCombustible.selectedIndex].text;


		valorSeleccionado.textContent = barraSelectora.value;
		barraSelectora.addEventListener("input", function(){
		valorSeleccionado.textContent = barraSelectora.value;
		
		const consumo = Number(calculo.dataset.consumo);
		const valorBarra = Number(barraSelectora.value);
		
		const resultado = (valorBarra * consumo)/100;
		calculo.textContent = resultado.toFixed(2);
		});        
		fetch('/procesar-cheked', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			marca: marcaSeleccionada,
			modelo: modeloSeleccionado,
			cilindrada: cilindradaSeleccionada,
			transmision: transmisionSeleccionada,
			combustible: combustibleSeleccionado,
			check: selectedValue,
		})
		}).then(response => response.json())
		.then(data => {
			calculo.dataset.consumo = data.consumo;
			const consumo = Number(calculo.dataset.consumo);
			const valorBarra = Number(barraSelectora.value);

			const resultado = (valorBarra * consumo)/100;
			calculo.textContent = resultado.toFixed(2);          
		})
		.catch(error => console.log(error));
			
	});
			
});
