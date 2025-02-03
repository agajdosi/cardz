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

<h1>NoneCard</h1>

<p>
  NoneCard allows you to share customer cards in the community.
  You can easily and freely access and use the cards.
  And make it harder for companies to analyze anything meaningul from the stolen data.
  Customers of the world, unite!
</p>

<details id="manifesto">
  <summary>More info:</summary>
  <h2>NoneCard Manifesto</h2>
  <p>
  Customer cards promise discounts, but in reality they just track the customers.
  They intrude our privacy and suck data about our purchasing behaviour into clouds somewhere in a sec haven.
  Customer cards are just a tool of surveillance capitalism.
  No longer we are customers, we are tagged herds.
  </p>
  <p>
  As if that wasn't shitty enough, it's also just extremely annoying to carry around customer cards.
  To keep them. Search them in a wallet. To keep track of them.
  </p>
  <p>
  And if you can't find a customer card, or simply don't have one, you get fined the "regular" price, which is out of touch with reality.
  We are human beings, we have our dignity and it is our right not to be stalked.
  </p>

  <p>
  Share and use cards to get the discount while contaminating the extracted data with random noise.
  Let's obfuscate the data of others and let the others to obfuscate yours.
  Once the card purchases meat in Prague, then seconds later it makes a vegan purchase in Ostrava.
  Nonsense to the companies, value to the people!
  </p>
</details>



<h3>Add your customer card</h3>
<p>
If you want to add your customer card, send its picture to: <a href="mailto:nonecard@gajdosik.org">nonecard@gajdosik.org</a>.<br>
(You can also join development of this site at: <a href="https://github.com/agajdosi/nonecard">github.com/agajdosi/nonecard</a>).
</p>

<h2>Available Cards</h2>
{#if error}
  <p class="error">Failed to load records: {error}</p>
{:else}
  <ul>
    {#each records as record}
      {#if record.devel === false || window.location.hostname === 'localhost'}
      <li>
        <h2>{record.company} - {record.name} ({record.country})</h2>
        <img use:barcode={{ code: record.code, type: record.type }} alt="Barcode for {record.code}"/>
      </li>
      {/if}
    {/each}
  </ul>
{/if}


