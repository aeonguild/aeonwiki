
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',"Date");
                    data.addColumn("number","b");
                    
                    data.addRows(
	                [['January, 2015', 35178478.0], ['February, 2015', 15785074.0], ['March, 2015', 21131899.0], ['April, 2015', 22678683.0], ['May, 2015', 71441549.0], ['June, 2015', 53294291.0], ['July, 2015', 76104474.0], ['August, 2015', 78577315.0], ['September, 2015', 27200046.0], ['October, 2015', 23359841.0], ['November, 2015', 30998782.0], ['December, 2015', 19788005.0], ['January, 2016', 10787504.0], ['February, 2016', 18266977.0], ['March, 2016', 16224882.0], ['April, 2016', 13960615.0], ['May, 2016', 16187335.0], ['June, 2016', 10427059.0], ['July, 2016', 18740461.0], ['August, 2016', 17416683.0], ['September, 2016', 29291490.0], ['October, 2016', 21178480.0], ['November, 2016', 12639204.0], ['December, 2016', 21181524.0], ['January, 2017', 34334475.0], ['February, 2017', 24704806.0], ['March, 2017', 22389233.0], ['April, 2017', 35826107.0], ['May, 2017', 40707314.0], ['June, 2017', 39197084.0], ['July, 2017', 34615055.0], ['August, 2017', 46818734.0], ['September, 2017', 35593900.0], ['October, 2017', 79879120.0], ['November, 2017', 67182648.0], ['December, 2017', 106745716.0], ['January, 2018', 112049667.0], ['February, 2018', 52634447.0], ['March, 2018', 52241953.0], ['April, 2018', 55613959.0], ['May, 2018', 56741287.0], ['June, 2018', 78535748.0], ['July, 2018', 75129118.0], ['August, 2018', 53193796.0], ['September, 2018', 54944817.0], ['October, 2018', 51923386.0], ['November, 2018', 70827019.0], ['December, 2018', 40766567.0], ['January, 2019', 26742157.0], ['February, 2019', 27495811.0], ['March, 2019', 35641284.0], ['April, 2019', 38706447.0], ['May, 2019', 48895368.0], ['June, 2019', 41071219.0], ['July, 2019', 34065198.0], ['August, 2019', 36758067.0], ['September, 2019', 27214591.0], ['October, 2019', 34637685.0], ['November, 2019', 21066179.0], ['December, 2019', 19235808.0], ['January, 2020', 20129005.0], ['February, 2020', 15589921.0], ['March, 2020', 13803040.0], ['April, 2020', 18345973.0], ['May, 2020', 18053369.0], ['June, 2020', 16875638.0], ['July, 2020', 17462227.0], ['August, 2020', 17197895.0], ['September, 2020', 15640438.0], ['October, 2020', 15397934.0], ['November, 2020', 16050386.0], ['December, 2020', 7683269.0]] );

                  var options = {
                      title: "Aeon Blockchain Size Monthly Growth",
                      legend: { position: 'bottom' },
                      hAxis: {title:  "Date"},
                      vAxis: {logScale : "none",
                                title: "b",
                                format: "decimal" },
                      explorer: { 
                        actions: ['dragToZoom', 'rightClickToReset'],
                        axis: 'horizontal',
                        keepInBounds: true,
                        maxZoomIn: 10.0},
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById('line_div'));
                    
                      google.visualization.events.addListener(chart, 'ready', function () {
                        document.getElementById('img').innerHTML =  '<a href="' + chart.getImageURI() + '" download="block_size".png">Save image</a>';
                      });

                    chart.draw(data, options);
                    
                }