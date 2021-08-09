-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 08, 2021 at 05:46 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `digitalibrary`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `Id` int(10) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `email` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`Id`, `username`, `password`, `email`) VALUES
(1, 'Ali', '123456', ''),
(2, 'Afaq', '123', ''),
(4, 'inzi', '123', 'inziraja@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `citationcontext`
--

CREATE TABLE `citationcontext` (
  `CitationId` int(30) NOT NULL,
  `PaperName` varchar(300) NOT NULL,
  `CitationContext` longtext NOT NULL,
  `Sentiments` varchar(100) NOT NULL,
  `Subjectivity` double NOT NULL,
  `PaperId` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `citedpaper`
--

CREATE TABLE `citedpaper` (
  `CitedPaperId` int(30) NOT NULL,
  `ReferencePaper` varchar(300) NOT NULL,
  `CitationId` int(30) NOT NULL,
  `CitingPaperName` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `cittingpaper`
--

CREATE TABLE `cittingpaper` (
  `PaperId` int(30) NOT NULL,
  `PaperName` varchar(300) DEFAULT NULL,
  `AuthorName` varchar(200) DEFAULT NULL,
  `CreationDate` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `citationcontext`
--
ALTER TABLE `citationcontext`
  ADD PRIMARY KEY (`CitationId`),
  ADD KEY `PaperId` (`PaperId`);

--
-- Indexes for table `citedpaper`
--
ALTER TABLE `citedpaper`
  ADD PRIMARY KEY (`CitedPaperId`),
  ADD KEY `CitationId` (`CitationId`);

--
-- Indexes for table `cittingpaper`
--
ALTER TABLE `cittingpaper`
  ADD PRIMARY KEY (`PaperId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `citationcontext`
--
ALTER TABLE `citationcontext`
  MODIFY `CitationId` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19593;

--
-- AUTO_INCREMENT for table `citedpaper`
--
ALTER TABLE `citedpaper`
  MODIFY `CitedPaperId` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19811;

--
-- AUTO_INCREMENT for table `cittingpaper`
--
ALTER TABLE `cittingpaper`
  MODIFY `PaperId` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=296;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
