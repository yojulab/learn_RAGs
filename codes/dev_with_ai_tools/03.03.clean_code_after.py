"""학생 점수 통계 처리 모듈

이 모듈은 학생 점수 리스트를 분석하고 다양한 통계 정보를 제공합니다.
클린 코드 원칙을 적용하여 구현되었습니다.
"""
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
import statistics
from collections import Counter


@dataclass
class StatisticsResult:
    """통계 분석 결과를 담는 데이터 클래스"""
    count: int
    sum: float
    average: Optional[float]
    median: Optional[float]
    mode: Optional[List[float]]
    max_value: Optional[float]
    min_value: Optional[float]
    range: Optional[float]
    variance: Optional[float]
    std_deviation: Optional[float]
    

def calculate_statistics(data: List[float]) -> StatisticsResult:
    """데이터 리스트에 대한 통계 정보를 계산합니다.
    
    Args:
        data: 통계를 계산할 숫자 리스트
        
    Returns:
        StatisticsResult: 통계 계산 결과
    """
    if not data:
        return StatisticsResult(
            count=0,
            sum=0.0,
            average=None,
            median=None,
            mode=None,
            max_value=None,
            min_value=None,
            range=None,
            variance=None,
            std_deviation=None
        )
    
    # 기본 통계값 계산
    data_sum = sum(data)
    count = len(data)
    avg = data_sum / count
    
    # 모드(최빈값) 계산
    data_counter = Counter(data)
    max_frequency = max(data_counter.values())
    mode_values = [val for val, freq in data_counter.items() if freq == max_frequency]
    
    # 결과 반환
    return StatisticsResult(
        count=count,
        sum=data_sum,
        average=avg,
        median=statistics.median(data),
        mode=mode_values,
        max_value=max(data),
        min_value=min(data),
        range=max(data) - min(data),
        variance=statistics.variance(data) if count > 1 else 0,
        std_deviation=statistics.stdev(data) if count > 1 else 0
    )


def print_statistics(data: List[float], decimal_places: int = 2) -> None:
    """데이터 리스트의 통계 정보를 계산하고 출력합니다.
    
    Args:
        data: 통계를 계산할 숫자 리스트
        decimal_places: 소수점 표시 자릿수 (기본값: 2)
    """
    if not data:
        print("데이터가 없습니다.")
        return
        
    stats = calculate_statistics(data)
    
    # 결과 출력 형식 지정
    fmt = f":.{decimal_places}f"
    
    print(f"데이터 개수: {stats.count}")
    print(f"합계: {stats.sum:{fmt}}")
    print(f"평균: {stats.average:{fmt}}")
    print(f"중앙값: {stats.median:{fmt}}")
    print(f"최빈값: {', '.join(f'{x:{fmt}}' for x in stats.mode)}")
    print(f"최댓값: {stats.max_value:{fmt}}")
    print(f"최솟값: {stats.min_value:{fmt}}")
    print(f"범위: {stats.range:{fmt}}")
    print(f"분산: {stats.variance:{fmt}}")
    print(f"표준편차: {stats.std_deviation:{fmt}}")


def analyze_score_distribution(scores: List[float], 
                               bins: List[int] = [0, 60, 70, 80, 90, 100]) -> Dict[str, int]:
    """점수 분포를 분석하여 각 구간별 학생 수를 반환합니다.
    
    Args:
        scores: 분석할 점수 리스트
        bins: 점수 구간 경계값 (기본값: [0, 60, 70, 80, 90, 100])
        
    Returns:
        Dict[str, int]: 구간별 학생 수
    """
    # 결과를 저장할 딕셔너리 초기화
    distribution = {f"{bins[i]}-{bins[i+1]}": 0 for i in range(len(bins)-1)}
    
    # 각 점수를 해당 구간에 배치
    for score in scores:
        for i in range(len(bins)-1):
            if bins[i] <= score < bins[i+1]:
                distribution[f"{bins[i]}-{bins[i+1]}"] += 1
                break
            # 최고점이 마지막 구간의 상한과 같은 경우를 처리
            elif i == len(bins)-2 and score == bins[i+1]:
                distribution[f"{bins[i]}-{bins[i+1]}"] += 1
                break
                
    return distribution


def print_grade_distribution(scores: List[float]) -> None:
    """점수 분포를 계산하고 출력합니다.
    
    Args:
        scores: 분석할 점수 리스트
    """
    if not scores:
        print("데이터가 없습니다.")
        return
        
    distribution = analyze_score_distribution(scores)
    total = len(scores)
    
    print("점수 분포:")
    for range_str, count in distribution.items():
        percentage = (count / total) * 100 if total > 0 else 0
        bar = "#" * int(percentage / 2)  # 분포를 시각적으로 표현
        print(f"{range_str}: {count}명 ({percentage:.1f}%) {bar}")


if __name__ == "__main__":
    # 테스트 데이터
    sample_scores = [85, 92, 78, 45, 63, 59, 71, 88, 95, 32, 85, 91]
    
    print("\n=== 기본 통계 정보 ===")
    print_statistics(sample_scores)
    
    print("\n=== 점수 분포 ===")
    print_grade_distribution(sample_scores)
