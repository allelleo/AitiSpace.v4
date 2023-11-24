new Chart(document.getElementById("pie-chart"), {
  type: 'pie',
  data: {
    labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
    datasets: [{
      label: "Population (millions)",
      backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
      data: [2478,5267,734,784,433]
    }]
  },
  options: {
    title: {
      display: true,
      text: 'Predicted world population (millions) in 2050'
    }
  }
});

const apiURL = 'http://127.0.0.1:81/api/v1/log_count';
const create_chart = (data) => {
  console.log(data);
  new Chart(document.getElementById("line-chart"), {
    type: 'line',
    data: data
  });
}
const fetch_api = () => {
  fetch(apiURL).then(res => res.json()).then(res => create_chart(res)).then(setTimeout(fetch_api, 5000));
}

fetch_api()