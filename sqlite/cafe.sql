--
-- Base de données: cafe
--

-- --------------------------------------------------------

--
-- Structure de la table consommations
--

CREATE TABLE IF NOT EXISTS consommations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  utilisateur INTEGER NOT NULL,
  date INTEGER NOT NULL,
  longueur INTEGER NOT NULL,
  intensite INTEGER NOT NULL,
  sucre INTEGER NOT NULL,
  selection_automatique INTEGER NOT NULL DEFAULT '0',
  valeurs text
);

--
-- Contenu de la table consommations
--

INSERT INTO consommations (id, utilisateur, date, longueur, intensite, sucre, selection_automatique, valeurs) VALUES
(1, 1, 1353329616, 0, 9, 0, 0, ''),
(2, 1, 1354452816, 9, 0, 1, 0, '');

-- --------------------------------------------------------

--
-- Structure de la table parametres
--

CREATE TABLE IF NOT EXISTS parametres (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  bac_vide INTEGER NOT NULL DEFAULT '1',
  distance INTEGER NOT NULL,
  demande_purge INTEGER NOT NULL,
  demande_cafe INTEGER NOT NULL DEFAULT '0',
  demande_cafe_longueur INTEGER NOT NULL DEFAULT '0',
  demande_cafe_intensite INTEGER NOT NULL DEFAULT '0'
);

--
-- Contenu de la table parametres
--

INSERT INTO parametres (id, bac_vide, distance, demande_purge, demande_cafe, demande_cafe_longueur, demande_cafe_intensite) VALUES
(1, 0, 0, 0, 0, 1, 3);

-- --------------------------------------------------------

--
-- Structure de la table utilisateurs
--

CREATE TABLE IF NOT EXISTS utilisateurs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  uid varchar(255) NOT NULL,
  prenom varchar(255) NOT NULL,
  nom varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  mot_de_passe varchar(255) NOT NULL,
  date_inscription INTEGER NOT NULL,
  date_derniere_visite INTEGER NOT NULL,
  souhait_longueur INTEGER NOT NULL DEFAULT '-1',
  souhait_intensite INTEGER NOT NULL DEFAULT '-1',
  souhait_sucre INTEGER NOT NULL DEFAULT '-1',
  proposition_automatique INTEGER NOT NULL DEFAULT '0'
);

--
-- Contenu de la table utilisateurs
--

INSERT INTO utilisateurs (id, uid, prenom, nom, email, mot_de_passe, date_inscription, date_derniere_visite, souhait_longueur, souhait_intensite, souhait_sucre, proposition_automatique) VALUES
(1, 'user1', 'Simon', 'Rohou', 'simon.rohou@insa-rouen.fr', '61de962f19b684dc9ce24c0fdcdbd0de', 1355399619, 1355399619, 0, 1, 1, 1),
(2, 'user8', 'Anthonin', 'Liz&eacute;', 'anthonin.lize@insa-rouen.fr', '61de962f19b684dc9ce24c0fdcdbd0de', 1355176651, 1355176651, 0, 0, 1, 0),
(3, 'user9', 'Simon', 'Pro du Css', 'simon.pro_du_css@insa-rouen.fr', '6e0e17f3525f07215c728450f35d250d', 1355218273, 1355218273, 1, 0, 1, 0),
(99, 'user16', 'Regis', 'Kara', 'toto@insa-rouen.fr', 'f71dbe52628a3f83a77ab494817525c6', 1355230789, 1355230789, 0, 0, 1, 0),
(100, 'user17', 'L&eacute;o', 'Lefebvre', 'leo.lefebvre@insa-rouen.fr', 'f71dbe52628a3f83a77ab494817525c6', 1355399106, 1355399106, 1, 1, 1, 0),
(101, 'user14', 'Testp', 'Test', 'dd@insa-rouen.fr', '6226f7cbe59e99a90b5cef6f94f966fd', 1357890335, 1357890335, 0, 0, 1, 0),
(102, 'user42', 'Simon', 'Rohou', 'simon.rohou@gmail.com', 'b0faa5b71430b6636bc5216c6f390696', 1365245727, 1365245727, 0, 0, 1, 0);
