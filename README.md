# SecurityProject
Our attempt at making LLM's more secure

:bookmark_tabs:HOW TO CLONE::bookmark_tabs:
1. Above the list of files click on <>Code
2. Copy the HTTPS
3. Open Git Bash
4. Type "git clone "
5. Paste the link you copied.

:hammer_and_wrench:HOW TO BUILD/DEPLOY(with integration)::hammer_and_wrench:

NOTE: to use the integrated version you must set your api key enviroment variable, and MUST have credit from openAI to run.
1. In the command line, locate the file "llm-security" and change directory into it.
2. use command "pip install -r requirements.txt"
3. run using command "python main.py"
4. choose option "1" when prompted, it is the only option integrated with our solution.

:hammer_and_wrench:HOW TO BUILD/DEPLOY(without integration)::hammer_and_wrench:
1. To run only our solution, without integration, find file "homoglyph_check.py", change directory into the folder the file is in.
2. run using command "python homoglyph_check.py"


FUNCTIONALITY:

:white_check_mark:Working::white_check_mark:
1. Checks for homoglyphs.
2. Checks for banned phrases.
3. Check homoglyph based on a set ratio.
4. Denies chat if rules are broken.(rules = using high ratio of homoglyphs to normal acsii chars and using banned phrases)

:x:Not working::x:
1. Breaks if not using provided scenario of continuing after scenario.
2. Limitation to list of homoglyphs.(extensive list would be needed for real world applications)
3. Limitation to list of banned phrases.(extensive list would be needed for real world applications)

:books:SCHOLARLY REFERENCES::books:

prior research
1. Kang, D., Li, X., Stoica, I., Guestrin, C., Zaharia, M., & Hashimoto, T. (2024). Exploiting programmatic behavior of LLMS: Dual-use through standard security attacks. 2024 IEEE Security and Privacy Workshops (SPW), 132–143. https://doi.org/10.1109/spw63631.2024.00018

contemporary work
1. 
