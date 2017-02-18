<?php 

function connexionBase($path2DB)
{
	return $db = new SQLite3($path2DB); // Retour sur la base de l'application
}

function bdd_query($db, $requete)
{
	return $db->query($requete);
}

function bdd_close($db){
    return $db->close();
}

function bdd_fetch_array($result_set){
    return $result_set->fetchArray()
}

$path2DB = "/home/pi/Documents/SQLite/cafe.db";

// Par défaut, on se connecte sur la base principale
$db = connexionBase($path2DB);
?>
