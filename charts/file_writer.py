from params import params
import os
def build_chart(x_data, y_data, key):
    if not os.path.exists("charts/"+key):
        os.makedirs("charts/"+key)
    i=0
    while y_data[i] == None:
        i+=1
    x_data=x_data[i:]
    y_data=y_data[i:]
    with open("charts/"+key+'/chart.js','w',encoding='utf-8') as f:
        if params[key]['chartType'] != 'ColumnChart':
            f.write(
                """
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('date',""" + "\""+ params[key]['x-axis'] +"\""+ """);
                    data.addColumn(""" + "\""+ params[key]['type'] +"\""+ """,""" + "\""+ params[key]['y-axis'] +"\""+ """);
                    
                    data.addRows(
	                """
            )
            f.write(str([list(i) for i in zip(*[x_data,y_data])][::int(params[key]['interval'])]).replace("'",""))
            f.write(""" );

                  var options = {
                      title: """ + "\""+ params[key]['title'] +"\""+ """,
                      curveType: """ + "'"+ params[key]['curveType'] +"'"+ """,
                      legend: { position: 'bottom' },
                      lineWidth: """ + "'"+ params[key]['lineWidth'] +"'"+ """,
                      hAxis: {title:  """ + "\""+ params[key]['x-axis'] +"\""+ """},
                      vAxis: {logScale : """ + "\""+ params[key]['logScale'] +"\""+ """,
                                title: """ + "\""+ params[key]['y-axis'] +"\""+ """,
                                format: """ + "\""+ params[key]['format'] +"\""+ """ },
                      pointSize: """ + "\""+ params[key]['pointSize'] +"\""+ """,
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.LineChart(document.getElementById('line_div'));
                      // Wait for the chart to finish drawing before calling the getImageURI() method.
                      google.visualization.events.addListener(chart, 'ready', function () {
                        document.getElementById('img').innerHTML =  '<a href="' + chart.getImageURI() + '" download=""" + "\""+ key +"\""+ """.png">Save image</a>';
                      });
                    chart.draw(data, options);
                }"""
            )
        else:
            f.write(
                """
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',""" + "\""+ params[key]['x-axis'] +"\""+ """);
                    data.addColumn(""" + "\""+ params[key]['type'] +"\""+ """,""" + "\""+ params[key]['y-axis'] +"\""+ """);
                    
                    data.addRows(
	                """
            )
            f.write(str([list(i) for i in zip(*[x_data,y_data])]))
            f.write(""" );

                  var options = {
                      title: """ + "\""+ params[key]['title'] +"\""+ """,
                      legend: { position: 'bottom' },
                      hAxis: {title:  """ + "\""+ params[key]['x-axis'] +"\""+ """},
                      vAxis: {logScale : """ + "\""+ params[key]['logScale'] +"\""+ """,
                                title: """ + "\""+ params[key]['y-axis'] +"\""+ """,
                                format: """ + "\""+ params[key]['format'] +"\""+ """ },
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById('line_div'));
                    
                      google.visualization.events.addListener(chart, 'ready', function () {
                        document.getElementById('img').innerHTML =  '<a href="' + chart.getImageURI() + '" download=""" + "\""+ key +"\""+ """.png">Save image</a>';
                      });

                    chart.draw(data, options);
                    
                }"""
            )














