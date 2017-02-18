<?php

class Longueur
{
	const TRES_COURT = 0;
	const COURT = 1;
	const NORMAL = 2;
	const LONG = 3;
	const TRES_LONG = 4;
	
	public static function nom($longueur)
	{
		switch($longueur)
		{
			case Longueur::TRES_COURT:
				return "très court";
				
			case Longueur::COURT:
				return "court";
				
			case Longueur::NORMAL:
				return "normal";
				
			case Longueur::LONG:
				return "long";
				
			case Longueur::TRES_LONG:
				return "très long";
			
			default:
				return "inconnue";
		}
	}
	
	private static function ensembleValeurs()
	{
		return array(Longueur::TRES_COURT, Longueur::COURT, Longueur::NORMAL, Longueur::LONG, Longueur::TRES_LONG);
	}
	
	public static function afficherChoix($selection)
	{
		$ensemble_longueurs = Longueur::ensembleValeurs();
		
		echo "<select name=\"longueur\">";
		
		for($i = 0 ; $i < count($ensemble_longueurs) ; $i ++)
		{
			echo "<option ";
			
			if($selection == $i)
				echo " selected=\"selected\" ";
				
			echo "<option value=\"" . $i . "\">" . Longueur::nom($ensemble_longueurs[$i]) . "</option>";
		}
		
		echo "</select>";
	}
}

class Intensite
{
	const POUDRE = 0;
	const GRAIN_TRES_ALLONGE = 1;
	const GRAIN_ALLONGE = 2;
	const GRAIN_NORMAL = 3;
	const GRAIN_SERRE = 4;
	const GRAIN_TRES_SERRE = 5;
	
	public static function nom($intensite)
	{
		switch($intensite)
		{
			case Intensite::POUDRE:
				return "en poudre : selon la dose";
				
			case Intensite::GRAIN_TRES_ALLONGE:
				return "en grains : très allongé";
			
			case Intensite::GRAIN_ALLONGE:
				return "en grains : allongé";
				
			case Intensite::GRAIN_NORMAL:
				return "en grains : normal";
			
			case Intensite::GRAIN_SERRE:
				return "en grains : serré";
			
			case Intensite::GRAIN_TRES_SERRE:
				return "en grains : très serré";
				
			default:
				return "inconnue";
		}
	}
	
	private static function ensembleValeurs()
	{
		return array(Intensite::POUDRE, Intensite::GRAIN_TRES_ALLONGE, Intensite::GRAIN_ALLONGE, Intensite::GRAIN_NORMAL, Intensite::GRAIN_SERRE, Intensite::GRAIN_TRES_SERRE);
	}
	
	public static function afficherChoix($selection)
	{
		$ensemble_intensites = Intensite::ensembleValeurs();
		
		echo "<select name=\"intensite\">";
		
		for($i = 0 ; $i < count($ensemble_intensites) ; $i ++)
		{
			echo "<option ";
			
			if($selection == $i)
				echo " selected=\"selected\" ";
				
			echo "value=\"" . $i . "\">" . Intensite::nom($ensemble_intensites[$i]) . "</option>";
		}
		
		echo "</select>";
	}
}

class Sucre
{
	public static function afficherChoix($selection)
	{
		echo "<label>aucun</label>";
	}
	
	public static function equivalentBinaireTextuel($valeur_binaire)
	{
		if($valeur_binaire)
			return "Oui";
		
		else
			return "Non";
	}
}

?>
