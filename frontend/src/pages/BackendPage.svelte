<script>
    import * as d3 from 'd3'
    import EthnicalProfile from '../components/EthnicalProfile.svelte'
    import { sourcesRaw } from '../util/store.js'
    export let link

    async function getProfile(){
        if(!sourcesRaw.length){
            const items = await fetch('library.json')
                .then(res => res.json())
            sourcesRaw.set(items)
        }
        const res = await fetch(link.replace('ethnical', 'ethnical/count'))
        if(res.status != 200) throw 'Ошибка при загрузке контента.'
        return await res.json()
    }
</script>

{#await getProfile() then data}
    <EthnicalProfile data={data} link={link} />
{:catch error}
    <div class="alert alert-danger text-center me-3 mt-3" role="alert">
        {error}
    </div>
{/await}

