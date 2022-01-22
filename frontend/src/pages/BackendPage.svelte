<script>
    import * as d3 from 'd3'
    import EthnicalProfile from '../components/EthnicalProfile.svelte'
    export let link

    async function getProfile(){
        const res = await fetch(link)
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

