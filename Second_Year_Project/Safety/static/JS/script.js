const lightbox = document.createElement('div')
lightbox.id = 'lightbox'
document.body.appendChild(lightbox)

const system_data_all = document.querySelectorAll('.system_data_all')

function show_image(x){

    system_data_all.forEach(image => {
        image.addEventListener('click' ,e => {
            lightbox.classList.add('active')
            const img = document.createElement('img')
            img.src = x
            while(lightbox.firstChild){
                lightbox.removeChild(lightbox.firstChild)
            }
            lightbox.appendChild(img)
        })
    })

    lightbox.addEventListener('click' , e=>{
        if(e.target !== e.currentTarget)return
        lightbox.classList.remove('active')
    })

}

function submit(){ 
    document.submit.submit()
}

function show_bar(){
    const bar = document.getElementById("account_bar_border")
    bar.classList.toggle('active')
}