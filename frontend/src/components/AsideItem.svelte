<script>
    import BookIcon from '@yababay67/svelte-meets-bootstrap-icons/book.svelte'
    import SignpostIcon from '@yababay67/svelte-meets-bootstrap-icons/signpost.svelte'
    export let author, title, link, year, activate, current
    export let icon = 'book'
    let yearSuffix = ' г.'
    if(year < 0) {
        year = 0 - year
        yearSuffix += ' до н.э.'
    }
    link = `#/api/ethnical/${link}`

    let active = false
</script>

<li>
    <a href={link} class="nav-link link-secondary" on:click={e => activate(link)} class:asideActive={current == link ? "active" : ""}>
        {#if icon == 'signpost'}
            <SignpostIcon size="24" />
        {:else}
            <BookIcon size="24" />
        {/if}
        {author}&nbsp;&mdash;
        <b>{title}</b>
        <i>{year ? `(${year}${yearSuffix})` : ''}</i>
    </a>
</li>

<style>
    .asideActive {
        color: steelblue !important;
        border-color: steelblue !important;
        border-left: 3px solid;
    }
</style>

