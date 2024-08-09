import sys

def sys_module():
    # argv 속성: 명령형에서 넘어온 인수
    print(sys.argv)

    args = sys.argv[1:] # 스크립트를 제외한 인수
    print("명령행 인수:", args)

    # 시스템 관련 정보
    print("Platform:", sys.platform) # 플랫폼 정보
    print("Version:", sys.version)  # 버전 정보

    # 파이썬은 모듈을 검색할때 sys.path 에 등록된 디렉토리를 대상으로 검색
    print("모듈 검색 경로:", sys.path)
    # 찾는 모듈이 sys.path에 없을 경우 append해주기
    # sys.path.append("추가할 모듈 경로")

def regex_ex():
    """
    정규표현식 예제
    """
    import re

    namecard = """
    Email: hong@hwalvin.org
    Phone: 010-1234-5678
    
    Email: gildong@dooly.net
    Phone: 010-4352-6435
    
    Email: qwerty@example.com
    Phone: 010-6342-5634
    """

    emaillist = re.findall(r"\w+[\w\.]*@\w+[\w\.]\.[a-z]+", namecard)
    print(emaillist)

    phonelist = re.findall(r"[0-9]{3}-[0-9]{4}-[0-9]{4}",namecard)
    print(phonelist)


def random_ex():
    import random

    random.seed(42) # 난수 계산을 위한 기초 값

    print(random.random()) # 0-1의 난수
    print(random.randint(1,6)) # 1-6사이의 정수,난수
    print(random.randrange(101)) # 0-100 사이의 난수
    print(random.randrange(1,101,3)) # 1-100 사이의 3간격 수 중에서 난수

    # 순차형에 무작위성을 추가하는 부가 기능들
    seqvar = ["짬뽕", "짜장면", "짬짜면", "마라탕"]
    print("seqvar:", seqvar)
    random.shuffle(seqvar)
    print("shuffle:", seqvar)
    print(random.choice(seqvar))

    # 샘플링
    for i in range(5):
        print(random.sample(range(1,101),10))


if __name__ == "__main__":
    #sys_module()
    #regex_ex()
    random_ex()



