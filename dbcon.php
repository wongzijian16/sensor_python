<?php

require __DIR__.'/vendor/autoload.php';

use Kreait\Firebase\Factory;

$factory = (new Factory)
    ->withServiceAccount('ff-management-database-firebase-adminsdk-k4qdq-72d3659a3b.json')
    ->withDatabaseUri('https://ff-management-database-default-rtdb.firebaseio.com');
    
    $database = $factory->createDatabase();
?>