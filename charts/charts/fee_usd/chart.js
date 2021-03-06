
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',"Date");
                    data.addColumn("number","$");
                    
                    data.addRows(
	                [['August, 2015', 0.4080598801926088], ['September, 2015', 0.3166028313237825], ['October, 2015', 0.9774575346327103], ['November, 2015', 2.3007657701129105], ['December, 2015', 0.8445114118620347], ['January, 2016', 0.9418916658004581], ['February, 2016', 1.377668583411557], ['March, 2016', 2.0715075765587647], ['April, 2016', 2.1131558309070995], ['May, 2016', 1.386215534554847], ['June, 2016', 1.1007800193343948], ['July, 2016', 1.388014941236788], ['August, 2016', 3.1648689685052807], ['September, 2016', 10.912784754793455], ['October, 2016', 4.350631609943567], ['November, 2016', 1.7760035264430412], ['December, 2016', 4.9161191676931955], ['January, 2017', 14.297382073578428], ['February, 2017', 13.159130289806942], ['March, 2017', 13.733698177669506], ['April, 2017', 17.790850174990034], ['May, 2017', 30.80550017899155], ['June, 2017', 103.82245728773928], ['July, 2017', 59.848397447792614], ['August, 2017', 81.4765843272322], ['September, 2017', 111.78772842968125], ['October, 2017', 614.8551574156635], ['November, 2017', 504.85725310402773], ['December, 2017', 1790.4099065363316], ['January, 2018', 6975.101210855652], ['February, 2018', 728.7872531552152], ['March, 2018', 583.0749122011885], ['April, 2018', 510.33039388902995], ['May, 2018', 544.977164877441], ['June, 2018', 279.32826792311414], ['July, 2018', 230.74996779475117], ['August, 2018', 86.57073505674083], ['September, 2018', 90.89717585697989], ['October, 2018', 58.69891365329993], ['November, 2018', 78.91133389423882], ['December, 2018', 24.23836244676812], ['January, 2019', 12.619884719330859], ['February, 2019', 14.672713499031033], ['March, 2019', 20.58615940145997], ['April, 2019', 33.76575780641902], ['May, 2019', 84.37493250859097], ['June, 2019', 79.74104663841773], ['July, 2019', 42.58561674171551], ['August, 2019', 40.784812165082734], ['September, 2019', 20.25330815961434], ['October, 2019', 13.520070946817881], ['November, 2019', 9.687114630764231], ['December, 2019', 5.387245678913273], ['January, 2020', 5.241373984034609], ['February, 2020', 4.089643454050852], ['March, 2020', 2.262835656846633], ['April, 2020', 12.518615705093042], ['May, 2020', 11.590406494908434], ['June, 2020', 13.741085707275099], ['July, 2020', 10.72341680503243], ['August, 2020', 13.838715499532938], ['September, 2020', 8.259910556795605], ['October, 2020', 7.9517995461836835], ['November, 2020', 11.138061946609266], ['December, 2020', 3.9707087499713016]] );

                  var options = {
                      title: "Aeon Transaction Fees in USD",
                      legend: { position: 'bottom' },
                      hAxis: {title:  "Date"},
                      vAxis: {logScale : "true",
                                title: "$",
                                format: "scientific" },
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById('line_div'));
                    
                      google.visualization.events.addListener(chart, 'ready', function () {
                        document.getElementById('img').innerHTML =  '<a href="' + chart.getImageURI() + '" download="fee_usd".png">Save image</a>';
                      });

                    chart.draw(data, options);
                    
                }