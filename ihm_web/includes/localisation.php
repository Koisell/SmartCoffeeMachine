<?php

class SelectionMenu
{
	const ACCUEIL = 1;
	const CONNEXION = 2;
	const A_PROPOS = 3;
	const COMPTE = 4;
	const PREPARATION_A_DISTANCE = 5;
}	
					
function accesRacine()
{
	$acces_relatif = "";
	
	for($i = 0 ; $i < substr_count($_SERVER['SCRIPT_NAME'], "/") - 2 ; $i ++)
	{
		$acces_relatif .= "../";
	}
	
	return $acces_relatif;
}

function accesHttpRacine()
{
	include(accesRacine() . "includes/config_local.php"); // Récupération de l'adresse
	return $url_plateforme;
}

function rediriger($page, $delais = 4)
{
	echo "<meta http-equiv=\"refresh\" content=\"" . $delais . "; URL=" . $page . "\">";
}

function selectionMenu()
{
	if(isset($_SERVER['SCRIPT_NAME']))
	{
		$chemin_restant = $_SERVER['SCRIPT_NAME'];
		
		// On parcourt les dossiers
		for($i = 0 ; $i < substr_count($_SERVER['SCRIPT_NAME'], "/") - 2 ; $i ++)
		{
			$chemin_restant = substr($chemin_restant, strpos($chemin_restant, '/') + 1);
			$chemin_restant = substr($chemin_restant, strpos($chemin_restant, '/') + 1);
			$sous_chemin = substr($chemin_restant, 0, strpos($chemin_restant, '/', 1));
			
			switch($sous_chemin)
			{
				case "connexion":
					return SelectionMenu::CONNEXION;
					
				case "a_propos":
					return SelectionMenu::A_PROPOS;
					
				case "utilisateur":
					return SelectionMenu::COMPTE;
					
				case "commande_distance":
					return SelectionMenu::PREPARATION_A_DISTANCE;
					
				default:
					return null;
			}
		}
		
		return SelectionMenu::ACCUEIL;
	}
	
	return null;
}
?>
