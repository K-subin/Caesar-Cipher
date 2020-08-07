# Caesar-Cipher
- 시저암호 암호화, 복호화 라이브러리 구현
- 시저암호 실행 코드 구현
- 메세지의 영어단어 비율 구하는 코드 구현
- 시저암호 공격 구현

## 시저암호 구조

- key = 3

![640px-Caesar3 svg](https://user-images.githubusercontent.com/68969252/89425190-a654af00-d773-11ea-86b1-f26fd9f93b46.png)


## 실행결과
### caesarcipher_lib.py 실행결과

시저암호 암호화, 복호화 라이브러리 구현

![시저](https://user-images.githubusercontent.com/68969252/89425465-0186a180-d774-11ea-99ab-cba36b4e2a2d.PNG)

- key = 3

![10](https://user-images.githubusercontent.com/68969252/89425802-62ae7500-d774-11ea-865d-25ce92dcd413.PNG)

- key = 10

### run_caesarcipher.py 실행결과

- 입출력을 통해 txt파일 받아오기
- caesarcipher_lib.py를 이용해 암호화, 복호화 실행하기 ( key = 13 )

![실행](https://user-images.githubusercontent.com/68969252/89431973-89bc7500-d77b-11ea-8b8d-2cdc07702134.PNG)


### EngDic_lib.py 실행결과

- 시저암호 전수조사 공격을 하기 위해 영어사전을 이용해서 메세지의 영어단어의 비율 구하기

![영단어](https://user-images.githubusercontent.com/68969252/89655628-59a0dd80-d905-11ea-98bf-bd00e6dcf5ad.PNG)


### break_caesarcipher.py 실행결과

- 시저암호로 암호화 된 txt 파일 받아오기
- key를 0부터 26까지 하나씩 복호화해보며 전수조사 하기
- EngDic_lib.py를 통해 복호화 한 메세지의 영어단어 비율이 가장 높은 key 찾기

![시저암호공격](https://user-images.githubusercontent.com/68969252/89655682-6c1b1700-d905-11ea-860f-7e61b21850bc.PNG)
