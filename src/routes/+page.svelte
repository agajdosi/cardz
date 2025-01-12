<script>
    import PocketBase from 'pocketbase';
    import { onMount } from 'svelte';

    let records = [];
    let error = null;

    // Initialize PocketBase client
    const pb = new PocketBase('https://pb1.lab.gajdosik.org');

    // Fetch data on component mount
    onMount(async () => {
        try {
            // Fetch all records from the collection 'cardz'
            records = await pb.collection('cardz').getFullList({
                sort: '-created',
            });
        } catch (err) {
            error = err.message;
        }
    });
</script>

<h1>Cardz</h1>

{#if error}
    <p class="error">Failed to load records: {error}</p>
{:else}
    <ul>
        {#each records as record}
            <li>{record.company} - {record.type}: {record.code}</li>
        {/each}
    </ul>
{/if}