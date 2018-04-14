
<!DOCTYPE html>
<html lang="en">
<?php 
$Servicio=$_GET["Servicio"]; 
$Estado=$_GET["Estado"]; 

?>

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Stylish Portfolio - Start Bootstrap Template</title>

    <!-- Bootstrap Core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
	<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <!-- Custom Fonts -->
    <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">
    <link href="vendor/simple-line-icons/css/simple-line-icons.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/stylish-portfolio.min.css" rel="stylesheet">

  </head>

    <!-- Navigation -->
 <body background="img/bg-callout_opt.jpg" >
    <!-- Navigation -->
    <br>
    <br>
    <br>
    <br>
    <br>
 <table>
<tr>
  <td><canvas id="polar-chart"  width="600" height="450" align="left"></canvas></td>
  <td>------------</td>
  <td><canvas id="bar-chart-grouped" width="600" height="450" align="left"></canvas></canvas></td>
</tr>
</table>


<p align="center"><a href= "index.html" style=" background-color:transparent; border: none;" ><img src="img/nuup_BotonRetroceso.png" width="80" height="80" alt="x" /></a>
                              <a href="mapview.html" style=" background-color:transparent; border: none;"><img src="img/nuup_BotonAvance.png" width="80" height="80" alt="x" /></a></p>
   
  </body>

</html>


    <script>

    $.getJSON("demo_ajax_json.js", function(result){
        $.each(result, function(i, field){
            $("div").append(field + " ");
        });
    });

    var json = '[{"Hashtag":"#notengodinero","tweets": 512},{"Hashtag":"#necesitodinero","tweets":1500},{"Hashtag":"$credito","tweets":312},{"Hashtag":"#vacaciones","tweets":212},{"Hashtag":"#Graducacion","tweets":1312}]';

 
//Lo parseamos para convertirlo en objeto
var types = JSON.parse(json);


	new Chart(document.getElementById("polar-chart"), {
    type: 'polarArea', 

    data: {
      labels: [types[0].Hashtag, types[1].Hashtag, types[2].Hashtag, types[3].Hashtag, types[4].Hashtag],
      datasets: [
        {
          label: "Population (millions)\n",
          backgroundColor: ["#444ca0", "#3f67B1","#478CCA","#70C6EF","#9DCAEC"],
          data: [types[0].tweets,types[1].tweets,types[2].tweets,types[3].tweets,types[4].tweets]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Top 5 #Hashtag Tweeter\n' 
      }
    }
});

json2 = '[{"Hashtag":"#notengodinero","insta": 512},{"Hashtag":"#necesitodinero","insta":1500},{"Hashtag":"#Graduacion","insta":312},{"Hashtag":"#vacaciones","insta":212},{"Hashtag":"#credito","insta":1312}]';
var types2 = JSON.parse(json2);
  new Chart(document.getElementById("bar-chart-grouped"), {
    type: 'bar',
    data: {
      labels: [""],
      datasets: [
        {
          label: types2[0].Hashtag,
          backgroundColor: "#FDC053",
          data: [types2[1].insta]
        }, {
          label: types2[1].Hashtag,
          backgroundColor: "#F26F48",
          data: [types2[4].insta]
        },        {
          label: types2[2].Hashtag,
          backgroundColor: "#ED2540",
          data: [types2[0].insta]
        },{
          label: types2[3].Hashtag,
          backgroundColor: "#AB3D96",
          data: [types2[2].insta]
        }, {
          label: types2[4].Hashtag,
          backgroundColor: "#5755A4",
          data: [types2[3].insta]
        } 
  
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Top 5 #Hashtag Instagram'
      }
    }
});
	</script>