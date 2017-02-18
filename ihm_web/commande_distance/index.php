<?php
include("../includes/fonctions.php");

$titre = "Préparation à distance";

include("../includes/haut.php");

if(isset($_POST['produire_cafe']))
	demanderUnCafe($_POST['longueur'], $_POST['intensite']);

if(isset($_POST['purger_machine']))
	demanderUnePurge();

$requete = bdd_query($db, "SELECT demande_purge, demande_cafe, demande_cafe_longueur AS longueur, demande_cafe_intensite AS intensite FROM parametres");
$donnees_preselection = bdd_fetch_array($requete);
	
if($donnees_preselection['demande_purge'] == 1 || $donnees_preselection['demande_cafe'] == 1)
{
	rediriger("", 1);
	?>
	<p class="intro"></p>

	<h1>Préparez un café en un clic</h1>
	<p>Instruction en cours d'exécution...</p>
	<?php
}
	
elseif($donnees_preselection['demande_purge'] == 2)
{
	rediriger("", 1);
	?>
	<p class="intro"></p>

	<h1>Préparez un café en un clic</h1>
	<p>La machine est en train d'être purgée...</p>
	<?php
}
	
elseif($donnees_preselection['demande_cafe'] == 2)
{
	rediriger("", 1);
	?>
	<p class="intro"></p>

	<h1>Préparez un café en un clic</h1>
	<p>Préparation de la boisson en cours...</p>
	<?php
}

else
{
	?>

	<p class="intro"></p>

	<h1>Préparez un café en un clic</h1>

	<?php
	if(true || machineLibre())
	{
		?>
		<p>Vous pouvez lancer une purge de la machine :</p>
		
		<form style="margin-top: 30px; text-align: center;" action="" method="post">
			<input style="padding: 6px 15px;" type="submit" value="Purger la machine" />
			<input type="hidden" name="purger_machine" value="1" />
		</form>
		
		<br />
		
		<p>Ou préparer un café à distance :</p>
		<div id="parametres_prochaine_consommation">
			<div id="informations_souhait" style="width: 90%;">
				<form style="text-align: center;" action="" method="post">
					<ul>
						<li>Longueur :&nbsp;&nbsp; <?php Longueur::afficherChoix($donnees_preselection['longueur']); ?></li>
						<li>Intensité &nbsp;:&nbsp;&nbsp; <?php Intensite::afficherChoix($donnees_preselection['intensite']); ?></li>
					</ul>
					<br />
					<input style="padding: 6px 15px;" type="submit" value="Préparer un café" />
					<input type="hidden" name="produire_cafe" value="1" />
				</form>
			</div>
		</div>
		<?php
	}
	
	else
	{
		?>
		La machine est actuellement en cours d'utilisation.
		<?php
	}
}
?>

<?php
include("../includes/fin.php");
?>