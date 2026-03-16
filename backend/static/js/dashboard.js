console.log("dashboard.js loaded");

// Store chart instances globally so we can destroy them before re-creating
// Without this, Chart.js throws "canvas already in use" error on every filter change
let productChart = null;
let statusChart = null;

// ── Entry point ───────────────────────────────────────────────────────────────
// Runs once when page loads. Calls applyFilter() with default "all"
document.addEventListener("DOMContentLoaded", function () {
    applyFilter();
});

// ── applyFilter ───────────────────────────────────────────────────────────────
// Called every time the date dropdown changes (onchange="applyFilter()")
// Reads the selected range value and passes it to all 3 loaders
function applyFilter() {
    const range = document.getElementById('dateFilter')?.value || 'all';
    loadKPI(range);
    loadProductChart(range);
    loadStatusChart(range);
}

// ── loadKPI ───────────────────────────────────────────────────────────────────
// Fetches total_revenue, total_orders, average_order_value
// Passes ?range= so backend filters by date
function loadKPI(range) {
    fetch(`/api/dashboard/kpi/?range=${range}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("revenue").innerText =
                '$' + parseFloat(data.total_revenue).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

            document.getElementById("orders").innerText =
                data.total_orders;

            document.getElementById("avg").innerText =
                '$' + parseFloat(data.average_order_value).toFixed(2);
        })
        .catch(err => console.error("KPI fetch failed:", err));
}

// ── loadProductChart ──────────────────────────────────────────────────────────
// Fetches revenue grouped by product
// Destroys old chart first — fixes "canvas already in use" bug
function loadProductChart(range) {
    fetch(`/api/dashboard/product-revenue/?range=${range}`)
        .then(response => response.json())
        .then(data => {
            const labels = data.map(item => item.product);
            const values = data.map(item => item.total_revenue);

            // IMPORTANT: destroy old instance before creating new one
            if (productChart) {
                productChart.destroy();
                productChart = null;
            }

            productChart = new Chart(document.getElementById('productChart'), {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Revenue ($)',
                        data: values,
                        backgroundColor: 'rgba(79, 123, 255, 0.7)',
                        borderColor: '#4f7bff',
                        borderWidth: 1,
                        borderRadius: 6,
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: '#8b92a9', font: { family: 'Plus Jakarta Sans' } }
                        }
                    },
                    scales: {
                        x: {
                            ticks: { color: '#555e7a' },
                            grid: { color: 'rgba(255,255,255,0.05)' }
                        },
                        y: {
                            ticks: { color: '#555e7a' },
                            grid: { color: 'rgba(255,255,255,0.05)' }
                        }
                    }
                }
            });
        })
        .catch(err => console.error("Product chart fetch failed:", err));
}

// ── loadStatusChart ───────────────────────────────────────────────────────────
// Fetches order count grouped by status
// Uses doughnut instead of pie — looks more professional
function loadStatusChart(range) {
    fetch(`/api/dashboard/order-status/?range=${range}`)
        .then(response => response.json())
        .then(data => {
            const labels = data.map(item => item.status);
            const values = data.map(item => item.count);

            // IMPORTANT: destroy old instance before creating new one
            if (statusChart) {
                statusChart.destroy();
                statusChart = null;
            }

            statusChart = new Chart(document.getElementById('statusChart'), {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        data: values,
                        backgroundColor: ['#f59e0b', '#4f7bff', '#22c55e'],
                        borderWidth: 0,
                        hoverOffset: 6,
                    }]
                },
                options: {
                    responsive: true,
                    cutout: '65%',
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                color: '#8b92a9',
                                padding: 16,
                                font: { family: 'Plus Jakarta Sans' }
                            }
                        }
                    }
                }
            });
        })
        .catch(err => console.error("Status chart fetch failed:", err));
}