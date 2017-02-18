<?php

function dateTextuelle($time, $detailler_jour = false, $preciser_annee = true, $preciser_heure = false, $sep = '/')
{
	// Informations sur le jour
	if($detailler_jour)
	{
		switch(date("N", $time))
		{
			case 1:
				$info_jour = "Lundi";
				break;
				
			case 2:
				$info_jour = "Mardi";
				break;
				
			case 3:
				$info_jour = "Mercredi";
				break;
				
			case 4:
				$info_jour = "Jeudi";
				break;
				
			case 5:
				$info_jour = "Vendredi";
				break;
				
			case 6:
				$info_jour = "Samedi";
				break;
				
			case 7:
				$info_jour = "Dimanche";
				break;
		}
		
		$info_jour .= " ";
	}

	else
		$info_jour = "";
	
	// Informations sur l'année
	if($preciser_annee)
		$detail_annee =  $sep . "Y";
	
	else
		$detail_annee = "";
	
	// Informations sur l'heure
	if($preciser_heure)
		$detail_heure =  " à " . "H:i";
	
	else
		$detail_heure = "";
		
	return $info_jour . date("d" . $sep . "m" . $detail_annee . $detail_heure, $time);
}

?>