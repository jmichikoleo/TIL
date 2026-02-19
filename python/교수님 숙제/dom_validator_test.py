"""
코딩 테스트 문제 10: DOM Validator (태그 구조 검증기)

문제 설명:
문자열로 주어진 간단한 HTML/XML 유사 문서의 DOM 구조가 올바른지 검증하는 프로그램을 작성하시오.

DOM 규칙:
1. 태그는 <tag> 또는 </tag> 형식
2. 태그 이름은 알파벳 대문자로만 구성 (예: A, DIV, SPAN)
3. 모든 시작 태그 <tag>에는 대응되는 종료 태그 </tag>가 필요
4. 태그는 올바르게 중첩되어야 함
5. 공백과 일반 텍스트는 검증에 영향 없음

실행 예시:
$ python dom_validator_test.py
===== DOM Validator =====

Input DOM string: <A>test<B>123</B></A>
Result: Valid DOM structure

Input DOM string: <A><B></A></B>
Result: Invalid DOM structure - Wrong nesting

Input DOM string: <A><B>text</B></A>
Result: Valid DOM structure

Input DOM string: <A>text</A><B>more</B>
Result: Valid DOM structure

Input DOM string: <A>text
Result: Invalid DOM structure - Unclosed tag

다시 검증하시겠습니까? (Y/N): N
프로그램을 종료합니다.

판정 예시:
✅ Valid:
- <A>test</A>                    → 단일 태그 정상
- <A><B>text</B></A>             → 중첩 구조 정상
- <A>text</A><B>more</B>         → 여러 태그 정상
- <DIV><SPAN>hello</SPAN></DIV>  → 긴 이름 정상

❌ Invalid:
- <A><B></A></B>                 → 잘못된 중첩
- <A>text                        → 닫히지 않은 태그
- </A>                           → 여는 태그 없음
- <A><B>text</A></B>             → 태그 교차
- <123>text</123>                → 잘못된 태그 이름

입력 검증:
1. 빈 문자열 입력 시 → Wrong Input
2. '<'나 '>' 불균형 시 → Invalid DOM
3. 태그 이름이 대문자 아닌 경우 → Invalid DOM

재시작:
- "Y" 또는 "Yes" 입력 (대소문자 무관) → 재시작
- "N" 또는 "No" 입력 (대소문자 무관) → 종료
- 기타 입력 → Wrong Input 후 재입력

요구사항:
1. tokenize(dom_string) - 문자열을 토큰으로 분리 (태그/텍스트)
2. is_valid_tag_name(tag_name) - 태그 이름이 대문자 알파벳인지 확인
3. validate_dom(dom_string) - DOM 구조 검증 (스택 사용)
4. get_error_message(error_type) - 에러 타입별 메시지 반환
5. is_yes(user_input) - Y/Yes 확인
6. is_no(user_input) - N/No 확인
7. main() - 메인 함수
"""


# ==================== 여기서부터 코드를 작성하세요 ====================

def tokenize(dom_string):
    """
    DOM 문자열을 토큰으로 분리
    
    토큰 형식:
    - 시작 태그: ("START", "TAG_NAME")
    - 종료 태그: ("END", "TAG_NAME")
    - 텍스트: ("TEXT", "content")
    
    Args:
        dom_string (str): DOM 문자열
        
    Returns:
        list: 토큰 리스트 또는 None (파싱 실패 시)
        
    예시:
        "<A>text</A>" → [("START", "A"), ("TEXT", "text"), ("END", "A")]
        "<A><B>hi</B></A>" → [("START", "A"), ("START", "B"), ("TEXT", "hi"), 
                               ("END", "B"), ("END", "A")]
    """
    # TODO: 여기에 코드를 작성하세요
    tokens = []
    i = 0 
    n = len(dom_string)

    while i < n:
        if dom_string[i] == "<":
            close_idx = dom_string.find(">", i)
            if close_idx == -1:
                return None
            
            tag_content = dom_string[i + 1:close_idx]

            if tag_content.startswith("/"):
                tokens.append(("END", tag_content[1:]))
            else:
                tokens.append(("START", tag_content))

            i = close_idx + 1
        else: 
            start = i
            while i < n and dom_string[i] != "<":
                i += 1 
            text = dom_string[start:i]
            if text:
                 tokens.append(("TEXT", text))
    return tokens
    # 힌트 1: '<'를 만나면 '>'까지 태그로 파싱
    # 힌트 2: '<' 다음 문자가 '/'면 종료 태그
    # 힌트 3: '>'가 없으면 잘못된 형식 (None 반환)


def is_valid_tag_name(tag_name):
    """
    태그 이름이 유효한지 확인 (알파벳 대문자만 허용)
    
    Args:
        tag_name (str): 태그 이름
        
    Returns:
        bool: 유효하면 True
        
    예시:
        "A" → True
        "DIV" → True
        "div" → False
        "A1" → False
        "123" → False
    """
    # TODO: 여기에 코드를 작성하세요 
    return bool(tag_name) and tag_name.isalpha() and tag_name.isupper()
    # 힌트: isupper()와 isalpha() 활용


def validate_dom(dom_string):
    """
    DOM 구조가 유효한지 검증 (스택 사용)
    
    검증 규칙:
    1. 모든 시작 태그는 대응되는 종료 태그 필요
    2. 태그는 올바르게 중첩되어야 함
    3. 태그 이름은 대문자 알파벳만 가능
    
    Args:
        dom_string (str): 검증할 DOM 문자열
        
    Returns:
        tuple: (bool, str) - (검증 결과, 에러 메시지)
        
    예시:
        "<A>test</A>" → (True, "")
        "<A><B></A></B>" → (False, "NESTING")
        "<A>test" → (False, "UNCLOSED")
    """
    # TODO: 여기에 코드를 작성하세요
    # 힌트 1: tokenize() 함수로 토큰화
    # 힌트 2: 스택 사용 (리스트로 구현)
    # 힌트 3: START 토큰 → 스택에 push
    # 힌트 4: END 토큰 → 스택 top과 비교 후 pop
    # 힌트 5: 최종적으로 스택이 비어있어야 valid
    
    # 에러 타입:
    # "EMPTY" - 빈 문자열
    # "PARSE" - 파싱 실패 (< > 불균형 등)
    # "INVALID_NAME" - 잘못된 태그 이름
    # "UNCLOSED" - 닫히지 않은 태그
    # "UNOPENED" - 여는 태그 없음
    # "NESTING" - 잘못된 중첩
    if dom_string == "" :
        return False, "EMPTY"
    
    tokens = tokenize(dom_string)
    if tokens is None:
        return False, "PARSE"
    
    stack = []

    for token_type, value in tokens:
        if token_type == "START":
            if not is_valid_tag_name(value):
                 return False, "INVALID_NAME"
            stack.append(value)

        elif token_type =="END":
            if not is_valid_tag_name(value):
                return False, "INVALID_NAME"
            if not stack:
                return False, "UNOPENED"
            if stack.pop() != value:
                return False, "NESTING"

    if stack:
        return False, "UNCLOSED"
    
    return True, ""

def get_error_message(error_type):
    """
    에러 타입에 따른 메시지 반환
    
    Args:
        error_type (str): 에러 타입
        
    Returns:
        str: 에러 메시지
    """
    # TODO: 여기에 코드를 작성하세요
    messages = {
        "EMPTY" : "empty input string",
        "PARSE" : "parse error",
        "INVALID_NAME" : "invalid tag name",
        "UNOPENED" : "no opening tag",
        "UNCLOSED" : "tag unclosed",
        "NESTING" : "wrong nesting tag"
    }

    return messages.get(error_type,"unknown error")
    # 힌트: 딕셔너리 사용
    


def is_yes(user_input):
    """
    Y 또는 Yes 입력 확인 (대소문자 무관)
    
    Args:
        user_input (str): 사용자 입력
        
    Returns:
        bool: Y 또는 Yes면 True
    """
    # TODO: 여기에 코드를 작성하세요
    return user_input.strip().lower() in ("y", "yes")


def is_no(user_input):
    """
    N 또는 No 입력 확인 (대소문자 무관)
    
    Args:
        user_input (str): 사용자 입력
        
    Returns:
        bool: N 또는 No면 True
    """
    # TODO: 여기에 코드를 작성하세요
    return user_input.strip().lower() in ("n", "no")


def main():
    """
    메인 함수
    
    규칙:
    - 사용자로부터 DOM 문자열 입력 받음
    - 검증 결과 출력
    - 재시작 여부 확인
    - 잘못된 입력 시 "Wrong Input" 출력
    """
    # TODO: 여기에 코드를 작성하세요
    while True:
        dom_string = input("\nInput DOM string: ")
        is_valid, error = validate_dom(dom_string)

        if is_valid:
            print("Result: Valid DOM structure")
        else: 
            if error =="EMPTY":
                print("Wrong Input")
            else:
                 print(f"Result: Invalid DOM structure - {get_error_message(error)} ")
    
        answer = input("\nValidate again ? (Y/N)")

        if is_yes(answer):
            continue
        elif is_no(answer):
            print("Program closing")
            break
        else:
            print("Wrong Input")


# ==================== 여기까지 코드를 작성하세요 ====================


# ==================== 테스트 코드 (수정하지 마세요) ====================
import pytest


class TestIsValidTagName:
    """is_valid_tag_name 함수 테스트"""
    
    def test_valid_single_letter(self):
        assert is_valid_tag_name("A") == True
        assert is_valid_tag_name("Z") == True
    
    def test_valid_multiple_letters(self):
        assert is_valid_tag_name("DIV") == True
        assert is_valid_tag_name("SPAN") == True
    
    def test_invalid_lowercase(self):
        assert is_valid_tag_name("div") == False
        assert is_valid_tag_name("Div") == False
    
    def test_invalid_with_numbers(self):
        assert is_valid_tag_name("A1") == False
        assert is_valid_tag_name("123") == False
    
    def test_invalid_empty(self):
        assert is_valid_tag_name("") == False


class TestTokenize:
    """tokenize 함수 테스트"""
    
    def test_simple_tag(self):
        tokens = tokenize("<A>text</A>")
        assert tokens == [("START", "A"), ("TEXT", "text"), ("END", "A")]
    
    def test_nested_tags(self):
        tokens = tokenize("<A><B>hi</B></A>")
        assert tokens == [("START", "A"), ("START", "B"), ("TEXT", "hi"), 
                          ("END", "B"), ("END", "A")]
    
    def test_multiple_root_tags(self):
        tokens = tokenize("<A>x</A><B>y</B>")
        assert len(tokens) == 6
        assert tokens[0] == ("START", "A")
        assert tokens[3] == ("START", "B")
    
    def test_invalid_missing_close_bracket(self):
        tokens = tokenize("<A>text")
        assert tokens is None
    
    def test_empty_text(self):
        tokens = tokenize("<A></A>")
        assert tokens == [("START", "A"), ("END", "A")]


class TestValidateDom:
    """validate_dom 함수 테스트"""
    
    def test_valid_simple(self):
        is_valid, error = validate_dom("<A>test</A>")
        assert is_valid == True
        assert error == ""
    
    def test_valid_nested(self):
        is_valid, error = validate_dom("<A><B>text</B></A>")
        assert is_valid == True
    
    def test_valid_multiple_roots(self):
        is_valid, error = validate_dom("<A>x</A><B>y</B>")
        assert is_valid == True
    
    def test_invalid_wrong_nesting(self):
        is_valid, error = validate_dom("<A><B></A></B>")
        assert is_valid == False
        assert error == "NESTING"
    
    def test_invalid_unclosed(self):
        is_valid, error = validate_dom("<A>text")
        assert is_valid == False
    
    def test_invalid_unopened(self):
        is_valid, error = validate_dom("</A>")
        assert is_valid == False
        assert error == "UNOPENED"
    
    def test_invalid_tag_name_lowercase(self):
        is_valid, error = validate_dom("<div>text</div>")
        assert is_valid == False
        assert error == "INVALID_NAME"
    
    def test_invalid_empty_string(self):
        is_valid, error = validate_dom("")
        assert is_valid == False
        assert error == "EMPTY"
    
    def test_valid_complex_nesting(self):
        is_valid, error = validate_dom("<A><B><C>deep</C></B></A>")
        assert is_valid == True
    
    def test_invalid_missing_close(self):
        is_valid, error = validate_dom("<A><B>text</B>")
        assert is_valid == False
        assert error == "UNCLOSED"


class TestGetErrorMessage:
    """get_error_message 함수 테스트"""
    
    def test_error_messages(self):
        assert "empty" in get_error_message("EMPTY").lower()
        assert "parse" in get_error_message("PARSE").lower() or "invalid" in get_error_message("PARSE").lower()
        assert "name" in get_error_message("INVALID_NAME").lower()
        assert "unclosed" in get_error_message("UNCLOSED").lower() or "not closed" in get_error_message("UNCLOSED").lower()
        assert "unopened" in get_error_message("UNOPENED").lower() or "not opened" in get_error_message("UNOPENED").lower()
        assert "nesting" in get_error_message("NESTING").lower() or "wrong" in get_error_message("NESTING").lower()


class TestIsYes:
    """is_yes 함수 테스트"""
    
    def test_yes_uppercase(self):
        assert is_yes("Y") == True
        assert is_yes("YES") == True
    
    def test_yes_lowercase(self):
        assert is_yes("y") == True
        assert is_yes("yes") == True
    
    def test_yes_mixedcase(self):
        assert is_yes("Yes") == True
        assert is_yes("yEs") == True
    
    def test_not_yes(self):
        assert is_yes("N") == False
        assert is_yes("NO") == False
        assert is_yes("Maybe") == False


class TestIsNo:
    """is_no 함수 테스트"""
    
    def test_no_uppercase(self):
        assert is_no("N") == True
        assert is_no("NO") == True
    
    def test_no_lowercase(self):
        assert is_no("n") == True
        assert is_no("no") == True
    
    def test_no_mixedcase(self):
        assert is_no("No") == True
        assert is_no("nO") == True
    
    def test_not_no(self):
        assert is_no("Y") == False
        assert is_no("YES") == False
        assert is_no("Maybe") == False


# pytest 실행을 위한 코드
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        main()
    else:
        pytest.main([__file__, "-v"])
