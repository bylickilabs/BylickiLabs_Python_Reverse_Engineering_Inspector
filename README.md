| [![BPREI](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/workflows/deploy-pages.yml) | [![Windows Build](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/workflows/build.yml/badge.svg)](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/workflows/build.yml) | [![Python 3.10](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/workflows/test-python-310.yml/badge.svg)](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/workflows/test-python-310.yml) | [![Python 3.11](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/workflows/test-python-311.yml/badge.svg)](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/workflows/test-python-311.yml) | [![Python 3.12](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/workflows/test-python-312.yml/badge.svg)](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/workflows/test-python-312.yml) |
|---|---|---|---|---|

![212284100-561aa473-3905-4a80-b561-0d28506553ee](https://github.com/user-attachments/assets/4e210bed-3f4a-47a4-9d13-46eec04c4020)

> [!IMPORTANT]
> **Direct Download - Windows Build**
>
> The current Windows version of the **Python Reverse Engineering Inspector** is available as a GitHub Actions artifact for direct download.
>
> **[Download .exe](https://github.com/bylickilabs/BylickiLabs_Python_Reverse_Engineering_Inspector/actions/runs/31265117105/artifacts/9023941771)**
>
> This build is only available for a limited time.

![212284100-561aa473-3905-4a80-b561-0d28506553ee](https://github.com/user-attachments/assets/4e210bed-3f4a-47a4-9d13-46eec04c4020)

<a id="top"></a>

### BylickiLabs Python Reverse Engineering Inspector

> Business Anwendung für statische Python Codeanalyse, 
  - Reverse Engineering, Abhängigkeitsanalyse, Komplexitätsauswertung, Risikoerkennung und Bytecode Inspektion.
    - Version 1.0.0

---

> Social Media & Contact
  - [LinkedIn](https://www.linkedin.com/in/bylicki/)  
  - [Facebook](https://www.facebook.com/BylickiLabs)

---

| [Deutsch](#deutsch) | [English](#english) |
|---|---|

<br>

---

<br>

<a id="deutsch"></a>

# Deutsch

<a id="de_inhalt"></a>

## Inhaltsverzeichnis

1. [Projektübersicht](#de_uebersicht)
2. [Funktionsumfang](#de_funktionen)
3. [Statische Analyse und Sicherheitsmodell](#de_statisch)
4. [Projekt und Symbolanalyse](#de_symbole)
5. [Abhängigkeitsanalyse](#de_abhaengigkeiten)
6. [Funktionsaufrufe](#de_aufrufe)
7. [Komplexitätsanalyse](#de_komplexitaet)
8. [NumPy und SciPy](#de_numpy_scipy)
9. [Risikoanalyse](#de_risiko)
10. [Bytecode Inspektion](#de_bytecode)
11. [Benutzeroberfläche](#de_ui)
12. [Deutsch und Englisch](#de_sprache)
13. [SQLite Verlauf](#de_sqlite)
14. [Exportformate](#de_export)
15. [Windows Testumgebung](#de_test)
16. [Windows Build](#de_build)
17. [Manuelle Installation](#de_installation)
18. [Projektstruktur](#de_struktur)
19. [Technische Anforderungen](#de_anforderungen)
20. [Analysierte und ausgeschlossene Verzeichnisse](#de_verzeichnisse)
21. [Projektstatus](#de_status)

<br>

---

<br>

<a id="de_uebersicht"></a>

## Projektübersicht

> Der BylickiLabs Python Reverse Engineering Inspector, kurz BPREI, ist eine Desktop Anwendung zur statischen Untersuchung vollständiger Python Projekte.
  - Die Anwendung liest Python Quellcode ein, analysiert die interne Struktur und stellt technische Zusammenhänge in mehreren spezialisierten Bereichen dar. 
    - Dazu gehören Module, Klassen, Funktionen, Methoden, Imports, Abhängigkeiten, direkte Funktionsaufrufe, Komplexitätswerte, statistische Auffälligkeiten, ausgewählte Risikomuster und Python Bytecode.
---
  - Das untersuchte Zielprojekt wird nicht importiert und nicht ausgeführt. 
    - Die Analyse basiert primär auf dem Python Abstract Syntax Tree.
      - Die grafische Oberfläche wird mit PySide6 umgesetzt. 
	  - NumPy und SciPy werden funktional für statistische Codeauswertungen eingesetzt.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_funktionen"></a>

## Funktionsumfang

Aktuell implementiert sind:

🔹 Analyse kompletter Projektverzeichnisse  
🔹 Unterstützung für `.py` und `.pyw`  
🔹 Projekt Explorer  
🔹 Quellcode Anzeige  
🔹 Erkennung von Klassen  
🔹 Erkennung von Funktionen und Methoden  
🔹 Erkennung asynchroner Funktionen und Methoden  
🔹 Parameteranalyse  
🔹 Decorator Analyse  
🔹 Import Analyse  
🔹 Klassifizierung von Abhängigkeiten  
🔹 Analyse direkter Funktionsaufrufe  
🔹 AST basierte Komplexitätsbewertung  
🔹 NumPy Projektmetriken  
🔹 SciPy Z Score Ausreißererkennung  
🔹 Risk Pattern Analyse  
🔹 Bytecode Disassemblierung  
🔹 SQLite Analyseverlauf  
🔹 JSON Export  
🔹 CSV Export  
🔹 HTML Export  
🔹 Markdown Export  
🔹 Deutsche Benutzeroberfläche  
🔹 Englische Benutzeroberfläche  
🔹 Sprachwechsel während der Laufzeit  
🔹 GitHub Button  
🔹 LinkedIn Button  
🔹 Facebook Button  
🔹 ausführlicher Info Dialog  
🔹 Analyse im Hintergrund über QThread  
🔹 Abbruch laufender Analysen

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_statisch"></a>

## Statische Analyse und Sicherheitsmodell

> BPREI führt das analysierte Python Projekt nicht aus.
  - Der Quellcode wird mit `ast.parse()` in einen Abstract Syntax Tree umgewandelt und anschließend strukturell ausgewertet.
  - Dadurch können Projektbestandteile untersucht werden, ohne Module des Zielprojekts mit `import` zu laden.
    - Die Bytecode Ansicht verwendet `compile()` ausschließlich zur Erzeugung von Codeobjekten. Diese Codeobjekte werden anschließend mit dem Python Modul `dis` disassembliert. Eine Ausführung des kompilierten Zielcodes findet innerhalb dieser Funktion nicht statt.
  - Syntaxfehler einzelner Dateien werden in den Analyseinformationen gespeichert, damit nicht automatisch das gesamte Projekt wegen einer einzelnen fehlerhaften Datei verworfen wird.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_symbole"></a>

## Projekt und Symbolanalyse

> Der Projekt Analyzer untersucht jede erkannte Python Datei und erfasst unter anderem:

🔹 relativen Dateipfad  
🔹 absoluten Dateipfad  
🔹 Gesamtzahl der Zeilen  
🔹 Codezeilen  
🔹 Kommentarzeilen  
🔹 Leerzeilen  
🔹 Klassen  
🔹 Funktionen  
🔹 Methoden  
🔹 asynchrone Funktionen  
🔹 asynchrone Methoden  
🔹 Parameter  
🔹 Decorators  
🔹 Startzeile  
🔹 Endzeile  
🔹 übergeordnete Symbole  
🔹 direkte Funktionsaufrufe  
🔹 Komplexitätswert

> Im Projekt Explorer kann eine Datei oder ein Symbol ausgewählt werden. Der zugehörige Quellcode wird angezeigt und bei Symbolen springt die Ansicht direkt zur entsprechenden Codeposition.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_abhaengigkeiten"></a>

## Abhängigkeitsanalyse

> Imports werden automatisch analysiert und in drei Kategorien eingeordnet:

🔹 Standardbibliothek  
🔹 Projektintern  
🔹 Drittanbieter

Für jede erkannte Abhängigkeit speichert BPREI:

🔹 Modulname  
🔹 Kategorie  
🔹 Anzahl der Verwendungen  
🔹 Dateien, in denen die Abhängigkeit vorkommt

> Projektinterne Abhängigkeiten werden anhand der vorhandenen Projektstruktur erkannt.
  - Module der Python Standardbibliothek werden über `sys.stdlib_module_names` klassifiziert.
    - Alle übrigen erkannten Imports werden als Drittanbieter Abhängigkeiten behandelt.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_aufrufe"></a>

## Funktionsaufrufe

> BPREI analysiert direkte Aufrufe innerhalb von Funktionen und Methoden.
  - Für einen Aufruf werden gespeichert:

🔹 aufrufendes Symbol  
🔹 aufgerufenes Ziel  
🔹 Datei  
🔹 Codezeile

> Dadurch kann nachvollzogen werden, welche Funktionen und Methoden innerhalb eines Projekts miteinander verbunden sind.
  - Verschachtelte Funktionsdefinitionen und Klassendefinitionen werden bei der direkten Aufrufanalyse bewusst separat behandelt und nicht automatisch dem äußeren Funktionskörper zugerechnet.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_komplexitaet"></a>

## Komplexitätsanalyse

> BPREI berechnet für Funktionen und Methoden einen AST basierten Komplexitätswert.
  - In die Bewertung fließen unter anderem folgende Strukturen ein:

🔹 `if`  
🔹 `for`  
🔹 `async for`  
🔹 `while`  
🔹 bedingte Ausdrücke  
🔹 `assert`  
🔹 Comprehensions  
🔹 boolesche Verknüpfungen  
🔹 Exception Handler  
🔹 `try` mit `else`  
🔹 `match` Fälle

> [!NOTE]
> Die Anwendung zeigt unter anderem:

🔹 durchschnittliche Komplexität  
🔹 Median  
🔹 95. Perzentil  
🔹 Standardabweichung  
🔹 maximale Komplexität  
🔹 statistisch auffällige Symbole

> Der Wert ist eine projektinterne AST basierte Bewertungsmetrik und wird nicht als vollständiger Ersatz für eine spezialisierte formale Codeanalyse verstanden.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_numpy_scipy"></a>

## NumPy und SciPy

> NumPy und SciPy sind funktionale Bestandteile der Anwendung.

### NumPy

> NumPy wird zur Verarbeitung der Komplexitätswerte und zur Berechnung folgender Kennzahlen eingesetzt:

🔹 Mittelwert mit `numpy.mean()`  
🔹 Median mit `numpy.median()`  
🔹 95. Perzentil mit `numpy.percentile()`  
🔹 Standardabweichung mit `numpy.std()`  
🔹 Maximum mit `numpy.max()`

### SciPy

> SciPy wird für die statistische Ausreißererkennung eingesetzt.

> Mit `scipy.stats.zscore()` werden Z Scores für die Komplexitätswerte der analysierten Funktionen und Methoden berechnet.
  - Ein Symbol wird aktuell als statistische Auffälligkeit aufgenommen, wenn sein Z Score mindestens `2.0` beträgt.
    - Für diese Auswertung müssen mindestens drei analysierbare Funktionen oder Methoden vorhanden sein.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_risiko"></a>

## Risikoanalyse

> Die Risk Pattern Analyse sucht nach ausgewählten Konstruktionen, die bei einer manuellen Codeprüfung besondere Aufmerksamkeit verdienen können.

> [!NOTE]
> Aktuell erkannt werden:

🔹 `eval()`  
🔹 `exec()`  
🔹 `compile()`  
🔹 `os.system()`  
🔹 `pickle.load()`  
🔹 `pickle.loads()`  
🔹 `yaml.load()`  
🔹 `tempfile.mktemp()`  
🔹 Aufrufe über `subprocess`  
🔹 `shell=True` bei Subprocess Aufrufen  
🔹 `verify=False` bei erkannten HTTP Aufrufen  
🔹 möglicherweise fest hinterlegte Secrets

> Bei möglichen fest hinterlegten Secrets werden unter anderem Variablennamen wie diese berücksichtigt:

`password`, `passwd`, `pwd`, `secret`, `token`, `api_key`, `apikey`, `access_token`, `private_key`, `client_secret`

> Gespeicherte Nachweise für erkannte String Secrets werden maskiert.
  - Die Risikoanalyse ist eine statische Mustererkennung. Ein Treffer bedeutet nicht automatisch, dass eine konkrete Sicherheitslücke vorliegt. Der Kontext des Codes muss weiterhin bewertet werden.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_bytecode"></a>

## Bytecode Inspektion

> Die Bytecode Ansicht verwendet das Python Modul `dis`.
  - Der ausgewählte Quellcode wird mit folgenden Eigenschaften kompiliert:

```python
compile(
    source,
    filename,
    "exec",
    dont_inherit=True,
    optimize=0,
)
```

> Anschließend werden das Haupt Codeobjekt und enthaltene untergeordnete Codeobjekte rekursiv disassembliert.
  - Damit lassen sich unter anderem Python Instruktionen von:

🔹 Modulen  
🔹 Funktionen  
🔹 Methoden  
🔹 verschachtelten Codeobjekten

untersuchen.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_ui"></a>

## Benutzeroberfläche

> Die Benutzeroberfläche basiert auf PySide6 und verwendet ein dunkles Business Design.

> [!NOTE]
> Vorhandene Hauptbereiche:

1. Dashboard
2. Projekt Explorer
3. Abhängigkeiten
4. Funktionsaufrufe
5. Komplexität
6. Risikoanalyse
7. Bytecode
8. Verlauf

> Das Dashboard zeigt zentrale Projektmetriken in separaten Karten.
  - Der Header enthält Funktionen zum Öffnen eines Projekts, Starten und Abbrechen einer Analyse sowie zum Exportieren.
  - Danach folgen optisch getrennt die Social Media Buttons für GitHub, LinkedIn und Facebook.
    - Ein weiterer vertikaler Separator trennt den Social Media Bereich von Info und Sprachumschaltung.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_sprache"></a>

## Deutsch und Englisch

> Die Anwendung besitzt eine zentrale Lokalisierung mit vollständigen deutschen und englischen Übersetzungsschlüsseln.
  - Aktuell enthalten beide Sprachen jeweils 102 übereinstimmende Schlüssel.
  - Der Sprachwechsel erfolgt direkt während der Laufzeit.

> [!NOTE]
> Beim Umschalten werden unter anderem aktualisiert:

🔹 Navigation  
🔹 Buttons  
🔹 Tabellenüberschriften  
🔹 Dashboard Beschriftungen  
🔹 Symboltypen  
🔹 Abhängigkeitskategorien  
🔹 Risikobeschreibungen  
🔹 Statusmeldungen  
🔹 Dialoge  
🔹 Verlauf  
🔹 Info Dialog

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_sqlite"></a>

## SQLite Verlauf

BPREI speichert Zusammenfassungen abgeschlossener Analysen in einer lokalen SQLite Datenbank.

Standardpfad unter dem Benutzerprofil:

```text
~/.bprei/bprei_history.sqlite3
```

Gespeichert werden:

🔹 Analysezeitpunkt  
🔹 Projektname  
🔹 Projektpfad  
🔹 Anzahl Dateien  
🔹 Anzahl Klassen  
🔹 Anzahl Funktionen  
🔹 Anzahl Methoden  
🔹 Anzahl Abhängigkeiten  
🔹 Anzahl Risikobefunde  
🔹 durchschnittliche Komplexität

Die Verlaufsansicht zeigt standardmäßig bis zu 100 der zuletzt gespeicherten Analysen.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_export"></a>

## Exportformate

> BPREI unterstützt vier Exportformate:

### JSON

> Exportiert die vollständige strukturierte `AnalysisResult` Datenstruktur.

### CSV

> Exportiert Symbole und Risikobefunde. 
  - Potenziell problematische Tabellenwerte mit führendem `=`, `+`, `-`, `@`, Tabulator oder Wagenrücklauf werden vor dem Schreiben neutralisiert.

### HTML

> Erzeugt einen eigenständigen HTML Bericht mit dunklem Design, Projektmetriken und Risikobefunden.

### Markdown

> Erzeugt einen Markdown Analysebericht mit Projektinformationen, Metriken und Risikobefunden.
  - CSV, HTML und Markdown verwenden die aktuell aktive Sprache der Benutzeroberfläche.
  - JSON exportiert die strukturierten internen Daten.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_test"></a>

## Windows Testumgebung

> [!NOTE]
> Das Projekt enthält:

```text
start_windows.bat
```

> Das Skript:

1. wechselt in das Projektverzeichnis
2. erstellt bei Bedarf eine eigene `.venv`
3. aktiviert die virtuelle Umgebung
4. aktualisiert `pip`
5. installiert beziehungsweise prüft die Pakete aus `requirements.txt`
6. startet `main.py`

> Damit kann die Anwendung in einer isolierten virtuellen Python Umgebung getestet werden.

Start:

```text
start_windows.bat
```

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_build"></a>

## Windows Build

> Das Projekt enthält zusätzlich:

```text
build_windows.bat
```

```yarn
Das Skript:
```

1. erstellt bei Bedarf die `.venv`
2. aktiviert die virtuelle Umgebung
3. aktualisiert `pip`
4. installiert die Projektabhängigkeiten
5. installiert PyInstaller
6. erstellt einen Windows Build ohne Konsolenfenster
7. sammelt NumPy und SciPy vollständig für den Build ein

```yarn
Verwendeter PyInstaller Name:
```

```text
BylickiLabs-Python-Reverse-Engineering-Inspector
```

```yarn
Die Ausgabe wird unter:
```

```text
dist\
```

erstellt.

> PyInstaller verwendet hier den normalen Verzeichnis Build. Dadurch befindet sich die ausführbare Anwendung zusammen mit den benötigten Laufzeitkomponenten im erzeugten Anwendungsverzeichnis.
  - Dieses Verzeichnis kann auf einen anderen Datenträger, beispielsweise einen USB Stick, kopiert werden. Auf einem kompatiblen Windows System können die mitgelieferten Komponenten anschließend direkt aus diesem Verzeichnis genutzt werden, ohne die Python Pakete erneut über `pip` installieren zu müssen.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_installation"></a>

## Manuelle Installation

> Aufgrund der im Quellcode verwendeten Python Syntax wird Python 3.10 oder neuer benötigt.

### Virtuelle Umgebung erstellen

```powershell
py -m venv .venv
```

### Virtuelle Umgebung aktivieren

```powershell
.venv\Scripts\activate
```

### Abhängigkeiten installieren

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Anwendung starten

```powershell
python main.py
```

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_struktur"></a>

## Projektstruktur

```text
BylickiLabs_Python_Reverse_Engineering_Inspector/
│
├── main.py
├── requirements.txt
├── start_windows.bat
├── build_windows.bat
├── README.md
│
└── src/
    ├── __init__.py
    ├── config.py
    ├── localization.py
    ├── models.py
    │
    ├── analyzers/
    │   ├── __init__.py
    │   ├── project_analyzer.py
    │   └── bytecode_analyzer.py
    │
    ├── services/
    │   ├── __init__.py
    │   ├── database.py
    │   └── exporter.py
    │
    └── ui/
        ├── __init__.py
        └── main_window.py
```

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_anforderungen"></a>

## Technische Anforderungen


> [!NOTE]
> Die aktuelle `requirements.txt` enthält:

```text
PySide6>=6.8
numpy>=2.0
scipy>=1.13
```

> Zusätzlich wird für den automatischen Windows Build PyInstaller durch `build_windows.bat` installiert.
  - Kerntechnologien:

🔹 Python  
🔹 PySide6  
🔹 AST  
🔹 NumPy  
🔹 SciPy  
🔹 SQLite  
🔹 `dis`  
🔹 PyInstaller für den Windows Build

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_verzeichnisse"></a>

## Analysierte und ausgeschlossene Verzeichnisse

> BPREI sucht rekursiv nach `.py` und `.pyw` Dateien.
  - Folgende Verzeichnisse werden aktuell von der Projektanalyse ausgeschlossen:

```text
.git
.hg
.svn
.idea
.vs
.vscode
__pycache__
.pytest_cache
.mypy_cache
.venv
venv
env
node_modules
build
dist
.tox
```

> Dadurch werden typische Versionsverwaltungsdaten, Entwicklungsumgebungen, virtuelle Umgebungen, Cache Daten und Build Ausgaben nicht als Bestandteil des Zielprojekts analysiert.

[Nach oben](#de_inhalt)

<br>

---

<br>

<a id="de_status"></a>

## Projektstatus

> Aktuelle Anwendungsversion:

```text
1.0.0
```

> Anwendungsname:

```text
BylickiLabs Python Reverse Engineering Inspector
```

> Kurzname:

```text
BPREI
```

> Entwickler:

```text
Thorsten Bylicki / BylickiLabs
```

> Die geprüfte Projektversion enthält eine syntaktisch valide Python Codebasis. 
  - Die deutsche und englische Lokalisierung besitzen jeweils 102 identische Übersetzungsschlüssel.

[Nach oben](#de_inhalt)

<br>

---
---

<br>

<a id="english"></a>

# English

<a id="en_contents"></a>

## Table of Contents

1. [Project Overview](#en_overview)
2. [Feature Set](#en_features)
3. [Static Analysis and Security Model](#en_static)
4. [Project and Symbol Analysis](#en_symbols)
5. [Dependency Analysis](#en_dependencies)
6. [Function Calls](#en_calls)
7. [Complexity Analysis](#en_complexity)
8. [NumPy and SciPy](#en_numpy_scipy)
9. [Risk Analysis](#en_risk)
10. [Bytecode Inspection](#en_bytecode)
11. [User Interface](#en_ui)
12. [German and English](#en_language)
13. [SQLite History](#en_sqlite)
14. [Export Formats](#en_export)
15. [Windows Test Environment](#en_test)
16. [Windows Build](#en_build)
17. [Manual Installation](#en_installation)
18. [Project Structure](#en_structure)
19. [Technical Requirements](#en_requirements)
20. [Analyzed and Excluded Directories](#en_directories)
21. [Project Status](#en_status)

<br>

---

<br>

<a id="en_overview"></a>

## Project Overview

> The BylickiLabs Python Reverse Engineering Inspector, short BPREI, is a desktop application for static inspection of complete Python projects.
  - The application reads Python source code, analyzes the internal structure and presents technical relationships in several specialized areas.
    - These include modules, classes, functions, methods, imports, dependencies, direct function calls, complexity values, statistical anomalies, selected risk patterns and Python bytecode.
---
  - The inspected target project is not imported and is not executed.
    - The analysis is primarily based on the Python Abstract Syntax Tree.
      - The graphical interface is implemented with PySide6.
	  - NumPy and SciPy are functionally used for statistical code analysis.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_features"></a>

## Feature Set

Currently implemented:

🔹 Complete project directory analysis  
🔹 Support for `.py` and `.pyw`  
🔹 Project Explorer  
🔹 Source code view  
🔹 Class detection  
🔹 Function and method detection  
🔹 Async function and method detection  
🔹 Parameter analysis  
🔹 Decorator analysis  
🔹 Import analysis  
🔹 Dependency classification  
🔹 Direct function call analysis  
🔹 AST based complexity scoring  
🔹 NumPy project metrics  
🔹 SciPy Z Score anomaly detection  
🔹 Risk Pattern analysis  
🔹 Bytecode disassembly  
🔹 SQLite analysis history  
🔹 JSON export  
🔹 CSV export  
🔹 HTML export  
🔹 Markdown export  
🔹 German interface  
🔹 English interface  
🔹 Runtime language switching  
🔹 GitHub button  
🔹 LinkedIn button  
🔹 Facebook button  
🔹 Detailed About dialog  
🔹 Background analysis with QThread  
🔹 Cancellation of running analyses

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_static"></a>

## Static Analysis and Security Model

> BPREI does not execute the inspected Python project.
  - The source code is converted into an Abstract Syntax Tree with `ast.parse()` and then evaluated structurally.
  - This allows project components to be inspected without loading target modules through `import`.
    - The Bytecode view uses `compile()` exclusively to create code objects. These code objects are then disassembled with the Python module `dis`. The compiled target code is not executed within this function.
  - Syntax errors in individual files are stored in the analysis information so that the entire project is not automatically discarded because of a single invalid file.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_symbols"></a>

## Project and Symbol Analysis

> The Project Analyzer inspects every detected Python file and records, among other things:

🔹 relative file path  
🔹 absolute file path  
🔹 total line count  
🔹 code lines  
🔹 comment lines  
🔹 blank lines  
🔹 classes  
🔹 functions  
🔹 methods  
🔹 async functions  
🔹 async methods  
🔹 parameters  
🔹 decorators  
🔹 start line  
🔹 end line  
🔹 parent symbols  
🔹 direct function calls  
🔹 complexity value

> A file or symbol can be selected in the Project Explorer. The corresponding source code is displayed and, for symbols, the view jumps directly to the relevant code position.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_dependencies"></a>

## Dependency Analysis

> Imports are analyzed automatically and assigned to three categories:

🔹 Standard Library  
🔹 Internal  
🔹 Third Party

For each detected dependency BPREI stores:

🔹 module name  
🔹 category  
🔹 number of uses  
🔹 files containing the dependency

> Internal dependencies are identified from the available project structure.
  - Python Standard Library modules are classified through `sys.stdlib_module_names`.
    - All remaining detected imports are treated as Third Party dependencies.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_calls"></a>

## Function Calls

> BPREI analyzes direct calls inside functions and methods.
  - For each call the following information is stored:

🔹 caller symbol  
🔹 called target  
🔹 file  
🔹 source line

> This makes it possible to understand which functions and methods are connected within a project.
  - Nested function definitions and class definitions are intentionally handled separately during direct call analysis and are not automatically attributed to the outer function body.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_complexity"></a>

## Complexity Analysis

> BPREI calculates an AST based complexity value for functions and methods.
  - The score includes structures such as:

🔹 `if`  
🔹 `for`  
🔹 `async for`  
🔹 `while`  
🔹 conditional expressions  
🔹 `assert`  
🔹 comprehensions  
🔹 boolean operations  
🔹 exception handlers  
🔹 `try` with `else`  
🔹 `match` cases

> [!NOTE]
> The application displays, among other things:

🔹 average complexity  
🔹 median  
🔹 95th percentile  
🔹 standard deviation  
🔹 maximum complexity  
🔹 statistically unusual symbols

> The value is an internal AST based project metric and is not intended as a complete replacement for specialized formal code analysis.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_numpy_scipy"></a>

## NumPy and SciPy

> NumPy and SciPy are functional parts of the application.

### NumPy

> NumPy is used to process complexity values and calculate the following metrics:

🔹 mean with `numpy.mean()`  
🔹 median with `numpy.median()`  
🔹 95th percentile with `numpy.percentile()`  
🔹 standard deviation with `numpy.std()`  
🔹 maximum with `numpy.max()`

### SciPy

> SciPy is used for statistical anomaly detection.

> `scipy.stats.zscore()` calculates Z Scores for the complexity values of the analyzed functions and methods.
  - A symbol is currently included as a statistical anomaly when its Z Score is at least `2.0`.
    - At least three analyzable functions or methods are required for this evaluation.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_risk"></a>

## Risk Analysis

> Risk Pattern analysis searches for selected constructs that may deserve additional attention during manual code review.

> [!NOTE]
> Currently detected:

🔹 `eval()`  
🔹 `exec()`  
🔹 `compile()`  
🔹 `os.system()`  
🔹 `pickle.load()`  
🔹 `pickle.loads()`  
🔹 `yaml.load()`  
🔹 `tempfile.mktemp()`  
🔹 calls through `subprocess`  
🔹 `shell=True` in subprocess calls  
🔹 `verify=False` in recognized HTTP calls  
🔹 possible hardcoded secrets

> Possible hardcoded secrets include variable names such as:

`password`, `passwd`, `pwd`, `secret`, `token`, `api_key`, `apikey`, `access_token`, `private_key`, `client_secret`

> Stored evidence for detected string secrets is masked.
  - Risk analysis is static pattern detection. A finding does not automatically mean that a concrete security vulnerability exists. The code context must still be evaluated.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_bytecode"></a>

## Bytecode Inspection

> The Bytecode view uses the Python module `dis`.
  - The selected source code is compiled with the following properties:

```python
compile(
    source,
    filename,
    "exec",
    dont_inherit=True,
    optimize=0,
)
```

> The main code object and contained child code objects are then recursively disassembled.
  - This allows inspection of Python instructions from:

🔹 modules  
🔹 functions  
🔹 methods  
🔹 nested code objects

inspect.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_ui"></a>

## User Interface

> The user interface is based on PySide6 and uses a dark business design.

> [!NOTE]
> Available main areas:

1. Dashboard
2. Project Explorer
3. Dependencies
4. Function Calls
5. Complexity
6. Risk Analysis
7. Bytecode
8. History

> The Dashboard presents central project metrics in separate cards.
  - The header contains controls for opening a project, starting and cancelling an analysis and exporting results.
  - Visually separated Social Media buttons for GitHub, LinkedIn and Facebook follow.
    - A second vertical separator separates the Social Media area from Info and language switching.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_language"></a>

## German and English

> The application uses centralized localization with complete German and English translation keys.
  - Both languages currently contain 102 matching keys.
  - Language switching happens directly during runtime.

> [!NOTE]
> When switching languages, the following elements are updated, among others:

🔹 navigation  
🔹 buttons  
🔹 table headers  
🔹 Dashboard labels  
🔹 symbol types  
🔹 dependency categories  
🔹 risk descriptions  
🔹 status messages  
🔹 dialogs  
🔹 history  
🔹 About dialog

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_sqlite"></a>

## SQLite History

> BPREI stores summaries of completed analyses in a local SQLite database.
  - Default location inside the user profile:

```text
~/.bprei/bprei_history.sqlite3
```

Stored information:

🔹 analysis timestamp  
🔹 project name  
🔹 project path  
🔹 file count  
🔹 class count  
🔹 function count  
🔹 method count  
🔹 dependency count  
🔹 risk finding count  
🔹 average complexity

The History view displays up to 100 of the most recently stored analyses by default.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_export"></a>

## Export Formats

> BPREI supports four export formats:

### JSON

> Exports the complete structured `AnalysisResult` data structure.

### CSV

> Exports symbols and risk findings.
  - Potentially problematic spreadsheet values starting with `=`, `+`, `-`, `@`, tab or carriage return are neutralized before writing.

### HTML

> Creates a standalone HTML report with a dark design, project metrics and risk findings.

### Markdown

> Creates a Markdown analysis report with project information, metrics and risk findings.
  - CSV, HTML and Markdown use the currently active interface language.
  - JSON exports the structured internal data.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_test"></a>

## Windows Test Environment

> [!NOTE]
> The project contains:

```text
start_windows.bat
```

> The script:

1. changes to the project directory
2. creates its own `.venv` when required
3. activates the virtual environment
4. upgrades `pip`
5. installs or verifies the packages from `requirements.txt`
6. starts `main.py`

> This allows the application to be tested in an isolated virtual Python environment.

Start:

```text
start_windows.bat
```

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_build"></a>

## Windows Build

> The project additionally contains:

```text
build_windows.bat
```

```yarn
The script:
```

1. creates the `.venv` when required
2. activates the virtual environment
3. upgrades `pip`
4. installs the project dependencies
5. installs PyInstaller
6. creates a Windows build without a console window
7. collects NumPy and SciPy completely for the build

```yarn
PyInstaller name used:
```

```text
BylickiLabs-Python-Reverse-Engineering-Inspector
```

```yarn
The output is written to:
```

```text
dist\
```

created.

> PyInstaller uses the normal directory build here. This means that the executable application is located together with the required runtime components inside the generated application directory.
  - This directory can be copied to another storage device, for example a USB drive. On a compatible Windows system the bundled components can then be used directly from this directory without reinstalling the Python packages through `pip`.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_installation"></a>

## Manual Installation

> Because of the Python syntax used in the source code, Python 3.10 or newer is required.

### Create virtual environment

```powershell
py -m venv .venv
```

### Activate virtual environment

```powershell
.venv\Scripts\activate
```

### Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Start application

```powershell
python main.py
```

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_structure"></a>

## Project Structure

```text
BylickiLabs_Python_Reverse_Engineering_Inspector/
│
├── main.py
├── requirements.txt
├── start_windows.bat
├── build_windows.bat
├── README.md
│
└── src/
    ├── __init__.py
    ├── config.py
    ├── localization.py
    ├── models.py
    │
    ├── analyzers/
    │   ├── __init__.py
    │   ├── project_analyzer.py
    │   └── bytecode_analyzer.py
    │
    ├── services/
    │   ├── __init__.py
    │   ├── database.py
    │   └── exporter.py
    │
    └── ui/
        ├── __init__.py
        └── main_window.py
```

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_requirements"></a>

## Technical Requirements

> [!NOTE]
> The current `requirements.txt` contains:

```text
PySide6>=6.8
numpy>=2.0
scipy>=1.13
```

> PyInstaller is additionally installed by `build_windows.bat` for the automated Windows build.
  - Core technologies:

🔹 Python  
🔹 PySide6  
🔹 AST  
🔹 NumPy  
🔹 SciPy  
🔹 SQLite  
🔹 `dis`  
🔹 PyInstaller for the Windows build

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_directories"></a>

## Analyzed and Excluded Directories

> BPREI recursively searches for `.py` and `.pyw` files.
  - The following directories are currently excluded from project analysis:

```text
.git
.hg
.svn
.idea
.vs
.vscode
__pycache__
.pytest_cache
.mypy_cache
.venv
venv
env
node_modules
build
dist
.tox
```

> This keeps common version control data, development environments, virtual environments, cache data and build output outside the target project analysis.

[Back to contents](#en_contents)

<br>

---

<br>

<a id="en_status"></a>

## Project Status

> Current application version:

```text
1.0.0
```

> Application name:

```text
BylickiLabs Python Reverse Engineering Inspector
```

> Short name:

```text
BPREI
```

> Developer:

```text
Thorsten Bylicki / BylickiLabs
```

> The inspected project version contains a syntactically valid Python codebase.
  - The German and English localization each contain 102 identical translation keys.

[Back to contents](#en_contents)

<br>

---

<br>

[Back to top](#top)
