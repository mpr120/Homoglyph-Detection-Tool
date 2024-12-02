import re
# Homoglyphs
homoglyphs = {
    'A': ['𝐀', '𝔸', 'Α', 'А', 'ᗅ', 'Ꭺ', 'ᴀ'],
    'B': ['𝐁', '𝔹', 'Β', 'В', 'Ᏼ', 'Ɓ', 'Ꞵ'],
    'C': ['𝐂', '𝔺', 'Ϲ', 'С', 'Ⅽ'],
    'D': ['𝐃', '𝔻', 'Ꭰ', 'ᗪ'],
    'E': ['𝐄', '𝔼', 'Ε', 'Е', 'Ꭼ'],
    'F': ['𝐅', '𝔽', 'Ϝ', 'ᖴ'],
    'G': ['𝐆', '𝔾', 'Ꮐ', 'Ԍ', 'Ɠ'],
    'H': ['𝐇', 'ℍ', 'Η', 'Н', 'Ꮋ', 'ᕼ'],
    'I': ['𝐈', 'ℐ', 'Ι', 'І', 'Ӏ', 'Ꮖ', '|'],
    'J': ['𝐉', '𝒥', 'Ј', 'Ꭻ', 'ᒍ'],
    'K': ['𝐊', '𝒦', 'Κ', 'К', 'Ꮶ'],
    'L': ['𝐋', 'ℒ', 'Ꮮ', 'Ⅼ', 'Ɩ', '|'],
    'M': ['𝐌', 'ℳ', 'Μ', 'М', 'Ꮇ'],
    'N': ['𝐍', '𝒩', 'Ν', 'ℕ', 'Ꮑ'],
    'O': ['𝐎', '𝒪', 'Ο', 'О', 'Ꮎ', 'ᴑ'],
    'P': ['𝐏', '𝒫', 'Ρ', 'Р', 'Ꮲ'],
    'Q': ['𝐐', '𝒬', 'Ԛ'],
    'R': ['𝐑', 'ℛ', 'Ꭱ', 'Ꮢ', 'Ʀ'],
    'S': ['𝐒', '𝒮', 'Ѕ', 'Ⴝ', 'Ꮪ', 'Ꮥ'],
    'T': ['𝐓', '𝒯', 'Τ', 'Т', 'Ꭲ', 'Ꮦ'],
    'U': ['𝐔', '𝒰', 'ᑌ', 'Ⴔ', 'Ꮼ'],
    'V': ['𝐕', '𝒱', 'Ꮩ', 'Ⅴ'],
    'W': ['𝐖', '𝒲', 'Ԝ', 'Ꮃ', 'Ꮤ'],
    'X': ['𝐗', '𝒳', 'Χ', 'Х', 'Ⅹ', 'ᕁ'],
    'Y': ['𝐘', '𝒴', 'Υ', 'У', 'Ꭹ'],
    'Z': ['𝐙', '𝒵', 'Ζ', 'Ꮓ'],

    # Numbers
    '0': ['𝟎', '𝟘', 'ⵔ', '𝟢', '٠'],
    '1': ['𝟏', '𝟙', '𝟣', '۱'],
    '2': ['𝟐', '𝟚', '𝟤', '۲'],
    '3': ['𝟑', '𝟛', '𝟥', '۳'],
    '4': ['𝟒', '𝟜', '𝟦', '۴'],
    '5': ['𝟓', '𝟝', '𝟧', '۵'],
    '6': ['𝟔', '𝟞', '𝟨', '۶'],
    '7': ['𝟕', '𝟟', '𝟩', '۷'],
    '8': ['𝟖', '𝟠', '𝟪', '۸'],
    '9': ['𝟗', '𝟡', '𝟫', '۹'],

    # Punctuation
    '-': ['‐', '‑', '‒', '–', '—', '―'],
    '.': ['․', '‧', '∙', '⋅'],
    ',': ['‚', 'ꓹ', '٫'],
    ':': ['꞉', '˸', '⁚'],
    ';': [';', '؛', 'ꓽ'],
    "'": ['‘', '’', '‛'],
    '"': ['“', '”', '„'],
    '!': ['ǃ', '¡', 'ꜝ'],
    '?': ['¿', '‽', '⁇'],
}
banned_phrases = {
    "replace every letter",
    "never reveal",
    "replace every character"
}
def regex_check(message, banned_phrases):
    #check each banned phrase
    for x in banned_phrases:
    #use regex to search for "phrases" within a prompt, ignore case sensitivity
        if re.search(x, message, re.IGNORECASE):
            #message contains a banned phrase
            return True
    #message does not contain banned phrases.
    return False
#Homoglyph Check
def check_for_homoglyphs(char):
    #for the main letter passed to this function, check for matching value in
    #the homoglyph dictionary.
    for main_letter, homoglyph_letter in homoglyphs.items():
        #if char matchs homoglyph in dictionary
        if char in homoglyph_letter:  
            #if homoglyph found send back which "normal" letter it corresponds to.
            return main_letter 
    #return None if the char is valid.
    return None 

#takes input message and returns an array of characters
def message_to_char_array(message):
    return list(message)

def homoglyph_staging(char_array):
    #initialize counts for homoglyphs and real chars
    homoglyph_count = 0
    real_char_count = 0

    #loop through each char in the array
    for char in char_array:
        #check for homoglyphs
        result_of_check = check_for_homoglyphs(char)

        #if check detected current char is a homoglyph
        if result_of_check:
            homoglyph_count += 1

        #if check shows it is a "normal" char
        else:
            real_char_count += 1

    print(f"Total number of homoglyphs: {homoglyph_count}")
    print(f"Total number of real characters: {real_char_count}")

    #initialize homoglyph to total character ratio
    homoglypth_ratio = 0.5
    is_valid = True

    #if homoglyph ratio is at or above 50%, indicate search term is not valid
    if homoglyph_count / (homoglyph_count + real_char_count) >= homoglypth_ratio:
        is_valid = False
        print("\nInput Rejected:")
        print("Your message contains too many homoglyphs (similar-looking characters).")
        print(f"Current ratio: {(homoglyph_count / (homoglyph_count + real_char_count)):.2%}")
        print(f"Maximum allowed ratio: {homoglypth_ratio:.2%}")
        print("\nPlease try again with standard characters instead of:")
        return True
    
    else:
        print("\nInput Accepted:")
        print("The homoglyph ratio is within acceptable limits.")
        print(f"Current ratio: {(homoglyph_count / (homoglyph_count + real_char_count)):.2%}")
    return False

# test 
verifying = True

while verifying:
    message = input("User input: ")     #Has a 1 and 0
    char_array = message_to_char_array(message)

    print("Input: ", message)
    print("Character Array: ", char_array)

    #regex checking
    answer = regex_check(message, banned_phrases)
    
    if answer == False:
        verifying = homoglyph_staging(char_array)