
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',"Date");
                    data.addColumn("number","BTC");
                    
                    data.addRows(
	                [['August, 2015', 115.19193598125796], ['September, 2015', 33.18813859823169], ['October, 2015', 71.45247351563232], ['November, 2015', 100.2726932228082], ['December, 2015', 75.36278437308782], ['January, 2016', 36.69435614352108], ['February, 2016', 61.51836693850479], ['March, 2016', 42.26904411169006], ['April, 2016', 38.97225985264194], ['May, 2016', 16.593371170037873], ['June, 2016', 11.99163066548579], ['July, 2016', 22.916719961950854], ['August, 2016', 109.52106353562714], ['September, 2016', 449.8979559419079], ['October, 2016', 133.03363944302433], ['November, 2016', 68.97312402082329], ['December, 2016', 64.86008388552534], ['January, 2017', 197.53047297070316], ['February, 2017', 274.14431558662363], ['March, 2017', 102.28275434506625], ['April, 2017', 255.8183351997015], ['May, 2017', 326.5908227122264], ['June, 2017', 380.81488095819867], ['July, 2017', 167.8943597036083], ['August, 2017', 104.41483643775847], ['September, 2017', 122.62375968666811], ['October, 2017', 1168.2527840494388], ['November, 2017', 725.0715495409612], ['December, 2017', 967.2014052338312], ['January, 2018', 1203.3820398903108], ['February, 2018', 665.673952350186], ['March, 2018', 611.1271442405962], ['April, 2018', 222.28220321969877], ['May, 2018', 343.82880895306454], ['June, 2018', 120.46846732324043], ['July, 2018', 154.9879664523852], ['August, 2018', 102.01901193940523], ['September, 2018', 175.35349246116402], ['October, 2018', 97.6857302817587], ['November, 2018', 90.96732737128913], ['December, 2018', 59.45126079191934], ['January, 2019', 48.4184791925326], ['February, 2019', 27.617946329286422], ['March, 2019', 29.94948486297263], ['April, 2019', 96.7177214744282], ['May, 2019', 129.602703804131], ['June, 2019', 187.92070888491108], ['July, 2019', 80.81001401582743], ['August, 2019', 110.0589824628414], ['September, 2019', 75.36717464593231], ['October, 2019', 52.49342169048558], ['November, 2019', 8.682522095351272], ['December, 2019', 22.84706847434321], ['January, 2020', 7.284691201554186], ['February, 2020', 9.643700140216394], ['March, 2020', 6.528952615668153], ['April, 2020', 103.84277484852718], ['May, 2020', 42.05862289884557], ['June, 2020', 37.614262501911604], ['July, 2020', 44.460182606924675], ['August, 2020', 45.517347509606104], ['September, 2020', 23.389487206070168], ['October, 2020', 33.03761670256996], ['November, 2020', 21.296858853969262]] );

                  var options = {
                      title: "Aeon Transaction Output Volume measured in Bitcoins",
                      legend: { position: 'bottom' },
                      hAxis: {title:  "Date"},
                      vAxis: {logScale : "true",
                                title: "BTC",
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