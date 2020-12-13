
	            google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {
                    var data = new google.visualization.DataTable();
                    data.addColumn('string',"Date");
                    data.addColumn("number","Coins");
                    
                    data.addRows(
	                [['January, 2015', 0.4605111635309965], ['February, 2015', 0.019100262291], ['March, 2015', 0.9509421602640001], ['April, 2015', 0.0724306900990002], ['May, 2015', 0.7198916600889893], ['June, 2015', 6.875533785434957], ['July, 2015', 1.959719493400904], ['August, 2015', 34.22939667458022], ['September, 2015', 53.525338055261244], ['October, 2015', 101.34371242696795], ['November, 2015', 156.58514980637068], ['December, 2015', 82.96228933771896], ['January, 2016', 86.45024735216153], ['February, 2016', 110.8956759734226], ['March, 2016', 125.77221260709936], ['April, 2016', 173.22000128909488], ['May, 2016', 162.43273991601532], ['June, 2016', 163.21289827024103], ['July, 2016', 95.21509072732799], ['August, 2016', 90.55007329728615], ['September, 2016', 101.35536840773015], ['October, 2016', 72.71751246340466], ['November, 2016', 40.27737480277441], ['December, 2016', 75.79280169683473], ['January, 2017', 113.70028340652418], ['February, 2017', 84.9426030433557], ['March, 2017', 79.03287352767207], ['April, 2017', 79.970711254761], ['May, 2017', 90.62880966032961], ['June, 2017', 143.12882016120233], ['July, 2017', 119.22112557493533], ['August, 2017', 123.75710976688896], ['September, 2017', 111.56346027236584], ['October, 2017', 326.57870291461], ['November, 2017', 227.19564326820125], ['December, 2017', 428.9293019103282], ['January, 2018', 1473.4277126910267], ['February, 2018', 219.42021184306088], ['March, 2018', 240.86152983164192], ['April, 2018', 279.34290261345683], ['May, 2018', 301.6432516706387], ['June, 2018', 195.79991334378852], ['July, 2018', 166.4471909426752], ['August, 2018', 96.98560049882316], ['September, 2018', 124.73182977939662], ['October, 2018', 106.13704237990989], ['November, 2018', 157.41683681496716], ['December, 2018', 86.6414533186032], ['January, 2019', 44.632047463223266], ['February, 2019', 51.97183138179807], ['March, 2019', 68.32288782911161], ['April, 2019', 90.28052560794227], ['May, 2019', 147.62696143810354], ['June, 2019', 84.82806497965369], ['July, 2019', 59.1439038389878], ['August, 2019', 60.891504808531124], ['September, 2019', 40.95275095927496], ['October, 2019', 64.71822303507093], ['November, 2019', 42.72521473166104], ['December, 2019', 32.77658338575518], ['January, 2020', 35.237898280136065], ['February, 2020', 21.9323595855851], ['March, 2020', 18.329224150264977], ['April, 2020', 38.15294134918801], ['May, 2020', 26.460796834421078], ['June, 2020', 25.195046797328025], ['July, 2020', 25.564628997996017], ['August, 2020', 26.504522009011048], ['September, 2020', 20.54208165000807], ['October, 2020', 20.986102247784036], ['November, 2020', 29.048415439611027], ['December, 2020', 9.766368490002998]] );

                  var options = {
                      title: "Aeon Transaction Fees",
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
                        document.getElementById('img').innerHTML =  '<a href="' + chart.getImageURI() + '" download="fee".png">Save image</a>';
                      });

                    chart.draw(data, options);
                    
                }