// Creating a new Date object
let currentDate = new Date();
const weekDay = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];

// Getting different components of the date
const year = currentDate.getFullYear();
const month = currentDate.getMonth(); // 0-indexed (0 - January, 11 - December)
const day = currentDate.getDate();

let mon = month+1;
if(mon<11) mon = "0"+mon;

document.getElementById('year').textContent = year;
document.getElementById('month').textContent = mon;
document.getElementById('date').textContent = day;
document.getElementById('day').textContent = weekDay[currentDate.getDay()];

function update() {
    const current = new Date();
    const hours = current.getHours();
    const minutes = current.getMinutes();
    const seconds = current.getSeconds();

    const formattedHours = hours < 10 ? `0${hours}` : hours;
    const formattedMinutes = minutes < 10 ? `0${minutes}` : minutes;
    const formattedSeconds = seconds < 10 ? `0${seconds}` : seconds;

    document.getElementById('hr').textContent = formattedHours;
    document.getElementById('min').textContent = formattedMinutes;
    document.getElementById('sec').textContent = formattedSeconds;

}
update();
setInterval(update, 1000);


