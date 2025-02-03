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

<svelte:head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>NoneCard - Customers of the World, Unite!</title>
</svelte:head>

<div class="container">
  <h1>NoneCard</h1>

  <p>
    NoneCard allows you to share customer cards in the community.
    You can easily and freely access and use the cards.
    And make it harder for companies to analyze anything meaningful from the stolen data.
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
      Let's obfuscate the data of others and let the others obfuscate yours.
      Once the card purchases meat in Prague, then seconds later it makes a vegan purchase in Ostrava.
      Nonsense to the companies, value to the people!
      Customers of the world, unite!
    </p>
  </details>

  <h2>Add your customer card</h2>
  <p id="add">
    If you want to add your customer card, please send its photo to: <a href="mailto:nonecard@gajdosik.org">nonecard@gajdosik.org</a>.<br>
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

  <footer>
    <div>{new Date().getFullYear()}, AndyG. Copyleft reserved.</div>
    <div>help development at: <a href="https://github.com/agajdosi/nonecard">github.com/agajdosi/nonecard</a></div>
  </footer>
</div>

<style>
  /* Center the container horizontally and set a max width */
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 1rem;
    font-family: sans-serif;
    line-height: 1.6;
  }

  h1, h2, h3 {
    text-align: center;
  }

  p {
    text-align: justify;
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

  details {
    margin: 1rem 0;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 5px;
  }

  #add{
    text-align: center;
  }

  footer {
    margin-top: 2rem;
    display: flex;
    justify-content: space-between;
    padding-top: 1rem;
    border-top: 1px solid #ddd;
    text-align: center;
    color: #666;
    font-size: 0.9rem;
  }
</style>
