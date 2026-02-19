"""
코딩 테스트 문제 9: 숫자 야구 게임

문제 설명:
컴퓨터가 생성한 3자리 숫자를 맞추는 게임을 작성하시오.

게임 규칙:
1. 컴퓨터는 중복되지 않는 3자리 숫자를 생성 (100~999)
2. 사용자가 3자리 숫자를 입력
3. 숫자와 위치가 모두 맞으면 1 Strike
4. 숫자는 맞지만 위치가 다르면 1 Ball
5. 3 Strike가 나오면 게임 종료

실행 예시:
$ python baseball_test.py
===== 숫자 야구 게임 시작! =====
컴퓨터가 숫자를 생성했습니다. (디버그: 472)

Input guess number (0 to exit): 123
Result: 0 Strike, 1 Ball

Input guess number (0 to exit): 472
Result: 3 Strike!
축하합니다! 정답을 맞추셨습니다!

다시 하시겠습니까? (Y/N): N
게임을 종료합니다.

판정 예시:
컴퓨터: 472
사용자: 123 → 0 Strike, 1 Ball (2가 위치 다름)
사용자: 547 → 0 Strike, 2 Ball (4, 7 위치 다름)
사용자: 247 → 0 Strike, 3 Ball (모두 위치 다름)
사용자: 742 → 1 Strike, 2 Ball (7 위치 맞음)
사용자: 472 → 3 Strike (정답!)

입력 검증:
1. 숫자가 아닌 문자 입력 시 → Wrong Input
2. 실수 입력 시 → Wrong Input
3. 100 미만 또는 999 초과 시 → Wrong Input
4. 중복 숫자 입력 시 (예: 112, 333) → Wrong Input

게임 재시작:
- "Y" 또는 "Yes" 입력 (대소문자 무관) → 게임 재시작
- "N" 또는 "No" 입력 (대소문자 무관) → 게임 종료
- 기타 입력 → Wrong Input 후 재입력

종료 조건:
- 게임 중 0 입력 시 즉시 종료

요구사항:
1. get_random_number() - 100~999 랜덤 숫자 반환 (제공됨)
2. is_digit(user_input_str) - 정수로 변환 가능한지 확인
3. is_between_100_and_999(user_input_str) - 100~999 범위 확인
4. is_duplicated_number(three_digit_str) - 중복 숫자 확인
5. is_validated_number(user_input_str) - 전체 검증
6. get_not_duplicated_three_digit_number() - 중복 없는 3자리 생성
7. get_strikes_or_balls(user_input, random_number) - Strike/Ball 판정
8. is_yes(one_more_input) - Y/Yes 확인
9. is_no(one_more_input) - N/No 확인
10. main() - 메인 함수
"""

import random

# ==================== 제공되는 Helper 함수 ====================

def get_random_number():
    """100~999 사이의 랜덤 숫자 반환"""
    return random.randint(100, 999)


# ==================== 여기서부터 코드를 작성하세요 ====================

def is_digit(user_input_str):
    """
    문자열이 정수로 변환 가능한지 확인
    
    Args:
        user_input_str (str): 사용자 입력
        
    Returns:
        bool: 정수로 변환 가능하면 True
    """
    # TODO: 여기에 코드를 작성하세요
    try:
        int(user_input_str)
        return True
    except:
        return False
    # 힌트: try-except 또는 isdigit() 사용
    


def is_between_100_and_999(user_input_str):
    """
    100 이상 1000 미만인지 확인
    
    Args:
        user_input_str (str): 정수 형태의 문자열
        
    Returns:
        bool: 100 이상 1000 미만이면 True
    """
    # TODO: 여기에 코드를 작성하세요
    return 100 <= int(user_input_str) < 1000


def is_duplicated_number(three_digit_str):
    """
    3자리 숫자에 중복이 있는지 확인
    
    Args:
        three_digit_str (str): 3자리 숫자 문자열
        
    Returns:
        bool: 중복이 있으면 True
    """
    # TODO: 여기에 코드를 작성하세요
    return (
        three_digit_str[0] == three_digit_str[1]
        or three_digit_str[0] == three_digit_str[2]
        or three_digit_str[1] == three_digit_str[2]
    )
    # 힌트: 각 자릿수를 비교
    


def is_validated_number(user_input_str):
    """
    유효한 입력인지 종합 검증
    
    조건:
    1. 숫자여야 함
    2. 100 이상 1000 미만
    3. 중복 숫자 없어야 함
    
    Args:
        user_input_str (str): 사용자 입력
        
    Returns:
        bool: 모든 조건 만족 시 True
    """
    # TODO: 여기에 코드를 작성하세요
    return (
        is_digit(user_input_str) and is_between_100_and_999(user_input_str)
        and not is_duplicated_number(user_input_str)
    )
    # 힌트: 위의 세 함수를 활용


def get_not_duplicated_three_digit_number():
    """
    중복되지 않는 3자리 숫자 생성
    
    Returns:
        int: 중복 없는 3자리 정수
    """
    # TODO: 여기에 코드를 작성하세요
    while True:
        number = get_random_number()
        if len(set(str(number))) == 3: 
            return number
    # 힌트: get_random_number()를 반복 호출하여 중복 없을 때까지


def get_strikes_or_balls(user_input, random_number):
    """
    Strike와 Ball 개수 계산
    
    Args:
        user_input (str): 사용자 입력 3자리 문자열
        random_number (str): 컴퓨터 숫자 3자리 문자열
        
    Returns:
        list: [strikes, balls]
    """
    # TODO: 여기에 코드를 작성하세요
    strike = 0 
    ball = 0 

    for i in range(3):
        if user_input[i] == random_number[i]:
            strike += 1 
        elif user_input[i] in random_number:
            ball += 1
    
    return [strike, ball]
    # 힌트: 각 자리를 비교하여 strike/ball 판정


def is_yes(one_more_input):
    """
    Y 또는 Yes 입력 확인 (대소문자 무관)
    
    Args:
        one_more_input (str): 사용자 입력
        
    Returns:
        bool: Y 또는 Yes면 True
    """
    # TODO: 여기에 코드를 작성하세요
    return one_more_input.lower() in ("y", "yes")


def is_no(one_more_input):
    """
    N 또는 No 입력 확인 (대소문자 무관)
    
    Args:
        one_more_input (str): 사용자 입력
        
    Returns:
        bool: N 또는 No면 True
    """
    # TODO: 여기에 코드를 작성하세요
    return one_more_input.lower() in ("n", "no")

def main():
    """
    메인 함수
    
    규칙:
    - 게임 시작 시 랜덤 숫자 생성 및 출력
    - 0 입력 시 즉시 종료
    - 3 Strike 시 게임 재시작 여부 확인
    - 잘못된 입력 시 "Wrong Input" 출력
    """
    # TODO: 여기에 코드를 작성하세요
    print ("Game Start!")
    random_num = str(get_not_duplicated_three_digit_number())
    print(f"{random_num}")

    while True: 
        user_input = input("Input Number:").strip()

        if user_input == "0":
            print ("Game Over")
            return

        if not is_validated_number(user_input):
            print ("Wrong Input")
            continue

        strike, ball = get_strikes_or_balls(user_input, random_num)

        if strike == 3: 
            print (" 3 Strike ! ")

            while True: 
                again = input("play again? (y/n):").strip()
                if is_yes(again):
                    main()
                    return
                if is_no(again):
                    print("Game Over")
                    return 
                else: 
                    print("Wrong Input")
        else:
            print(f"result : {strike} strike, {ball}ball")



# ==================== 여기까지 코드를 작성하세요 ====================


# ==================== 테스트 코드 (수정하지 마세요) ====================
import pytest
from io import StringIO
import sys


class TestIsDigit:
    """is_digit 함수 테스트"""
    
    def test_valid_digit(self):
        assert is_digit("123") == True
        assert is_digit("456") == True
    
    def test_invalid_digit(self):
        assert is_digit("abc") == False
        assert is_digit("12.3") == False
        assert is_digit("1a2") == False


class TestIsBetween100And999:
    """is_between_100_and_999 함수 테스트"""
    
    def test_valid_range(self):
        assert is_between_100_and_999("100") == True
        assert is_between_100_and_999("500") == True
        assert is_between_100_and_999("999") == True
    
    def test_invalid_range(self):
        assert is_between_100_and_999("99") == False
        assert is_between_100_and_999("1000") == False
        assert is_between_100_and_999("50") == False


class TestIsDuplicatedNumber:
    """is_duplicated_number 함수 테스트"""
    
    def test_duplicated(self):
        assert is_duplicated_number("112") == True
        assert is_duplicated_number("333") == True
        assert is_duplicated_number("121") == True
    
    def test_not_duplicated(self):
        assert is_duplicated_number("123") == False
        assert is_duplicated_number("456") == False
        assert is_duplicated_number("789") == False


class TestIsValidatedNumber:
    """is_validated_number 함수 테스트"""
    
    def test_valid_number(self):
        assert is_validated_number("123") == True
        assert is_validated_number("456") == True
    
    def test_invalid_not_digit(self):
        assert is_validated_number("abc") == False
    
    def test_invalid_out_of_range(self):
        assert is_validated_number("99") == False
        assert is_validated_number("1000") == False
    
    def test_invalid_duplicated(self):
        assert is_validated_number("112") == False
        assert is_validated_number("333") == False


class TestGetNotDuplicatedThreeDigitNumber:
    """get_not_duplicated_three_digit_number 함수 테스트"""
    
    def test_generate_number(self):
        """10번 생성하여 모두 유효한지 확인"""
        for _ in range(10):
            number = get_not_duplicated_three_digit_number()
            assert 100 <= number < 1000
            number_str = str(number)
            # 중복 확인
            assert len(set(number_str)) == 3


class TestGetStrikesOrBalls:
    """get_strikes_or_balls 함수 테스트"""
    
    def test_all_strikes(self):
        result = get_strikes_or_balls("472", "472")
        assert result == [3, 0]
    
    def test_all_balls(self):
        result = get_strikes_or_balls("247", "472")
        assert result == [0, 3]
    
    def test_mixed(self):
        result = get_strikes_or_balls("742", "472")
        assert result == [1, 2]
    
    def test_no_match(self):
        result = get_strikes_or_balls("123", "456")
        assert result == [0, 0]
    
    def test_one_ball(self):
        result = get_strikes_or_balls("123", "472")
        assert result == [0, 1]


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


class TestIsNo:
    """is_no 함수 테스트"""
    
    def test_no_uppercase(self):
        assert is_no("N") == True
        assert is_no("NO") == True
    
    def test_no_lowercase(self):
        assert is_no("n") == True
        assert is_no("no") == False
    
    def test_no_mixedcase(self):
        assert is_no("No") == True
        assert is_no("nO") == True
    
    def test_not_no(self):
        assert is_no("Y") == False
        assert is_no("YES") == False


class TestMainFunction:
    """main 함수 통합 테스트"""
    
    def test_main_exit_immediately(self, monkeypatch, capsys):
        """0 입력 시 즉시 종료"""
        monkeypatch.setattr('sys.stdin', StringIO('0\n'))
        main()
        captured = capsys.readouterr()
        assert "야구" in captured.out or "Baseball" in captured.out.lower()
    
    def test_main_wrong_input_letters(self, monkeypatch, capsys):
        """문자 입력 시 에러"""
        monkeypatch.setattr('sys.stdin', StringIO('abc\n0\n'))
        main()
        captured = capsys.readouterr()
        assert "Wrong Input" in captured.out or "wrong" in captured.out.lower()
    
    def test_main_wrong_input_duplicated(self, monkeypatch, capsys):
        """중복 숫자 입력 시 에러"""
        monkeypatch.setattr('sys.stdin', StringIO('112\n0\n'))
        main()
        captured = capsys.readouterr()
        assert "Wrong Input" in captured.out or "wrong" in captured.out.lower()


# pytest 실행을 위한 코드
if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        pytest.main([__file__, "-v"])
