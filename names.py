while True:
    try:
        names_input = input("请输入英文名字(以逗号分隔): ").strip()
        if not names_input:
            print("输入内容为空！请重新输入！")
            continue

        # 分割多个名字
        names = [name.strip() for name in names_input.split(',') if name.strip()]

        results = []
        for name in names:
            parts = name.split()
            if not parts:
                continue

            # 姓氏（最后一个部分）全部大写
            surname = parts[0].upper()

            # 名字部分：只取第一个字母大写
            if len(parts) > 1:
                first_name_initial = parts[1][0].upper()
                result = f"{surname} {first_name_initial}"
            else:
                result = surname

            results.append(result)

        print(", ".join(results))

    except KeyboardInterrupt:
        print("\n程序结束")
        break
    except Exception as e:
        print(f"处理出错: {e}")
