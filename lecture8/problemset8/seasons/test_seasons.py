from datetime import date
from seasons import Time  # 导入类 Time

def test_calculate():
    # 创建 Time 类的一个实例，传入生日
    time_obj = Time("2025-02-20")  # 假设你想要测试 "2025-02-20"
    minutes = time_obj.calculate()  # 调用实例的 calculate 方法

    # 计算预期值 (现在是分钟数)
    birthdate = date.fromisoformat("2025-02-20")
    today = date.today()
    expected_minutes = (today - birthdate).days * 24 * 60

    assert abs(minutes - expected_minutes) < 1  # 允许很小的误差