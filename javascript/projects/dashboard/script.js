const data = [
  { month: "Jan", sales: 1200, users: 200 },
  { month: "Feb", sales: 1800, users: 350 },
  { month: "Mar", sales: 1500, users: 300 }
];

let filteredData = [...data];

// Charts
const salesCtx = document.getElementById("salesChart");
const usersCtx = document.getElementById("usersChart");

let salesChart = new Chart(salesCtx, {
  type: "bar",
  data: {
    labels: [],
    datasets: [{
      label: "Sales ($)",
      data: [],
    }]
  }
});

let usersChart = new Chart(usersCtx, {
  type: "line",
  data: {
    labels: [],
    datasets: [{
      label: "Users",
      data: [],
    }]
  }
});

function updateDashboard() {
  const labels = filteredData.map(d => d.month);
  const sales = filteredData.map(d => d.sales);
  const users = filteredData.map(d => d.users);

  // Update totals
  document.getElementById("salesTotal").innerText =
    sales.reduce((a, b) => a + b, 0);

  document.getElementById("usersTotal").innerText =
    users.reduce((a, b) => a + b, 0);

  document.getElementById("growth").innerText =
    Math.round((users[users.length - 1] / users[0] - 1) * 100) + "%";

  // Update charts
  salesChart.data.labels = labels;
  salesChart.data.datasets[0].data = sales;
  salesChart.update();

  usersChart.data.labels = labels;
  usersChart.data.datasets[0].data = users;
  usersChart.update();
}

// Filter by month
function filterData() {
  const value = document.getElementById("monthFilter").value;

  filteredData = value === "all"
    ? [...data]
    : data.filter(d => d.month === value);

  updateDashboard();
}

// Sort data
function sortData(order) {
  filteredData.sort((a, b) =>
    order === "asc" ? a.sales - b.sales : b.sales - a.sales
  );
  updateDashboard();
}

updateDashboard();
