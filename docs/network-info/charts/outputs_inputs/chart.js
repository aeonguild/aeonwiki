
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',"Date");
                    data.addColumn("number","#");
                    
                    data.addRows(
	                [['January, 2015', -113010.0], ['February, 2015', 397.0], ['March, 2015', -25302.0], ['April, 2015', -29242.0], ['May, 2015', -273804.0], ['June, 2015', -216353.0], ['July, 2015', -300093.0], ['August, 2015', -303333.0], ['September, 2015', -104847.0], ['October, 2015', -130990.0], ['November, 2015', -158193.0], ['December, 2015', -108015.0], ['January, 2016', -31401.0], ['February, 2016', -107501.0], ['March, 2016', -40438.0], ['April, 2016', -34336.0], ['May, 2016', -69659.0], ['June, 2016', -21498.0], ['July, 2016', -89964.0], ['August, 2016', -63206.0], ['September, 2016', -29576.0], ['October, 2016', -29343.0], ['November, 2016', -29756.0], ['December, 2016', -32538.0], ['January, 2017', -6913.0], ['February, 2017', -1639.0], ['March, 2017', -4180.0], ['April, 2017', 14174.0], ['May, 2017', -1022.0], ['June, 2017', 19185.0], ['July, 2017', 50172.0], ['August, 2017', 63963.0], ['September, 2017', 44569.0], ['October, 2017', 29474.0], ['November, 2017', -13122.0], ['December, 2017', -58872.0], ['January, 2018', -148121.0], ['February, 2018', 70960.0], ['March, 2018', 114948.0], ['April, 2018', 104409.0], ['May, 2018', 108787.0], ['June, 2018', 169711.0], ['July, 2018', 68711.0], ['August, 2018', -23365.0], ['September, 2018', -49941.0], ['October, 2018', -300.0], ['November, 2018', -16917.0], ['December, 2018', -14514.0], ['January, 2019', -6925.0], ['February, 2019', -26245.0], ['March, 2019', -66655.0], ['April, 2019', -61985.0], ['May, 2019', -81319.0], ['June, 2019', -55244.0], ['July, 2019', -745.0], ['August, 2019', -25837.0], ['September, 2019', 15350.0], ['October, 2019', -54930.0], ['November, 2019', -26187.0], ['December, 2019', -52536.0], ['January, 2020', -57880.0], ['February, 2020', -50360.0], ['March, 2020', -39569.0], ['April, 2020', -70125.0], ['May, 2020', -60905.0], ['June, 2020', -50847.0], ['July, 2020', -51293.0], ['August, 2020', -59135.0], ['September, 2020', -54596.0], ['October, 2020', -52063.0], ['November, 2020', -53762.0]] );

                  var options = {
                      title: "Aeon Transaction Outputs minus Inputs",
                      legend: { position: 'bottom' },
                      hAxis: {title:  "Date"},
                      vAxis: {logScale : "none",
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