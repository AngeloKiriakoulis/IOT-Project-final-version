Οδηγίες Εγκατάστασης Edge-Level για το Project Ομάδας 3:"BLE-based Indoor asset and people tracking"

1. Εγκατάσταση λογισμικού Linux σε host ή virtual machine. Για το demo έγινε χρήση του Ubuntu OS, εγκατεστημένο στο VMWare Workstation 17 Player.
2. Εγκατάσταση Python Version 3.x, όπως περιγράφεται στο site https://opensource.com/article/20/4/install-python-linux. Εμείς έπρεπε να συμπεριλάβουμε το dependency python3-docutils.
3. Εγκατάσταση Bluez 5.x, σύμφωνα με τις οδηγίες στο site https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation.
4. Εγκατάσταση βιβλιοθηκών bluepy, requests, json μέσω της pip3.
5. Σύνδεση του BLE Controller (SmartBond™ DA14695 Bluetooth Low Energy 5.2 Main-Board) σε ένα USB-port της συσκευής (Αν γίνεται χρήση virtual machine, επιλογή για connect στο virtual machine και όχι στον host). Έπειτα χρήση της εντολής "hciattach -s 115200 /dev/ttyUSB0 any" για το setup.

Για το ble-mesh Demo:
6. Ενεργοποίηση των asset-beacons(SmartBond™ DA14695 Bluetooth Low Energy 5.2 Daughter-Board) από το built-in διακόπτη
7. Run το ble_mesh.py αρχείο. Ίσως κάποια asset-beacons χρειάζονται πάτημα reset, για data advertisement μετά από κάποιο διάστημα.

Για το WiRa Demo:
6. Εισαγωγή του SmartBond™ Wireless Ranging (WiRa™) σε ένα USB-port. Το configuration έγινε με τη χρήση του SmartSnippetsToolBox, υπό την εποπτεία ομάδας από τη ®Renesas. Για την εμφάνιση δεδομένων σειριακής εισόδου από το WiRa™ έγινε χρήση του λογισμικού Tera Term.
7. Run το wira.py αρχείο.

Για την πρόσβαση στο UI κομμάτι της εφαρμογής απαιτείται πρόσβαση στην πλατφόρμα της YODIWO.