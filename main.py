# -*- coding: utf-8 -*-
# 在此文件处编辑代码
def analyze_text(text):
    """
    分析文本中字符频率并按频率降序排列
    
    参数:
    text - 输入的字符串
    
    返回:
    list - 按字符频率降序排列的字符列表
    """
    # 1. 统计每个字符的出现频率
    frequency_dict = {}
    for char in text:
        # 用get方法安全获取字符计数，不存在则默认0
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    
    # 2. 按频率降序排序，频率相同时按字符ASCII码升序排列（保证结果一致性）
    # 排序key：(-频率, 字符)，负号表示降序
    sorted_items = sorted(frequency_dict.items(), key=lambda x: (-x[1], x[0]))
    
    # 3. 提取排序后的字符组成列表
    sorted_characters = [char for char, count in sorted_items]
    
    return sorted_characters

# 主程序，已完整
if __name__ == "__main__":
    print("文本字符频率分析器")
    print("====================")
    print("请输入一段文本（输入空行结束）：")
    
    # 读取多行输入
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    
    # 合并输入文本
    text = "\n".join(lines)
    
    if not text.strip():
        print("未输入有效文本！")
    else:
        # 分析文本
        sorted_chars = analyze_text(text)
        
        # 打印结果
        print("\n字符频率降序排列:")
        print(", ".join(sorted_chars))
        
        # 提示用户比较不同语言
        print("\n提示: 尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
