"""학생 점수 처리 모듈

이 모듈은 학생 점수 리스트를 분석하고 통계 정보를 제공합니다.
"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ScoreAnalysis:
    """점수 분석 결과를 담는 데이터 클래스"""
    total_count: int
    pass_count: int
    fail_count: int
    max_score: Optional[float]
    min_score: Optional[float]
    average: Optional[float]


def analyze_scores(scores: List[float], pass_threshold: float = 60.0) -> ScoreAnalysis:
    """점수 리스트를 분석하여 통계 정보를 반환합니다.

    Args:
        scores: 분석할 점수 리스트
        pass_threshold: 통과 기준 점수 (기본값: 60.0)

    Returns:
        ScoreAnalysis: 분석 결과를 담은 객체

    Raises:
        ValueError: 빈 리스트가 입력된 경우
    """
    if not scores:
        return ScoreAnalysis(
            total_count=0,
            pass_count=0,
            fail_count=0,
            max_score=None,
            min_score=None,
            average=None
        )

    # 통과한 학생 수 계산
    pass_count = sum(1 for score in scores if score >= pass_threshold)
    fail_count = len(scores) - pass_count

    # 통계 계산 (내장 함수 활용)
    max_score = max(scores)
    min_score = min(scores)
    average = sum(scores) / len(scores)

    return ScoreAnalysis(
        total_count=len(scores),
        pass_count=pass_count,
        fail_count=fail_count,
        max_score=max_score,
        min_score=min_score,
        average=average
    )


def print_analysis(analysis: ScoreAnalysis) -> None:
    """분석 결과를 출력합니다.
    
    Args:
        analysis: 출력할 분석 결과
    """
    print(f"총 학생 수: {analysis.total_count}")
    print(f"통과한 학생 수: {analysis.pass_count}")
    print(f"탈락한 학생 수: {analysis.fail_count}")
    
    if analysis.max_score is not None:
        print(f"최고 점수: {analysis.max_score}")
    else:
        print("최고 점수: 데이터 없음")
        
    if analysis.min_score is not None:
        print(f"최저 점수: {analysis.min_score}")
    else:
        print("최저 점수: 데이터 없음")
        
    if analysis.average is not None:
        print(f"평균 점수: {analysis.average:.1f}")
    else:
        print("평균 점수: 데이터 없음")


def print_statistics(data_list: List[float]) -> None:
    """리스트에서 통계 정보를 계산하고 결과를 출력합니다.
    
    Args:
        data_list: 통계를 계산할 숫자 리스트
    """
    if not data_list:
        print("데이터가 없습니다.")
        return
    
    # 통계 계산
    count = len(data_list)
    total = sum(data_list)
    average = total / count
    maximum = max(data_list)
    minimum = min(data_list)
    
    # 정렬된 리스트에서 중앙값(median) 계산
    sorted_data = sorted(data_list)
    middle = count // 2
    if count % 2 == 0:
        median = (sorted_data[middle-1] + sorted_data[middle]) / 2
    else:
        median = sorted_data[middle]
    
    # 표준편차 계산
    squared_diff_sum = sum((x - average) ** 2 for x in data_list)
    std_dev = (squared_diff_sum / count) ** 0.5
    
    # 결과 출력
    print(f"데이터 개수: {count}")
    print(f"합계: {total:.2f}")
    print(f"평균: {average:.2f}")
    print(f"중앙값: {median:.2f}")
    print(f"최댓값: {maximum:.2f}")
    print(f"최솟값: {minimum:.2f}")
    print(f"표준편차: {std_dev:.2f}")


def process_scores(scores: List[float]) -> None:
    """점수 리스트를 받아, 통과 여부 판단 및 통계 출력
    
    Args:
        scores: 처리할 점수 리스트
    """
    analysis = analyze_scores(scores)
    print_analysis(analysis)


# 기존 코드와의 호환성을 위해 원래 함수 구현은 유지하면서 새 방식으로 리팩토링
def process_scores_original(scores: List[float]) -> None:
    """기존 process_scores 함수의 동작을 유지하는 레거시 버전"""
    pass_count = 0
    for s in scores:
        if s >= 60:
            pass_count += 1
    fail_count = len(scores) - pass_count  # 실패한 학생 수
    
    # 2. 최고점과 최저점 찾기
    max_score = scores[0]
    min_score = scores[0]
    for s in scores:
        if s > max_score:
            max_score = s
        if s < min_score:
            min_score = s
    
    # 3. 평균 계산 (소수 첫째자리까지)
    total = 0
    for s in scores:
        total += s
    average = total / len(scores)
    
    # 4. 결과 출력
    print(f"총 학생 수: {len(scores)}")
    print(f"통과한 학생 수: {pass_count}")
    print(f"탈락한 학생 수: {fail_count}")
    print(f"최고 점수: {max_score}")
    print(f"최저 점수: {min_score}")
    print(f"평균 점수: {average:.1f}")


if __name__ == "__main__":
    # 테스트 데이터
    sample_scores = [85, 92, 78, 45, 63, 59, 71, 88, 95, 32]
    empty_scores = []
    
    print("\n=== 기본 리팩토링 버전 ===")
    process_scores(sample_scores)
    
    print("\n=== 빈 리스트 처리 테스트 ===")
    process_scores(empty_scores)
    
    print("\n=== 레거시 버전 테스트 ===")
    try:
        process_scores_original(sample_scores)
    except Exception as e:
        print(f"오류 발생: {e}")
    
    print("\n=== 성능 비교 테스트 ===")
    import time
    from random import random
    
    # 큰 데이터셋 생성 (1000개 점수)
    large_dataset = [random() * 100 for _ in range(1000)]
    
    # 새 버전 성능 측정
    start = time.time()
    process_scores(large_dataset)
    new_time = time.time() - start
    
    print(f"\n새 버전 실행 시간: {new_time:.6f}초")
    
    # 레거시 버전 성능 측정
    start = time.time()
    process_scores_original(large_dataset)
    legacy_time = time.time() - start
    
    print(f"레거시 버전 실행 시간: {legacy_time:.6f}초")
    print(f"성능 향상: {(legacy_time/new_time - 1)*100:.2f}%")
    
    print("\n=== 새로운 통계 함수 테스트 ===")
    print_statistics(sample_scores)
    print("\n=== 빈 리스트 통계 테스트 ===")
    print_statistics(empty_scores)