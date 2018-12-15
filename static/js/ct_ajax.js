$('.pie-chart').click(
    function () {
        var injection = $(this).attr("chance");

        var pred = injection*100;
        console.log(pred);
        var chart = new CanvasJS.Chart("chartContainer", {
            animationEnabled: true,
            title: {
                text: "Interveinal injection"
            },
            data: [{
                type: "pie",
                startAngle: 240,
                yValueFormatString: "##0.00\"%\"",
                indexLabel: "{label} {y}",
                dataPoints: [
                    {y: pred, label: "Taken"},
                    {y: 100-pred, label: "Not taken"},
                ]
            }]
        });
        chart.render();
    }
);