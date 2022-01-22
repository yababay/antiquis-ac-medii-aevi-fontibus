<script>
    export let ethnos, count, handler
</script>

<div class="badge-holder">
    <button type="button" class="btn btn-primary me-1 mb-1 btn-sm badge" on:click={handler}>
        {ethnos} <span class="badge bg-light text-muted">{count}</span>
    </button>
</div>

<style>
    .badge-holder {
        display: inline-block;
        margin-top: .5rem;
        margin-right: .5rem;
        margin-left: .5rem;
    }
    .badge {
        background-color: #CFDEEC;
        color: #386890;
    }
    .badge:hover {
        background-color: steelblue;
        color: #D9E5F0;
    }
</style>

