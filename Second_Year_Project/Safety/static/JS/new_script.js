const light = document.createElement('div')

light.id = 'light'
document.body.appendChild(light)

const system_data_all_intrue = document.querySelectorAll('.system_new_all')  

function show(x){

    system_data_all_intrue.forEach(image => {
        image.addEventListener('click' ,e => {
            light.classList.add('active')
            const img = document.createElement('img')
            img.src = x
            while(light.firstChild){
                light.removeChild(light.firstChild)
            }
            light.appendChild(img)
        })
    })

    light.addEventListener('click' , e=>{
        if(e.target !== e.currentTarget)return
        light.classList.remove('active')
    })
}