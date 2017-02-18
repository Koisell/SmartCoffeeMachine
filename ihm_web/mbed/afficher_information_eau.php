<?php
include("../includes/fonctions.php");

if(bacEauDeLaMachineEstVide())
{
	?>
	<div id="bandeau_information">
		<img src="<?php echo accesRacine(); ?>design/img/goutte.png" alt="Bac d'eau vide" title="Bac d'eau vide" />
		<span>
			Le bac d'eau de la machine à café est vide, elle a soif !
		</span>
	</div>
	<?php
}
?>