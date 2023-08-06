<script>
	import { onMount } from 'svelte';
	export let data;
    export let json_data;
	onMount(async () => {
		data = await fetch('http://localhost:8000/testresults/').then((x) => x.json());
        json_data = JSON.stringify(data, null, 2)
	});
</script>

<pre>
  {json_data}
</pre>

