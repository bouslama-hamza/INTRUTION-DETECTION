function htmlDecode(str) {
    const doc = new DOMParser().parseFromString(str, "text/html");
    return doc.documentElement.textContent;
}

date = htmlDecode(date).substring(1 , 59)
date = date.split(",")

students = htmlDecode(students).replace("[","")
students = htmlDecode(students).replace("]","")
students  = students.split(",")

intrusion = htmlDecode(intrusion).replace("[","")
intrusion = htmlDecode(intrusion).replace("]","")
intrusion = intrusion.split(",")

const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: date,
        datasets: [{
            label: 'Students Detection',
            data: students,
            backgroundColor: 'skyblue',
            borderColor: 'skyblue',
            borderWidth: 1

        },{
            label: 'Intrusion Detection',
            data: intrusion,
            backgroundColor: 'lightcoral',
            borderColor: 'lightcoral',
            borderWidth: 1
        }
    ]}
});

const pie = document.getElementById('mypie').getContext('2d');
const mypie = new Chart(pie, {
    type: 'doughnut',
    data : {
        labels: ['Students','Intrusion'],
        datasets: [{
          label: 'My First Dataset',
          data: [pie_students , pie_intrusion],
          backgroundColor: ['skyblue' , 'lightcoral'],
          hoverOffset: 4
        }]
      },
});