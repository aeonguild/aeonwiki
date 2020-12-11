
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',"Date");
                    data.addColumn("number","$");
                    
                    data.addRows(
	                [['August, 2015', 29776.87302769171], ['September, 2015', 7743.855850790927], ['October, 2015', 19968.754376394645], ['November, 2015', 35585.96404902444], ['December, 2015', 31760.96671847981], ['January, 2016', 14952.920153160916], ['February, 2016', 24659.195104914517], ['March, 2016', 17520.15144436394], ['April, 2016', 16595.358673812658], ['May, 2016', 7619.831046443609], ['June, 2016', 7351.969754820458], ['July, 2016', 15158.144114345474], ['August, 2016', 62994.098105417135], ['September, 2016', 271787.0599532227], ['October, 2016', 85281.12148777039], ['November, 2016', 49303.90673507234], ['December, 2016', 52997.389140644555], ['January, 2017', 180497.62107810215], ['February, 2017', 290620.2108158027], ['March, 2017', 110576.07923891283], ['April, 2017', 308660.95707379415], ['May, 2017', 619388.4608995081], ['June, 2017', 1019587.9888773988], ['July, 2017', 433948.4949478749], ['August, 2017', 411224.5507756013], ['September, 2017', 505641.7924086635], ['October, 2017', 5823243.4318052], ['November, 2017', 5374108.666541831], ['December, 2017', 14297018.317932332], ['January, 2018', 15711221.495273912], ['February, 2018', 6295081.450088469], ['March, 2018', 5441708.379274436], ['April, 2018', 1765897.7425463607], ['May, 2018', 2984613.1728802347], ['June, 2018', 829584.1065508934], ['July, 2018', 1076968.4176234226], ['August, 2018', 684915.4386627635], ['September, 2018', 1172347.1051373857], ['October, 2018', 635097.5497931185], ['November, 2018', 500979.0138953921], ['December, 2018', 219509.00355920615], ['January, 2019', 177672.21588482358], ['February, 2019', 103585.28667787935], ['March, 2019', 119491.68621291981], ['April, 2019', 501564.4018967759], ['May, 2019', 1007996.3225693124], ['June, 2019', 1716697.782682226], ['July, 2019', 876263.4909166051], ['August, 2019', 1190103.1274314742], ['September, 2019', 769692.3136718017], ['October, 2019', 437145.62191129656], ['November, 2019', 73131.69743251932], ['December, 2019', 166857.07618349185], ['January, 2020', 60065.67709412181], ['February, 2020', 96614.49090297658], ['March, 2020', 48654.550005334764], ['April, 2020', 761303.1154161991], ['May, 2020', 378272.08690353687], ['June, 2020', 355299.9942216817], ['July, 2020', 428691.32836705877], ['August, 2020', 529420.4709955903], ['September, 2020', 253421.8710407659], ['October, 2020', 389262.8431798656], ['November, 2020', 356647.9429717571]] );

                  var options = {
                      title: "Aeon Transaction Output Volume Measured in Dollars",
                      legend: { position: 'bottom' },
                      hAxis: {title:  "Date"},
                      vAxis: {logScale : "true",
                                title: "$",
                                format: "0.000E+00" },
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById('line_div'));
                    chart.draw(data, options);
                }