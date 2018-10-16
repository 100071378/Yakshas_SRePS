-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 15, 2018 at 07:22 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 5.6.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pharmacy`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `prodID` varchar(20) NOT NULL,
  `catogory` varchar(15) DEFAULT NULL,
  `brand` varchar(20) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `instockNo` varchar(10) DEFAULT NULL,
  `Price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`prodID`, `catogory`, `brand`, `name`, `instockNo`, `Price`) VALUES
('100', 'Skin care', 'Activase', 'Neostrata', '100', 120),
('101', 'Skin care', 'Acuvail', 'Vichy', '101', 95.1),
('102', 'Skin care', 'Adagen', 'SilkN', '102', 50.1),
('103', 'Skin care', 'Actimmune', 'Gergens', '103', 115.1),
('104', 'Skin care', 'Advair HFA', 'Garnier', '104', 100.1),
('105', 'Skin care', 'Adlyxin', 'Olay', '105', 25.15),
('106', 'Eye drop', 'Systane', 'Alcaftadine', '50', 150.25),
('107', 'hygiene', 'Good virtues', 'body wash', '20', 75),
('108', 'hygiene', 'Sunsilk', 'hand soap', '10', 20),
('109', 'healthcare', 'Sunsilk', 'Shampoo', '50', 120),
('110', 'medecine', 'Pantene', 'Conditioner', '25', 120),
('111', 'healthcare', 'Bajaj', 'Panadol', '50', 60),
('112', 'intimacy', 'Nivea', 'Alcaftadine', '50', 120),
('113', 'intimacy', 'Good Virtues', 'Face wash', '75', 120),
('114', 'healthcare', 'Bajaj', 'Doliprane', '60', 115),
('115', 'hygiene', 'Erycalm', 'Body wash', '15', 45),
('116', 'healthcare', 'Sensodyne', 'toothpaste', '30', 80),
('117', 'healthcare', 'brozers', 'piriton', '20', 15.15),
('118', 'medical equip', 'elianors', 'glucose tester', '50', 800.5),
('119', 'medical equip', 'elianors', 'blood pressure', '20', 1115.3);

-- --------------------------------------------------------

--
-- Table structure for table `recorddescri`
--

CREATE TABLE `recorddescri` (
  `recordID` varchar(20) NOT NULL,
  `prodID` varchar(20) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `userID` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `recorddescri`
--

INSERT INTO `recorddescri` (`recordID`, `prodID`, `quantity`, `userID`) VALUES
('301', '100', 1, '201'),
('301', '102', 6, '201'),
('301', '119', 1, '201'),
('302', '103', 1, '202'),
('303', '110', 2, '203'),
('304', '115', 1, '201'),
('305', '115', 4, '204'),
('306', '113', 1, '204'),
('307', '107', 3, '203'),
('308', '108', 1, '202'),
('309', '105', 2, '205'),
('309', '115', 1, '205'),
('310', '115', 4, '203'),
('311', '116', 1, '204'),
('311', '117', 5, '204'),
('312', '118', 2, '201'),
('312', '119', 1, '201'),
('313', '106', 3, '203'),
('314', '107', 1, '204'),
('314', '108', 1, '204');

-- --------------------------------------------------------

--
-- Table structure for table `salesrecord`
--

CREATE TABLE `salesrecord` (
  `recordID` varchar(20) NOT NULL,
  `Date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `salesrecord`
--

INSERT INTO `salesrecord` (`recordID`, `Date`) VALUES
('301', '2018-02-28'),
('302', '2018-03-20'),
('303', '2017-05-12'),
('304', '2018-08-28'),
('305', '2018-06-02'),
('306', '2018-10-16'),
('307', '2018-10-17'),
('308', '2018-10-12'),
('309', '2018-10-12'),
('310', '2018-10-19'),
('311', '2018-10-19'),
('312', '2018-10-08'),
('313', '2018-10-18'),
('314', '2018-10-04'),
('315', '2018-10-02'),
('316', '2018-10-03'),
('317', '2018-10-02'),
('318', '2018-10-01'),
('319', '2018-10-01'),
('320', '2018-10-12');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userID` varchar(15) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userID`, `username`, `password`, `name`, `email`) VALUES
('201', 'dulitha60', 'duli60', 'Dulitha', 'dulitha60@hotmail.co'),
('202', 'Anshena', 'anshusb', 'Anshena', 'anshena@gmail.com'),
('203', 'oshane69', 'mimi123', 'Oshane', 'oshanemimi@live.com'),
('204', 'isal123', 'isalcrazy', 'Isal', 'Isal@icloud.com'),
('205', 'Sam', 'sam93', 'Samshan', 'samshan89@hotmail.co');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`prodID`);

--
-- Indexes for table `recorddescri`
--
ALTER TABLE `recorddescri`
  ADD PRIMARY KEY (`recordID`,`prodID`),
  ADD KEY `prodID` (`prodID`),
  ADD KEY `userID` (`userID`);

--
-- Indexes for table `salesrecord`
--
ALTER TABLE `salesrecord`
  ADD PRIMARY KEY (`recordID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `recorddescri`
--
ALTER TABLE `recorddescri`
  ADD CONSTRAINT `recorddescri_ibfk_1` FOREIGN KEY (`recordID`) REFERENCES `salesrecord` (`recordID`),
  ADD CONSTRAINT `recorddescri_ibfk_2` FOREIGN KEY (`prodID`) REFERENCES `product` (`prodID`),
  ADD CONSTRAINT `recorddescri_ibfk_3` FOREIGN KEY (`userID`) REFERENCES `user` (`userID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
