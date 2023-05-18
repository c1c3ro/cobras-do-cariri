-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 18-Maio-2023 às 17:43
-- Versão do servidor: 10.4.24-MariaDB
-- versão do PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `cobras`
--
CREATE DATABASE IF NOT EXISTS `cobras` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `cobras`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cobra`
--

DROP TABLE IF EXISTS `cobra`;
CREATE TABLE `cobra` (
  `idCOBRA` int(10) UNSIGNED NOT NULL,
  `peconhenta` tinyint(4) NOT NULL DEFAULT 0,
  `idUSUARIO` int(10) UNSIGNED NOT NULL,
  `familia` text NOT NULL,
  `grupo` int(11) NOT NULL,
  `especie` text NOT NULL,
  `idDenticao` int(11) DEFAULT NULL,
  `tam_max` decimal(4,1) DEFAULT NULL,
  `alimentacao` text DEFAULT NULL,
  `habitate` text DEFAULT NULL,
  `atividade` text DEFAULT NULL,
  `encontro` text NOT NULL,
  `reproducao` text DEFAULT NULL,
  `temperamento` text NOT NULL,
  `mcor` int(11) NOT NULL DEFAULT 0,
  `grande_cor` text NOT NULL,
  `segundo_cor` text NOT NULL,
  `Terceiro_Cor` text NOT NULL,
  `fonte` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `cobra`
--

INSERT INTO `cobra` (`idCOBRA`, `peconhenta`, `idUSUARIO`, `familia`, `grupo`, `especie`, `idDenticao`, `tam_max`, `alimentacao`, `habitate`, `atividade`, `encontro`, `reproducao`, `temperamento`, `mcor`, `grande_cor`, `segundo_cor`, `Terceiro_Cor`, `fonte`) VALUES
(0, 0, 1, 'Aniliidae', 0, 'Anilius scytale', 1, '110.7', 'Anfisbena, serpente, peixe, cecília', 'Fossorial (eventualmente pode ser vista no solo ou em ambiente aquático).', 'Noturna (pode ser ativo durante o dia, mas menos frequente)', 'Raro', 'vivípara', '', 0, 'Preto e vermelho (aneis alternados nas cores)', '', '', '1ª - Maschio, G. F.; Prudente, A. L. C.; Lima, A. C.; Feitosa, D. T. Reproductive Biology Of Anilius Scytale (Linnaeus, 1758) (Serpentes, Aniliidae) From Eastern Amazonia, Brazil. South American Journal of Herpetology 2(3), 179-183, 2007. 2ª - Maschio, G. F.; Prudente, A. L. C.; Rodrigues, F. S.; Hoogmoed, M. S. Food habits of Anilius scytale (Serpentes: Aniliidae) in the Brazilian Amazonia. Biology, Zoologia (Curitiba) 27 (2), 2010. \r\n'),
(1, 0, 1, 'Boidae', 1, 'Boa constrictor', 1, NULL, 'Mamíferos, aves e anfíbios', 'Terrestre (eventualmente arborícola)', 'Noturna', 'Frequente', 'vivípara', '', 0, '', '', '', ''),
(2, 0, 1, 'Boidae', 1, 'Corallus hortulana', 1, NULL, 'Roedor', 'Arborícola', 'Noturna', 'Frequente', 'vivípara', '', 0, '', '', '', '1ª - Palmuti, C. F. S.; Cassimiro, J.; Bertoluci, J. Food habits of snakes from the RPPN Feliciano Miguel Abdala, an Atlantic Forest fragment of southeastern Brazil. Biota Neotrop., vol. 9, no. 1, 2009. 2ª - Costa, H. C.; Pantoja, D. L.; Pontes, J. L.; Feio, R. N. Serpentes do Município de Viçosa, Mata Atlântica do Sudeste do Brasil. Biota Neotrop. 10 (3), 2010.'),
(3, 0, 1, 'Boidae', 1, 'Epicrates assisi', 1, NULL, 'Roedor', 'Arborícola', NULL, 'Pouco frequente', 'vivípara', '', 0, '', '', '', ''),
(4, 0, 1, 'Colubridae', 2, 'Chironius flavolineatus', 1, '140.4', 'Anuros e lagartos', 'Semi-arborícola', 'Diurna', 'Pouco frequente', 'Ovípara', '', 0, 'Cabeça marrom', 'Faixa vertebral amarela ou creme, estendendo-se por todo o corpo', 'O primeiro 1/3 do corpo é cinza escuro ou  preto', '1ª - Hamdan, B.; Fernandes, D. S. Taxonomic revision of Chironius flavolineatus (Jan, 1863) with description of a new species (Serpentes: Colubridae). Zootaxa, 4012(1), 97, 2015. 2ª - Mascarenhas, W.; Oliveira, C. R.; Ribeiro, S. C. Defensive Behaviour of Chironius flavolineatus Jan, 1863\r\n(Serpentes: Colubridae) in Northeastern Brazil. Herpetology Notes, volume 13: 607-608, 2020. 3ª - Roberto, I. J.; Souza, A. R. Review of prey items recorded for snakes of the genus\r\nChironius (Squamata, Colubridae), including the first record of\r\nOsteocephalus as prey. Herpetology Notes, volume 13: 1-5, 2020. 4ª - Pinto, R. R.; Marques, O. A. V.; Fernandes, R. Reproductive biology of two sympatric colubrid snakes, Chironius flavolineatus and Chironius quadricarinatus, from the Brazilian Cerrado domain. Amphibia-Reptilia 31 (4): 463-473, 2010.'),
(6, 0, 1, 'Colubridae', 2, 'Drymoluber dichrous', 1, NULL, 'Anuros e lagartos', 'Terrestre', 'Diurna', 'Raro', 'Ovípara', '', 1, '', '', '', '1ª - Palmuti, C. F. S.; Cassimiro, J.; Bertoluci, J. Food habits of snakes from the RPPN Feliciano Miguel Abdala, an Atlantic Forest fragment of southeastern Brazil. Biota Neotrop., vol. 9, no. 1, 2009. 2ª - Bilce, T. M.; Monteiro, L. B.; Coêlho, T. A.; De Souza, D. C. Predation of the snake Drymoluber dichrous (Peters, 1863)(Serpentes: Colubridae) by the spider Theraphosa blondi (Latreille, 1804) (Araneae: Theraphosidae) in the Brazilian Amazon. Herpetology Notes, volume 14: 239-241, 2021.'),
(7, 0, 1, 'Colubridae', 2, 'Drymoluber brazili', 1, NULL, NULL, 'Terrestre', 'Diurna', 'Raro', 'Ovípara', '', 1, '', '', '', 'Costa, H. C.; Moura R. M.; Feio, R. N. Taxonomic revision of Drymoluber Amaral, 1930 (Serpentes: Colubridae). Zootaxa 3716 (3): 349–394, 2013.'),
(8, 0, 1, 'Colubridae', 2, 'Leptophis dibernadoi', 3, NULL, NULL, NULL, NULL, 'Pouco frequente', 'Ovípara', '', 0, '', '', '', ''),
(9, 0, 1, 'Colubridae', 2, 'Oxybelis aeneus', 2, NULL, 'Lagartos, sapos e pássaros', 'Arborícola', 'Diurna', 'Pouco frequente', 'Ovípara', '', 0, 'Marrom e amarelo', 'Região ventral amarelo claro', '', '1ª - Keiser; Davis, E.; JR. Oxybelis aeneus (Wagler) Neotropical vine snake. Catalogue of American Amphibians and Reptiles, 1982. 2ª - Keiser; Davis, E.; JR.  A Monographic Study of the Neotropical Vine Snake, Oxybelis aeneus (Wagler). Louisiana State University and Agricultural & Mechanical College ProQuest Dissertations Publishing,  1967. 29117369'),
(10, 0, 1, 'Colubridae', 2, 'Spilotes pullatus', 1, NULL, 'Roedor', 'Semi-arborícola', 'Diurna', 'Frequente', 'Ovípara', '', 0, '', '', '', '1ª - Palmuti, C. F. S.; Cassimiro, J.; Bertoluci, J. Food habits of snakes from the RPPN Feliciano Miguel Abdala, an Atlantic Forest fragment of southeastern Brazil. Biota Neotrop., vol. 9, no. 1, 2009. 2ª - Costa, H. C.; Pantoja, D. L.; Pontes, J. L.; Feio, R. N. Serpentes do Município de Viçosa, Mata Atlântica do Sudeste do Brasil. Biota Neotrop. 10 (3), 2010.'),
(11, 0, 1, 'Colubridae', 2, 'Tantilla melanocephala', 2, '30.0', 'Quilópodes, principalmente centopeias (lacraias)', 'Terrestre', 'Diurna e crepúscular/noturna', 'Pouco frequente', 'Ovígera', '', 0, 'Marrom', 'Corpo marrom, bronze ou castanho', 'Região ventral cor creme ou bege', 'Wilson, L. D. Catalogue of American Amphibians and Reptiles. CAAR, 1992.'),
(12, 0, 1, 'Dipsadidae', 3, 'Atractus ronnie', 1, NULL, NULL, 'Fossorial', 'Noturna', 'Raro', 'Ovípara', '', 0, '', '', '', ''),
(13, 0, 1, 'Dipsadidae ', 3, 'Apostolepis cearensis', 2, '40.0', 'Invertebrados e larvas encontrados no solo como minhocas', 'Terrestre, fossorial, criptozoica', 'Diurna', 'Pouco frequente', 'Ovípara', '', 0, 'Preto e vermelho', 'Região dorsal do corpo vermelha ou alaranjada, região ventral branca (exceto na cabeça)', 'Sem manchas ou listras ao longo do corpo', 'Mesquita, P. C. M. D., Passos, D. C., Borges-Nojosa, D. M. & Cechin, S. z. Ecologia e história natural das serpentes de uma área de Caatinga no Nordeste brasileiro. Papeis Avulsos de Zoologia, 53(8), 99-113, 2013. '),
(14, 0, 1, 'Dipsadidae', 3, 'Boiruna sertaneja', 2, '190.0', 'Pequenos mamíferos, lagartos e serpentes', 'Terrestre ', 'Noturna', 'Frequente', 'Ovípara', '', 1, '', '', '', ''),
(15, 0, 1, 'Dipsadidae', 3, 'Helicops angulatus', 1, '100.0', NULL, 'Aquática', 'Noturna', 'Pouco frequente', 'Vivípora e ovípara', '', 0, '', '', '', 'SILVA, Raiany Cristine Cruz da. O ambiente e a diversidade das serpentes no estado do Tocantins–Brasil. 2017.'),
(17, 0, 1, 'Dipsadidae ', 3, 'Helicops leopardinus', 1, '100.0', 'Peixes e anfíbios anuros', 'Aquática', 'Noturna', 'Raro', 'Vivípara', '', 0, 'Preto e cinza', 'Região dorsal do corpo preta, acizentada, castanha ou esverdeada', 'Fileiras de manchas dorsais quadrangulares ou xadrez ', ''),
(18, 0, 1, 'Dipsadidae', 3, 'Leptodeira tarairiu', NULL, NULL, 'Carnívoros e invertebrados', 'Terrestre', 'Diurna', 'Frequente', NULL, '', 0, 'Marrom', 'Região dorsal marrom escuro listrada, região ventral, marrom claro.', '', 'https://www.biofaces.com/specie/22893/leptodeira-tarairiu'),
(19, 0, 1, 'Dipsadidae', 0, 'Lygophis dilepis', 1, '30.0', 'Minhocas, lagartos, peixes, sapos', 'Terrestre', 'Noturno', 'Frequente', 'Ovípara', '', 0, '', '', '', 'OLIVEIRA, RH de; SILVA, C. L.; ÁVILA, Robson Waldemar. Predation of Leptodactylus macrosternum Miranda-Ribeiro, 1926 (Anura: Leptodactylidae) by Lygophis dilepis Cope, 1862 (Squamata: Dipsadidae). Herpetology Notes, v. 7, p. 357-358, 2014.'),
(21, 0, 1, 'Dipsadidae', 3, 'Erythrolamprus mossoroensis', NULL, '69.4', 'Sapos', 'Terrestre e aquática ', 'Diurna e noturna', 'Raro', 'Ovípara', '', 1, 'Preto e cinza', 'Região dorsal do corpo preta, região ventral acinzentada.', '', 'MARQUES, Ricardo et al. Species richness and distribution patterns of the snake fauna of Rio Grande do Norte state, northeastern Brazil. Anais da Academia Brasileira de Ciências, v. 93, 2021.'),
(22, 0, 1, 'Dipsadidae', 3, 'Erythrolamprus poecilogyrus', 1, '80.0', 'Anuro, peixe.', 'Terrestre e semi-aquática', 'Diurno e norturno', 'Frequente', 'Ovípara', '', 1, '', '', '', ''),
(23, 0, 1, 'Dipsadidae', 3, 'Philodryas nattereri', 2, NULL, 'lagartos, aves, anfibios e peixes', 'Semi-arborícola', 'Diurna', 'Frequente', NULL, '', 0, '', '', '', 'MESQUITA, Paulo César Mattos Dourado de. História natural das serpentes Oxibelis aeneus (Wagler, 1824)(Squamata, Colubridae) e Philodryas nattereri Steindachner, 1870 (Squamata, Dipsadidae) em domínio de caatinga no estado do Ceará. 2010.'),
(24, 0, 1, 'Dipsadidae', 3, 'Erythrolamprus reginae', 1, '60.0', NULL, 'Terrestre e semi-aquática', 'Diurno e norturno', 'Pouco frequente', 'Ovípara', '', 1, '', '', '', 'SILVA, Raiany Cristine Cruz da. O ambiente e a diversidade das serpentes no estado do Tocantins–Brasil. 2017.'),
(26, 0, 1, 'Dipsadidae', 0, 'Erythrolamprus taeniogaster', NULL, NULL, 'vermes, insetos, peixes,salamandras,sapos, lagartos, anfisbenas,pássaros, mamíferos, outras serpentes e ovos de répteis.', NULL, NULL, 'Raro', NULL, '', 1, 'Preta e marrom', 'Região dorsal preta ou marrom, região ventral cor creme com listras vermelhas.', '', 'BARBOSA, LAIS DE NB et al. REPRODUCTIVE AND TROPHIC ECOLOGY OF ERYTHROLAMPRUS TAENIOGASTER (SERPENTES: DIPSADIDAE) IN THE BRAZILIAN EASTERN AMAZON. Herpetological Conservation and Biology, v. 17, n. 1, p. 131-144, 2022. BERNARDO, Pedro H. et al. Checklist of amphibians and reptiles of Reserva Biológica do Tapirapé, Pará, Brazil. Check List, v. 8, n. 5, p. 839-846, 2012.'),
(27, 0, 1, 'Dipsadidae', 3, 'Erythrolamprus viridis', NULL, '38.0', 'Anfíbios e lagartos', 'Terrestre', NULL, 'Frequente', 'Ovípara', '', 1, 'Verde e Marrom', 'Região dorsal e ventral completamente verde ou região doresal marrome região ventral e frontal verde. ', '', 'WALTERMAN, Suellen; MORAES-DA-SILVA, Antonio; CURCIO, Felipe Franco. First record of Erythrolamprus viridis (Günther, 1862) to the state of Tocantins, in the Brazillian Cerrado, with comments on some puzzling literature reports. Herpetology Notes, v. 14, p. 791-794, 2021./ http://www.portal.zoo.bio.br/media614'),
(28, 0, 1, 'Dipsadidae', 3, 'Oxyrhopus melanogenys', NULL, '68.0', NULL, NULL, NULL, 'Raro', 'Ovípara', '', 0, '', '', '', ''),
(30, 0, 1, 'Dipsadidae', 3, 'Oxyrhopus trigeminus', 2, '70.3', 'Mamíferos, lagartos e aves', 'Terrestre', 'Noturna', 'Frequente', 'Ovípara', 'dócil', 0, '', '', '', ''),
(31, 0, 1, 'Dipsadidae', 3, 'Philodryas olfersii', 2, NULL, NULL, 'Semi-arborícola', 'Diurna', 'Frequente', 'Ovípara', '', 0, '', '', '', ''),
(32, 0, 1, 'Dipsadidae', 3, 'Pseudoboa nigra', 2, NULL, 'Lagarto, roedor', 'Terrestre', 'Noturna', 'Frequente', 'Ovípara', '', 1, '', '', '', '1ª - Palmuti, C. F. S.; Cassimiro, J.; Bertoluci, J. Food habits of snakes from the RPPN Feliciano Miguel Abdala, an Atlantic Forest fragment of southeastern Brazil. Biota Neotrop., vol. 9, no. 1, 2009. 2ª - Costa, H. C.; Pantoja, D. L.; Pontes, J. L.; Feio, R. N. Serpentes do Município de Viçosa, Mata Atlântica do Sudeste do Brasil. Biota Neotrop. 10 (3), 2010.'),
(33, 0, 1, 'Dipsadidae', 3, 'Psomophis joberti', 1, '40.0', 'Anfíbios e lagartos', 'Terrestre e arborícola', 'Diurna', 'Pouco frequente', 'Ovípara', '', 0, '', '', '', 'SILVA, Raiany Cristine Cruz da. O ambiente e a diversidade das serpentes no estado do Tocantins–Brasil. 2017.'),
(35, 0, 1, 'Dipsadidae', 3, 'Dipsas mikanii', 1, '50.0', 'Gastrópodes, principalmente lesmas', 'Terrestre', 'Noturna', 'Pouco frequente', 'Ovípara', '', 0, 'Preto e branco', 'Corpo branco ou acizentado ', 'Região ventral branca', 'Costa, H. C.; Pantoja, D. L.; Pontes, J. L.; Feio, R. N. Serpentes do Município de Viçosa, Mata Atlântica do Sudeste do Brasil. Biota Neotrop. 10 (3), 2010.'),
(37, 0, 1, 'Dipsadidae', 3, 'Adelphostigma occipitalis', 1, NULL, 'Anuros e lagartos', NULL, 'Criptozoico e diurno', 'Raro', 'Ovípara', '', 0, '', '', '', 'Costa, H. C.; Pantoja, D. L.; Pontes, J. L.; Feio, R. N. Serpentes do Município de Viçosa, Mata Atlântica do Sudeste do Brasil. Biota Neotrop. 10 (3), 2010.'),
(39, 0, 1, 'Dipsadidae', 3, 'Dryophylax phoenix', 2, '47.0', 'Anfibios, lagartos, peixes e mamiferos', 'Terrestre', 'Noturna/crepuscular', 'Frequente', 'Viviparo', '', 0, '', '', '', 'COELHO, Rafael Damasceno Fernandes et al. Overview of the distribution of snakes of the genus Thamnodynastes (Dipsadidae) in northeastern Brazil, with new records and remarks on their morphometry and pholidosis. Herpetology Notes, v. 6, p. 355-360, 2013. /// FRANCO, Francisco L. et al. A new species of Thamnodynastes from the open areas of central and northeastern Brazil (Serpentes: Dipsadidae: Tachymenini). Salamandra, v. 53, n. 3, p. 339-350, 2017.'),
(40, 0, 1, 'Dipsadidae', 3, 'Dryophylax almae', 2, '54.0', 'Anfibios, lagartos, peixes e mamiferos', 'Terrestre', 'Noturna/crepuscular', 'Pouco frequente', 'Viviparo', '', 0, '', '', '', 'COELHO, Rafael Damasceno Fernandes et al. Overview of the distribution of snakes of the genus Thamnodynastes (Dipsadidae) in northeastern Brazil, with new records and remarks on their morphometry and pholidosis. Herpetology Notes, v. 6, p. 355-360, 2013. /// FRANCO, Francisco L. et al. A new species of Thamnodynastes from the open areas of central and northeastern Brazil (Serpentes: Dipsadidae: Tachymenini). Salamandra, v. 53, n. 3, p. 339-350, 2017.'),
(42, 0, 1, 'Dipsadidae', 3, 'Thamnodynastes sertanejo', 2, '67.0', 'Anfibios, lagartos, peixes e mamiferos', 'Arborícola', 'Noturna/crepuscular', 'Pouco frequente', 'Viviparo', '', 0, '', '', '', 'COELHO, Rafael Damasceno Fernandes et al. Overview of the distribution of snakes of the genus Thamnodynastes (Dipsadidae) in northeastern Brazil, with new records and remarks on their morphometry and pholidosis. Herpetology Notes, v. 6, p. 355-360, 2013.   ///  ZAHER, HUSSAM. A new species of  Thamnodynastes Wagler, 1830 from western Amazonia, with notes on morphology for members of the Thamnodynastes pallidus group (Serpentes, Dipsadidae, Tachymenini). Zootaxa, v. 4952, n. 2, p. 235-256, 2021. /// FRANCO, Francisco L. et al. A new species of Thamnodynastes from the open areas of central and northeastern Brazil (Serpentes: Dipsadidae: Tachymenini). Salamandra, v. 53, n. 3, p. 339-350, 2017.'),
(43, 0, 1, 'Dipsadidae', 3, 'Xenodon merremii', 1, NULL, NULL, 'Terrestre', 'Diurna', 'Frequente', 'Ovípara', '', 0, '', '', '', 'Costa, H. C.; Pantoja, D. L.; Pontes, J. L.; Feio, R. N. Serpentes do Município de Viçosa, Mata Atlântica do Sudeste do Brasil. Biota Neotrop. 10 (3), 2010.'),
(44, 1, 1, 'Elapidae', 4, 'Micrurus ibiboboca', 3, '150.0', 'Anfíbios, lagartos, Amphisbaeneas e outras serpentes', 'Terrestre (fossorial)', 'Diurna/noturna', 'Frequente', 'Ovípara', '', 0, '', '', '', 'BARBOSA, Vanessa do Nascimento. et al. Comportamento alimentar de Micrurus ibiboboca (Merrem, 1828) – Ingestão de regurgito. Natureza online,  17 (1): 061-063, jun 2019.   /   GOUVEIA, Soares Gouveia. et al. Case report of a coral snake bite (micrurus ibiboboca) in the state of pernambuco, northeast brazil, Umuarama, v. 24, n. 2cont., e2406, 2021.'),
(45, 1, 1, 'Elapidae ', 4, 'Micrurus lemniscatus', 3, NULL, 'Peixes, gimnofionos, anfisbênios, serpentes e lagartos', NULL, 'Noturna', 'Pouco frequente', 'Ovípara', '', 0, 'Preto, vermelho e branco', 'Padrão de anéis sequenciais vermelho, preto, branco, preto, branco, preto e vermelho', '', '1ª - PIRES, Matheus Godoy. Revisão taxonômica do complexo Micrurus lemniscatus (Linnaeus, 1758)(Serpentes: Elapidae). 2011. Tese de Doutorado. Universidade de São Paulo. 2ª - Cunha, O.R. & Nascimento, F.P. 1993. Ofídios da Amazônia: As cobras da Região Leste do Pará. Boletim do Museu Paraense Emílio Goeldi 9 (1): 1-191. 3ª - Martins, M. & Oliveira, M.E. 1998. Natural history of snakes in forests of the Manaus region, Central Amazonia, Brazil. Herpetological Natural History 6 (2): 78-150. '),
(46, 0, 1, 'Leptotyphlopidae ', 5, 'Trilepida brasiliensis', 1, '15.0', NULL, 'Terrestre (fossorial)', 'Noturna', 'Raro', 'Ovípara', '', 0, '', '', '', 'SILVA, Raiany Cristine Cruz da. O ambiente e a diversidade das serpentes no estado do Tocantins–Brasil. 2017.'),
(47, 0, 1, 'Leptotyphlopidae ', 5, 'Epictia borapeliotes', 1, '15.0', 'Artrópodes ', 'Terrestre (fossorial)', 'Noturna', 'Pouco frequente', 'Ovípara', '', 0, '', '', '', 'Campos, Gabriel Leite dos Santos. SERPENTES EM ÁREAS  SINANTROPICAS NO BREJO DE ALTITUDE PARAIBANO: UM INVENTÁRIO PARA EDUCAÇÃO '),
(48, 1, 1, 'Viperidae', 6, 'Bothrops erythromelas', 4, NULL, NULL, NULL, 'Noturna', 'Pouco frequente', 'Vivípara', '', 0, '', '', '', ''),
(51, 1, 1, 'Viperidae', 6, 'Bothrops atrox', 4, NULL, NULL, NULL, 'Noturna', 'Frequente', 'Vivípara', '', 0, '', '', '', ''),
(52, 1, 1, 'Viperidae', 6, 'Crotalus durissus', 4, NULL, NULL, 'Terrestre', 'Noturna (predominantemente)', 'Pouco frequente', 'Vivípara', '', 0, '', '', '', '');

-- --------------------------------------------------------

--
-- Estrutura da tabela `cobra_nome_pop`
--

DROP TABLE IF EXISTS `cobra_nome_pop`;
CREATE TABLE `cobra_nome_pop` (
  `idCOBRA` int(10) UNSIGNED NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `cobra_nome_pop`
--

INSERT INTO `cobra_nome_pop` (`idCOBRA`, `nome`) VALUES
(0, 'Cobra-Cega'),
(0, 'Cobra-Coral'),
(0, 'Cobra-Coral-Falsa'),
(0, 'Cobra-de-Duas-Cabeças'),
(0, 'Coral'),
(0, 'Coral-D’Água'),
(0, 'Coral-Falsa'),
(0, 'Falsa-Coral'),
(1, 'Anaconda'),
(1, 'Boiuçu'),
(1, 'Cobra-de-Veado'),
(1, 'Ctaia'),
(1, 'Jauacanga'),
(1, 'Jiboia'),
(1, 'Jiboia-Branca'),
(1, 'Jiboia-Cinzenta'),
(1, 'Jiboia-da-Cauda-Vermelha'),
(1, 'Jiboia-do-Cerrado'),
(1, 'Kuong-Kuong'),
(1, 'Salamanta-Boi'),
(1, 'Suaçu'),
(2, 'Boitinga'),
(2, 'Cobra-de-Veado'),
(2, 'Cobra-Veadeira'),
(2, 'Jiboia-Branca'),
(2, 'Salamanta'),
(2, 'Suaçuboia'),
(2, 'Suassuboia'),
(2, 'Veadeira'),
(3, 'Cobra-Arco-Íris'),
(3, 'Jiboia-Arco-Íris'),
(3, 'Jiboia'),
(3, 'Salamanta'),
(3, 'Serpente-de-Veado'),
(3, 'Serpente-Furta-Cor'),
(3, 'Uaçubói'),
(4, 'Acutimboia'),
(4, 'Acutioia'),
(4, 'Boitipó'),
(4, 'Caninana-Marrom-Listrada'),
(4, 'Cipó'),
(4, 'Cobra-Cipó'),
(4, 'Cobra-Espada'),
(4, 'Sacaiboia'),
(6, 'Cobra-Cipó'),
(6, 'Corredeira'),
(6, 'Papa-Rato'),
(6, 'Rateira'),
(7, 'Cobra-Cipó'),
(9, 'Bicuda'),
(9, 'Boitiaboia'),
(9, 'Cipó'),
(9, 'Cipó-Bicuda'),
(9, 'Cobra-Bicuda'),
(9, 'Cobra-Cipó'),
(9, 'Cobra-Cipó-Bicuda'),
(9, 'Cobra-Flecha'),
(10, 'Araboia'),
(10, 'Cainana'),
(10, 'Cainana-Flor-de-Algodão'),
(10, 'Cainana-Teiú'),
(10, 'Caninana'),
(10, 'Cobra-Tigre'),
(10, 'Cobra-Voadora'),
(10, 'Jacaninã'),
(10, 'Malha-de-Teiú'),
(10, 'Papa-Ovo'),
(10, 'Papa-Pinto'),
(10, 'Yacaninã'),
(11, 'Cinco-Minutos'),
(11, 'Cobra-da-Terra'),
(11, 'Cobra-do-Folhiço'),
(11, 'Cobra-Rainha'),
(11, 'Coral-Falsa'),
(11, 'Falsa-Cabeça-Preta'),
(11, 'Falsa-Coral'),
(11, 'Onze-Horas'),
(11, 'Tantila'),
(12, 'Cobra-da-Terra'),
(13, 'Cobra-de-Ferrão'),
(13, 'Cobra-Rainha'),
(13, 'Coral-Falsa'),
(13, 'Coralzinha'),
(13, 'Falsa-Coral'),
(14, 'Cobra-de-Leite'),
(14, 'Cobra-Preta'),
(14, 'Limpa-Mato'),
(14, 'Muçurana'),
(14, 'Mussurana'),
(15, 'Cobra-D’água'),
(15, 'Jararaca-D’água'),
(15, 'Surucucurana'),
(15, 'Trairamboia'),
(17, 'Cobra-D’água'),
(17, 'Jararaca-D’água'),
(19, 'Cobra-D’água'),
(19, 'Cobra-de-Cadarço'),
(19, 'Cobra-de-Caçote'),
(19, 'Cobra-de-Listra-Vermelha'),
(19, 'Corre-Campo'),
(21, 'Cobra-D’água'),
(21, 'Cobra-Preta'),
(21, 'Jararacuçu-D’água'),
(21, 'Jararaquinha'),
(22, 'Boipeva'),
(22, 'Casco-de-Burro'),
(22, 'Cobra-Corredeira'),
(22, 'Cobra-D’água'),
(22, 'Cobra-de-Caçote'),
(22, 'Cobra-de-Caçote-Amarela'),
(22, 'Cobra-de-Capim'),
(22, 'Cobra-de-Jardim'),
(22, 'Cobra-de-Lixo'),
(22, 'Cobra-do-Capim'),
(22, 'Cobra-do-Lixo'),
(22, 'Cobra-Lisa'),
(22, 'Cobra-Verde'),
(22, 'Cobra-Verde-Argentina'),
(22, 'Cobra-Verde-do-Capim'),
(22, 'Coral-Falsa'),
(22, 'Falsa-Coral'),
(22, 'Jararaquinha'),
(22, 'Parelheira'),
(22, 'Peça-Nova'),
(22, 'Rainha'),
(23, 'Cobra-Cipó'),
(23, 'Corre-Campo'),
(23, 'Surradeira'),
(23, 'Tabuleira'),
(24, 'Cobra-D’água'),
(24, 'Cobra-Verde'),
(24, 'Jabutuboia'),
(24, 'Jararaquinha'),
(24, 'Parelheira'),
(26, 'Cobra-Coral (juvenil)'),
(26, 'Cobra-D’água'),
(26, 'Cobra-Espada'),
(26, 'Jararaquinha'),
(26, 'Parelheira'),
(26, 'Surucucu-de-Fogo'),
(27, 'Cobra-D’água'),
(27, 'Cobra-Verde'),
(27, 'Cobra-Verde-da-Caatinga'),
(28, 'Coral'),
(28, 'Coral-Falsa'),
(28, 'Falsa-Coral'),
(30, 'Bacorá'),
(30, 'Boi-Corá'),
(30, 'Boicorá'),
(30, 'Cobra-Coral'),
(30, 'Cobra-Coral-Falsa'),
(30, 'Cobra-de-Coral'),
(30, 'Coral'),
(30, 'Coral-Falsa'),
(30, 'Falsa-Coral-de-Barriga-Branca'),
(30, 'Falsa-Coral-Tricolor'),
(31, 'Boiubu'),
(31, 'Bojobi'),
(31, 'Caninana'),
(31, 'Cipó-Verde'),
(31, 'Cobra-Cipó'),
(31, 'Cobra-Cipó-Comum'),
(31, 'Cobra-Cipó-Listrada'),
(31, 'Cobra-Cipó-Verde'),
(31, 'Cobra-Corredeira'),
(31, 'Cobra-Facão'),
(31, 'Cobra-Papagaio'),
(31, 'Cobra-Verde'),
(31, 'Cobra-Verde-Lisa'),
(31, 'Corre-Campo'),
(31, 'Papagaia'),
(31, 'Papa-Pinto'),
(32, 'Boiru'),
(32, 'Boiúna'),
(32, 'Cobra-de-Leite'),
(32, 'Cobra-Preta'),
(32, 'Coral-Falsa'),
(32, 'Falsa-Coral'),
(32, 'Limpa-Mato'),
(32, 'Limpa-Pasto'),
(32, 'Mamadeira'),
(32, 'Moçurana'),
(32, 'Muçurana'),
(32, 'Mussurana'),
(32, 'Mussurana-Limpa-Campo'),
(33, 'Cobra-Corredeira'),
(35, 'Come-Lesma'),
(35, 'Dorme-Dorme'),
(35, 'Dormideira'),
(35, 'Dormideira-de-Jardim'),
(35, 'Dorminhoca'),
(35, 'Jaracuçu-Dormideira'),
(35, 'Jararaca-Preguiçosa'),
(35, 'Papa-Lesma'),
(35, 'Urutú-Péva'),
(35, 'Urutuzinho-Pequeno'),
(37, 'Cobra-Corredeira'),
(37, 'Cobra-Capim'),
(37, 'Cobra-do-Capim'),
(37, 'Cobra-do-Folhiço'),
(37, 'Cobra-Rainha'),
(37, 'Corre-Campo'),
(37, 'Corredeira-do-Campo'),
(37, 'Corredeira-Pintada'),
(37, 'Corredeirinha'),
(37, 'Jararaquinha'),
(39, 'Cobra-Espada'),
(39, 'Corre-Campo'),
(40, 'Jararaca'),
(40, 'Jararaca-Falsa'),
(40, 'Jararaquinha'),
(42, 'Cipó-do-Papo-Amarelo'),
(42, 'Jararaquinha'),
(43, 'Achatadeira'),
(43, 'Boca-de-Caçapa'),
(43, 'Boca-de-Capanga'),
(43, 'Boipeba'),
(43, 'Boipeva'),
(43, 'Boipeva-Comum'),
(43, 'Boipeva-do-Campo'),
(43, 'Boipeva-Grande'),
(43, 'Cabeça-de-Patrona'),
(43, 'Capitão-do-Campo'),
(43, 'Capitão-do-Mato'),
(43, 'Cobra-Chata'),
(43, 'Corre-Campo'),
(43, 'Cotiara'),
(43, 'Cururuboia'),
(43, 'Esparradeira'),
(43, 'Falsa-Jararaca'),
(43, 'Focinho-de-Cachorro'),
(43, 'Goipeba'),
(43, 'Goipeva'),
(43, 'Jararaca-Malha-de-Cascavel'),
(43, 'Jaracambeva'),
(43, 'Jaracuçu'),
(43, 'Jaracuçu-Capitão'),
(43, 'Jaracuçu-de-Tapiti'),
(43, 'Jaracuçu-do-Brejo'),
(43, 'Jaracuçu-Dourado'),
(43, 'Jaracuçu-Não-Venenoso'),
(43, 'Jaracuçu-Tapete'),
(43, 'Jararaca'),
(43, 'Jararaca-Amarela'),
(43, 'Jararacambeva'),
(43, 'Jararacuçu-Bolacha'),
(43, 'Jararacuçu-Tapiti'),
(43, 'Jericá'),
(43, 'Jeriquá'),
(43, 'Jurucoá'),
(43, 'Malha-de-Sapo'),
(43, 'Mata-Boi'),
(43, 'Pepeua'),
(43, 'Pepeva'),
(43, 'Surucucu-Cascuda'),
(43, 'Urutu'),
(43, 'Urutu-Amarelo'),
(43, 'Urutu-Falsa'),
(43, 'Urutu-Preto'),
(43, 'Urutu-Tábua'),
(43, 'Urutu-Tapete'),
(44, 'Cobra-Corá'),
(44, 'Cobra-Coral'),
(44, 'Cobra-de-Coral'),
(44, 'Coral'),
(44, 'Coral-Verdadeira'),
(44, 'Ibiboboca'),
(45, 'Boichumbeguaçu'),
(45, 'Cobra-Corá'),
(45, 'Cobra-Coral'),
(45, 'Cobra-Coral-de-Bigode'),
(45, 'Cobra-Coral-da-Guiana'),
(45, 'Cobra-Coral-Vermelha'),
(45, 'Coral'),
(45, 'Coral-Verdadeira'),
(46, 'Cobra-Cega'),
(46, 'Cobra-de-Chumbinho'),
(47, 'Cobra-Chumbo'),
(47, 'Cobra-da-Terra'),
(47, 'Cobra-de-Chumbinho'),
(48, 'Cabeça-de-Capanga'),
(48, 'Jararaca'),
(48, 'Jararaca-Avermelhada'),
(48, 'Jararaca-Malha-de-Cascavel'),
(48, 'Jararaca-da-Seca'),
(48, 'Jararaca-da-Caatinga'),
(48, 'Jararaca-do-Sertão'),
(48, 'Jararaca-Rosada'),
(48, 'Jararaca-Vermelha'),
(48, 'Jararaquinha'),
(48, 'Jararacussu'),
(48, 'Jararaca-da-Folha-Seca '),
(51, 'Acuambóia'),
(51, 'Boca-Podre'),
(51, 'Cambéua'),
(51, 'Caiçaca'),
(51, 'Caiçara'),
(51, 'Comboia'),
(51, 'Cuamboia'),
(51, 'Japoboia'),
(51, 'Jaracuçu'),
(51, 'Jararaca'),
(51, 'Jararaca-Açu'),
(51, 'Jararaca-da-Amazônia'),
(51, 'Jararaca-do-Amazonas'),
(51, 'Jararaca-do-Norte'),
(51, 'Jararaca-do-Rabo-Branco'),
(51, 'Jararaca-Grão-de-Arroz'),
(51, 'Jararacarana'),
(51, 'Mapanare'),
(51, 'Surucucu'),
(51, 'Surucucu-da-Várzea'),
(51, 'Surucucu-do-Barranco'),
(51, 'Surucucurana'),
(52, 'Boicinim'),
(52, 'Boicininga'),
(52, 'Boiçununga'),
(52, 'Boiquira'),
(52, 'Cascabel'),
(52, 'Cascavé'),
(52, 'Cascavel'),
(52, 'Cascavel-de-Quatro-Ventas'),
(52, 'Cascavelha'),
(52, 'Cobra-de-Chocalho'),
(52, 'Cobra-de-Guizo'),
(52, 'Cobra-do-Chocalho'),
(52, 'Maracá'),
(52, 'Maracaboia'),
(52, 'Maracamboia'),
(52, 'Surucucu-Cascavel');

-- --------------------------------------------------------

--
-- Estrutura da tabela `denticao`
--

DROP TABLE IF EXISTS `denticao`;
CREATE TABLE `denticao` (
  `idDenticao` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `descricao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `denticao`
--

INSERT INTO `denticao` (`idDenticao`, `nome`, `descricao`) VALUES
(1, 'Áglifa', 'As serpentes que estão no grupo das áglifas caracterizam-se pela ausência de dentes com a capacidade de inocular o veneno.'),
(2, 'Opistóglifa', 'A dentição opistóglifa é caracterizada pela presença de dentes capazes de inocular o veneno, porém encontrados na região posterior da boca das serpentes. Assim como na dentição proteróglifa, os dentes apresentam um sulco por onde o veneno escorre. Em virtude de esses dentes serem encontrados na região posterior da boca, dificilmente as serpentes com esse tipo de dentição conseguem injetar o veneno durante uma mordida. Entretanto, eles são capazes de aplicar o veneno nas vítimas que estão no interior da sua boca.'),
(3, 'Proteróglifa', 'As serpentes com dentição proteróglifa caracterizam-se por possuírem dentes capazes de inocular o veneno na região anterior da boca. Esses dentes apresentam um sulco por onde o veneno escorre.'),
(4, 'Solenóglifa', 'A dentição solenóglifa se caracteriza pela presença de dentes inoculadores na região anterior da boca. As cobras com essa dentição possuem um canal no interior do dente por onde passa o veneno. Esse tipo de dentição é o mais especializado de todos os tipos descritos e, por isso, nesse grupo estão inclusas as cobras que mais causam acidentes ofídicos.'),
(5, 'Não informado', 'A dentição para esta cobra não foi informada ainda');

-- --------------------------------------------------------

--
-- Estrutura da tabela `familia`
--

DROP TABLE IF EXISTS `familia`;
CREATE TABLE `familia` (
  `idFam` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `familia`
--

INSERT INTO `familia` (`idFam`, `nome`) VALUES
(0, 'Aniliidae'),
(1, 'Boidae'),
(2, 'Colubridae'),
(3, 'Dipsadidae'),
(4, 'Elapidae'),
(5, 'Leptotyphlopidae'),
(6, 'Viperidae'),
(7, 'Não informado');

-- --------------------------------------------------------

--
-- Estrutura da tabela `hospital`
--

DROP TABLE IF EXISTS `hospital`;
CREATE TABLE `hospital` (
  `idHOSPITAL` int(10) UNSIGNED NOT NULL,
  `nome` varchar(100) NOT NULL,
  `localizacao` varchar(300) NOT NULL,
  `municipio` varchar(50) NOT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `mapa` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `hospital`
--

INSERT INTO `hospital` (`idHOSPITAL`, `nome`, `localizacao`, `municipio`, `telefone`, `mapa`) VALUES
(1, 'Hospital São Lucas', 'Rua São Benedito, nº 243 - São Miguel. CEP 63020-080', 'Juazeiro do Norte', '(88) 3587 3353', 'https://www.google.com/maps/place/Hospital+Maternidade+S%C3%A3o+Lucas/@-7.205665,-39.310192,15z/data=!4m5!3m4!1s0x0:0x6cb7789d4c312b35!8m2!3d-7.205665!4d-39.310192?hl=pt'),
(2, 'HRC - Hospital Regional do Cariri', 'Rua Catulo da Paixão, s/n - Triângulo. CEP 63041-162', 'Juazeiro do Norte', '(88) 3566 3600', 'https://www.google.com/maps/place/Hospital+Regional+do+Cariri+(HRC)/@-7.2263193,-39.3254599,15z/data=!4m5!3m4!1s0x0:0x9f3b3df2b38469ec!8m2!3d-7.2263193!4d-39.3254599?hl=pt');

-- --------------------------------------------------------

--
-- Estrutura da tabela `hospital_soro`
--

DROP TABLE IF EXISTS `hospital_soro`;
CREATE TABLE `hospital_soro` (
  `idHOSPITAL` int(10) UNSIGNED NOT NULL,
  `idCOBRA` int(10) UNSIGNED NOT NULL,
  `nome_soro` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `registro`
--

DROP TABLE IF EXISTS `registro`;
CREATE TABLE `registro` (
  `idREGISTRO` int(10) UNSIGNED NOT NULL,
  `localizacao` text NOT NULL,
  `localizacao_lat` decimal(11,8) DEFAULT NULL,
  `localizacao_log` decimal(11,8) DEFAULT NULL,
  `imagem` tinyint(4) DEFAULT NULL,
  `informacao_adc` text DEFAULT NULL,
  `data_hora` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `registro`
--

INSERT INTO `registro` (`idREGISTRO`, `localizacao`, `localizacao_lat`, `localizacao_log`, `imagem`, `informacao_adc`, `data_hora`) VALUES
(26, 'Registro teste, não exclua por enquanto', '-7.14670000', '-39.24700000', 1, 'Não excluir esse registro', '2020-05-20 11:05:00'),
(50, 'Rua Farias Brito 1667', '-7.23606840', '-39.31666810', 1, 'Ela é bem feia viu\r\nSe quiser me contatar, meu whatsapp é 88 9 9207 5140', '2022-06-20 19:03:00'),
(51, 'Teste de envio sem arquivos', '0.00000000', '0.00000000', 0, 'Não tem foto nenhuma porque eu não sou doido de ver uma cobra e sair tirando foto', '2022-06-20 19:05:00'),
(52, 'Teste Heroku', '0.00000000', '0.00000000', 1, 'Teste teste teste teste teste', '2022-06-24 00:00:00');

-- --------------------------------------------------------

--
-- Estrutura da tabela `registro_cobra`
--

DROP TABLE IF EXISTS `registro_cobra`;
CREATE TABLE `registro_cobra` (
  `idREGISTRO` int(10) UNSIGNED NOT NULL,
  `IDCOBRA` int(10) UNSIGNED NOT NULL,
  `idUSUARIO` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `idUSUARIO` int(10) UNSIGNED NOT NULL,
  `password` varchar(65) NOT NULL,
  `user` varchar(20) NOT NULL,
  `email` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `usuario`
--

INSERT INTO `usuario` (`idUSUARIO`, `password`, `user`, `email`) VALUES
(1, 'aef660c03b813f2de3e11c37465c472f6ad84e2dcdc24a4c3e0d16b49a50514f', 'csamuelssm', 'csamuelssm@gmail.com'),
(2, '12345678', 'teste', 'teste205@gmail.com'),
(3, '27f8cb5ae83708175944c94bd32e9f86c5c076b538e32bf4d1a88e9d769e423d', 'Rinvox', 'thiagocarlossilvapereira@gmail.com'),
(4, '9e6f791d2433656aa89788079cb4db22fdd812353d7cd7ed0cb08b85198e35ec', 'samuel.cardozo', 'samuel.ribeiro@ufca.edu.br'),
(18, '94689279d21cae7afb73dbe78d4022b2036b95e0c7498af6eb076274a878e027', 'c1c3ro', 'cicerosousa205@gmail.com');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `cobra`
--
ALTER TABLE `cobra`
  ADD PRIMARY KEY (`idCOBRA`),
  ADD KEY `peconhenta` (`peconhenta`,`idUSUARIO`,`grupo`,`idDenticao`,`tam_max`),
  ADD KEY `grupo` (`grupo`),
  ADD KEY `idUSUARIO` (`idUSUARIO`),
  ADD KEY `idDenticao` (`idDenticao`);

--
-- Índices para tabela `cobra_nome_pop`
--
ALTER TABLE `cobra_nome_pop`
  ADD KEY `idCOBRA` (`idCOBRA`);

--
-- Índices para tabela `denticao`
--
ALTER TABLE `denticao`
  ADD PRIMARY KEY (`idDenticao`);

--
-- Índices para tabela `familia`
--
ALTER TABLE `familia`
  ADD PRIMARY KEY (`idFam`);

--
-- Índices para tabela `hospital`
--
ALTER TABLE `hospital`
  ADD PRIMARY KEY (`idHOSPITAL`);

--
-- Índices para tabela `hospital_soro`
--
ALTER TABLE `hospital_soro`
  ADD KEY `idHOSPITAL` (`idHOSPITAL`),
  ADD KEY `idCOBRA` (`idCOBRA`);

--
-- Índices para tabela `registro`
--
ALTER TABLE `registro`
  ADD PRIMARY KEY (`idREGISTRO`),
  ADD UNIQUE KEY `idREGISTRO_UNIQUE` (`idREGISTRO`);

--
-- Índices para tabela `registro_cobra`
--
ALTER TABLE `registro_cobra`
  ADD PRIMARY KEY (`idREGISTRO`),
  ADD KEY `fk_REGISTRO_COBRA_COBRA1_idx` (`IDCOBRA`),
  ADD KEY `fk_REGISTRO_COBRA_USUARIO1_idx` (`idUSUARIO`),
  ADD KEY `idREGISTRO` (`idREGISTRO`,`IDCOBRA`);

--
-- Índices para tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idUSUARIO`),
  ADD UNIQUE KEY `idUSUARIO_UNIQUE` (`idUSUARIO`),
  ADD UNIQUE KEY `user_UNIQUE` (`user`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cobra`
--
ALTER TABLE `cobra`
  MODIFY `idCOBRA` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT de tabela `denticao`
--
ALTER TABLE `denticao`
  MODIFY `idDenticao` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `hospital`
--
ALTER TABLE `hospital`
  MODIFY `idHOSPITAL` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `registro`
--
ALTER TABLE `registro`
  MODIFY `idREGISTRO` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idUSUARIO` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `cobra`
--
ALTER TABLE `cobra`
  ADD CONSTRAINT `cobra_ibfk_2` FOREIGN KEY (`grupo`) REFERENCES `familia` (`idFam`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cobra_ibfk_3` FOREIGN KEY (`idUSUARIO`) REFERENCES `usuario` (`idUSUARIO`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cobra_ibfk_4` FOREIGN KEY (`idDenticao`) REFERENCES `denticao` (`idDenticao`);

--
-- Limitadores para a tabela `cobra_nome_pop`
--
ALTER TABLE `cobra_nome_pop`
  ADD CONSTRAINT `cobra_nome_pop_ibfk_1` FOREIGN KEY (`idCOBRA`) REFERENCES `cobra` (`idCOBRA`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `hospital_soro`
--
ALTER TABLE `hospital_soro`
  ADD CONSTRAINT `hospital_soro_ibfk_1` FOREIGN KEY (`idCOBRA`) REFERENCES `cobra` (`idCOBRA`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `hospital_soro_ibfk_2` FOREIGN KEY (`idHOSPITAL`) REFERENCES `hospital` (`idHOSPITAL`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `registro_cobra`
--
ALTER TABLE `registro_cobra`
  ADD CONSTRAINT `fk_REGISTRO_COBRA_COBRA1` FOREIGN KEY (`IDCOBRA`) REFERENCES `cobra` (`idCOBRA`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_REGISTRO_COBRA_REGISTRO1` FOREIGN KEY (`idREGISTRO`) REFERENCES `registro` (`idREGISTRO`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_REGISTRO_COBRA_USUARIO1` FOREIGN KEY (`idUSUARIO`) REFERENCES `usuario` (`idUSUARIO`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
