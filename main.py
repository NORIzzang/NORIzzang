import os
import sys
from tkinter import Tk, Label, Entry, Button, Text, END, Frame


def load_data(file_path):
    data = {}
    current_dish = None

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.isdigit():
            continue
        if not line:
            continue
        if current_dish is None:
            current_dish = line
            data[current_dish] = []
        else:
            if line == '------------------------------------------------------------':
                current_dish = None
            else:
                data[current_dish].append(line)

    return data


def search_data(data, region_query, food_query):
    results = []
    region_query = region_query.lower()
    food_query = food_query.lower()

    for dish, locations in data.items():
        dish_matched = food_query in dish.lower()

        for location in locations:
            location_matched = region_query in location.lower()

            if (dish_matched and region_query == '') or (location_matched and food_query == ''):
                # Extract only the store name
                store_name = location.split('-')[-1].strip()
                results.append(store_name)
            elif dish_matched and location_matched:
                store_name = location.split('-')[-1].strip()
                results.append(store_name)

    return results


def on_search():
    region_query = region_entry.get()
    food_query = food_entry.get()
    results = search_data(data, region_query, food_query)

    text_box.delete(1.0, END)

    if results:
        for result in results:
            text_box.insert(END, result + "\n")
    else:
        text_box.insert(END, "검색 결과가 없습니다.\n")


def main():
    global region_entry, food_entry, text_box, data

    # 파일 경로를 지정하세요.
    file_path = os.path.expanduser("~/Desktop/맛집 목록.txt")
    data = load_data(file_path)

    root = Tk()
    root.title("맛집 검색 프로그램")

    # Frame for inputs
    input_frame = Frame(root)
    input_frame.pack(pady=10)

    # 지역 검색 필드
    Label(input_frame, text="지역 검색:").grid(row=0, column=0, padx=5)
    region_entry = Entry(input_frame)
    region_entry.grid(row=0, column=1, padx=5)

    # 음식 검색 필드
    Label(input_frame, text="음식 검색:").grid(row=1, column=0, padx=5)
    food_entry = Entry(input_frame)
    food_entry.grid(row=1, column=1, padx=5)

    # 검색 버튼
    Button(input_frame, text="검색", command=on_search).grid(
        row=2, columnspan=2, pady=10)

    # 결과 출력 필드
    text_box = Text(root, height=20, width=50)
    text_box.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
