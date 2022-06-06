var div=document.querySelector(".log_out")
var newdiv=document.createElement("div")
var p=document.createElement("a")
p.className="lin";
var i=document.createElement("i")
var newText = document.createTextNode("Log out");
var view=document.querySelector(".view")
p.appendChild(newText)
newdiv.appendChild(p)
newdiv.appendChild(i)
div.appendChild(newdiv)
newdiv.className="out";
document.querySelector(".lin").href="../HTML/addStu.html";
document.querySelector(".lin").style.textDecoration="none";
document.querySelector(".lin").style.color="#000";
i.className="fa-solid fa-arrow-right-from-bracket log";
document.querySelector(".out").style.marginLeft="65.5%";
document.querySelector(".out").style.marginTop="0px";
document.querySelector(".out").style.backgroundColor="white";
document.querySelector(".out").style.padding="14px 50px";
document.querySelector(".out").style.borderRadius="5px";
document.querySelector(".out").style.marginRight="0";
document.querySelector(".out").style.fontFamily="roboto";
document.querySelector(".out").style.display="flex";
document.querySelector(".out").style.width="230px";
document.querySelector(".out").style.display="none";
document.querySelector(".log").style.marginLeft="20px";
document.querySelector(".out").style.boxShadow="0 0.5rem 1rem rgb(0 0 0 / 18%)";
let open = false;


function logOut(){
    if (!open){
        document.querySelector(".out").classList.toggle("out1")
        document.querySelector(".out1").style.display="flex"
        open=true
    }
    else{
        open = false
        document.querySelector(".out").style.display="none"
    } 
}
document.querySelector(".fa-cog").addEventListener("click",logOut)

