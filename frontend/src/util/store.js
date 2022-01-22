import { writable } from 'svelte/store';

const sourcesRaw = writable([])
const sourcesDict = {}

sourcesRaw.subscribe(items => {
    for(const item of items){
        const {sha256, authors, title} = item
        sourcesDict[sha256] = {authors, title}
    }
})

export { sourcesRaw, sourcesDict }

