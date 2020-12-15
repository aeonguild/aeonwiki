
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',"Date");
                    data.addColumn("number","Transactions");
                    
                    data.addRows(
	                [['January, 2015', 1057.0], ['February, 2015', 85.0], ['March, 2015', 318.0], ['April, 2015', 417.0], ['May, 2015', 4594.0], ['June, 2015', 3893.0], ['July, 2015', 6222.0], ['August, 2015', 11827.0], ['September, 2015', 5828.0], ['October, 2015', 1761.0], ['November, 2015', 2487.0], ['December, 2015', 1761.0], ['January, 2016', 991.0], ['February, 2016', 1724.0], ['March, 2016', 2622.0], ['April, 2016', 1567.0], ['May, 2016', 1899.0], ['June, 2016', 1720.0], ['July, 2016', 2416.0], ['August, 2016', 2856.0], ['September, 2016', 6977.0], ['October, 2016', 5223.0], ['November, 2016', 3139.0], ['December, 2016', 5775.0], ['January, 2017', 13025.0], ['February, 2017', 7334.0], ['March, 2017', 3927.0], ['April, 2017', 10165.0], ['May, 2017', 10522.0], ['June, 2017', 10466.0], ['July, 2017', 8689.0], ['August, 2017', 10451.0], ['September, 2017', 8706.0], ['October, 2017', 16301.0], ['November, 2017', 13375.0], ['December, 2017', 20060.0], ['January, 2018', 20209.0], ['February, 2018', 12938.0], ['March, 2018', 13622.0], ['April, 2018', 17398.0], ['May, 2018', 19465.0], ['June, 2018', 16453.0], ['July, 2018', 20490.0], ['August, 2018', 13286.0], ['September, 2018', 13394.0], ['October, 2018', 14780.0], ['November, 2018', 21693.0], ['December, 2018', 10315.0], ['January, 2019', 7140.0], ['February, 2019', 7987.0], ['March, 2019', 8518.0], ['April, 2019', 9226.0], ['May, 2019', 10286.0], ['June, 2019', 9159.0], ['July, 2019', 7884.0], ['August, 2019', 7515.0], ['September, 2019', 7221.0], ['October, 2019', 9223.0], ['November, 2019', 8400.0], ['December, 2019', 4365.0], ['January, 2020', 4952.0], ['February, 2020', 3779.0], ['March, 2020', 3783.0], ['April, 2020', 3736.0], ['May, 2020', 3917.0], ['June, 2020', 4150.0], ['July, 2020', 4268.0], ['August, 2020', 3739.0], ['September, 2020', 3392.0], ['October, 2020', 3622.0], ['November, 2020', 3838.0], ['December, 2020', 1492.0]] );

                  var options = {
                      title: "Aeon Transactions",
                      legend: { position: 'bottom' },
                      hAxis: {title:  "Date"},
                      vAxis: {logScale : "none",
                                title: "Transactions",
                                format: "long" },
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById('line_div'));
                    
                      google.visualization.events.addListener(chart, 'ready', function () {
                        document.getElementById('img').innerHTML =  '<a href="' + chart.getImageURI() + '" download="tx".png">Save image</a>';
                      });

                    chart.draw(data, options);
                    
                }