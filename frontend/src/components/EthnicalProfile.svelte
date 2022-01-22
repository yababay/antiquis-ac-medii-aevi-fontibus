<script>
    import { onMount } from 'svelte'
    import showdown from 'showdown'
    import { sourcesDict } from '../util/store.js'
    import EthnicalBarChart from './EthnicalBarChart.js'
    import EthnosBadges from './EthnosBadges.svelte'

    const converter = new showdown.Converter()
    
    export let data, link
    let figure
    const sha256 = /.*\/([^\/]+)$/.exec(link)[1]

    async function getComments(){
        const res = await fetch(`content/comments/${sha256}.md`)
        if(res.status != 200) throw 'No comments.'
        const md = await res.text()
        return converter.makeHtml(md)
    }

    onMount(() => {
        const chart = new EthnicalBarChart(figure)
        const {authors, title} = sourcesDict[sha256]    
        chart.caption = `Частотность упоминания этносов в источнике<br> <em>${authors}</em>&nbsp;&mdash; <strong>${title}</strong>`
        chart.draw(data)
    })
</script>

{#await getComments() then html}
<section class="comments">
    {@html html}
</section>
<hr>
{:catch}
    <div class="hidden"></div>
{/await}

<figure bind:this={figure} class="profile-holder"/>
<EthnosBadges data={data} link={link} />

<style>
    .profile-holder {
        margin: 1rem 0;
    }
</style>
