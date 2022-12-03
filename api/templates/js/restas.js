var form = document.querySelector("form");
form.onsubmit = e => {
    var season = document.querySelector("[id=season]").value;
    var month = document.querySelector("[id=month]").value;
    var holiday = document.querySelector("[id=holiday]").value;
    var weekday = document.querySelector("[id=weekday]").value;
    var Workday = document.querySelector("[id=Workday]").value;
    var weathersit = document.querySelector("[id=weathersit]").value;
    var Temp = document.querySelector("[id=Temp]").value;
    var Atemp = document.querySelector("[id=Atemp]").value;
    var Hum = document.querySelector("[id=Hum]").value;
    var Windspeed = document.querySelector("[id=Windspeed]").value;
    e.preventDefault();
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:8000/prediccion/" + season + "/" + month + '/' + holiday + "/" + weekday + "/" + Workday + '/' + weathersit + "/" + Temp + "/" + Atemp + "/" + Hum + "/" + Windspeed)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onload = function () {
        const data = JSON.parse(xhr.response);
        const new_data = JSON.stringify(data)
        console.log(data);
        alert(new_data);
    }
    xhr.send();
}