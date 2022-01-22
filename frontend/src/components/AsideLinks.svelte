<script>
    import AsideItem from './AsideItem.svelte'
    export let links
</script>

{#each links as link}
    <AsideItem author={link.authors} title={link.title} link={link.sha256} year={link.year || 0} />
{/each}

