fetch('/api/dashboard/kpi/')
.then(response => response.json())
.then(data => {

document.getElementById("revenue").innerText = data.total_revenue;
document.getElementById("orders").innerText = data.total_orders;
document.getElementById("avg").innerText = data.average_order_value;

});


fetch('/api/dashboard/product-revenue/')
.then(response => response.json())
.then(data => {

const labels = data.map(item => item.product);
const values = data.map(item => item.total_revenue);

new Chart(document.getElementById('productChart'),{

type:'bar',

data:{
labels:labels,
datasets:[{
label:'Revenue',
data:values
}]
}

});

});

fetch('/api/dashboard/status-distribution/')
.then(response => response.json())
.then(data => {

const labels = data.map(item => item.status);
const values = data.map(item => item.count);

new Chart(document.getElementById('statusChart'),{

type:'pie',

data:{
labels:labels,
datasets:[{
data:values
}]
}

});

});

const filter = document.getElementById("dateFilter");

filter.addEventListener("change", function () {
    loadDashboard(filter.value);
});

function loadDashboard(range="all") {

    fetch(`/api/dashboard/kpi/?range=${range}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("revenue").innerText = data.total_revenue;
            document.getElementById("orders").innerText = data.total_orders;
            document.getElementById("avg").innerText = data.average_order_value;
        });

}