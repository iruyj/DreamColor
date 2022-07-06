#Dream Color

---
### About it
   - 자신이 꾼 꿈을 컬러로 기록하며, 꿈 키워드로 해몽 및 다른 사람들의 꿈 이야기를 볼 수 있는 웹사이트
   - 하루의 시작인 꿈을 색깔로서 쌓아나가기 위해 계획하였다.


###Main Effect
   1. 꿈을 색깔로 표시하면서 그날의 꿈을 더 자세히 기억할 수 있다.
   2. 꿈을 꾼 후에 어떤 의미를 가진 꿈인지 관련 내용을 찾아볼 수 있다.
   3. 다른 사람들의 꿈 내용을 읽으면서 재밌는 시간을 보낼 수 있다.

###installed packages
| package | purpose |
|---|:---:|
| `Django` | 장고 프레임워크 |
| `beautifulsoup4` | 웹 크롤링 |
| `Konlpy` | 키워드 분석 | 
| `Markdown` | 마크다운 문법 사용 |

###Execution method
      
   1. 회원가입
      1. nav바에 있는 회원가입 버튼을 클릭하여 회원가입을 한다.
         - 비밀번호 8자 이상, 아이디와 비밀번호는 서로 다르게 설정
      2. 로그인 한다.


   2. 게시물 작성&수정
      1. 메인화면에서 '글 작성하기'를 클릭하여 나의 꿈 이야기와 색을 작성한다.
      2. 마이페이지로 이동하여 나의 프로필과 내가 작성한 글을 확인할 수 있다.
      3. 만약, 나의 게시글을 수정하거나 삭제하고 싶다면 나의 게시물을 클릭하여 수정할 수 있다.


   3. 게시물 확인&검색
      1. 메인 화면에서 다른 사람들이 작성한 게시글들을 확인할 수 있다.
      2. 검색창을 클릭하면 제목을 검색할 수 있고 인기 색상을 선택하여 게시물을 볼 수 있다.
      3. 제목을 검색하거나 색상을 선택하면 메인페이지 아래에 원하는 게시물을 확인할 수 있다.


###Route
| url | template |
|---|:---:|
| `''` | main.html |
| `account/login` | login.html |
| `account/signup` | signup.html | 
| `account/mypage` | mypage.html |
| `dream/create` | new.html |
| `dream/search` | search.html |
| `dream/{index}` | view.html | 
| `dream/modify/{index}` | modify.html |



