SUJITHX — Python Utility Toolkit



A modular, lightweight Python toolkit for file management, security utilities, automation, terminal styling, logging, system information, and network checks.



Build useful things with Python. Keep everyday utilities in one toolkit.



Features



\- File Intelligence: Search files, analyze folders, identify duplicate files, and find large files.

\- Security Utilities: Generate secure random tokens and passwords, calculate SHA-256 hashes, and perform basic password-strength checks.

\- File Automation: Create directories, inspect files, read text, and copy files without overwriting by default.

\- Terminal Styling: Colored messages, banners, and progress bars.

\- Logging: Write structured log messages to the console and log files.

\- System Information: Inspect Python, operating system, and disk usage information.

\- Network Utilities: Retrieve hostname and local IP information and check internet connectivity.

\- Interactive Command Center: Access utilities through a command-line menu.



Requirements



\- Python 3.12 or newer

\- Windows, macOS, or Linux

\- No third-party runtime dependencies



Installation



Install SUJITHX from PyPI:



python -m pip install sujithx



Quick Start



import sujithx



print(sujithx.hello("Developer"))

print(sujithx.add(10, 20))

print(sujithx.multiply(5, 4))

print(sujithx.percentage(25, 100))



Expected output:



Hello, Developer! Welcome to SUJITHX.

30

20

25.0



Using Individual Utilities



from sujithx import (

&#x20;   generate\_token,

&#x20;   generate\_password,

&#x20;   sha256\_text,

&#x20;   analyze\_folder,

)



print(generate\_token())

print(generate\_password())

print(sha256\_text("Hello SUJITHX"))

print(analyze\_folder("."))



Choose the directory you want to analyze before using file-analysis utilities.



Launch the Command Center



Run the interactive menu:



sujithx



Alternatively:



python -m sujithx.cli



Developer Installation



To work on the source code, clone the GitHub repository:



git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd SUJITHX

python -m venv .venv



Activate the environment on Windows:



.venv\\Scripts\\activate



Install the project in editable mode:



python -m pip install -e .



Replace "YOUR\_GITHUB\_REPOSITORY\_URL" with the actual URL of your SUJITHX GitHub repository.



Security Notes



\- Random tokens and passwords use Python's "secrets" module.

\- SHA-256 calculates hashes; it does not encrypt data.

\- The password-strength checker is a basic heuristic, not a comprehensive security assessment.

\- Review file paths before running file operations.

\- Keep generated passwords and tokens private.



Project Status



\- Package: "sujithx"

\- Version: 0.1.0

\- License: MIT

\- Status: Initial public release



Contributions, suggestions, and bug reports are welcome.



Author



Sujith



License



This project is licensed under the MIT License. See the "LICENSE" file for details.

