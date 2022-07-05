## K-means 

### `1. K-means란?`
- 군집분석의 방법 중 하나
- 중심점의 개수(k개)를 설정하고 비슷한 거리에 있는 개체끼리 군집화 함
- 계산과정이 비교적 간단하기 때문에 안정적인 성능을 보이며 큰 집단의 군집화에 적합함

** 과정
1. k 개의 군집 대표 벡터 (centroids) 를 데이터의 임의의 k 개의 점으로 선택
2. 모든 점에 대하여 가장 가까운 centroid 를 찾아 cluster label 을 부여
3. 같은 cluster label 을 지닌 데이터들의 평균 벡터를 구하여 centroid 를 업데이트
4. 2,3 의 과정을 label 의 변화가 없을때까지 반복.

### `2. K-means 구현`
```
from sklearn.cluster import KMeans
```
[시각화]

![Figure 2021-08-15 173706](https://user-images.githubusercontent.com/57973170/129478844-6e2ea627-6820-4355-9639-5c38e1220fa0.png)


### `3. K-means 성능 평가`
- PCA후 시각화로 Cluster를 나타내어 시각적으로 확인가능
- Silhouette Score : 각 군집간의 거리가 효율적으로 나눠져 있는지 평가
```
from sklearn.metrics import silhouette_score ,silhouette_samples
```
![image](https://user-images.githubusercontent.com/57973170/129478811-f996ac2f-adaf-4cf5-8fcf-df0db5037f66.png)

** 사용한 데이터는 project153 레퍼지토리에 있음 8.15 현재 비공개지만 프로젝트 마무리된 후 공개예정 

