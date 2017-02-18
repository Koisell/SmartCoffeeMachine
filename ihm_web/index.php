<?php
include("includes/fonctions.php");

$titre = "Accueil";

include("includes/haut.php");
?>

	<p class="intro">
		<span>Bienvenue sur le site <strong>cafe.insa-rouen.fr</strong></span>
		<br /><br />
		Ces quelques pages vous permettront de vous identifier sur la machine à café
		intelligente de l'INSA de Rouen, ou d'en apprendre plus sur ce projet d'ouverture
		mené par quatre étudiants ASI.
	</p>

	<h1>Vous n'avez pas encore créé votre compte utilisateur ?</h1>

	<p>
		Saisissez la clef d'inscription que vous a fourni la machine à café à cette adresse :

		<a href="<?php echo accesRacine(); ?>connexion/inscription.php" class="lien_important">Créer un compte utilisateur</a>
	</p>

<?php
include("includes/fin.php");
?>