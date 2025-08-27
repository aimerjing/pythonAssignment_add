import main  # 导入学生的main模块

def test_add():
    """测试add函数的正确性"""
    # 定义测试用例（输入a、b，预期输出expected）
    test_cases = [
        (1, 2, 3),    # 正数相加
        (0, 0, 0),    # 零相加
        (-1, 1, 0),   # 正负抵消
        (5, 7, 12),   # 更大的数
        (100, 200, 300)  # 边界值
    ]
    
    # 遍历测试用例
    for a, b, expected in test_cases:
        try:
            result = main.add(a, b)  # 调用学生的add函数
            assert result == expected, f"❌ 测试失败：add({a}, {b}) 应返回 {expected}，但得到 {result}"
        except AssertionError as e:
            print(e)
            exit(1)  # 测试失败，退出码1

if __name__ == "__main__":
    try:
        test_add()
        print("✅ 所有测试通过！")
        exit(0)  # 测试成功，退出码0
    except Exception as e:
        print(f"❌ 测试执行失败：{str(e)}")
        exit(1)  # 其他错误，退出码1
