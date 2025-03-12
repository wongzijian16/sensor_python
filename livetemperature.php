<?php
 
    include('dbcon.php');
    $ref_table = 'Frozen_Lorry';
    $fetchdata = $database->getReference($ref_table)->getValue();

    if($fetchdata>0)
    {
        $dataPoints = array();
        foreach ($fetchdata as $key => $value) {
           $dataPoints[] = array("y" =>  $value["Temperature"], "label" => $value['Datetime']);
           
            }

        
    }
    else{
        ?>
            <tr>
                <td colspan="7">No record found</td>
            </tr>
        <?php
    }

    
    
?>

<html>
<head>

<script>
window.onload = function() {
 
var dataPoints = <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK); ?>;
 
var chart = new CanvasJS.Chart("chartContainer", {
	theme: "dark1",
	title: {
		text: "Live Temperature Result"
	},
	axisX:{
		title: "Date and Time"
	},
	axisY:{
		suffix: "\u2103"
	},
	data: [{
		type: "line",
		yValueFormatString: "#,##0.0#",
		toolTipContent: "Temperature:{y}\u2103 <br> Date:{label}",
		dataPoints: dataPoints
	}]
});
chart.render();
 
var updateInterval = 1500;
setInterval(function () { updateChart() }, updateInterval);
 
var xValue = dataPoints.length;
var yValue = dataPoints[dataPoints.length - 1].y;
 
function updateChart() {
	yValue += (Math.random() - 0.5) * 0.1;
	dataPoints.push({ x: xValue, y: yValue });
	xValue++;
	chart.render();
};
 
}
</script>
</head>
<body>
<div id="chartContainer" style="height: 370px; width: 100%;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>
