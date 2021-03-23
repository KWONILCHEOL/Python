# [S1]20055 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055

#include<cstdio>
#include<queue>
int a[200];
int check[200];
std::queue<int> q;
int main() {
	int n, m, ans, s = 0;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < (2 * n); i++)
		scanf("%d", &a[i]);

	for (ans = 1; m > 0; ans++) {
		//1. 벨트가 한 칸 회전한다.
 		s = (s - 1 + 2 * n) % (2 * n);
		
		//2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
		int size = q.size();
		for (int i = 0; i < size; i++) {
			int x = q.front();
            q.pop();
			
			////회전 시 로봇이 떨어지는 경우
			if (x == (s + n - 1) % (2 * n)) {
				check[x] = false;
				continue;
			}

			int nx = (x + 1) % (2 * n);
			//이동 가능
			if (a[nx] > 0 && check[nx] == false) {
				check[x] = false;
				a[nx]--;
				if (nx != (s + n - 1) % (2 * n)) {
					check[nx] = true;
					q.push(nx);
				}
				if (a[nx] == 0)
					m--;
			}
			//이동 불가
			else if(x != ((s + n - 1) % (2 * n)))
				q.push(x);
		}
		
		//3. 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
		if (a[s] > 0) {
			a[s]--;
			check[s] = true;
			q.push(s);
			if (a[s] == 0)
				m--;
		}
		if (m <= 0)
			break;
		//4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
	}
	printf("%d", ans);
}