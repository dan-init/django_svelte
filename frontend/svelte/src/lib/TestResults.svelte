<script>

import { onMount } from 'svelte';
const endpoint = 'http://localhost:8000/testresults/';
export let results = []

const load = async function () {
	const jsonResponse = await fetch(endpoint);
	const data = await jsonResponse.json();	
	results = data
}

onMount(load);


</script>

<div>
	<img src="/jlr-logo-removed.png" alt="jlr logo">
</div>

<div class="input-group">
	<input type="text" name="search" id="search" placeholder="Search"/>
</div>

<div class="table-div">
	<table class="content-table" id="myTable">
		<thead>
			<tr>
				<th>ID<span class="icon-arrow">&uparrow;</span></th>
				<th>Test Name<span class="icon-arrow">&uparrow;</span></th>
				<th>Test DateTime<span class="icon-arrow">&uparrow;</span></th>
				<th>Engineer<span class="icon-arrow">&uparrow;</span></th>
				<th>Driver<span class="icon-arrow">&uparrow;</span></th>
				<th>Cell<span class="icon-arrow">&uparrow;</span></th>
				<th>Vehicle<span class="icon-arrow">&uparrow;</span></th>
				<th>IWR<span class="icon-arrow">&uparrow;</span></th>
				<th>RMMSE<span class="icon-arrow">&uparrow;</span></th>
				<th>Total c0<span class="icon-arrow">&uparrow;</span></th>
				<th>Total c02<span class="icon-arrow">&uparrow;</span></th>
			</tr>
		</thead>
		<tbody>
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
		</tbody>
			
		</table>
</div>

<style>

	.table-div {
		margin: auto;
  		width: 80%;;
	}
	
	img {
  		display: block;
  		margin-left: auto;
  		margin-right: auto;
	}


	thead tr span.icon-arrow {
		display: inline-block;
		width: 1.3rem;
		height: 1.3rem;
	}

	.content-table {
		border-collapse: collapse;
		border-radius: 5px 5px 0 0;
		margin:25px 0;
		font-size: 0.9em;
		text-align: center;
		overflow: hidden;
		overflow-y: scroll;
		height: 300px;
		width: 1270px;
		display:block;
		box-shadow: 0 0 20px rgba(0,0,0,0.15);

	}

	.content-table th {
		cursor: pointer;
		background-color: black;
		position: sticky;
		top: 0; /* Don't forget this, required for the stickiness */
	}

	.content-table thead tr {
		background-color: black;
		color: #ffffff;
		text-align: center;
		font-weight: bold;
	}

	.content-table th,
	.content-table td {
		padding: 12px 15px;
	}

	.content-table tbody tr {
		border-bottom: 1px solid #dddddd;
	}

	.content-table tbody tr:nth-last-of-type(even) {
		background-color: #f3f3f3;
	}

	.content-table tbody tr:nth-last-of-type(odd) {
		background-color: #a1a1a1;
	}
	
	.content-table tbody tr:last-of-type {
		border-bottom: 2px solid black;
	}

	thead th.active {
		color: red;
	}

	/* .search-input {
		width: 90px;
		text-align: center;
		border: none;
		outline: none;
	} */

</style>
