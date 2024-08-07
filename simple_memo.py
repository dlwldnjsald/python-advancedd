"""
def save_note():
    note = input("메모를 입력하세요: ")
    with open("note.txt", "a") as file:
        file.write(note + "\n")
    print("메모가 저장되었습니다.")

save_note()
"""

def save_note():
    note = input("메모를 입력하세요: ")
    with open("note.txt", "a") as file:
        file.write(note + "\n")
    print("메모가 저장되었습니다.")

def read_notes():
    try:
        with open("note.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("저장된 메모:")
                for idx, note in enumerate(notes, 1):
                    print(f"{idx}. {note.strip()}")
            else:
                print("저장된 메모가 없습니다.")
    except FileNotFoundError:
        print("메모 파일이 없습니다.")

def delete_note():
    try:
        with open("note.txt", "r") as file:
            notes = file.readlines()
        if notes:
            read_notes()
            note_number = int(input("삭제할 메모 번호를 입력하세요: "))
            if 1 <= note_number <= len(notes):
                del notes[note_number - 1]
                with open("note.txt", "w") as file:
                    file.writelines(notes)
                print("메모가 삭제되었습니다.")
            else:
                print("유효한 번호를 입력하세요.")
        else:
            print("삭제할 메모가 없습니다.")
    except FileNotFoundError:
        print("메모 파일이 없습니다.")
    except ValueError:
        print("유효한 숫자를 입력하세요.")

def main():
    while True:
        print("\n메뉴:")
        print("1. 메모 저장")
        print("2. 메모 읽기")
        print("3. 메모 삭제")
        print("4. 종료")
        choice = input("선택하세요 (1/2/3/4): ")

        if choice == '1':
            save_note()
        elif choice == '2':
            read_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("유효한 선택이 아닙니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
