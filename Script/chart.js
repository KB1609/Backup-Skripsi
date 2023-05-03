class ChartCreator {

    createLineChart(labels, data, label, borderColor, fill) {
        // eslint-disable-next-line no-undef
        var ctx = document.getElementById("lineChart").getContext("2d");
        var gradient = ctx.createLinearGradient(0, 0, 0, 550);
        gradient.addColorStop(0, 'rgba(4, 173, 191, 1)');
        gradient.addColorStop(1, 'rgba(4, 173, 191, 0.01)');
        var lineChart = new Chart(ctx, {
            type: "line",
            data: {
                labels: {{ mydata['labels'] | safe }},
    datasets: [
        {
            label: "Adj Close",
            data: {{ mydata['values'] | safe }},
fill: 'true',
    backgroundColor: gradient,
        borderColor: 'rgba(4, 173, 191, 1)',
            borderWidth: "2",
                pointBackgroundColor: 'rgba(4, 173, 191, 1)',
                    pointBorderWidth: '150px',
                        pointRadius: '3',
                            pointHoverRadius: 5,
                                pointHitRadius: 10,
           
              

                      }]
              },
options: {
    animation: {
        onComplete: () => {
            delayed = true
        }
    },
    hover: {
        mode: 'nearest',
            intersect: true
    },
    tooltips: {
        callbacks: {
            mode: 'index',
                intersect: false,
                    label: function(tooltipItem, data) {
                        var label = data.datasets[tooltipItem.datasetIndex].label || '';
                        if (label) {
                            label += ': ';
                        }
                        label += tooltipItem.yLabel.toFixed(2);

                        var open_data = 'Open :' + chart_tooltip.open_data[tooltipItem.index].toFixed(2);
                        var close_data = 'High :' + chart_tooltip.high_data[tooltipItem.index].toFixed(2);
                        var low_data = 'Low :' + chart_tooltip.low_data[tooltipItem.index].toFixed(2);
                        var close_data = 'Close :' + chart_tooltip.close_data[tooltipItem.index].toFixed(2);
                        var volume_data = 'Volume :' + chart_tooltip.volume_data[tooltipItem.index].toFixed(2);


                        return [label, open_data, close_data, low_data, close_data, volume_data];
                    }
        }
    },
    scales: {
        xAxes: [{
            type: 'time',
            time: {
                unit: 'month'
            },
            display: true,
            ticks: { fontColor: '#FFFFFF' },
            gridLines: {
                display: true,
                color: "rgba(255, 255, 255, 0.5)"
            },
        }],
            yAxes: [{
                display: true,
                ticks: { fontColor: '#FFFFFF' },
                gridLines: {
                    display: true,
                    color: "rgba(255, 255, 255, 0.5)"
                },
            }]
    }

}
             });

    }
  }
