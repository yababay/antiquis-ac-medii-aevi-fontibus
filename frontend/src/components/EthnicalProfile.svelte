<script>
    import { onMount } from 'svelte'
    import { sourcesDict } from '../util/store.js'
    import EthnicalBarChart from './EthnicalBarChart.js'
    //import EthnosBadges from './EthnosBadges.svelte'

    export let data, link
    let figure

    onMount(() => {
        const chart = new EthnicalBarChart(figure)
        const {authors, title} = sourcesDict[/.*\/([^\/]+)$/.exec(link)[1]]    
        chart.caption = `Частотность упоминания этносов в источнике<br> <em>${authors}</em>&nbsp;&mdash; <strong>${title}</strong>`
        chart.draw(data)
    })
</script>

<figure bind:this={figure} class="profile-holder"/>
<!-- EthnosBadges data={data} link={link}/ -->

<style>
    .profile-holder {
        margin: 3rem;
    }
</style>
