document.addEventListener('DOMContentLoaded',function(){
    const menu=document.getElementsByClassName("menu")[0];
    const close_b=document.getElementsByClassName("close")[0];
    const sidebar=document.getElementsByClassName("sidebar")[0];
    const buy=document.getElementsByClassName("buy_button")[0];
    menu.addEventListener("click",()=>{
        console.log("tera bhai")
        sidebar.style.left="10px"
    });

    close_b.addEventListener("click",()=>{
        console.log("tera bhai")
        sidebar.style.left="-240px"
    });
    buy.addEventListener("click",()=>{
        window.open("/buy")
    });
});
