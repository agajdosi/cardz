<script>
  import PocketBase from 'pocketbase';
  import JsBarcode from 'jsbarcode'
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

  function barcode(node, { code, type }) {
    const renderBarcode = (barcodeData) => {
      if (window.JsBarcode) {
        window.JsBarcode(node, barcodeData.code, {
          format: barcodeData.type || "CODE128",
          lineColor: "#000000",
          width: 2,
          height: 100
        });
      }
    };

    renderBarcode({ code, type });

    return {
      update(newParams) {
        renderBarcode(newParams);
      }
    };
  }

</script>

<h1>Cardz</h1>

{#if error}
    <p class="error">Failed to load records: {error}</p>
{:else}
    <ul>
        {#each records as record}
            <li>
                <h2>{record.company} - {record.type}: {record.code}</h2>
                <img use:barcode={{ code: record.code, type: record.type }} alt="Barcode for {record.code}"/>
            </li>
        {/each}
    </ul>
{/if}


