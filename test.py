import pandas as pd

# 1. 기본 데이터셋 생성
data = {
    'Team': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B'],
    'Year': [2023, 2023, 2023, 2024, 2024, 2024, 2024, 2023],
    'Score': [80, 90, 85, 88, 92, 87, 75, 95]
}

df = pd.DataFrame(data)

print("--- 원본 데이터프레임 ---")
print(df)
print("\n")

# 2. GroupBy 기본 테스트

# 테스트 1: Team별 평균 점수 구하기
team_mean = df.groupby('Team')['Score'].mean()
print("--- 1. Team별 평균 점수 ---")
print(team_mean)
print("\n")

# 테스트 2: Year별 점수 합계 구하기
year_sum = df.groupby('Year')['Score'].sum()
print("--- 2. Year별 점수 합계 ---")
print(year_sum)
print("\n")

# 테스트 3: Team별로 묶은 뒤, 여러 통계량(평균, 최대, 최소) 한번에 보기 (agg 사용)
team_agg = df.groupby('Team')['Score'].agg(['mean', 'max', 'min', 'count'])
print("--- 3. Team별 점수 요약 통계 ---")
print(team_agg)
print("\n")

# 테스트 4: 두 개 이상의 컬럼으로 그룹화 (Team과 Year별 평균)
multi_group = df.groupby(['Team', 'Year'])['Score'].mean()
print("--- 4. Team 및 Year별 평균 점수 ---")
print(multi_group)
