let isClosed = true
const hamburger = document.querySelector(".navbar-toggler")
hamburger.addEventListener('click', ()=>{
    isClosed = !isClosed
    hamburger.className = isClosed ? "navbar-toggler text-white" : "navbar-toggler text-white spin"
    const navbar = document.querySelector(".navbar-collapse")
    navbar.style.display = isClosed ? "none" : "block"
    document.querySelector('nav').className = isClosed ? "navbar navbar-expand-lg" : "navbar navbar-expand-lg showingToo"
    navbar.className = isClosed ? "collapse navbar-collapse" : "collapse navbar-collapse showing"
    document.querySelector('#logoFriburgo').style.display = isClosed ? 'block' : 'none'
})