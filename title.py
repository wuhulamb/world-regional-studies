while True:
    try:
        text = input("请输入英文句子: ").strip()
        
        if not text:
            print("输入内容为空！请重新输入！")
            continue
        # 分割冒号前后的部分
        if ':' in text:
            parts = text.split(':', 1)
            before_colon = parts[0].strip()
            after_colon = parts[1].strip()

            # 处理冒号前的部分
            result = before_colon[0].upper() + before_colon[1:].lower() + ': ' + after_colon[0].upper() + after_colon[1:].lower()
        else:
            # 没有冒号的情况
            result = text[0].upper() + text[1:].lower()
        print(f"{result}")

    except KeyboardInterrupt:
        print("\n程序结束")
        break
    except Exception as e:
        print(f"处理出错: {e}")
