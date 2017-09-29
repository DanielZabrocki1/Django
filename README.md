# Django

1. Installiere Django (Die Installation von Phyton3 ist dabei vorausgesetzt)
2. Öffne die Konsole und betrete das ProjektVerzeichnis  "../myproject" 
3. führe folgendes aus: "python manage.py runserver"
4. der Server sollte nun auf dem Port 1:8000 laufen
5. "Starting development server at http://127.0.0.1:8000/" sollte im Terminal stehen.
6. http://127.0.0.1:8000/ im Browser seines Vertrauens aufrufen.
7. Alles andere wird in der Webseite passieren. =)
  
  

# eine kurze Projektbeschreibung
In der Datenbank wird ein recht simples Objekt erzeugt. Person, bestehend aus [Vorname,Zuname,Alter].
Diese werden in der Startseite aufgelistet und verlinken zu einer Info-Seite auf der diese Daten aufgelistet stehen.
Die URL's für jede dieser Personen wird dynamisch erzeugt, sprich man benutzt den Primary-key jeder Person in der URL um die eindeutigkeit  beizubehalten.
Dies wäre auch mit anderen Daten, wie Kombination aus Vor- und Nachname möglich, jedoch werden Zwei gleichnamige Personen auf die selbe Seite verlinkt und das würde ein Problem darstellen.
Weiterhin ist es nun möglich auf der Info-Seite einer Person die einzelnen Attribute zu verändern, bzw das gesamte Objekt zu löschen.
Django übernimmt hierbei die größte Arbeit selbst, man muss nur  die Funktionen"UpdateView" oder "DeleteView" richtig benutzen.
(Richtig benutzen heißt hier: Primary Key für das Objekt bereithalten, bzw für Update eine Umgebung erzeugen in der die Attribute tatsächlich umgeschrieben und bestätigt werden können)
Ebenso ist die Admin-Seite verlinkt (ein Account mit BN und PW wurde bereits bereitgestellt) mit der man ebenfalls die Datenbanken manipulieren kann.
Hier kann man zusätzlich (ich habe keinerlei Rechte entfernt) auch Admin-bezogene Daten ändern, wie zB Rechte hinzufügen/entfernen, Gruppen erstellen und auch User manipulieren (haben in diesem Fall nichts mit den Objekten "Personen" zu tun).
