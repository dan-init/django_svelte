<script>

import { onMount } from 'svelte';
const endpoint = 'http://localhost:8000/testresults/';
export let results = []

onMount(async function () {
	const jsonResponse = await fetch('http://localhost:8000/testresults/');
	const data = await jsonResponse.json();
	console.log(data[0]);		
results = data
});


function myFunction() {
	// Declare variables
	var input, filter, table, tr, td, i, txtValue;
	input = document.getElementById("myInput");
	filter = input.value.toUpperCase();
	table = document.getElementById("myTable");
	tr = table.getElementsByTagName("tr");

	// Loop through all table rows, and hide those who don't match the search query
	for (i = 0; i < tr.length; i++) {
		td = tr[i].getElementsByTagName("td")[0];
		if (td) {
		txtValue = td.textContent || td.innerText;
		if (txtValue.toUpperCase().indexOf(filter) > -1) {
			tr[i].style.display = "";
		} else {
			tr[i].style.display = "none";
		}
		}
	}
};

</script>

<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names..">

<div>
	<table id="myTable">
		<tr class="header">
			<th>id</th>
			<th>Test Name</th>
			<th>Test DateTime</th>
			<th>Engineer</th>
			<th>Driver</th>
			<th>Cell</th>
			<th>Vehicle</th>
			<th>IWR</th>
			<th>RMMSE</th>
			<th>Total c0</th>
			<th>Total c02</th>
		</tr>
		{#each results as result }
		<tr>
			<td> {result.id}</td>
			<td> {result.test_name}</td>
			<td> {result.test_datetime}</td>
			<td> {result.engineer}</td>
			<td> {result.driver}</td>
			<td> {result.cell}</td>
			<td> {result.vehicle_id}</td>
			<td> {result.iwr}</td>
			<td> {result.rmsse}</td>
				<td> {result.total_co}</td>
				<td> {result.total_co2}</td>
			</tr>
		{/each}
	
	</table>
</div>

<style>

	table {
	text-align: left;
	position: relative;
	border-collapse: collapse; 
	}

	th, td {
	padding: 0.25rem;
	}

	tr {
	background: rgba(51, 255, 0, 0.23);
	color: rgb(0, 0, 0);
	}

	th {
	background: white;
	position: sticky;
	top: 0; /* Don't forget this, required for the stickiness */
	box-shadow: 0 2px 2px -1px rgba(0, 0, 0, 0.4);
	}

</style>
