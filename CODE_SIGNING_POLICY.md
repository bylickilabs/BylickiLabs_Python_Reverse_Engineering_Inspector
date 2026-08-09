# Code Signing Policy

## Deutsch

Der **BylickiLabs Python Reverse Engineering Inspector (BPREI)** wird als öffentliches Open Source Projekt entwickelt. Windows Builds werden über den im Repository dokumentierten GitHub Actions Workflow aus dem veröffentlichten Quellcode erzeugt.

Kostenlose Code Signierung wird durch [SignPath.io](https://signpath.io/) bereitgestellt. Das verwendete Zertifikat wird von der [SignPath Foundation](https://signpath.org/) bereitgestellt.

### Rollen

**Maintainer und Committer**

- [bylickilabs](https://github.com/bylickilabs)

**Reviewer**

- [bylickilabs](https://github.com/bylickilabs)

**Signing Approver**

- [bylickilabs](https://github.com/bylickilabs)

Änderungen von externen Mitwirkenden werden vor der Übernahme in den Hauptzweig geprüft. Signierungsanforderungen für veröffentlichte Windows Builds werden manuell freigegeben.

### Build Herkunft

Die zu signierenden Windows Binärdateien werden automatisiert über GitHub Actions aus dem Quellcode dieses Repositories erzeugt. Der Build Prozess, die PyInstaller Konfiguration und die CI Konfiguration befinden sich unter Versionskontrolle und sind öffentlich nachvollziehbar.

GitHub Artifact Attestations werden zusätzlich verwendet, um die Herkunft veröffentlichter Windows Builds kryptografisch nachvollziehbar zu dokumentieren.

### Datenschutz

BPREI analysiert ausgewählte lokale Python Projekte auf dem System des Benutzers. Analysierter Quellcode und daraus erzeugte Analyseergebnisse werden von BPREI nicht automatisch an externe Netzwerksysteme übertragen.

Dieses Programm überträgt keine Informationen an andere Netzwerksysteme, sofern dies nicht ausdrücklich durch den Benutzer oder die Person, die das Programm installiert oder ausführt, angefordert wird. Das Öffnen externer Projektseiten oder Social Media Links erfolgt ausschließlich nach einer entsprechenden Benutzeraktion.

### Signierte Veröffentlichungen

Eine digitale Signatur bestätigt die Herkunft und Integrität des signierten Builds. Sie stellt keine Garantie dafür dar, dass eine Anwendung frei von Fehlern oder Sicherheitsproblemen ist.

---

## English

The **BylickiLabs Python Reverse Engineering Inspector (BPREI)** is developed as a public open source project. Windows builds are produced from the published source code through the GitHub Actions workflow documented in this repository.

Free code signing is provided by [SignPath.io](https://signpath.io/), certificate by [SignPath Foundation](https://signpath.org/).

### Roles

**Maintainer and Committer**

- [bylickilabs](https://github.com/bylickilabs)

**Reviewer**

- [bylickilabs](https://github.com/bylickilabs)

**Signing Approver**

- [bylickilabs](https://github.com/bylickilabs)

Changes submitted by external contributors are reviewed before they are merged into the main branch. Signing requests for published Windows builds are manually approved.

### Build Provenance

Windows binaries submitted for signing are built automatically from this repository through GitHub Actions. The build process, PyInstaller configuration, and CI configuration are stored under version control and are publicly auditable.

GitHub Artifact Attestations are additionally used to provide cryptographically verifiable provenance for published Windows builds.

### Privacy

BPREI analyzes selected local Python projects on the user's system. Analyzed source code and generated analysis results are not automatically transferred by BPREI to external networked systems.

This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it. External project pages or social media links are opened only after an explicit user action.

### Signed Releases

A digital signature confirms the origin and integrity of a signed build. It does not guarantee that an application is free from defects or security issues.
