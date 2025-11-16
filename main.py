# main.py
def analyze_text(text: str):
    """返回按字符出现频率降序排列的字符列表"""
    freq = {}
    text_lower = text.lower()
    for char in text_lower:
        if char.isalpha():  # 只统计字母（包括中文）
            freq[char] = freq.get(char, 0) + 1

    # 按频率降序排序（相同频率不强制字典序，符合测试标准）
    sorted_chars = sorted(freq, key=lambda c: freq[c], reverse=True)
    return sorted_chars


def main():
    print("=== 文本字符频率分析器 ===")
    print("请输入一段文本（按回车确认）：")

    text = input()

    print("\n--- 字符频率降序排列 ---")
    result = analyze_text(text)
    print(result)

    print("\n提示: 尝试输入中英文文章片段，更容易看出频率差异。")


if __name__ == "__main__":
    main()

