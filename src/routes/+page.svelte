<script>
  import PocketBase from 'pocketbase';
  import JsBarcode from 'jsbarcode'
  import { onMount } from 'svelte';
  import Artsclaimer from './Artsclaimer.svelte';

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

<svelte:head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>NoneCard - Nonsense to the companies, value to the people!</title>
</svelte:head>

<h1>NoneCard</h1>

<p>
  To be stalked or fined by a company?
  None of that.
  NoneCard lets you use shared customer cards, making it harder for companies to extract meaningful insights from the data they steal—while still keeping the "club" prices.
  Nonsense to the companies, value to the people!
</p>

<h2>Shared Customers Cards</h2>
{#if error}
  <p class="error">Failed to load records: {error}</p>
{:else}
  <ul>
    {#each records as record}
      {#if record.devel === false || window.location.hostname === 'localhost'}
        <li class="card">
          <h3>{record.company} - {record.name} ({record.country})</h3>
          <img use:barcode={{ code: record.code, type: record.type }} alt="Barcode for {record.code}"/>
        </li>
      {/if}
    {/each}
  </ul>
{/if}

<div id="contribute">
<h2>How to help</h2>
<p>
  <b>A. Spread the word:</b>
  There's no netarte útil without viewers.
  Telling your friends about NoneCard is great.
  Thx!
</p>
<p>
  <b>C. Share your card:</b>
  If you want to add your customer card, please send its photo to: <a href="mailto:nonecard@gajdosik.org">nonecard@gajdosik.org</a>.
</p>
<p>
  <b>A. Join DB team:</b>
  If you wish you can request a login to the database and add the cards yourself.
</p>
<p>
  <b>B. Develop Code:</b>
  Fork it, improve it, make PR. Thanks! Or just run your own instance. Great! Here's <a href="https://github.com/agajdosi/nonecard">repo</a>.
</p>
</div>

<style>
  /* Center the container horizontally and set a max width */


  h1, h2, h3 {
    text-align: center;
  }
  h2 {
    margin-top: 5rem;
  }

  h3 {
    font-size: 1.1rem;
    margin-bottom: 0;
    padding: 0;
  }

  p {
    text-align: center;
  }

  ul {
    list-style: none;
    padding: 0;
  }

  li {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 1rem;
    margin-bottom: 1rem;
    text-align: center;
  }

  a {
    color: #007acc;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

  .card h3 {
    font-size: 1.6rem;
    margin-top: 1rem;
  }

  #contribute > p{
    text-align: justify;
  }

</style>
