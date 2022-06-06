let services=document.querySelector(".services")
let evall=document.querySelector(".eval")
let child=document.querySelector(".child")
let child1=document.querySelector(".child1")
services.addEventListener('click',()=>{
    child.classList.toggle('dis');
})
evall.addEventListener('click',()=>{
    child1.classList.toggle('dis');
})

