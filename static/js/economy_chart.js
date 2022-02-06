$(document).ready(function () {
    let xml = new XMLHttpRequest();
    xml.open("POST", "/getEconomy", true);
    xml.setRequestHeader("Content-Type", "application/json");
    xml.addEventListener('load', createChart)
    xml.send(JSON.stringify({country:document.getElementById('alpha2').innerText}) );
});



function createChart() {
    data = JSON.parse(this.responseText);
    console.log(data);
    const ctx = $('#economyChart');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [data['x_axis']],
            datasets: [{
                label: 'Annual Infation %',
                data: data['inflation'],
                borderColor: "#3e95cd",
                fill: false
            },
                {
                    label: 'GDP Per Capita',
                    data: data['gdp'],
                    borderColor: "#8e5ea2",
                    fill: false
                },
                {
                    label: 'GNI Per Capita',
                    data: data['gni'],
                    borderColor: "#3cba9f",
                    fill: false
                }
            ]
        },
        options: {
            title: {
                display: true,
                text: 'World population per region (in millions)'
            }
        }
    });
}

