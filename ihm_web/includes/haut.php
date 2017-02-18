<?php
// Affichage d'un titre dans la barre du navigateur
if(isset($titre))
	$titre_fenetre = $titre . " - ";

else
	$titre_fenetre = "";
?>

<!DOCTYPE html>

<html>
	
	<head>
		
		<title><?php echo $titre_fenetre . "Machine à café intelligente de l'INSA de Rouen"; ?></title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="author" content="Laurent Georges, Léo Lefebvre, Anthonin Lizé et Simon Rohou" />
		<link rel="stylesheet" media="screen" type="text/css" title="style" href="<?php echo accesRacine(); ?>/design/style.css" />
		<script src="<?php echo accesRacine(); ?>/includes/javascript/jquery.min.js"></script>
		
<!-- 		<script>
			function actualiser()
			{
				$('#actualisation_bandeau').load('<?php echo accesRacine(); ?>mbed/afficher_information_eau.php');
			}
			
			var refreshId = setInterval(actualiser, 500);
		</script>
 -->
	</head>
	
	<body>
		
		<div id="page">
			
			<a href="<?php echo accesRacine(); ?>"><span class="titre">Café</span></a>
			<span class="sous-titre">
				<?php 
				if(utilisateurEstIdentifie())
					echo "Comme d'habitude monsieur " . nomUtilisateur() . " ?";
				
				else
					echo "Quand de la reconnaissance faciale se mélange à de la caféine...";
				?>
			</span>
			
			<div id="cadre_principal">
				
				<div id="menu">
					<ul>
						<?php
						$base = "href=\"";
						$base_selection = "class=\"selection\" " . $base;
						$selection_accueil = $base;
						$selection_connexion = $base;
						$selection_compte = $base;
						$selection_preparation_distance = $base;
						$selection_a_propos = $base;
						
						switch(selectionMenu())
						{
							case SelectionMenu::ACCUEIL;
								$selection_accueil = $base_selection;
								break;
								
							case SelectionMenu::CONNEXION;
								$selection_connexion = $base_selection;
								break;
					
							case SelectionMenu::A_PROPOS;
								$selection_a_propos = $base_selection;
								break;
								
							case SelectionMenu::COMPTE;
								$selection_compte = $base_selection;
								break;
								
							case SelectionMenu::PREPARATION_A_DISTANCE;
								$selection_preparation_distance = $base_selection;
								break;
						}
						
						if(utilisateurEstIdentifie())
							$prefixe_connexion = "Déc";
						
						else
							$prefixe_connexion = "C";
						?>
					
						<li class="accueil"><a <?php echo $selection_accueil . accesRacine(); ?>">Accueil</a></li>
						<li class="connexion"><a <?php echo $selection_connexion . accesRacine(); ?>/connexion"><?php echo $prefixe_connexion; ?>onnexion</a></li>
						<li class="compte"><a <?php echo $selection_compte . accesRacine(); ?>/utilisateur">Votre compte</a></li>
						<li class="preparer"><a <?php echo $selection_preparation_distance . accesRacine(); ?>/commande_distance">Préparer un café</a></li>
						<li class="apropos"><a <?php echo $selection_a_propos . accesRacine(); ?>/a_propos">À propos</a></li>
					</ul>
				</div>
				
				<div id="contenu">
					