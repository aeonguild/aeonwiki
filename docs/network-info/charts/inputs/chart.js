
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',"Date");
                    data.addColumn("number","#");
                    
                    data.addRows(
	                [['January, 2015', 124678.0], ['February, 2015', 583.0], ['March, 2015', 28013.0], ['April, 2015', 33161.0], ['May, 2015', 328545.0], ['June, 2015', 262243.0], ['July, 2015', 363526.0], ['August, 2015', 410113.0], ['September, 2015', 154349.0], ['October, 2015', 145331.0], ['November, 2015', 178242.0], ['December, 2015', 120165.0], ['January, 2016', 41731.0], ['February, 2016', 123625.0], ['March, 2016', 76812.0], ['April, 2016', 50257.0], ['May, 2016', 89945.0], ['June, 2016', 40972.0], ['July, 2016', 115668.0], ['August, 2016', 94247.0], ['September, 2016', 122545.0], ['October, 2016', 92746.0], ['November, 2016', 60133.0], ['December, 2016', 89087.0], ['January, 2017', 139965.0], ['February, 2017', 105628.0], ['March, 2017', 79184.0], ['April, 2017', 155620.0], ['May, 2017', 171359.0], ['June, 2017', 157137.0], ['July, 2017', 143977.0], ['August, 2017', 173540.0], ['September, 2017', 134282.0], ['October, 2017', 289142.0], ['November, 2017', 270962.0], ['December, 2017', 439465.0], ['January, 2018', 471160.0], ['February, 2018', 186917.0], ['March, 2018', 167850.0], ['April, 2018', 173854.0], ['May, 2018', 172911.0], ['June, 2018', 269385.0], ['July, 2018', 236954.0], ['August, 2018', 173008.0], ['September, 2018', 184654.0], ['October, 2018', 166328.0], ['November, 2018', 229466.0], ['December, 2018', 134242.0], ['January, 2019', 82541.0], ['February, 2019', 92310.0], ['March, 2019', 138757.0], ['April, 2019', 137503.0], ['May, 2019', 177439.0], ['June, 2019', 143608.0], ['July, 2019', 110061.0], ['August, 2019', 123147.0], ['September, 2019', 84906.0], ['October, 2019', 135559.0], ['November, 2019', 98832.0], ['December, 2019', 96085.0], ['January, 2020', 102544.0], ['February, 2020', 79344.0], ['March, 2020', 68112.0], ['April, 2020', 99917.0], ['May, 2020', 93809.0], ['June, 2020', 85883.0], ['July, 2020', 88638.0], ['August, 2020', 89987.0], ['September, 2020', 81112.0], ['October, 2020', 79937.0], ['November, 2020', 82521.0]] );

                  var options = {
                      title: "Tx Inputs",
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