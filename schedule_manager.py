import pymysql

from pymysql.cursors import Cursor

# db 연결하는 함수
def get_db_connection() -> pymysql.Connection:
    try:
        return pymysql.connect(host="localhost", port=3307, user="root", password='1234', database='schedule_db')
    except Exception as e:
        print(f"데이터베이스 연결 실패: {e}")
        exit(1)

def add_schedule(cursor: Cursor):
    # Todo: 여기에 일정 추가 코드를 작성합니다.
    title = input('제목: ')
    desc = input('내용: ')
    start_date = input('시작일: ')
    end_date = input('종료일: ')

    insert_query = 'insert into schedules (title, description, start_datetime, end_datetime) values(%s,%s,%s,%s)'
    
    cursor.execute(insert_query,(title, desc, start_date, end_date))
    print('일정이 추가되었음')

def get_schedules(cursor: Cursor):
    # Todo: 여기에 일정 정보를 가져오는 코드를 작성합니다.
    select_query = 'select id, title, description, start_datetime, end_datetime, is_completed from schedules'
    cursor.execute(select_query)
    schedules = cursor.fetchall()

    for schedule in schedules:
        id, title, description, start_datetime, end_datetime, is_completed = schedule
        print(f'{id}| {title}')
        print(f'    상태: {is_completed}')
        print(f'    기간: {start_datetime} ~ {end_datetime}')
        print(f'    설명: {description}')

def complete_schedule(cursor: Cursor):
    # Todo: 여기에 일정을 완료처리하는 코드를 작성합니다.
    renew_id = input('완료시킬 일정 id: ')
    update_query = 'update schedules set is_completed = true where id = %s'
    
    cursor.execute(update_query, renew_id)
    print('해당 일정을 완료했습니다.')

# 메뉴 나타내기
def show_menu() -> str:
    print("1. 일정 추가")  # insert
    print("2. 일정 보기")  # select
    print("3. 일정 완료")  # update
    print("4. 종료")
    return get_user_choice()

# 선택한 메뉴 입력받는 함수
def get_user_choice() -> str:
    return input("선택: ")

def main():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        while True:
            choice = show_menu()
            if choice == "1":
                add_schedule(cursor)
                conn.commit()
            elif choice == "2":
                get_schedules(cursor)
            elif choice == "3":
                complete_schedule(cursor)
                conn.commit()
            elif choice == "4":
                print("종료합니다.")
                break
            else:
                print("다시 선택해주세요")

    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()