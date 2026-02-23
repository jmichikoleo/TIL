"""
코딩 테스트 문제 8: 모스 부호 변환기

문제 설명:
모스 부호(Morse Code)를 번역하는 프로그램을 작성하시오.
사용자가 알파벳을 입력하면 모스 부호로, 모스 부호를 입력하면 알파벳으로 변환합니다.

실행 예시 1 (알파벳 → 모스부호):
$ python morse_test.py
===== 모스 부호 변환기 =====
Input your message (H-Help, 0-Exit): SOS
... --- ...

실행 예시 2 (모스부호 → 알파벳):
Input your message (H-Help, 0-Exit): ... --- ...
SOS

실행 예시 3 (도움말):
Input your message (H-Help, 0-Exit): H
===== 모스 부호 표 =====
A: .-    B: -...  C: -.-.  D: -..   E: .
F: ..-.  G: --.   H: ....  I: ..    J: .---
K: -.-   L: .-..  M: --    N: -.    O: ---
P: .--.  Q: --.-  R: .-.   S: ...   T: -
U: ..-   V: ...-  W: .--   X: -..-  Y: -.--
Z: --..

실행 예시 4 (띄어쓰기 포함):
Input your message (H-Help, 0-Exit): HELLO WORLD
.... . .-.. .-.. ---  .-- --- .-. .-.. -..

Input your message (H-Help, 0-Exit): .... . .-.. .-.. ---  .-- --- .-. .-.. -..
HELLO WORLD

규칙:
1. 알파벳 → 모스부호 변환 시:
   - 각 문자 사이는 한 칸 띄어쓰기
   - 단어 사이는 두 칸 띄어쓰기
   - 문장부호(.,!?)는 삭제

2. 모스부호 → 알파벳 변환 시:
   - 한 칸 띄어쓰기: 문자 구분
   - 두 칸 띄어쓰기: 단어 구분

3. 입력 검증:
   - 알파벳: 숫자나 특수문자 포함 시 에러
   - 모스부호: "-", ".", " " 외 문자 포함 시 에러

요구사항:
1. get_morse_code_dict() - 모스 부호 딕셔너리 반환 (제공됨)
2. is_help_command(user_input) - "H" 또는 "HELP" 입력 확인
3. is_validated_english_sentence(user_input) - 알파벳 문장 검증
4. is_validated_morse_code(user_input) - 모스 부호 검증
5. get_cleaned_english_sentence(raw_english_sentence) - 문장부호 제거
6. encoding_character(english_character) - 알파벳 → 모스부호
7. decoding_character(morse_character) - 모스부호 → 알파벳
8. encoding_sentence(english_sentence) - 문장 → 모스부호
9. decoding_sentence(morse_sentence) - 모스부호 → 문장
10. main() - 메인 함수
"""

# ==================== 제공되는 Helper 함수 ====================

def get_morse_code_dict():
    """모스 부호 딕셔너리 반환"""
    morse_code = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--.."
    }
    return morse_code


def get_help_message():
    """도움말 메시지 반환"""
    message = "===== 모스 부호 표 =====\n"
    morse_code = get_morse_code_dict()
    counter = 0
    for key, value in sorted(morse_code.items()):
        message += f"{key}: {value:<5} "
        counter += 1
        if counter % 5 == 0:
            message += "\n"
    return message


# ==================== 여기서부터 코드를 작성하세요 ====================

def is_help_command(user_input):
    """
    "H" 또는 "HELP" 입력 확인 (대소문자 구분 없음)
    
    Args:
        user_input (str): 사용자 입력
        
    Returns:
        bool: "H" 또는 "HELP"면 True
    """
    # TODO: 여기에 코드를 작성하세요
    return user_input.strip().upper() in ("H", "HELP")


def is_validated_english_sentence(user_input):
    """
    알파벳 문장으로 유효한지 검증
    
    조건:
    1. 숫자가 포함되면 False
    2. 특수문자 포함 시 False (.,!? 제외)
    3. 문장부호 제외하고 비어있으면 False
    
    Args:
        user_input (str): 사용자 입력
        
    Returns:
        bool: 유효하면 True
    """
    # TODO: 여기에 코드를 작성하세요
    clean = ""
    
    for c in user_input:
        if c.isdigit():
            return False 
        if c.isalpha() or c == " ":
            clean += c
        elif c in ".,!?":
            continue
        else:
            return False
    return clean.strip() != ""

    # 힌트: 문장부호를 제거한 후 검증


def is_validated_morse_code(user_input):
    """
    모스 부호로 유효한지 검증
    
    조건:
    1. "-", ".", " " 외 문자 포함 시 False
    2. 유효하지 않은 모스 부호 조합 시 False
    
    Args:
        user_input (str): 사용자 입력
        
    Returns:
        bool: 유효하면 True
    """
    # TODO: 여기에 코드를 작성하세요
    allow = {"-", ".", " "}
    morse_dict = get_morse_code_dict()
    valid = set(morse_dict.values())

    for c in user_input:
        if c not in allow:
            return False
        
    w = user_input.strip().split(" ")
    for word in w : 
        letters = word.split()
        for letter in letters :
            if letter not in valid:
                return False
    return True

    # 힌트: 각 모스 부호가 딕셔너리에 있는지 확인


def get_cleaned_english_sentence(raw_english_sentence):
    """
    문장부호 제거 및 공백 정리
    
    Args:
        raw_english_sentence (str): 원본 문장
        
    Returns:
        str: 정리된 문장
    """
    # TODO: 여기에 코드를 작성하세요
    res = ""
    for c in raw_english_sentence:
        if c.isalpha() or c == " ":
            res += c
    return res.strip().upper()

    # 힌트: .,!? 제거하고 양쪽 공백 제거


def encoding_character(english_character):
    """
    알파벳 한 글자를 모스 부호로 변환
    
    Args:
        english_character (str): 알파벳 한 글자
        
    Returns:
        str: 모스 부호
    """
    # TODO: 여기에 코드를 작성하세요
    morse_dict = get_morse_code_dict()
    return morse_dict[english_character.upper()]


def decoding_character(morse_character):
    """
    모스 부호를 알파벳 한 글자로 변환
    
    Args:
        morse_character (str): 모스 부호
        
    Returns:
        str: 알파벳
    """
    # TODO: 여기에 코드를 작성하세요
    morse_dict = get_morse_code_dict()
    for key, value in morse_dict.items():
        if value == morse_character:
            return key
    # 힌트: 딕셔너리의 value로 key 찾기
    
def encoding_sentence(english_sentence):
    """
    알파벳 문장을 모스 부호로 변환
    
    규칙:
    - 문자 사이: 한 칸 띄어쓰기
    - 단어 사이: 두 칸 띄어쓰기
    
    Args:
        english_sentence (str): 알파벳 문장
        
    Returns:
        str: 모스 부호 문장
    """
    # TODO: 여기에 코드를 작성하세요
    clean = get_cleaned_english_sentence(english_sentence)
    w = clean.split()

    encoded = []
    for word in w:
        encoded_letter = []
        for c in word:
            encoded_letter.append(encoding_character(c))
        encoded.append(" ".join(encoded_letter))

    return "  ".join(encoded)
    # 힌트: 단어별로 split하고, 각 단어를 변환 후 join


def decoding_sentence(morse_sentence):
    """
    모스 부호 문장을 알파벳으로 변환
    
    규칙:
    - 한 칸 띄어쓰기: 문자 구분
    - 두 칸 띄어쓰기: 단어 구분
    
    Args:
        morse_sentence (str): 모스 부호 문장
        
    Returns:
        str: 알파벳 문장
    """
    # TODO: 여기에 코드를 작성하세요
    w = morse_sentence.strip().split(" ")

    decoded_word = []
    for word in w:
        letters = word.split()
        decoded_letter = []
        for letter in letters : 
            decoded_letter.append(decoding_character(letter))
        decoded_word.append("".join(decoded_letter))
    
    return " ".join(decoded_word)
    # 힌트: 두 칸으로 split해서 단어 분리, 한 칸으로 문자 분리


def main():
    """
    메인 함수
    
    규칙:
    - 0 입력 시 종료
    - H 또는 HELP 입력 시 도움말 출력
    - 알파벳 입력 시 모스 부호로 변환
    - 모스 부호 입력 시 알파벳으로 변환
    - 잘못된 입력 시 "Wrong Input" 출력
    """
    # TODO: 여기에 코드를 작성하세요
    while True: 
        user_input = input("Input Message (H = Help, 0 = Exit)")

        if user_input == "0":
            break

        elif is_help_command(user_input):
            print(get_help_message())
            continue
        
        elif is_validated_english_sentence(user_input): 
            print(encoding_sentence(user_input))

        elif is_validated_morse_code(user_input):
            print(decoding_sentence(user_input))
        
        else:
            print("Wrong Input")
        



# ==================== 여기까지 코드를 작성하세요 ====================


# ==================== 테스트 코드 (수정하지 마세요) ====================
import pytest
from io import StringIO
import sys


class TestIsHelpCommand:
    """is_help_command 함수 테스트"""
    
    def test_help_uppercase(self):
        assert is_help_command("H") == True
        assert is_help_command("HELP") == True
    
    def test_help_lowercase(self):
        assert is_help_command("h") == True
        assert is_help_command("help") == True
    
    def test_help_mixedcase(self):
        assert is_help_command("HeLp") == True
    
    def test_not_help(self):
        assert is_help_command("SOS") == False
        assert is_help_command("0") == False


class TestIsValidatedEnglishSentence:
    """is_validated_english_sentence 함수 테스트"""
    
    def test_valid_english(self):
        assert is_validated_english_sentence("HELLO") == True
        assert is_validated_english_sentence("Hello World") == True
    
    def test_with_punctuation(self):
        assert is_validated_english_sentence("Hello!") == True
        assert is_validated_english_sentence("SOS.") == True
    
    def test_with_numbers(self):
        assert is_validated_english_sentence("Hello123") == False
        assert is_validated_english_sentence("CS50") == False
    
    def test_with_special_chars(self):
        assert is_validated_english_sentence("Hello@World") == False
        assert is_validated_english_sentence("I'm fine") == False
    
    def test_empty_or_punctuation_only(self):
        assert is_validated_english_sentence("!!!") == False
        assert is_validated_english_sentence("   ") == False


class TestIsValidatedMorseCode:
    """is_validated_morse_code 함수 테스트"""
    
    def test_valid_morse(self):
        assert is_validated_morse_code("... --- ...") == True
        assert is_validated_morse_code(".-") == True
    
    def test_invalid_characters(self):
        assert is_validated_morse_code("... A ...") == False
        assert is_validated_morse_code("...-1") == False
    
    def test_invalid_morse_pattern(self):
        assert is_validated_morse_code("......") == False
        assert is_validated_morse_code("-----.") == False


class TestGetCleanedEnglishSentence:
    """get_cleaned_english_sentence 함수 테스트"""
    
    def test_remove_punctuation(self):
        result = get_cleaned_english_sentence("Hello!")
        assert result == "Hello"
    
    def test_remove_multiple_punctuation(self):
        result = get_cleaned_english_sentence("Hello, World!")
        assert result == "Hello World"
    
    def test_trim_spaces(self):
        result = get_cleaned_english_sentence("  Hello  ")
        assert result == "Hello"


class TestEncodingCharacter:
    """encoding_character 함수 테스트"""
    
    def test_encode_basic(self):
        assert encoding_character("A") == ".-"
        assert encoding_character("S") == "..."
        assert encoding_character("O") == "---"
    
    def test_encode_lowercase(self):
        assert encoding_character("a") == ".-"
        assert encoding_character("s") == "..."


class TestDecodingCharacter:
    """decoding_character 함수 테스트"""
    
    def test_decode_basic(self):
        assert decoding_character(".-") == "A"
        assert decoding_character("...") == "S"
        assert decoding_character("---") == "O"


class TestEncodingSentence:
    """encoding_sentence 함수 테스트"""
    
    def test_encode_word(self):
        result = encoding_sentence("SOS")
        assert result == "... --- ..."
    
    def test_encode_sentence(self):
        result = encoding_sentence("HELLO WORLD")
        assert "  " in result  # 두 칸 띄어쓰기 확인
    
    def test_single_spaces_between_chars(self):
        result = encoding_sentence("SOS")
        parts = result.split(" ")
        assert len(parts) == 3  # 세 문자, 두 개의 한 칸 띄어쓰기


class TestDecodingSentence:
    """decoding_sentence 함수 테스트"""
    
    def test_decode_word(self):
        result = decoding_sentence("... --- ...")
        assert result == "SOS"
    
    def test_decode_sentence(self):
        result = decoding_sentence(".... . .-.. .-.. ---  .-- --- .-. .-.. -..")
        assert result == "HELLO WORLD"


class TestMainFunction:
    """main 함수 통합 테스트"""
    
    def test_main_exit(self, monkeypatch, capsys):
        """0 입력 시 종료"""
        monkeypatch.setattr('sys.stdin', StringIO('0\n'))
        main()
        captured = capsys.readouterr()
        assert "모스 부호 변환기" in captured.out or "Morse" in captured.out
    
    def test_main_help(self, monkeypatch, capsys):
        """도움말 출력"""
        monkeypatch.setattr('sys.stdin', StringIO('H\n0\n'))
        main()
        captured = capsys.readouterr()
        assert "모스 부호 표" in captured.out or "A:" in captured.out
    
    def test_main_encoding(self, monkeypatch, capsys):
        """알파벳 → 모스부호 변환"""
        monkeypatch.setattr('sys.stdin', StringIO('SOS\n0\n'))
        main()
        captured = capsys.readouterr()
        assert "... --- ..." in captured.out
    
    def test_main_decoding(self, monkeypatch, capsys):
        """모스부호 → 알파벳 변환"""
        monkeypatch.setattr('sys.stdin', StringIO('... --- ...\n0\n'))
        main()
        captured = capsys.readouterr()
        assert "SOS" in captured.out
    
    def test_main_wrong_input(self, monkeypatch, capsys):
        """잘못된 입력"""
        monkeypatch.setattr('sys.stdin', StringIO('Hello123\n0\n'))
        main()
        captured = capsys.readouterr()
        assert "Wrong Input" in captured.out or "wrong" in captured.out.lower()


# pytest 실행을 위한 코드
if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        pytest.main([__file__, "-v"])
