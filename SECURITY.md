# Security Policy

### Supported Versions

> The following BPREI version is currently maintained for security related issues:

| Version | Supported |
|---|---|
| `1.0.x` | ✅ |
| `< 1.0` | ❌ |

### Reporting a Vulnerability

> Security related issues should be reported responsibly and with sufficient technical detail.
  - Do not publish sensitive details, exploit instructions, credentials, tokens, secrets, or other information that could make a vulnerability immediately exploitable in a public issue.

>Preferred reporting process:

1. Use GitHub private vulnerability reporting for this repository if it is enabled.
2. Provide the affected BPREI version.
3. Identify the affected component or file.
4. Describe the potential impact.
5. Include reproducible steps when this can be done without exposing sensitive information.
6. Attach relevant logs, error messages, or technical evidence.
7. Remove passwords, tokens, API keys, and other secrets from all attachments.

> If private vulnerability reporting is unavailable, a public issue may be opened only to request a private contact channel. Do not include actionable exploit details in that issue.

### Scope

> This policy applies to security issues in the BPREI source code, bundled build configuration, local data processing, and analysis functionality provided by BPREI.
  - Security issues in third party dependencies should also be reported to the corresponding upstream project.

### Analysis of Target Projects

> BPREI is designed for static analysis of Python projects. 
  - Reports showing that analyzed target code is executed or imported contrary to the intended architecture are especially relevant and should be clearly identified.
