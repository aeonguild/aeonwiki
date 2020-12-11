
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',"Date");
                    data.addColumn("number","#");
                    
                    data.addRows(
	                [['January, 2015', 11668.0], ['February, 2015', 980.0], ['March, 2015', 2711.0], ['April, 2015', 3919.0], ['May, 2015', 54741.0], ['June, 2015', 45890.0], ['July, 2015', 63433.0], ['August, 2015', 106780.0], ['September, 2015', 49502.0], ['October, 2015', 14341.0], ['November, 2015', 20049.0], ['December, 2015', 12150.0], ['January, 2016', 10330.0], ['February, 2016', 16124.0], ['March, 2016', 36374.0], ['April, 2016', 15921.0], ['May, 2016', 20286.0], ['June, 2016', 19474.0], ['July, 2016', 25704.0], ['August, 2016', 31041.0], ['September, 2016', 92969.0], ['October, 2016', 63403.0], ['November, 2016', 30377.0], ['December, 2016', 56549.0], ['January, 2017', 133052.0], ['February, 2017', 103989.0], ['March, 2017', 75004.0], ['April, 2017', 169794.0], ['May, 2017', 170337.0], ['June, 2017', 176322.0], ['July, 2017', 194149.0], ['August, 2017', 237503.0], ['September, 2017', 178851.0], ['October, 2017', 318616.0], ['November, 2017', 257840.0], ['December, 2017', 380593.0], ['January, 2018', 323039.0], ['February, 2018', 257877.0], ['March, 2018', 282798.0], ['April, 2018', 278263.0], ['May, 2018', 281698.0], ['June, 2018', 439096.0], ['July, 2018', 305665.0], ['August, 2018', 149643.0], ['September, 2018', 134713.0], ['October, 2018', 166028.0], ['November, 2018', 212549.0], ['December, 2018', 119728.0], ['January, 2019', 75616.0], ['February, 2019', 66065.0], ['March, 2019', 72102.0], ['April, 2019', 75518.0], ['May, 2019', 96120.0], ['June, 2019', 88364.0], ['July, 2019', 109316.0], ['August, 2019', 97310.0], ['September, 2019', 100256.0], ['October, 2019', 80629.0], ['November, 2019', 72645.0], ['December, 2019', 43549.0], ['January, 2020', 44664.0], ['February, 2020', 28984.0], ['March, 2020', 28543.0], ['April, 2020', 29792.0], ['May, 2020', 32904.0], ['June, 2020', 35036.0], ['July, 2020', 37345.0], ['August, 2020', 30852.0], ['September, 2020', 26516.0], ['October, 2020', 27874.0], ['November, 2020', 28759.0]] );

                  var options = {
                      title: "Aeon Transaction Outputs",
                      legend: { position: 'bottom' },
                      hAxis: {title:  "Date"},
                      vAxis: {logScale : "true",
                                title: "#",
                                format: "######" },
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById('line_div'));
                    chart.draw(data, options);
                }