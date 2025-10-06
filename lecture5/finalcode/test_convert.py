"""我们需要你实现以下几个方面的测试：
整数转换测试：
验证 convert(1) 的结果是否等于 149597870700。
验证 convert(50) 的结果是否等于 7479893535000。

类型错误测试：
确保当 convert 函数接收到字符串类型的输入（例如 "1"）时，会抛出一个类型错误。

浮点数转换测试：
验证 convert(0.001) 的结果是否约等于 149597870.691， 允许一定的误差范围（例如，绝对误差小于 1e-2）。

我们需要你编写的测试脚本能够自动运行这些测试用例，并报告测试结果。 这份测试脚本将帮助我们确保 convert 函数在各种情况下都能正确工作。
"""
import pytest
from convert import convert

def test_int():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000

def test_type():
    with pytest.raises(TypeError):
        convert("1")

def test_float():
    assert convert(0.001) == pytest.approx(149597870.691, abs = 1e-2)