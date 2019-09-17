## Chapter 1.1 Adjacency Matrix 인접행렬

인접행렬은 인접리스트와 같이 그래프를 저장하고 탐색할 수 있도록 도와주는 하나의 자료구조이다. 보통 배열을 사용해서 그래프의 정보를 저장한다. 최근 SNS의 인기에 따라서 소셜 네트워크를 분석하는 데 많이 쓰이는 도구 중 하나이다. Chapter 1에서는 인접행렬과 인접리스트를 다룬다.

아래에 나오는 그래프는 모두 Directed Graph로써, 방향성을 갖추고 있다. 보통 그래프로 표현하지만, matrix 형태로 표현할 수도 있다.

2차원 배열의 특성상 공간복잡도가 ![](https://t1.daumcdn.net/cfile/tistory/21473C4C56AF54680D) 이므로 정점의 수가 많을 경우 인접행렬을 사용한다면 메모리의 낭비가 문제가 될 수 있다.

한 번에 이동하여 갈 수 있는 거리를 **hop**이라고 부른다. 정확히는 1회 이동으로 갈 수 있는 거리를 **1 hop**라고 일컫는다. 대부분의 인접행렬의 탐색은 시간복잡도도 ![](https://t1.daumcdn.net/cfile/tistory/21473C4C56AF54680D)이다. ***n hops*** 만큼 가서 도달할 수 있는 path의 거리도 matrix의 곱셈에 따라서 A의 n승이라고 볼 수 있다.

인접행렬의 구성을 그림으로 살펴보자. 여기서 행은 출발하는 노드(matrix.py에는 vertexfrom이라고 변수를 선언했다)이고, 열은 도착하는 노드(matrix.py에는 vertexto)이다.

![](https://t1.daumcdn.net/cfile/tistory/2615F83D56AF573315)

1행과 1열은 정점의 번호를 의미하며 나머지 칸의 0은 연결되지 않음을 의미하고 1은 연결되어 있음을 의미한다. 

이 부분은 파이썬 코드로 구현하여 matrix.py로 레포에 올려두었으니 확인하기를 바란다.

### 무방향 무가중치 그래프의 입력과 출력

  

2차원 배열을 만들면 2차원 배열의 그래프의 구조는 다음과 같다.

* vertex(정점의 수) = 6, edge(간선의 수) = 8

* 간선들 1-2, 1-3, 2-3, 2-4, 3-4, 3-5, 4-5, 4-6

![](https://t1.daumcdn.net/cfile/tistory/2648384156AF59DE0E)

### 무방향 가중치 그래프의 입력과 출력

가중치는 어떻게 표현할까? 하는 고민을 하게 되는데 우리는 연결되어 있음을 의미하는 1이 아니라 가중치를 저장하면 된다. 즉, 2-3 간선의 가중치가 3이라면 1이아니라 3을 저장하는 것이다.

그래프의 구조는 다음과 같다. vertex(정점의 수) = 5, edge(간선의 수) = 6

간선들 1-2(1) , 4-1(5), 2-3(3), 5-2(2),3-5(4),4-5(6)

![](https://t1.daumcdn.net/cfile/tistory/2364234456AE272804)

### n hops로 갈 수 있는 거리 살펴보기
```python
>>> import numpy as np

## Adjacency matrix
>>> A = np.array([[0,1,1,1,0],[0,0,1,0,0],[0,1,0,0,0],[0,0,0,1,0],[0,1,0,0,0]])
>>> print A
[[0 1 1 1 0]
 [0 0 1 0 0]
 [0 1 0 0 0]
 [0 0 0 1 0]
 [0 1 0 0 0]]

## A^2를 구해서 2 hops만에 도달할 수 있는 경우의 수
>>> A2 = A.dot(A)
>>> print A2
[[0 1 1 1 0]
 [0 1 0 0 0]
 [0 0 1 0 0]
 [0 0 0 1 0]
 [0 0 1 0 0]]
```

결과를 분석해보자. 우선 A2에서 1번 노드를 살펴보자. A2는 A의 2승을 하였으므로, 2번 만에 도달할 수 있는 경우의 수를 의미한다. 2, 3, 4번 노드가 ***2 hop*** 임을 알 수 있다. 다음의 케이스를 고려해볼 수 있다.

* 1->2로 갈 때, 1->3->2의 ***2 hop*** 인 경우의 수
* 1->3로 갈 때, 1->2->3의 ***2 hop*** 인 경우의 수
* 1->4로 갈 때, 1->4->4의 ***2 hop*** 인 경우의 수 (단, self-loop)

따라서, 우리는 **어느 network에서  (n x n) hops를 거쳐서 도달할 수 있는 노드들은  (A의 n승) x (A의 n승)을 통해 알 수 있다**는 결론에 이른다.

### Reachability Matrix
새로운 질문을 던져보자. 특정한 노드에 ***n hops*** 이내에 도착할 수 있는 지 물어본다고 치자. 위의 방식은 사용할 수 없는데, 그 이유는 정확히 ***n hops*** 에 도달하는 경우의 수를 상정하였기 때문이다.

n개의 노드와 출발 노드 간의 거리를 가장 멀리 배치하는 방법은 바로 일렬로 배치하는 것이다. 그래프 이론에서 [도달 가능성]([https://en.wikipedia.org/wiki/Reachability](https://en.wikipedia.org/wiki/Reachability))은 그래프 내부 하나의 꼭짓점에서 다른 하나의 꼭짓점으로 도달할 수 있는 가능성을 일컫는다.

N개의 노드에서 출발 노드를 제외한 n-1개의 노드를 일렬로 배치한다고 할 때, A의 1승부터 A의 (n-1)승까지 모두 or 조건을 걸어버리면 된다. **하나만 만족하면 1로 처리한다는 뜻이다.**

```python
>>> n = 5
>>> An = A
>>> R = A
>>> for i in range(2, n):
...     An = An.dot(A)
...     R += An
>>> R = 1*(R>0)
>>> print R
[[0 1 1 1 0]
 [0 1 1 0 0]
 [0 1 1 0 0]
 [0 0 0 1 0]
 [0 1 1 0 0]]
```
사실 파이썬에는 [NetworkX]([https://networkx.github.io/](https://networkx.github.io/))라는 재미있는 패키지가 있다. 아직 사용해보지는 않았는데, Reachability를 파악해주는 강력한 기능도 포함되어 있다고 한다. 이 책을 보면서 해당 라이브러리를 쓸 즈음이 있을 때 사용법을 한 번 포스팅하도록 하겠다.

### 정리

- 인접행렬은 간단한 그래프를 표현하기에 적합하며 탐색도 비교적 손쉽게 가능하다. 하지만 시간과 공간복잡도가 비효율적이므로 사용에 주의가 필요하다.

- 인접행렬의 구현목적은 그래프의 탐색에 있다. 인접행렬을 통해서 깊이 또는 너비 우선 탐색 구현 연습을 많이 해보기를 추천한다.

- 인접리스트와 비교하여 상황에 적합한 자료구조를 선택하여 사용해야 한다. 네트워크 이론에서 많이 쓰이며, Chapter 1의 Food Web에서도 많이 강조된다.

  
  
### Reference
 [https://lasthere.tistory.com/15](https://lasthere.tistory.com/15) 
 [http://ddmix.blogspot.com/2015/06/cppalgo-22-directed-graph.html](http://ddmix.blogspot.com/2015/06/cppalgo-22-directed-graph.html)
 [https://smlee729.github.io/python/network%20analysis/2015/03/31/1-reachability.html](https://smlee729.github.io/python/network%20analysis/2015/03/31/1-reachability.html)
 [https://frhyme.github.io/python-libs/check_reachability_in_graph/](https://frhyme.github.io/python-libs/check_reachability_in_graph/)