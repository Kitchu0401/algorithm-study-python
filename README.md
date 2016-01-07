# 개요
본 저장소는 파이썬 알고리즘 연구회를 위한 저장소입니다.  
*제출일자(YYYYMMDD)*/*Dovelet제출ID*/*문제명*.py 형식을 준수해주세요. :)  
폴더는 모두 Python Package가 아닌, Directory입니다!
( 주석 첨부 여부는 자율입니다. )

## 설정가이드
**본 설정가이드는 PyCharm Community Edition 5.0.1 버전을 기준으로 합니다.**  
커맨드라인 등에서 직접 git 명령어로 push/pull 하셔도 무관합니다.  
단, **.idea 폴더 아래의 파일은 반드시 커밋에서 제외**해주세요.

**Git이 사전에 설치되어있어야합니다.**  
https://git-scm.com/book/ko/v1/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%84%A4%EC%B9%98#윈도에-설치  
https://rogerdudler.github.io/git-guide/index.ko.html  
등의 페이지를 참고하셔서 Git을 미리 설치해주세요.

#### 1. 프록시 환경변수 설정
- 윈도우 시작 - 컴퓨터 우클릭 - 속성을 클릭합니다.
- 좌측 고급 시스템 설정을 클릭합니다.
- 아래 환경 변수를 클릭합니다.
- 변수명 "https_proxy"로 해당하는 값을 등록해줍니다.

#### 2. PyCharm Git Plugin 설치
- 상단 File탭 - Settings를 클릭합니다.
- 좌측 Plugins를 클릭하여 우측 목록에서 Git Integration, Github 설치여부를 확인해주세요.  
( 제 경우는 플러그인이 모두 설치된 상태였는데, 만약 아니라면 설치해주시면 됩니다. )

#### 3. Gitignore 추가
- 상단 File탭 - Settings를 클릭합니다.
- 좌측 Version Control 아래 Ignored files를 클릭합니다.
- 목록 우측 상단의 녹색 화살표를 클릭합니다.
- 라디오 버튼 두 번째 Ignore all files under: 를 클릭한 후, .idea/를 입력하고 추가합니다.
- Directory: .idea/ 항목이 추가되었는지 확인합니다.

#### 4. 프로젝트 Clone
- 상단 VCS탭 - Checkout from version control - Git을 클릭합니다.
- Git Repository URL에 본 저장소의 url을 입력합니다. ( https://github.com/Kitchu0401/algorithm-study-python.git )
- Parent Directory는 프로젝트를 clone할 부모 디렉토리를, Directory Name은 프로젝트 이름을 편한대로 넣어줍니다.  
예) Parent Directory: C:\Users\SDS\PycharmProjects, Directory Name: algorithm-study-python
- Clone을 클릭하여 작업을 완료합니다.

#### 5. 프로젝트 pull & commit - push
- 기본적인 git의 프로세스는 상단 VCS탭 - Git을 클릭하여 수행할 수 있습니다.
- 폴더를 나누어놓아 소스가 엉킬 일은 거의 없을겁니다만, **작업 전 항시 Pull을 먼저 받아주세요.**
- 코드를 작성 후 우클릭 - Git - Commit File을 클릭하여 Commit만 한 후 상단 VCS탭 - Git에서 일괄적으로 Push 하거나,
- 우클릭 - Git - Commit File에서 Commit 버튼에 마우스를 올려놓으면 Commit and Push를 선택할 수 있습니다.
