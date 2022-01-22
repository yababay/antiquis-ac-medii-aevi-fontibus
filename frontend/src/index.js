import useHashRouting from './util/router.js'
import NavbarIcons from './components/NavbarIcons.svelte'
import AsideLinks  from './components/AsideLinks.svelte'
import settings from './settings.json'
import { sourcesRaw } from './util/store.js'

const navUl = document.querySelector('nav ul')

if(settings.navbarIcons && navUl){
    new NavbarIcons({
        target: navUl
    })
}

const [sources, researches] = document.querySelectorAll('aside ul')

fetch('library.json')
    .then(res => res.json())
    .then(items => {
        sourcesRaw.set(items)
        new AsideLinks({
            target: sources,
            props: {links: items.filter(el => el.is_source).sort((a, b) => a.year - b.year)}
        })
        new AsideLinks({
            target: researches,
            props: {links: items.filter(el => !el.is_source)}
        })
    })

if(settings.withHashRouting){
    useHashRouting()
}
