# [kakao][2017][예선]카카오프렌즈 컬러링북
# https://programmers.co.kr/learn/courses/30/lessons/1829

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int dx[] = { 0,1,0,-1 };
int dy[] = { 1,0,-1,0 };
bool visit[100][100];
vector<int> solution(int m, int n, vector<vector<int>> picture) {
	int number_of_area = 0;
	int max_size_of_one_area = 0;

	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			visit[i][j] = false;

	vector<int> answer(2);
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (visit[i][j] || picture[i][j] == 0)
				continue;
			
			int value = picture[i][j];
			queue<pair<int, int>> q;
			q.push({ i,j });
			visit[i][j] = true;
			int cnt = 0;
			while (!q.empty()) {
				cnt++;
				int x = q.front().first;
				int y = q.front().second;
				q.pop();
				for (int d = 0; d < 4; d++) {
					int nx = x + dx[d];
					int ny = y + dy[d];
					if (nx < 0 || ny < 0 || nx == m || ny == n)
						continue;
					if (visit[nx][ny] || value != picture[nx][ny])
						continue;
					q.push({ nx,ny });
					visit[nx][ny] = true;
				}
			}

			number_of_area++;
			max_size_of_one_area = max_size_of_one_area > cnt ? max_size_of_one_area : cnt;
		}
	}
	answer[0] = number_of_area;
	answer[1] = max_size_of_one_area;
	return answer;
}

int main() {
	int m = 6;
	int n = 4;
	vector<vector<int>> picture;
	#pragma region picture
	vector<int> temp;
	temp.push_back(1);
	temp.push_back(1);
	temp.push_back(1);
	temp.push_back(0);
	picture.push_back(temp);
	temp.clear();
	temp.push_back(1);
	temp.push_back(2);
	temp.push_back(2);
	temp.push_back(0);
	picture.push_back(temp);
	temp.clear();
	temp.push_back(1);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(1);
	picture.push_back(temp);
	temp.clear();
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(1);
	picture.push_back(temp);
	temp.clear();
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(3);
	picture.push_back(temp);
	temp.clear();
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(3);
	picture.push_back(temp);
	#pragma endregion
	vector<int> answer = solution(m, n, picture);
	cout << answer[0] << "," << answer[1] << '\n';
}