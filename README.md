# 📄 문장 유형 분류 AI 경진대회
## 소개
문장 유형 분류 AI 모델 개발 프로젝트<br/><br/>
<img width="1256" alt="스크린샷 2022-12-28 오후 11 50 16" src="https://user-images.githubusercontent.com/108471861/209829915-1a63d497-1be6-48ab-ac16-11532688db8d.png">
## 데이터
|순번|데이터|구성|             
|:-:|:-------:|:------:|          
|1|train.csv|(1000행 X 28열)<br/>ID : 부여번호<br/>img_path : 각 ID에 매핑되는 학습용 유방암 병리 슬라이드 영상 파일 경로<br/>mask_path : 각 ID에 매핑되는 학습용 유방암 병리 슬라이드 영상에 해당하는 어노테이션 마스크 파일 경로<br/>N_category : 임파선(림프절) 전이 여부 (0, 1)|                       
|2|test.csv|(250행 X 26열)<br/>ID : 부여번호<br/>img_path : 각 ID에 매핑되는 학습용 유방암 병리 슬라이드 영상 파일 경로|
|3|train_imgs|1000개<br/>각 ID에 매핑되는 학습용 유방암 병리 슬라이드 영상 (png)|                       
|4|train_masks|58개<br/>각 ID에 매핑되는 학습용 유방암 병리 슬라이드 영상에 해당하는 어노테이션 마스크<br/>학습 유방암 병리 슬라이드 영상 중 일부만 존재|
|5|test_imgs|250개<br/>각 ID에 매핑되는 추론용 유방암 병리 슬라이드 영상 (png)|           
## 링크
Link: [Dacon_유방암의 임파선 전이 예측 AI 경진대회][Daconlink]

[Daconlink]: https://dacon.io/competitions/official/236011/overview/description
