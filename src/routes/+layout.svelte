<script>
    import { base } from '$app/paths';
</script>

<svelte:head>

</svelte:head>

<div class="container">
    <header>

    </header>

    <main>
        <slot />
    </main>

    <footer>
        <div>{new Date().getFullYear()}, AG. Copyleft reserved.</div>
        <div><a href="https://github.com/agajdosi/nonecard">github.com/agajdosi/nonecard</a></div>
    </footer>
</div>

<style>
:global(body) {
    margin: 0;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 1rem;
    font-family: sans-serif;
    line-height: 1.6;
  }

footer {
    margin-top: 5rem;
    display: flex;
    justify-content: space-between;
    padding-top: 0.7rem;
    border-top: 0px solid #ddd;
    text-align: center;
    color: #666;
    font-size: 0.9rem;
  }

</style>
