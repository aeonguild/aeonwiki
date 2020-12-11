from chart_definitions import definitions
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
        if definitions[key]['chartType'] != 'ColumnChart':
            f.write(
                """
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('date',""" + "\""+ definitions[key]['x-axis'] +"\""+ """);
                    data.addColumn(""" + "\""+ definitions[key]['type'] +"\""+ """,""" + "\""+ definitions[key]['y-axis'] +"\""+ """);
                    
                    data.addRows(
	                """
            )
            f.write(str([list(i) for i in zip(*[x_data,y_data])][::int(definitions[key]['interval'])]).replace("'",""))
            f.write(""" );

                  var options = {
                      title: """ + "\""+ definitions[key]['title'] +"\""+ """,
                      curveType: """ + "'"+ definitions[key]['curveType'] +"'"+ """,
                      legend: { position: 'bottom' },
                      lineWidth: """ + "'"+ definitions[key]['lineWidth'] +"'"+ """,
                      hAxis: {title:  """ + "\""+ definitions[key]['x-axis'] +"\""+ """},
                      vAxis: {logScale : """ + "\""+ definitions[key]['logScale'] +"\""+ """,
                                title: """ + "\""+ definitions[key]['y-axis'] +"\""+ """,
                                format: """ + "\""+ definitions[key]['format'] +"\""+ """ },
                      pointSize: """ + "\""+ definitions[key]['pointSize'] +"\""+ """,
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.LineChart(document.getElementById('line_div'));
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
                    data.addColumn('string',""" + "\""+ definitions[key]['x-axis'] +"\""+ """);
                    data.addColumn(""" + "\""+ definitions[key]['type'] +"\""+ """,""" + "\""+ definitions[key]['y-axis'] +"\""+ """);
                    
                    data.addRows(
	                """
            )
            f.write(str([list(i) for i in zip(*[x_data,y_data])]))
            f.write(""" );

                  var options = {
                      title: """ + "\""+ definitions[key]['title'] +"\""+ """,
                      legend: { position: 'bottom' },
                      hAxis: {title:  """ + "\""+ definitions[key]['x-axis'] +"\""+ """},
                      vAxis: {logScale : """ + "\""+ definitions[key]['logScale'] +"\""+ """,
                                title: """ + "\""+ definitions[key]['y-axis'] +"\""+ """,
                                format: """ + "\""+ definitions[key]['format'] +"\""+ """ },
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById('line_div'));
                    chart.draw(data, options);
                }"""
            )














