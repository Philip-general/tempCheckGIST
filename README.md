# 오토 체온체크 사용법 

zeus id와 pw만 입력해두면 12시간마다 자동으로 자가건강검진에 접속해 36~37도의 랜덤한 체온으로 입력해줌
일단 윈도우만 되게 만들어놨는데 맥 버전 필요하면 말하셈

체온체크.exe 는 dist 폴더 안에 있다.

## Chrome Driver 설치
	
	1.
	  크롬을 조작해서 접속하는거라 지금 쓰고 있는 Chrome Driver를 깔아야 해
	  크롬 들어가서,

  	  chrome://version/

  	  입력하면 가장 윗줄에 크롬 버전이 뜰꺼야. 참고로 내꺼는 밑처럼 나오네
	  ex) 93.0.4577.63 (공식 빌드) (64비트) (cohort: Stable)

	  여기서 가장 앞 숫자인 93이 중요한거임

	2.
	  https://chromedriver.chromium.org/downloads 접속

	  들어가면 Current Releases 라고 크롬 드라이버 다운로드 받을 수 있음.
	  나같은 경우는 93을 쓰고 있으니까,
	  
	  ChromeDriver 93.0.4577.15  =>  chromedriver_win32.zip
	  
	  클릭해서 다운로드 하면 됨
	  
	3. 
	  그 zip 파일을 C 드라이브 들어가서 바로 압축해제 해
	  
	  chromedriver.exe

	  가 생겼다면 성공이야.
	  ** chromedriver 폴더가 있으면 안되고 압축해제 폴더 안에 있는 chromedriver.exe가 C드라이브 안에 있어야 함

## 체온체크.exe 실행

	1. 눌러서 실행하기

	2. 실행하면 콘솔 창 열림

	3. zeus id, pw 입력하기

	4. 최초 실행시 한 번 체온측정이 바로 되는데 액세스 권한이 필요하다고 뜨면 허용해주고 잘 되는지 확인하기 (크롬 창은 가만히 두면 알아서 꺼진다.)

	5. 콘솔창 내려놓고 그냥 살면 알아서 12시간마다 체온측정 해준다.
