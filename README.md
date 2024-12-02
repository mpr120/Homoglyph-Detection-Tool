# SecurityProject
Our attempt at making LLM's more secure

HOW TO CLONE:
1. Above the list of files click on <>Code
2. Copy the HTTPS
3. Open Git Bash
4. Type "git clone "
5. Paste the link you copied.

HOW TO BUILD/DEPLOY(with integration):
1. In the command line, locate the file "llm-security" and change directory into it.
2. run using command "python main.py"
3. choose option 1. when prompted, it is the only only integrated with our solution.

HOW TO BUILD/DEPLOY(without integration):
1. To run only our solution, without integration, find file "homoglyph_check.py"
2. run using command "python homoglyph_check.py"


FUNCTIONALITY:
Working:
1. Checks for homoglyphs.
2. Checks for banned phrases.
3. Check homoglyph based on a set ratio.
4. Denies chat if rules are broken.

Not working:
1. Breaks if not using provided scenario of continuing after scenario.
2. Limitation to list of homoglyphs.(extensive list would be needed for real world applications)
3. Limitation to list of banned phrases.(extensive list would be needed for real world applications)
