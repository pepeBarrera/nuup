<?php

if ($_SERVER['REQUEST_METHOD'] == 'GET') {

    if ((isset($_GET['service']) && !empty($_GET['service'])) && isset($_GET['state']) && !empty($_GET['state'])) {

        $service = $_GET['service'];
        $state = $_GET['state'];

		// Execute the python script with the JSON data
		$result = shell_exec('python ./NUPP/Tweepy/tweetsDataRequest.py ' . $service.' '.$state );
print $result;
		// Decode the result
		$resultData = json_decode($result, true);

        print $result;

		print json_encode($resultData);

    } else {
        // Enviar respuesta de error
        print json_encode(
            array(
                'success' => 'false',
                'mensaje' => 'Error al recibir identificador'
            )
        );
    }
}

?>