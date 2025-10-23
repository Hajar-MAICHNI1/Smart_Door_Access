🔐 Système de Contrôle d’Accès avec RFID et gRPC
🧠 Description du projet

Ce projet consiste à développer un système intelligent de contrôle d’accès basé sur une ESP32 et un module RFID permettant de sécuriser l’ouverture d’une porte.

L’architecture repose sur une communication gRPC entre les différents composants afin d’assurer des échanges rapides et sécurisés.

⚙️ Composants principaux

ESP32 : microcontrôleur chargé de lire les cartes RFID et de communiquer avec le serveur.

Module RFID : identification des utilisateurs autorisés.

Serveur backend (Python) : gestion de la logique d’authentification et de communication via gRPC.

Application mobile (Flutter) : interface pour administrer les accès, consulter les journaux d’activité et gérer les utilisateurs.

🚀 Fonctionnalités

Lecture des identifiants RFID et vérification d’accès.

Communication en temps réel entre l’ESP32 et le serveur via gRPC.

Gestion des utilisateurs autorisés depuis l’application mobile.

Notification ou journalisation des tentatives d’accès.

🛠️ Technologies utilisées

Matériel : ESP32, module RFID RC522

Backend : Python, gRPC

Frontend mobile : Flutter

Communication : Wi-Fi / gRPC
