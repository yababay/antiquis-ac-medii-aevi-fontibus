<script>
    import AsideItem from './AsideItem.svelte'
    export let links

    S: current = null

    function activate(link){
       current = link 
    }
</script>

{#each links as link}
    <AsideItem author={link.authors} title={link.title} link={link.sha256} year={link.year || 0} 
        activate={activate} current={current}
    />
{/each}

