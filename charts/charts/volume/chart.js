
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',"Date");
                    data.addColumn("number","Coins");
                    
                    data.addRows(
	                [['January, 2015', 457497.40195616], ['February, 2015', 88980.93609073773], ['March, 2015', 920416.4080085015], ['April, 2015', 122265.61711441365], ['May, 2015', 1821704.0036218078], ['June, 2015', 1137040.7649747548], ['July, 2015', 2878990.263351019], ['August, 2015', 2645496.016932987], ['September, 2015', 1502431.0974568448], ['October, 2015', 2552975.4450845355], ['November, 2015', 2241185.967391894], ['December, 2015', 2920312.760000144], ['January, 2016', 1370173.465344374], ['February, 2016', 1935658.0464146], ['March, 2016', 1006376.5004824804], ['April, 2016', 1315104.2353998732], ['May, 2016', 868140.1567346527], ['June, 2016', 949873.0265324676], ['July, 2016', 1085141.4140815577], ['August, 2016', 1240924.8705280987], ['September, 2016', 2472774.662400077], ['October, 2016', 1482753.7021644444], ['November, 2016', 1174581.5420741246], ['December, 2016', 867837.4492189538], ['January, 2017', 1404293.9295288227], ['February, 2017', 1916571.449672439], ['March, 2017', 696154.3475301155], ['April, 2017', 1380341.9954543912], ['May, 2017', 1867470.1325886063], ['June, 2017', 1271393.0549569996], ['July, 2017', 858822.8922985641], ['August, 2017', 605465.1651369822], ['September, 2017', 514797.912230254], ['October, 2017', 3029280.1141880928], ['November, 2017', 2822314.92667272], ['December, 2017', 3471024.8090520515], ['January, 2018', 2801355.9077251684], ['February, 2018', 1917602.2877039725], ['March, 2018', 2463409.359866994], ['April, 2018', 984800.3515653596], ['May, 2018', 1605417.4560648357], ['June, 2018', 583370.7081807847], ['July, 2018', 776488.5027583238], ['August, 2018', 848877.1400356846], ['September, 2018', 1507682.7391098181], ['October, 2018', 1161074.683865166], ['November, 2018', 1054931.700695214], ['December, 2018', 776399.971587106], ['January, 2019', 629635.1948234693], ['February, 2019', 360412.09766656015], ['March, 2019', 390520.5904600193], ['April, 2019', 1347543.055674723], ['May, 2019', 1739273.2430139005], ['June, 2019', 1826614.1772618117], ['July, 2019', 1214518.3299413356], ['August, 2019', 1780015.2892035677], ['September, 2019', 1426809.2802756939], ['October, 2019', 2007723.8094364693], ['November, 2019', 328141.0887852684], ['December, 2019', 1044685.5363796599], ['January, 2020', 403615.062959414], ['February, 2020', 500455.7455404139], ['March, 2020', 376334.1204187092], ['April, 2020', 1942776.2832506406], ['May, 2020', 861084.1610977543], ['June, 2020', 682034.179136204], ['July, 2020', 1003517.8484710017], ['August, 2020', 1008258.0172239298], ['September, 2020', 617977.0587887395], ['October, 2020', 1012570.9036873829], ['November, 2020', 946935.6186354555], ['December, 2020', 587773.9599359167]] );

                  var options = {
                      title: "Aeon Transaction Output Volume",
                      legend: { position: 'bottom' },
                      hAxis: {title:  "Date"},
                      vAxis: {logScale : "none",
                                title: "Coins",
                                format: "0.000E+00" },
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById('line_div'));
                    
                      google.visualization.events.addListener(chart, 'ready', function () {
                        document.getElementById('img').innerHTML =  '<a href="' + chart.getImageURI() + '" download="volume".png">Save image</a>';
                      });

                    chart.draw(data, options);
                    
                }