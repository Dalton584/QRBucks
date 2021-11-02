-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 30, 2021 at 05:47 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `QRBucks`
--

-- --------------------------------------------------------

--
-- Table structure for table `Beverages`
--

CREATE TABLE `Beverages` (
  `BeverageID` int(11) NOT NULL,
  `BeverageName` varchar(200) NOT NULL,
  `Tall` float NOT NULL,
  `Grande` float NOT NULL,
  `Venti` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Beverages`
--

INSERT INTO `Beverages` (`BeverageID`, `BeverageName`, `Tall`, `Grande`, `Venti`) VALUES
(1, 'Americano', 2.25, 4.25, 6.25),
(2, 'Blonde Roast', 2.25, 4.25, 6.25),
(3, 'Pike Place Roast', 2.25, 4.25, 6.25),
(4, 'Dark Roast', 2.25, 4.25, 6.25),
(5, 'Decaf Pike Place Roast', 2.25, 4.25, 6.25),
(6, 'Cappuccino', 3.5, 4.75, 6.75),
(7, 'Espresso', 3.5, 4.75, 6.75),
(8, 'Espresso Con Panna', 3.5, 4.75, 6.75),
(9, 'Flat White', 3.5, 4.75, 6.75),
(10, 'Honey Almondmilk Flat White', 3.5, 4.75, 6.75),
(11, 'Pumpkin Spice Latte', 3.75, 4.95, 6.95),
(12, 'Honey Oatmilk Latte', 3.75, 4.95, 6.95),
(13, 'Latte', 3.75, 4.95, 6.95),
(14, 'Cinnamon Dolce Latte', 3.75, 4.95, 6.95),
(15, 'Blonde Vanilla Latte', 3.75, 4.95, 6.95),
(16, 'Apple Crisp Macchiato', 3.75, 4.95, 6.95),
(17, 'Caramel Macchiato', 3.75, 4.95, 6.95),
(18, 'Espresso Macchiato', 3.75, 4.95, 6.95),
(19, 'Mocha', 3.75, 4.95, 6.95),
(20, 'White Chocolate Mocha', 3.75, 4.95, 6.95),
(21, 'Pumpkin Cream Cold Brew', 2.5, 3.95, 6),
(22, 'Salted Caramel Cream Cold Brew', 2.5, 3.95, 6),
(23, 'Honey Almondmilk Cold Brew', 2.5, 3.95, 6),
(24, 'Cold Brew', 2.5, 3.95, 6),
(25, 'Vanilla Sweet Cream Cold Brew', 2.5, 3.95, 6),
(26, 'Cold Brew With Milk', 2.5, 3.95, 6),
(27, 'Honey Almondmilk Nitro Cold Brew', 2.5, 3.95, 6),
(28, 'Nitro Cold Brew', 2.5, 3.95, 6),
(29, 'Vanilla Sweet Cream Nitro Cold Brew', 2.5, 3.95, 6),
(30, 'Iced Coffee', 2.75, 4.1, 6.25),
(31, 'Iced Coffee with Milk', 2.75, 4.1, 6.25),
(32, 'Iced Brown Sugar Oatmilk Shaken Espresso', 3, 4.75, 6.5),
(33, 'Iced Chocolate Almondmilk Shaken Espresso', 3, 4.75, 6.5),
(34, 'Iced Shaken Espresso', 3, 4.75, 6.5),
(35, 'Chai Tea', 3, 4.25, 6),
(36, 'Chai Tea Latte', 3, 4.25, 6),
(37, 'Earl Grey Tea', 3, 4.25, 6),
(38, 'London Fog Tea Latte', 3, 4.25, 6),
(39, 'Royal English Breakfast Tea', 3, 4.25, 6),
(40, 'Royal English Breakfast Tea Latte', 3, 4.25, 6),
(41, 'Emperor’s Clouds & Mist', 3, 4.25, 6),
(42, 'Matcha Tea Latte', 3, 4.25, 6),
(43, 'Honey Citrus Mint Tea', 3, 4.25, 6),
(44, 'Jade Citrus Mint Tea', 3, 4.25, 6),
(45, 'Mint Majesty', 3, 4.25, 6),
(46, 'Peach Tranquility', 3, 4.25, 6),
(47, 'Iced Guava Black Tea', 3, 4.25, 6),
(48, 'Iced Guava Black Tea Lemonade', 3, 4.25, 6),
(49, 'Iced Black Tea', 3, 4.25, 6),
(50, 'Iced Black Tea Lemonade', 3, 4.25, 6),
(51, 'Iced Royal English Breakfast Tea Latte', 3, 4.25, 6),
(52, 'Iced London Fog Tea Latte', 3, 4.25, 6),
(53, 'Iced Chai Tea Latte', 3, 4.25, 6),
(54, 'Iced Peach Green Tea', 3, 4.25, 6),
(55, 'Iced Peach Green Tea Lemonade', 3, 4.25, 6),
(56, 'Iced Matcha Tea Latte', 3, 4.25, 6),
(57, 'Iced Green Tea', 3, 4.25, 6),
(58, 'Iced Green Tea Lemonade', 3, 4.25, 6),
(59, 'Iced Matcha Lemonade', 3, 4.25, 6),
(60, 'Iced Passion Tango Tea', 3, 4.25, 6),
(61, 'Iced Passion Tango Tea Lemonade', 3, 4.25, 6),
(62, 'Pumpkin Spice Frappuccino', 3.5, 4.75, 6.5),
(63, 'Apple Crisp Frappuccino', 3.5, 4.75, 6.5),
(64, 'Strawberry Funnel Cake Frappuccino', 3.5, 4.75, 6.5),
(65, 'Mocha Cookie Crumble Frappuccino', 3.5, 4.75, 6.5),
(66, 'Caramel Ribbon Crunch Frappuccino', 3.5, 4.75, 6.5),
(67, 'Espresso Frappuccino', 3.5, 4.75, 6.5),
(68, 'Caffè Vanilla Frappuccino', 3.5, 4.75, 6.5),
(69, 'Caramel Frappuccino', 3.5, 4.75, 6.5),
(70, 'Coffee Frappuccino', 3.5, 4.75, 6.5),
(71, 'Mocha Frappuccino', 3.5, 4.75, 6.5),
(72, 'Java Chip Frappuccino', 3.5, 4.75, 6.5),
(73, 'White Chocolate Mocha Frappuccino', 3.5, 4.75, 6.5),
(74, 'Pumpkin Spice Creme Frappuccino', 3.5, 4.75, 6.5),
(75, 'Apple Crisp Creme Frappuccino', 3.5, 4.75, 6.5),
(76, 'Strawberry Funnel Cake Creme Frappuccino', 3.5, 4.75, 6.5),
(77, 'Chocolate Cookie Crumble Creme Frappuccino', 3.5, 4.75, 6.5),
(78, 'Caramel Ribbon Crunch Creme Frappuccino', 3.5, 4.75, 6.5),
(79, 'Strawberry Creme Frappuccino', 3.5, 4.75, 6.5),
(80, 'Chai Creme Frappuccino', 3.5, 4.75, 6.5),
(81, 'Double Chocolatey Chip Creme Frappuccino', 3.5, 4.75, 6.5),
(82, 'Match Creme Frappuccino', 3.5, 4.75, 6.5),
(83, 'Vanilla Bean Creme Frappuccino', 3, 4.25, 6),
(84, 'White Chocolate Creme Frappuccino', 3, 4.25, 6),
(85, 'Hot Chocolate', 3, 4.25, 6),
(86, 'White Hot Chocolate', 3, 4.25, 6),
(87, 'Caramel Apple Spice', 3, 4.25, 6),
(88, 'Steamed Apple Juice', 3, 4.25, 6),
(89, 'Pumpkin Spice Creme', 3, 4.25, 6),
(90, 'Cinnamon Dolce Creme', 3, 4.25, 6),
(91, 'Steamed Milk', 3, 4.25, 6),
(92, 'Vanilla Creme', 3, 4.25, 6),
(93, 'Star Drink', 3, 4.25, 6),
(94, 'Kiwi Starfruit Refresher', 3, 4.25, 6),
(95, 'Kiwi Starfruit Refresher Lemonade', 3, 4.25, 6),
(96, 'Dragon Drink', 3, 4.25, 6),
(97, 'Mango Dragonfruit Refresher', 3, 4.25, 6),
(98, 'Mango Dragonfruit Refresher Lemonade', 3, 4.25, 6),
(99, 'Pink Drink', 3, 4.25, 6),
(100, 'Strawberry Acai Refresher', 3, 4.25, 6),
(101, 'Strawberry Acai Refresher Lemonade', 3, 4.25, 6),
(102, 'Violet Drink', 3, 4.25, 6),
(103, 'Very Berry Refresher', 3, 4.25, 6),
(104, 'Very Berry Refresher Lemonade', 3, 4.25, 6),
(105, 'Blended Strawberry Lemonade', 3, 4.25, 6),
(106, 'Lemonade', 2.75, 4, 5.5),
(107, 'Water', 2.75, 4, 5.5),
(108, 'Milk', 2.75, 4, 5.5);

-- --------------------------------------------------------

--
-- Table structure for table `Drizzles`
--

CREATE TABLE `Drizzles` (
  `DrizzleID` int(11) NOT NULL,
  `DrizzleName` varchar(50) NOT NULL,
  `DrizzlePrice` float NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Drizzles`
--

INSERT INTO `Drizzles` (`DrizzleID`, `DrizzleName`, `DrizzlePrice`) VALUES
(1, 'Mocha Drizzle', 0.1),
(2, 'Caramel Drizzle', 0.1),
(3, 'Strawberry Drizzle', 0.1);

-- --------------------------------------------------------

--
-- Table structure for table `Espresso`
--

CREATE TABLE `Espresso` (
  `EspressoID` int(11) NOT NULL,
  `EspressoName` varchar(50) NOT NULL,
  `EspressoPrice` float NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Espresso`
--

INSERT INTO `Espresso` (`EspressoID`, `EspressoName`, `EspressoPrice`) VALUES
(1, 'Blonde', 0.5),
(2, 'Regular', 0.5),
(3, 'Decaf', 0.5);

-- --------------------------------------------------------

--
-- Table structure for table `Milk`
--

CREATE TABLE `Milk` (
  `MilkID` int(11) NOT NULL,
  `MilkName` varchar(50) NOT NULL,
  `MilkPrice` float NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Milk`
--

INSERT INTO `Milk` (`MilkID`, `MilkName`, `MilkPrice`) VALUES
(1, '2%', 0.5),
(2, 'Whole', 0.5),
(3, 'Skim', 0.5),
(4, 'Almond', 0.5),
(5, 'Oat', 0.5),
(6, 'Coconut', 0.5),
(7, 'Soy', 0.5);

-- --------------------------------------------------------

--
-- Table structure for table `Syrups`
--

CREATE TABLE `Syrups` (
  `SyrupID` int(11) NOT NULL,
  `SyrupName` varchar(50) NOT NULL,
  `SyrupPrice` float NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Syrups`
--

INSERT INTO `Syrups` (`SyrupID`, `SyrupName`, `SyrupPrice`) VALUES
(1, 'Vanilla', 0.25),
(2, 'Caramel', 0.25),
(3, 'Hazelnut', 0.25),
(4, 'Brown Sugar', 0.25),
(5, 'Apple Brown Sugar', 0.25),
(6, 'Sugar Free Vanilla', 0.25),
(7, 'Liquid Cane', 0.25),
(8, 'Classic', 0.25);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Beverages`
--
ALTER TABLE `Beverages`
  ADD PRIMARY KEY (`BeverageID`);

--
-- Indexes for table `Drizzles`
--
ALTER TABLE `Drizzles`
  ADD PRIMARY KEY (`DrizzleID`);

--
-- Indexes for table `Espresso`
--
ALTER TABLE `Espresso`
  ADD PRIMARY KEY (`EspressoID`);

--
-- Indexes for table `Milk`
--
ALTER TABLE `Milk`
  ADD PRIMARY KEY (`MilkID`);

--
-- Indexes for table `Syrups`
--
ALTER TABLE `Syrups`
  ADD PRIMARY KEY (`SyrupID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Beverages`
--
ALTER TABLE `Beverages`
  MODIFY `BeverageID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;

--
-- AUTO_INCREMENT for table `Drizzles`
--
ALTER TABLE `Drizzles`
  MODIFY `DrizzleID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Espresso`
--
ALTER TABLE `Espresso`
  MODIFY `EspressoID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Milk`
--
ALTER TABLE `Milk`
  MODIFY `MilkID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `Syrups`
--
ALTER TABLE `Syrups`
  MODIFY `SyrupID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
