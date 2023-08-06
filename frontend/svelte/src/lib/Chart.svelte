<script>

import { onMount } from 'svelte';
const endpoint = 'http://localhost:8000/testresults/';
export let results = []

onMount(async function () {
	const jsonResponse = await fetch('http://localhost:8000/testresults/');
	const data = await jsonResponse.json();
results = data
});

</script>

<div>
    <h1>
        CHART GOES HERE
    </h1>
</div>