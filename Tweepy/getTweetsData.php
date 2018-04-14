<?php

if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    if ((isset($_GET['service']) && !empty($_GET['service'])) && isset($_GET['state']) && !empty($_GET['state'])) {

        $service = $_GET['service'];
        $state = $_GET['state'];

        $data = [$service, $state];

		// Execute the python script with the JSON data
		$result = shell_exec('python C:/wamp64/www/NUUP/TweepytweetsDataRequest.py ' . $service.' '.$state);
       // $result = shell_exec('python ./NUUP/Tweepy/tweetsDataRequest.py ' . base64_encode(json_encode($data)));

		// Decode the result
		$resultData = json_decode($result, true);

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