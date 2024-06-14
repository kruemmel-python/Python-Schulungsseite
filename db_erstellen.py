import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('quiz.db')
c = conn.cursor()

# Tabelle für Fragen erstellen
c.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL
)
''')

# Tabelle für Antworten erstellen
c.execute('''
CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER,
    answer TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    explanation TEXT,
    FOREIGN KEY (question_id) REFERENCES questions (id)
)
''')

# Liste von Fragen, Antworten und Erklärungen
questions = [
    ("Was ist die richtige Syntax, um eine Variable in Python zu erstellen?", 
        [("let x = 5", False, "Python verwendet das Schlüsselwort 'let' nicht zur Variablendeklaration."),
         ("x = 5", True, "Dies ist die korrekte Syntax, um eine Variable in Python zu erstellen."),
         ("int x = 5", False, "Python benötigt keine explizite Typangabe."),
         ("var x = 5", False, "Python verwendet das Schlüsselwort 'var' nicht zur Variablendeklaration.")]),
    ("Welche der folgenden Aussagen sind wahr über Listen in Python?", 
        [("Listen sind unveränderlich.", False, "Listen sind veränderlich, was bedeutet, dass ihre Elemente geändert werden können."),
         ("Listen sind veränderlich.", True, "Richtig, Listen in Python können geändert werden."),
         ("Listen können Elemente verschiedener Typen enthalten.", True, "Ja, Listen können Elemente beliebiger Typen enthalten."),
         ("Listen können nicht verschachtelt werden.", False, "Listen können Listen als Elemente enthalten.")]),
    ("Wie erstellt man eine Funktion in Python?", 
        [("def my_function():", True, "Dies ist die korrekte Syntax, um eine Funktion in Python zu erstellen."),
         ("function my_function() {}", False, "Dies ist keine gültige Python-Syntax."),
         ("create my_function():", False, "Dies ist keine gültige Python-Syntax."),
         ("function: my_function", False, "Dies ist keine gültige Python-Syntax.")]),
    ("Wie öffnet man eine Datei zum Lesen in Python?", 
        [("open('file.txt', 'r')", True, "Dies ist die korrekte Syntax, um eine Datei im Lesemodus zu öffnen."),
         ("open('file.txt', 'read')", False, "'read' ist kein gültiger Modus."),
         ("open('file.txt', 'w')", False, "'w' öffnet die Datei im Schreibmodus."),
         ("open('file.txt')", False, "Es wird ein Modus benötigt, z.B. 'r' für Lesen.")]),
    ("Was ist die Ausgabe von print(2 ** 3)?", 
        [("8", True, "2 hoch 3 ist 8."),
         ("6", False, "Das ist nicht korrekt. 2 hoch 3 ist 8."),
         ("9", False, "Das ist nicht korrekt. 2 hoch 3 ist 8."),
         ("12", False, "Das ist nicht korrekt. 2 hoch 3 ist 8.")]),
    ("Wie kommentiert man eine einzelne Zeile in Python?", 
        [("# Kommentar", True, "Dies ist die korrekte Syntax, um einen Kommentar in Python zu erstellen."),
         ("// Kommentar", False, "Dies ist die Syntax für Kommentare in C++ und Java, nicht in Python."),
         ("/* Kommentar */", False, "Dies ist die Syntax für Kommentare in C und Java, nicht in Python."),
         ("-- Kommentar", False, "Dies ist die Syntax für Kommentare in SQL, nicht in Python.")]),
    ("Was ist die richtige Syntax, um ein Modul in Python zu importieren?", 
        [("import modulename", True, "Dies ist die korrekte Syntax, um ein Modul in Python zu importieren."),
         ("import modulename()", False, "Dies ist keine gültige Syntax zum Importieren eines Moduls."),
         ("#include <modulename>", False, "Dies ist die Syntax für C/C++ und nicht für Python."),
         ("using modulename", False, "Dies ist keine gültige Syntax zum Importieren eines Moduls in Python.")]),
    ("Wie erstellt man ein Dictionary in Python?", 
        [("my_dict = {'key': 'value'}", True, "Dies ist die korrekte Syntax, um ein Dictionary in Python zu erstellen."),
         ("my_dict = ['key': 'value']", False, "Dies ist die Syntax für eine Liste, nicht für ein Dictionary."),
         ("my_dict = ('key', 'value')", False, "Dies ist die Syntax für ein Tupel, nicht für ein Dictionary."),
         ("my_dict = {'key', 'value'}", False, "Dies ist eine fehlerhafte Syntax für ein Dictionary.")]),
    ("Wie entfernt man ein Element aus einer Liste in Python?", 
        [("my_list.remove(element)", True, "Dies ist die korrekte Methode, um ein Element aus einer Liste zu entfernen."),
         ("my_list.delete(element)", False, "Dies ist keine gültige Methode zum Entfernen eines Elements aus einer Liste."),
         ("my_list.del(element)", False, "Dies ist keine gültige Methode zum Entfernen eines Elements aus einer Liste."),
         ("my_list.pop(element)", False, "pop() entfernt ein Element an einem bestimmten Index oder das letzte Element, nicht ein bestimmtes Element.")]),
    ("Wie kann man den Typ einer Variable in Python überprüfen?", 
        [("type(variable)", True, "Dies ist die korrekte Methode, um den Typ einer Variable in Python zu überprüfen."),
         ("typeof(variable)", False, "typeof() ist in Python nicht definiert, es wird in anderen Sprachen wie JavaScript verwendet."),
         ("getType(variable)", False, "getType() ist in Python nicht definiert."),
         ("varType(variable)", False, "varType() ist in Python nicht definiert.")]),
    ("Welche Methode wird verwendet, um eine Liste in Python zu sortieren?", 
        [("my_list.sort()", True, "Dies ist die korrekte Methode, um eine Liste in Python zu sortieren."),
         ("my_list.order()", False, "order() ist in Python nicht definiert."),
         ("sort(my_list)", False, "sort() ist eine Methode der Listenobjekte und muss auf einem Listenobjekt aufgerufen werden."),
         ("order(my_list)", False, "order() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print('Hello' + ' ' + 'World')?", 
        [("Hello World", True, "Dies ist die korrekte Ausgabe."),
         ("HelloWorld", False, "Ein Leerzeichen ist erforderlich, um die Wörter zu trennen."),
         ("Hello + World", False, "Die Zeichenfolge '+' wird nicht als Operator interpretiert."),
         ("Hello World!", False, "Ein zusätzliches Ausrufezeichen wurde hinzugefügt.")]),
    ("Wie erstellt man ein Set in Python?", 
        [("my_set = {1, 2, 3}", True, "Dies ist die korrekte Syntax, um ein Set in Python zu erstellen."),
         ("my_set = [1, 2, 3]", False, "Dies ist die Syntax für eine Liste, nicht für ein Set."),
         ("my_set = (1, 2, 3)", False, "Dies ist die Syntax für ein Tupel, nicht für ein Set."),
         ("my_set = <1, 2, 3>", False, "Dies ist keine gültige Syntax in Python.")]),
    ("Welche der folgenden Methoden gibt die Anzahl der Elemente in einer Liste zurück?", 
        [("len(my_list)", True, "len() ist die korrekte Methode, um die Anzahl der Elemente in einer Liste zu ermitteln."),
         ("count(my_list)", False, "count() ist eine Methode der Listenobjekte und gibt die Anzahl der Vorkommen eines Elements in der Liste zurück."),
         ("size(my_list)", False, "size() ist in Python nicht definiert."),
         ("length(my_list)", False, "length() ist in Python nicht definiert.")]),
    ("Was ist ein Tuple in Python?", 
        [("Eine unveränderliche Liste", True, "Ein Tuple ist eine unveränderliche Liste."),
         ("Eine veränderliche Liste", False, "Listen sind veränderlich, aber Tupel sind unveränderlich."),
         ("Ein Dictionary", False, "Ein Dictionary ist eine Sammlung von Schlüssel-Wert-Paaren."),
         ("Ein Set", False, "Ein Set ist eine ungeordnete Sammlung von eindeutigen Elementen.")]),
    ("Welche der folgenden Funktionen konvertiert einen String zu einem Integer?", 
        [("int('123')", True, "int() konvertiert einen String in einen Integer."),
         ("str('123')", False, "str() konvertiert Daten in einen String."),
         ("float('123')", False, "float() konvertiert einen String in eine Fließkommazahl."),
         ("convert('123')", False, "convert() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(bool(0))?", 
        [("False", True, "0 wird in ein Boolesches False konvertiert."),
         ("True", False, "Nur Nicht-Null-Werte werden in ein Boolesches True konvertiert."),
         ("0", False, "bool(0) gibt False zurück."),
         ("None", False, "bool(0) gibt False zurück.")]),
    ("Wie iteriert man über eine Liste in Python?", 
        [("for element in my_list:", True, "Dies ist die korrekte Methode, um über eine Liste zu iterieren."),
         ("foreach element in my_list:", False, "foreach ist in Python nicht definiert."),
         ("loop element in my_list:", False, "loop ist in Python nicht definiert."),
         ("iterate element in my_list:", False, "iterate ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(10 // 3)?", 
        [("3", True, "10 // 3 gibt den ganzzahligen Quotienten zurück."),
         ("3.3333", False, "// ist der Ganzzahloperator, nicht der Fließkommaoperator."),
         ("4", False, "Das Ergebnis ist kleiner als 4."),
         ("3.0", False, "Das Ergebnis ist eine Ganzzahl, nicht eine Fließkommazahl.")]),
    ("Welche der folgenden Funktionen generiert eine Zufallszahl?", 
        [("random.randint(1, 10)", True, "random.randint() generiert eine Zufallszahl im angegebenen Bereich."),
         ("rand(1, 10)", False, "rand() ist in Python nicht definiert."),
         ("randomize(1, 10)", False, "randomize() ist in Python nicht definiert."),
         ("random(1, 10)", False, "random() ist eine Funktion im random-Modul, aber nicht mit diesen Parametern.")]),
    ("Wie öffnet man eine Datei zum Schreiben in Python?", 
        [("open('file.txt', 'w')", True, "Dies ist die korrekte Syntax, um eine Datei im Schreibmodus zu öffnen."),
         ("open('file.txt', 'r')", False, "'r' öffnet die Datei im Lesemodus."),
         ("open('file.txt', 'read')", False, "'read' ist kein gültiger Modus."),
         ("open('file.txt', 'write')", False, "'write' ist kein gültiger Modus, 'w' ist korrekt.")]),
    ("Was ist die Ausgabe von print('Python'[0])?", 
        [("P", True, "Der Index 0 gibt das erste Zeichen des Strings zurück."),
         ("y", False, "Der Index 1 gibt das zweite Zeichen zurück."),
         ("n", False, "Der Index 2 gibt das dritte Zeichen zurück."),
         ("o", False, "Der Index 4 gibt das fünfte Zeichen zurück.")]),
    ("Welche der folgenden Funktionen konvertiert einen String zu einem Float?", 
        [("float('123.45')", True, "float() konvertiert einen String in eine Fließkommazahl."),
         ("int('123.45')", False, "int() konvertiert einen String in einen Integer, aber nur, wenn der String keine Dezimalstellen hat."),
         ("str('123.45')", False, "str() konvertiert Daten in einen String."),
         ("convert('123.45')", False, "convert() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(len('Python'))?", 
        [("6", True, "len() gibt die Länge des Strings zurück."),
         ("5", False, "Die Länge des Strings 'Python' ist 6."),
         ("7", False, "Die Länge des Strings 'Python' ist 6."),
         ("8", False, "Die Länge des Strings 'Python' ist 6.")]),
    ("Wie kommentiert man einen Block von Zeilen in Python?", 
        [("''' Kommentar '''", True, "Dreifach-Einzel- oder Doppelzitate können verwendet werden, um mehrzeilige Kommentare zu erstellen."),
         ("// Kommentar", False, "Dies ist die Syntax für einzeilige Kommentare in C++ und Java, nicht für mehrzeilige Kommentare in Python."),
         ("/* Kommentar */", False, "Dies ist die Syntax für mehrzeilige Kommentare in C und Java."),
         ("-- Kommentar", False, "Dies ist die Syntax für einzeilige Kommentare in SQL.")]),
    ("Was ist die Ausgabe von print('Python'.lower())?", 
        [("python", True, "Die Methode lower() gibt den String in Kleinbuchstaben zurück."),
         ("PYTHON", False, "Die Methode upper() gibt den String in Großbuchstaben zurück."),
         ("Python", False, "Der ursprüngliche String wird nicht verändert."),
         ("pYTHON", False, "Die Methode lower() gibt den String in Kleinbuchstaben zurück.")]),
    ("Wie erstellt man eine leere Liste in Python?", 
        [("my_list = []", True, "Dies ist die korrekte Syntax, um eine leere Liste zu erstellen."),
         ("my_list = {}", False, "Dies ist die Syntax für ein leeres Dictionary."),
         ("my_list = ()", False, "Dies ist die Syntax für ein leeres Tupel."),
         ("my_list = set()", False, "Dies ist die Syntax für ein leeres Set.")]),
    ("Welche Methode fügt ein Element an das Ende einer Liste an?", 
        [("my_list.append(element)", True, "append() fügt ein Element an das Ende der Liste an."),
         ("my_list.add(element)", False, "add() ist in Python nicht definiert."),
         ("my_list.insert(element)", False, "insert() fügt ein Element an einem bestimmten Index ein."),
         ("my_list.extend(element)", False, "extend() fügt mehrere Elemente an das Ende der Liste an.")]),
    ("Was ist die Ausgabe von print('Python'.find('y'))?", 
        [("1", True, "Der Index von 'y' im String 'Python' ist 1."),
         ("0", False, "Der Index 0 gibt das erste Zeichen zurück."),
         ("2", False, "Der Index 2 gibt das dritte Zeichen zurück."),
         ("3", False, "Der Index 3 gibt das vierte Zeichen zurück.")]),
    ("Wie erstellt man eine leere Menge (Set) in Python?", 
        [("my_set = set()", True, "Dies ist die korrekte Syntax, um eine leere Menge zu erstellen."),
         ("my_set = {}", False, "Dies ist die Syntax für ein leeres Dictionary."),
         ("my_set = []", False, "Dies ist die Syntax für eine leere Liste."),
         ("my_set = ()", False, "Dies ist die Syntax für ein leeres Tupel.")]),
    ("Welche der folgenden Funktionen rundet eine Zahl auf die nächste Ganzzahl ab?", 
        [("round(3.7)", True, "round() rundet die Zahl auf die nächste Ganzzahl ab."),
         ("ceil(3.7)", False, "ceil() rundet die Zahl auf die nächste Ganzzahl auf."),
         ("floor(3.7)", False, "floor() rundet die Zahl auf die nächste Ganzzahl ab."),
         ("truncate(3.7)", False, "truncate() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print('Python'.upper())?", 
        [("PYTHON", True, "Die Methode upper() gibt den String in Großbuchstaben zurück."),
         ("python", False, "Die Methode lower() gibt den String in Kleinbuchstaben zurück."),
         ("Python", False, "Der ursprüngliche String wird nicht verändert."),
         ("PytHon", False, "Die Methode upper() gibt den String in Großbuchstaben zurück.")]),
    ("Wie erstellt man eine leere Dictionary in Python?", 
        [("my_dict = {}", True, "Dies ist die korrekte Syntax, um ein leeres Dictionary zu erstellen."),
         ("my_dict = []", False, "Dies ist die Syntax für eine leere Liste."),
         ("my_dict = ()", False, "Dies ist die Syntax für ein leeres Tupel."),
         ("my_dict = set()", False, "Dies ist die Syntax für ein leeres Set.")]),
    ("Welche Methode gibt die Anzahl der Elemente in einer Menge zurück?", 
        [("len(my_set)", True, "len() gibt die Anzahl der Elemente in der Menge zurück."),
         ("count(my_set)", False, "count() ist in Python nicht definiert."),
         ("size(my_set)", False, "size() ist in Python nicht definiert."),
         ("length(my_set)", False, "length() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(2 + 3 * 4)?", 
        [("14", True, "Die Multiplikation wird vor der Addition durchgeführt."),
         ("20", False, "Die Multiplikation hat Vorrang vor der Addition."),
         ("24", False, "Die Multiplikation hat Vorrang vor der Addition."),
         ("10", False, "Die Multiplikation hat Vorrang vor der Addition.")]),
    ("Wie erstellt man eine neue Klasse in Python?", 
        [("class MyClass:", True, "Dies ist die korrekte Syntax, um eine Klasse in Python zu erstellen."),
         ("new class MyClass:", False, "Dies ist keine gültige Syntax in Python."),
         ("class: MyClass", False, "Dies ist keine gültige Syntax in Python."),
         ("create class MyClass:", False, "Dies ist keine gültige Syntax in Python.")]),
    ("Welche Methode wird verwendet, um ein Element aus einer Menge zu entfernen?", 
        [("my_set.remove(element)", True, "remove() entfernt ein Element aus der Menge."),
         ("my_set.delete(element)", False, "delete() ist in Python nicht definiert."),
         ("my_set.pop(element)", False, "pop() entfernt und gibt ein zufälliges Element aus der Menge zurück."),
         ("my_set.del(element)", False, "del() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(10 % 3)?", 
        [("1", True, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("3", False, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("0", False, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("2", False, "Der Modulo-Operator gibt den Rest der Division zurück.")]),
    ("Wie erstellt man eine Instanz einer Klasse in Python?", 
        [("obj = MyClass()", True, "Dies ist die korrekte Syntax, um eine Instanz einer Klasse zu erstellen."),
         ("obj = new MyClass()", False, "Dies ist keine gültige Syntax in Python."),
         ("obj = MyClass", False, "Dies ist keine gültige Syntax in Python."),
         ("obj = create MyClass()", False, "Dies ist keine gültige Syntax in Python.")]),
    ("Welche Methode wird verwendet, um ein Element an einem bestimmten Index in einer Liste einzufügen?", 
        [("my_list.insert(index, element)", True, "insert() fügt ein Element an einem bestimmten Index ein."),
         ("my_list.add(index, element)", False, "add() ist in Python nicht definiert."),
         ("my_list.append(index, element)", False, "append() fügt ein Element an das Ende der Liste an."),
         ("my_list.extend(index, element)", False, "extend() fügt mehrere Elemente an das Ende der Liste an.")]),
    ("Was ist die Ausgabe von print(3 ** 2)?", 
        [("9", True, "3 hoch 2 ist 9."),
         ("6", False, "Das ist nicht korrekt. 3 hoch 2 ist 9."),
         ("12", False, "Das ist nicht korrekt. 3 hoch 2 ist 9."),
         ("8", False, "Das ist nicht korrekt. 3 hoch 2 ist 9.")]),
    ("Wie kann man in Python eine Ausnahme abfangen?", 
        [("try: ... except:", True, "Dies ist die korrekte Syntax, um eine Ausnahme abzufangen."),
         ("try: ... catch:", False, "catch wird in Python nicht verwendet."),
         ("try: ... error:", False, "error wird in Python nicht verwendet."),
         ("try: ... rescue:", False, "rescue wird in Python nicht verwendet.")]),
    ("Welche Methode wird verwendet, um alle Elemente einer Liste zu entfernen?", 
        [("my_list.clear()", True, "clear() entfernt alle Elemente aus der Liste."),
         ("my_list.delete_all()", False, "delete_all() ist in Python nicht definiert."),
         ("my_list.remove_all()", False, "remove_all() ist in Python nicht definiert."),
         ("my_list.empty()", False, "empty() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(4 // 2)?", 
        [("2", True, "Der Operator // gibt den ganzzahligen Quotienten zurück."),
         ("2.0", False, "Der Operator // gibt den ganzzahligen Quotienten zurück."),
         ("4", False, "Der Operator // gibt den ganzzahligen Quotienten zurück."),
         ("1", False, "Der Operator // gibt den ganzzahligen Quotienten zurück.")]),
    ("Wie kann man eine Datei zum Anhängen in Python öffnen?", 
        [("open('file.txt', 'a')", True, "'a' öffnet die Datei im Anhangmodus."),
         ("open('file.txt', 'w')", False, "'w' öffnet die Datei im Schreibmodus."),
         ("open('file.txt', 'r')", False, "'r' öffnet die Datei im Lesemodus."),
         ("open('file.txt', 'append')", False, "'append' ist kein gültiger Modus.")]),
    ("Was ist die Ausgabe von print('Hello' * 3)?", 
        [("HelloHelloHello", True, "Der Operator * wiederholt die Zeichenkette."),
         ("Hello3", False, "Der Operator * wiederholt die Zeichenkette."),
         ("Hello, Hello, Hello", False, "Der Operator * wiederholt die Zeichenkette ohne Kommas."),
         ("Hello * 3", False, "Der Operator * wiederholt die Zeichenkette.")]),
    ("Welche Methode wird verwendet, um einen Schlüssel aus einem Dictionary zu entfernen?", 
        [("my_dict.pop(key)", True, "pop() entfernt einen Schlüssel aus dem Dictionary und gibt dessen Wert zurück."),
         ("my_dict.remove(key)", False, "remove() ist in Python nicht definiert."),
         ("my_dict.delete(key)", False, "delete() ist in Python nicht definiert."),
         ("my_dict.clear(key)", False, "clear() entfernt alle Schlüssel-Wert-Paare aus dem Dictionary.")]),
    ("Was ist die Ausgabe von print(5 / 2)?", 
        [("2.5", True, "Der Operator / gibt den Fließkommaquotienten zurück."),
         ("2", False, "Der Operator / gibt den Fließkommaquotienten zurück."),
         ("3", False, "Der Operator / gibt den Fließkommaquotienten zurück."),
         ("2.0", False, "Der Operator / gibt den Fließkommaquotienten zurück.")]),
    ("Wie kann man in Python eine Liste kopieren?", 
        [("my_list.copy()", True, "copy() erstellt eine flache Kopie der Liste."),
         ("my_list.clone()", False, "clone() ist in Python nicht definiert."),
         ("my_list.duplicate()", False, "duplicate() ist in Python nicht definiert."),
         ("my_list.copy_all()", False, "copy_all() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(10 - 4)?", 
        [("6", True, "10 - 4 ergibt 6."),
         ("7", False, "Das ist nicht korrekt. 10 - 4 ergibt 6."),
         ("5", False, "Das ist nicht korrekt. 10 - 4 ergibt 6."),
         ("4", False, "Das ist nicht korrekt. 10 - 4 ergibt 6.")]),
    ("Wie kann man eine Zahl in einen String konvertieren?", 
        [("str(123)", True, "str() konvertiert eine Zahl in einen String."),
         ("string(123)", False, "string() ist in Python nicht definiert."),
         ("int_to_str(123)", False, "int_to_str() ist in Python nicht definiert."),
         ("convert_to_string(123)", False, "convert_to_string() ist in Python nicht definiert.")]),
    ("Welche Methode wird verwendet, um ein Element an einem bestimmten Index in einer Liste zu ändern?", 
        [("my_list[index] = element", True, "Dies ist die korrekte Syntax, um ein Element an einem bestimmten Index zu ändern."),
         ("my_list.modify(index, element)", False, "modify() ist in Python nicht definiert."),
         ("my_list.update(index, element)", False, "update() ist in Python nicht definiert."),
         ("my_list.change(index, element)", False, "change() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(3 + 5)?", 
        [("8", True, "3 + 5 ergibt 8."),
         ("9", False, "Das ist nicht korrekt. 3 + 5 ergibt 8."),
         ("7", False, "Das ist nicht korrekt. 3 + 5 ergibt 8."),
         ("10", False, "Das ist nicht korrekt. 3 + 5 ergibt 8.")]),
    ("Wie kann man den letzten Wert aus einer Liste entfernen und zurückgeben?", 
        [("my_list.pop()", True, "pop() entfernt und gibt den letzten Wert der Liste zurück."),
         ("my_list.remove_last()", False, "remove_last() ist in Python nicht definiert."),
         ("my_list.delete_last()", False, "delete_last() ist in Python nicht definiert."),
         ("my_list.pull()", False, "pull() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(7 % 2)?", 
        [("1", True, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("2", False, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("3", False, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("0", False, "Der Modulo-Operator gibt den Rest der Division zurück.")]),
    ("Wie kann man den Index eines Elements in einer Liste finden?", 
        [("my_list.index(element)", True, "index() gibt den Index eines Elements in der Liste zurück."),
         ("my_list.find(element)", False, "find() ist in Python nicht definiert."),
         ("my_list.search(element)", False, "search() ist in Python nicht definiert."),
         ("my_list.locate(element)", False, "locate() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(2 * 3)?", 
        [("6", True, "2 * 3 ergibt 6."),
         ("5", False, "Das ist nicht korrekt. 2 * 3 ergibt 6."),
         ("7", False, "Das ist nicht korrekt. 2 * 3 ergibt 6."),
         ("8", False, "Das ist nicht korrekt. 2 * 3 ergibt 6.")]),
    ("Wie kann man alle Elemente einer Liste in umgekehrter Reihenfolge sortieren?", 
        [("my_list.reverse()", True, "reverse() sortiert die Liste in umgekehrter Reihenfolge."),
         ("my_list.sort_reverse()", False, "sort_reverse() ist in Python nicht definiert."),
         ("my_list.order_reverse()", False, "order_reverse() ist in Python nicht definiert."),
         ("my_list.revert()", False, "revert() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(9 / 3)?", 
        [("3.0", True, "Der Operator / gibt den Fließkommaquotienten zurück."),
         ("3", False, "Der Operator / gibt den Fließkommaquotienten zurück."),
         ("2", False, "Der Operator / gibt den Fließkommaquotienten zurück."),
         ("4", False, "Der Operator / gibt den Fließkommaquotienten zurück.")]),
    ("Wie kann man in Python eine Liste zusammenfügen?", 
        [("list1.extend(list2)", True, "extend() fügt alle Elemente von list2 an list1 an."),
         ("list1.append(list2)", False, "append() fügt list2 als einzelnes Element an list1 an."),
         ("list1.add(list2)", False, "add() ist in Python nicht definiert."),
         ("list1.concat(list2)", False, "concat() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(4 + 4)?", 
        [("8", True, "4 + 4 ergibt 8."),
         ("7", False, "Das ist nicht korrekt. 4 + 4 ergibt 8."),
         ("9", False, "Das ist nicht korrekt. 4 + 4 ergibt 8."),
         ("10", False, "Das ist nicht korrekt. 4 + 4 ergibt 8.")]),
    ("Wie kann man eine Liste in Python sortieren?", 
        [("my_list.sort()", True, "sort() sortiert die Liste in aufsteigender Reihenfolge."),
         ("my_list.order()", False, "order() ist in Python nicht definiert."),
         ("sort(my_list)", False, "sort() ist eine Methode der Listenobjekte und muss auf einem Listenobjekt aufgerufen werden."),
         ("order(my_list)", False, "order() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(5 * 5)?", 
        [("25", True, "5 * 5 ergibt 25."),
         ("20", False, "Das ist nicht korrekt. 5 * 5 ergibt 25."),
         ("30", False, "Das ist nicht korrekt. 5 * 5 ergibt 25."),
         ("15", False, "Das ist nicht korrekt. 5 * 5 ergibt 25.")]),
    ("Wie kann man in Python einen Schlüssel-Wert-Paar in ein Dictionary einfügen?", 
        [("my_dict[key] = value", True, "Dies ist die korrekte Syntax, um ein Schlüssel-Wert-Paar in ein Dictionary einzufügen."),
         ("my_dict.add(key, value)", False, "add() ist in Python nicht definiert."),
         ("my_dict.insert(key, value)", False, "insert() ist in Python nicht definiert."),
         ("my_dict.put(key, value)", False, "put() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(10 - 2)?", 
        [("8", True, "10 - 2 ergibt 8."),
         ("7", False, "Das ist nicht korrekt. 10 - 2 ergibt 8."),
         ("9", False, "Das ist nicht korrekt. 10 - 2 ergibt 8."),
         ("6", False, "Das ist nicht korrekt. 10 - 2 ergibt 8.")]),
    ("Wie kann man in Python den Wert eines Schlüssels in einem Dictionary aktualisieren?", 
        [("my_dict[key] = new_value", True, "Dies ist die korrekte Syntax, um den Wert eines Schlüssels in einem Dictionary zu aktualisieren."),
         ("my_dict.update(key, new_value)", False, "update() ist eine Methode, die ein Dictionary mit einem anderen aktualisiert."),
         ("my_dict.modify(key, new_value)", False, "modify() ist in Python nicht definiert."),
         ("my_dict.change(key, new_value)", False, "change() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(6 / 2)?", 
        [("3.0", True, "Der Operator / gibt den Fließkommaquotienten zurück."),
         ("3", False, "Der Operator / gibt den Fließkommaquotienten zurück."),
         ("2", False, "Der Operator / gibt den Fließkommaquotienten zurück."),
         ("4", False, "Der Operator / gibt den Fließkommaquotienten zurück.")]),
    ("Wie kann man in Python alle Schlüssel eines Dictionaries erhalten?", 
        [("my_dict.keys()", True, "keys() gibt eine Ansicht der Schlüssel im Dictionary zurück."),
         ("my_dict.get_keys()", False, "get_keys() ist in Python nicht definiert."),
         ("my_dict.all_keys()", False, "all_keys() ist in Python nicht definiert."),
         ("my_dict.key_list()", False, "key_list() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(4 * 4)?", 
        [("16", True, "4 * 4 ergibt 16."),
         ("12", False, "Das ist nicht korrekt. 4 * 4 ergibt 16."),
         ("14", False, "Das ist nicht korrekt. 4 * 4 ergibt 16."),
         ("18", False, "Das ist nicht korrekt. 4 * 4 ergibt 16.")]),
    ("Wie kann man in Python alle Werte eines Dictionaries erhalten?", 
        [("my_dict.values()", True, "values() gibt eine Ansicht der Werte im Dictionary zurück."),
         ("my_dict.get_values()", False, "get_values() ist in Python nicht definiert."),
         ("my_dict.all_values()", False, "all_values() ist in Python nicht definiert."),
         ("my_dict.value_list()", False, "value_list() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(12 // 5)?", 
        [("2", True, "Der Operator // gibt den ganzzahligen Quotienten zurück."),
         ("2.4", False, "Der Operator // gibt den ganzzahligen Quotienten zurück."),
         ("3", False, "Der Operator // gibt den ganzzahligen Quotienten zurück."),
         ("4", False, "Der Operator // gibt den ganzzahligen Quotienten zurück.")]),
    ("Wie kann man in Python ein Element zu einem Set hinzufügen?", 
        [("my_set.add(element)", True, "add() fügt ein Element zum Set hinzu."),
         ("my_set.insert(element)", False, "insert() ist in Python nicht definiert."),
         ("my_set.push(element)", False, "push() ist in Python nicht definiert."),
         ("my_set.append(element)", False, "append() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(7 + 2)?", 
        [("9", True, "7 + 2 ergibt 9."),
         ("8", False, "Das ist nicht korrekt. 7 + 2 ergibt 9."),
         ("10", False, "Das ist nicht korrekt. 7 + 2 ergibt 9."),
         ("11", False, "Das ist nicht korrekt. 7 + 2 ergibt 9.")]),
    ("Wie kann man in Python ein Element aus einem Set entfernen?", 
        [("my_set.remove(element)", True, "remove() entfernt ein Element aus dem Set."),
         ("my_set.delete(element)", False, "delete() ist in Python nicht definiert."),
         ("my_set.pop(element)", False, "pop() entfernt und gibt ein zufälliges Element aus dem Set zurück."),
         ("my_set.erase(element)", False, "erase() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(8 % 3)?", 
        [("2", True, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("1", False, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("0", False, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("3", False, "Der Modulo-Operator gibt den Rest der Division zurück.")]),
    ("Wie kann man in Python überprüfen, ob ein Set ein bestimmtes Element enthält?", 
        [("element in my_set", True, "Dies ist die korrekte Syntax, um zu überprüfen, ob ein Set ein bestimmtes Element enthält."),
         ("element.contains(my_set)", False, "contains() ist in Python nicht definiert."),
         ("element in_set(my_set)", False, "in_set() ist in Python nicht definiert."),
         ("element.has(my_set)", False, "has() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(5 // 2)?", 
        [("2", True, "Der Operator // gibt den ganzzahligen Quotienten zurück."),
         ("2.5", False, "Der Operator // gibt den ganzzahligen Quotienten zurück."),
         ("3", False, "Der Operator // gibt den ganzzahligen Quotienten zurück."),
         ("1", False, "Der Operator // gibt den ganzzahligen Quotienten zurück.")]),
    ("Wie kann man in Python zwei Sets vereinigen?", 
        [("set1.union(set2)", True, "union() vereinigt zwei Sets."),
         ("set1.add(set2)", False, "add() ist in Python nicht definiert."),
         ("set1.combine(set2)", False, "combine() ist in Python nicht definiert."),
         ("set1.merge(set2)", False, "merge() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(9 - 3)?", 
        [("6", True, "9 - 3 ergibt 6."),
         ("7", False, "Das ist nicht korrekt. 9 - 3 ergibt 6."),
         ("8", False, "Das ist nicht korrekt. 9 - 3 ergibt 6."),
         ("5", False, "Das ist nicht korrekt. 9 - 3 ergibt 6.")]),
    ("Wie kann man in Python den Durchschnitt einer Liste berechnen?", 
        [("sum(my_list) / len(my_list)", True, "Dies ist die korrekte Methode, um den Durchschnitt einer Liste zu berechnen."),
         ("avg(my_list)", False, "avg() ist in Python nicht definiert."),
         ("mean(my_list)", False, "mean() ist in Python nicht definiert."),
         ("average(my_list)", False, "average() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(15 % 4)?", 
        [("3", True, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("2", False, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("4", False, "Der Modulo-Operator gibt den Rest der Division zurück."),
         ("1", False, "Der Modulo-Operator gibt den Rest der Division zurück.")]),
    ("Wie kann man in Python eine Datei schließen?", 
        [("file.close()", True, "close() schließt die Datei."),
         ("file.end()", False, "end() ist in Python nicht definiert."),
         ("file.stop()", False, "stop() ist in Python nicht definiert."),
         ("file.terminate()", False, "terminate() ist in Python nicht definiert.")]),
    ("Was ist die Ausgabe von print(2 ** 4)?", 
        [("16", True, "2 hoch 4 ist 16."),
         ("8", False, "Das ist nicht korrekt. 2 hoch 4 ist 16."),
         ("12", False, "Das ist nicht korrekt. 2 hoch 4 ist 16."),
         ("14", False, "Das ist nicht korrekt. 2 hoch 4 ist 16.")]),
    ("Wie kann man in Python den Inhalt einer Datei lesen?", 
        [("file.read()", True, "read() liest den gesamten Inhalt der Datei."),
         ("file.read_all()", False, "read_all() ist in Python nicht definiert."),
         ("file.get_content()", False, "get_content() ist in Python nicht definiert."),
         ("file.fetch()", False, "fetch() ist in Python nicht definiert.")]),
]

# Fragen und Antworten einfügen
for question, answers in questions:
    c.execute("INSERT INTO questions (question) VALUES (?)", (question,))
    question_id = c.lastrowid
    for answer, is_correct, explanation in answers:
        c.execute("INSERT INTO answers (question_id, answer, is_correct, explanation) VALUES (?, ?, ?, ?)", (question_id, answer, is_correct, explanation))

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
