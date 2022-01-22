<script>
    import showdown from 'showdown'
    import EthnosBadge from './EthnosBadge.svelte'

    export let data, link

    data = data.map(el => ({label: el[0], value: el[1][0]}))
        .filter(el => el.label != 'весь')
        .filter(el => el.label != 'меря')

    const converter = new showdown.Converter()

    let paragraphs

    function onEthnos(ethnos){
        fetch(link.replace('ethnical', 'ethnical/sents') + `/${ethnos}`)
        .then(res => res.json())
        .then(txt => {
            paragraphs.innerHTML = converter.makeHtml(txt)
        })
    }

</script>

<div class="card badges">
  <div class="card-body text-center">
    {#each data as tag}
        <EthnosBadge ethnos={tag.label} count={tag.value} handler={e => onEthnos(tag.label)} />
    {/each}
  </div>
</div>
<div class="container paras" bind:this={paragraphs}/>

<style>
    .badges {
        margin: 4rem 1rem;
        width: 100%;
    }

    .paras {
        margin-left: 3rem;
        padding-left: 1rem;
        border-left: 2px solid silver;
    }
</style>

