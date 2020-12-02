from chart_definitions import definitions
import os
def build_chart(x_data, y_data, key):
    if not os.path.exists("charts/"+key):
        os.makedirs("charts/"+key)
    with open("charts/"+key+'/chart.js','w',encoding='utf-8') as f:
        f.write(
    """
	google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('date',""" + "\""+ definitions[key]['x-axis'] +"\""+ """);
        data.addColumn(""" + "\""+ definitions[key]['type'] +"\""+ """,""" + "\""+ definitions[key]['y-axis'] +"\""+ """);
        
        data.addRows(
	    """)
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















