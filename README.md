# 🎬 영화 관객수 예측 경진대회
## 소개
주어진 데이터를 바탕으로 영화의 관객수를 예측 모델 개발 프로젝트<br/><br/>
<img width="1250" alt="스크린샷 2022-12-29 오전 12 10 07" src="https://user-images.githubusercontent.com/108471861/209832549-9ba2aa32-2958-4f67-a6eb-5c8ce5e7add2.png">
## 데이터
|순번|데이터|구성|             
|:-:|:-------:|:------:|          
|1|train.csv|(600행 X 12열)<br/>title : 영화의 제목<br/>distributor : 배급사<br/>genre : 장르<br/>release_time : 개봉일<br/>time : 상영시간(분)<br/>screening_rat : 상영등급<br/>director : 감독이름<br/>dir_prev_bfnum : 해당 감독이 이 영화를 만들기 전 제작에 참여한 영화에서의 평균 관객수(단 관객수가 알려지지 않은 영화 제외)<br/>dir_prev_num : 해당 감독이 이 영화를 만들기 전 제작에 참여한 영화의 개수(단 관객수가 알려지지 않은 영화 제외)<br/>num_staff : 스텝수<br/>num_actor : 주연배우수<br/>box_off_num : 관객수|                       
|2|test.csv|(243행 X 11열)<br/>title : 영화의 제목<br/>distributor : 배급사<br/>genre : 장르<br/>release_time : 개봉일<br/>time : 상영시간(분)<br/>screening_rat : 상영등급<br/>director : 감독이름<br/>dir_prev_bfnum : 해당 감독이 이 영화를 만들기 전 제작에 참여한 영화에서의 평균 관객수(단 관객수가 알려지지 않은 영화 제외)<br/>dir_prev_num : 해당 감독이 이 영화를 만들기 전 제작에 참여한 영화의 개수(단 관객수가 알려지지 않은 영화 제외)<br/>num_staff : 스텝수<br/>num_actor : 주연배우수|
        
## 링크
Link: [Dacon_영화 관객수 예측 경진대회][Daconlink]

[Daconlink]: https://dacon.io/competitions/open/235536/overview/description
