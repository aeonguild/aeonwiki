
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('date',"Date");
                    data.addColumn("number","Nonce Value Normalized by Maximum Nonce Value");
                    
                    data.addRows(

                  var options = {
                      title: "Aeon Nonces",
                      curveType: 'none',
                      legend: { position: 'bottom' },
                      lineWidth: '0',
                      hAxis: {title:  "Date"},
                      vAxis: {logScale : "none",
                                title: "Nonce Value Normalized by Maximum Nonce Value",
                                format: "##.###" },
                      pointSize: "0.025",
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.LineChart(document.getElementById('line_div'));
                      // Wait for the chart to finish drawing before calling the getImageURI() method.
                      google.visualization.events.addListener(chart, 'ready', function () {
                        document.getElementById('img').innerHTML =  '<a href="' + chart.getImageURI() + '" download="nonce_recent".png">Save image</a>';
                      });
                    chart.draw(data, options);
                }